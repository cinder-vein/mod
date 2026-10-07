"""Ability icons: 32x32 pixel-art glyphs, recolored per corps.

Every glyph is a 32-line ASCII map in tools/icon_glyphs/*.py (each module defines GLYPHS = {name: [32 strings of
32 chars]}). One character is one pixel; each character is a color role, so one glyph renders in any corps' colors:

    .  transparent
    M  main color         L  light (highlight)    D  dark (shadow)       H  white-hot core (near white)
    A  accent main        a  accent light         B  accent dark         (accent = a second color: the
                                                                           second ring of a pair, or for
                                                                           a single corps its own light)
    R  rainbow: the seven spectrum colors across the icon (by column)
    K  near-black ink     G  grey                 S  silver (light grey) W  pure white
    Y  gold               O  outline-only: transparent, but forces the dark outline here

render() adds a 1-pixel dark outline around the drawn shape (outside pixels that touch it, 4-way), so glyphs
don't need to draw their own outer outline. Icons are drawn for the 16x16 slot of the ability bar, at 2x.

    python3 tools/icons.py out.png [names...]   # preview sheet in every corps color
"""
import importlib
import pkgutil
import sys
from pathlib import Path

from PIL import Image

SIZE = 32
CLEAR = (0, 0, 0, 0)

SPECTRUM_RGB = [(46, 200, 70), (245, 205, 30), (220, 30, 35), (250, 130, 20), (40, 130, 255), (215, 55, 220),
                (105, 60, 230)]


def _shade(rgb, f):
    if f >= 1:
        return tuple(int(v + (255 - v) * (f - 1)) for v in rgb[:3])
    return tuple(int(v * f) for v in rgb[:3])


def roles(rgb, accent=None):
    """Color roles for a main color (and an optional accent color)."""
    rgb = tuple(rgb[:3])
    lum = 0.3 * rgb[0] + 0.59 * rgb[1] + 0.11 * rgb[2]
    if lum > 215:  # near-white (White Lantern): shade with cool greys so the glyph keeps its form
        main, light, dark = rgb, (255, 255, 255), (150, 158, 176)
    elif lum < 110:  # dark (Black Lantern): lift the highlights so it reads on the dark bar
        main, light, dark = _shade(rgb, 1.25), _shade(rgb, 1.7), _shade(rgb, 0.55)
    else:
        main, light, dark = rgb, _shade(rgb, 1.45), _shade(rgb, 0.55)
    if accent is None:
        a_main, a_light, a_dark = light, _shade(light, 1.3), main
    else:
        a_main, a_light, a_dark = roles(accent)["M"], roles(accent)["L"], roles(accent)["D"]
    return {"M": main, "L": light, "D": dark, "H": _shade(light, 1.6), "A": a_main, "a": a_light, "B": a_dark,
            "K": (16, 17, 22), "G": (96, 100, 110), "S": (190, 194, 204), "W": (255, 255, 255),
            "Y": (232, 186, 70)}


def outline_color(rgb):
    return tuple(max(8, int(v * 0.22)) for v in rgb[:3]) + (255,)


def _glyph_modules():
    pkg = Path(__file__).resolve().parent / "icon_glyphs"
    sys.path.insert(0, str(pkg.parent))
    glyphs = {}
    for info in pkgutil.iter_modules([str(pkg)]):
        if info.name.startswith("example"):  # style reference only
            continue
        mod = importlib.import_module(f"icon_glyphs.{info.name}")
        for name, rows in getattr(mod, "GLYPHS", {}).items():
            if name in glyphs:
                raise ValueError(f"glyph '{name}' defined twice")
            glyphs[name] = rows
    return glyphs


GLYPHS = _glyph_modules()


def check(name, rows):
    if len(rows) != SIZE or any(len(r) != SIZE for r in rows):
        raise ValueError(f"glyph '{name}' must be {SIZE} rows of {SIZE} characters")
    bad = set("".join(rows)) - set(".MLDHAaBRKGSWYO")
    if bad:
        raise ValueError(f"glyph '{name}' uses unknown roles {sorted(bad)}")


def render(name, rgb, accent=None):
    """The 32x32 RGBA icon for glyph `name` in a corps color (plus an optional accent color)."""
    rows = GLYPHS[name]
    check(name, rows)
    pal = roles(rgb, accent)
    img = Image.new("RGBA", (SIZE, SIZE), CLEAR)
    filled = [[False] * SIZE for _ in range(SIZE)]
    force = [[False] * SIZE for _ in range(SIZE)]
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == ".":
                continue
            if ch == "O":
                force[y][x] = True
                continue
            if ch == "R":
                c = SPECTRUM_RGB[min(len(SPECTRUM_RGB) - 1, x * len(SPECTRUM_RGB) // SIZE)]
            else:
                c = pal[ch]
            img.putpixel((x, y), tuple(c) + (255,))
            filled[y][x] = True
    ink = outline_color(pal["D"])
    for y in range(SIZE):
        for x in range(SIZE):
            if filled[y][x]:
                continue
            near = any(0 <= x + dx < SIZE and 0 <= y + dy < SIZE and filled[y + dy][x + dx]
                       for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            if near or force[y][x]:
                img.putpixel((x, y), ink)
    return img


PREVIEW_COLORS = [(46, 200, 70), (245, 205, 30), (220, 30, 35), (250, 130, 20), (40, 130, 255), (215, 55, 220),
                  (105, 60, 230), (235, 242, 250), (95, 98, 110)]


def preview(path, names=None, scale=3):
    """A sheet: one row per glyph, one column per corps color, on a dark slot-like background."""
    names = names or sorted(GLYPHS)
    cell = SIZE * scale + 8
    sheet = Image.new("RGBA", (cell * (len(PREVIEW_COLORS) + 1), cell * len(names)), (40, 42, 48, 255))
    for i, name in enumerate(names):
        for j, rgb in enumerate(PREVIEW_COLORS + [None]):
            icon = render(name, rgb or (46, 200, 70), (40, 130, 255) if rgb is None else None)
            icon = icon.resize((SIZE * scale, SIZE * scale), Image.NEAREST)
            bg = Image.new("RGBA", icon.size, (22, 23, 27, 255))
            bg.alpha_composite(icon)
            sheet.paste(bg, (j * cell + 4, i * cell + 4))
    sheet.save(path)


if __name__ == "__main__":
    preview(sys.argv[1], sys.argv[2:] or None)
