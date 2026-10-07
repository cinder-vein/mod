"""Textures and models for the Lantern Corps, drawn in code.

Used by gen_corps.py. Every corps gets the same shapes in its own colors,
with its own logo. Replace any generated PNG with hand-drawn art if you like,
but it will be overwritten the next time gen_corps.py runs unless you remove
that step there.
"""
from pathlib import Path

from PIL import Image, ImageDraw

CLEAR = (0, 0, 0, 0)
WHITE = (245, 250, 245, 255)

# 11x11 corps logos ("#" = symbol). Used on the chest, the ring face and the lantern core.
LOGOS = {
    "green": [
        "...........",
        "###########",
        "..#######..",
        ".##.....##.",
        ".#.......#.",
        ".#.......#.",
        ".#.......#.",
        ".##.....##.",
        "..#######..",
        "###########",
        "...........",
    ],
    "yellow": [
        "...#####...",
        "..#.....#..",
        ".#..###..#.",
        "#..#...#..#",
        "#.#..#..#.#",
        "#.#.###.#.#",
        "#.#..#..#.#",
        "#..#...#..#",
        ".#..###..#.",
        "..#.....#..",
        "...#####...",
    ],
    "red": [
        "..#######..",
        ".#.......#.",
        "#.#.....#.#",
        "#.##...##.#",
        "#.#.#.#.#.#",
        "#.#..#..#.#",
        "#..#.#.#..#",
        "#...###...#",
        ".#...#...#.",
        "..#######..",
        ".....#.....",
    ],
    "orange": [
        "...#####...",
        "..#.....#..",
        ".#.#...#.#.",
        "#..#...#..#",
        "#..#####..#",
        "#..#...#..#",
        "#..#...#..#",
        "#..#####..#",
        ".#.......#.",
        "..#.....#..",
        "...#####...",
    ],
    "blue": [
        "...#####...",
        "..#..#..#..",
        ".#...#...#.",
        "#...###...#",
        "#..#####..#",
        "####.#.####",
        "#..#####..#",
        "#...###...#",
        ".#...#...#.",
        "..#..#..#..",
        "...#####...",
    ],
    "indigo": [
        "...#####...",
        "..#.....#..",
        ".#.......#.",
        "#.#######.#",
        "#..#...#..#",
        "#...#.#...#",
        "#....#....#",
        "#.........#",
        ".#.......#.",
        "..#.....#..",
        "...#####...",
    ],
    "violet": [
        ".....#.....",
        "....###....",
        "....#.#....",
        "...#...#...",
        ".##.....##.",
        "#....#....#",
        ".##.....##.",
        "...#...#...",
        "....#.#....",
        "....###....",
        ".....#.....",
    ],
    "white": [
        "...#####...",
        "..#..#..#..",
        ".#.#.#.#.#.",
        "#...###...#",
        "#.##...##.#",
        "###.....###",
        "#.##...##.#",
        "#...###...#",
        ".#.#.#.#.#.",
        "..#..#..#..",
        "...#####...",
    ],
    "black": [
        "...#####...",
        "..#.....#..",
        ".#.#.#.#.#.",
        "#..#.#.#..#",
        "#..#.#.#..#",
        "#..#####..#",
        "#....#....#",
        "#.#######.#",
        ".#.......#.",
        "..#.....#..",
        "...#####...",
    ],
}



def shade(rgb, f):
    """f < 1 darkens, f > 1 lightens towards white."""
    if f >= 1:
        return tuple(int(v + (255 - v) * (f - 1)) for v in rgb[:3]) + (255,)
    return tuple(int(v * f) for v in rgb[:3]) + (255,)


GOLD = (222, 178, 76, 255)


def palette(corps, rgb):
    p = {
        "main": shade(rgb, 1.0), "light": shade(rgb, 1.28), "dark": shade(rgb, 0.62), "deep": shade(rgb, 0.4),
        "trim": (20, 21, 24, 255), "trim2": (38, 40, 45, 255), "symbol": WHITE, "glow": shade(rgb, 1.4),
        "disc": (14, 15, 17, 255), "gold": (222, 178, 76, 255), "metal": (110, 114, 122, 255),
        "metal_dark": (60, 63, 70, 255), "lens": (40, 44, 52, 255),
    }
    if corps == "white":  # an all-white suit with soft grey shading, like the reference
        p.update(main=(236, 239, 244, 255), light=(255, 255, 255, 255), dark=(190, 195, 206, 255),
                 deep=(150, 156, 168, 255), trim=(206, 211, 221, 255), trim2=(178, 184, 196, 255),
                 symbol=(120, 126, 140, 255), glow=(255, 255, 255, 255), disc=(52, 58, 70, 255),
                 metal=(225, 228, 235, 255), metal_dark=(170, 175, 186, 255), lens=(225, 232, 240, 255))
    if corps == "black":
        p.update(main=(58, 60, 68, 255), light=(92, 95, 105, 255), dark=(36, 37, 42, 255), deep=(16, 16, 18, 255),
                 trim=(12, 12, 14, 255), trim2=(26, 27, 31, 255), symbol=(225, 230, 240, 255),
                 glow=(215, 222, 235, 255), disc=(6, 6, 8, 255), metal=(50, 52, 58, 255), metal_dark=(28, 29, 33, 255))
    return p


# --- suits ---------------------------------------------------------------------------------
# Suits are standard 64x64 skin layouts rendered on their own two-layer model (see
# suit_model): the inner layer is the under-suit, the outer layer adds raised armor
# (shoulder pads, chest plate, gauntlets, knee guards) for depth. The head is left alone,
# so the wearer's face shows; masks are a separate accessory.

GLOWING = {"line", "symbol", "gem"}
PANELS = {"main", "light", "dark", "deep", "gold"}
FABRIC = {"trim", "trim2", "disc"}

# Small chest emblems (6x5) that fit a 64x64 suit.
MINI = {
    "green": ["######", ".####.", "#....#", ".####.", "######"],
    "yellow": ["..##..", ".#..#.", "#.##.#", ".#..#.", "..##.."],
    "red": [".####.", "#.##.#", "#.##.#", ".#..#.", "..##.."],
    "orange": ["#.##.#", ".#..#.", ".####.", ".#..#.", "#.##.#"],
    "blue": ["..##..", "#.##.#", "######", "#.##.#", "..##.."],
    "violet": ["..##..", ".####.", "######", ".####.", "..##.."],
    "indigo": ["######", "#....#", ".#..#.", "..##..", "......"],
    "white": ["#.##.#", ".####.", "##..##", ".####.", "#.##.#"],
    "black": ["#.##.#", "#.##.#", "######", "..##..", "######"],
}

# Suit designs (id, name); the first is the default. Every corps gets all three.
# Suit designs (id, name); the first is the default. All are recolors of the hand-made
# template in tools/templates/suit_base.png, so they keep its shading.
DESIGNS = {c: [("uniform", "Corps Uniform"), ("shadow", "Shadow"), ("classic", "Classic")] for c in LOGOS}

# Mask designs (id, name). "corps" is the template's own mask; "none" removes it.
MASKS = [("corps", "Corps Mask"), ("domino", "Domino Mask"), ("goggles", "Lens Goggles"), ("cowl", "Gem Cowl"),
         ("none", "No Mask")]
MASK_EXTRAS = {"black": [("deathly", "Deathly Pallor")]}  # corps-only masks
DEFAULT_MASK = {c: "corps" for c in LOGOS}
DEFAULT_MASK.update(violet="cowl", white="goggles", indigo="none", black="none")

PARTS = {
    "head": ((0, 0), (32, 0), 8, 8, 8),
    "body": ((16, 16), (16, 32), 8, 12, 4),
    "right_arm": ((40, 16), (40, 32), 4, 12, 4),
    "left_arm": ((32, 48), (48, 48), 4, 12, 4),
    "right_leg": ((0, 16), (0, 32), 4, 12, 4),
    "left_leg": ((16, 48), (0, 48), 4, 12, 4),
}


def box_faces(u, v, w, h, d):
    return {
        "top": (u + d, v, w, d), "bottom": (u + d + w, v, w, d), "right": (u, v + d, d, h),
        "front": (u + d, v + d, w, h), "left": (u + d + w, v + d, d, h), "back": (u + d + w + d, v + d, w, h),
    }


def mix(c1, c2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(c1[:3], c2[:3])) + (255,)


def scale(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c[:3]) + (255,)


def paint_box(imgs, colors, u, v, w, h, d, painter):
    """painter(face, x, y, face_w, face_h) -> palette key or None.

    Shades like a hand-made skin: a soft top-to-bottom gradient, darker seams where
    panels meet, a highlight on each panel's top edge, a little grain on the under-suit,
    and colored light bleeding next to glowing lines."""
    suit, glow = imgs
    for face, (fx, fy, fw, fh) in box_faces(u, v, w, h, d).items():
        keys = [[painter(face, x, y, fw, fh) for x in range(fw)] for y in range(fh)]
        for y in range(fh):
            for x in range(fw):
                key = keys[y][x]
                if key is None:
                    continue
                pos = (fx + x, fy + y)
                c = colors[key]
                if key in GLOWING:
                    suit.putpixel(pos, c)
                    glow.putpixel(pos, colors["glow"] if key != "symbol" else colors["symbol"])
                    continue
                around = [keys[j][i] for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
                          if 0 <= i < fw and 0 <= j < fh]
                above = keys[y - 1][x] if y > 0 else None
                f = 1.0 if face in ("top", "bottom") else 1.06 - 0.14 * (y / max(1, fh - 1))
                if key in PANELS:
                    if above != key and face not in ("top", "bottom"):
                        f *= 1.15  # highlight on the panel's top edge
                    elif any(n is not None and n != key and n not in GLOWING for n in around):
                        f *= 0.86  # seam
                elif key in FABRIC:
                    f *= 0.94 + ((x * 7 + y * 13 + x * y) % 4) * 0.03
                    if any(n in ("line", "gem") for n in around):
                        c = mix(c, colors["glow"], 0.3)
                suit.putpixel(pos, scale(c, f))


# --- the suit template -----------------------------------------------------------------------

TEMPLATE = Path(__file__).resolve().parent / "templates" / "suit_base.png"

# The template's three color families, lightest first. Each maps shade-for-shade onto a corps palette.
T_PRIMARY = [(1, 137, 86), (1, 120, 78), (1, 103, 70), (0, 86, 61), (0, 69, 50)]       # green panels
T_BASE = [(22, 31, 58), (20, 28, 53), (18, 25, 48), (16, 22, 42), (14, 19, 37)]          # navy under-suit
T_LIGHT = [(255, 255, 255), (231, 231, 231), (213, 213, 213), (195, 195, 195), (178, 178, 178),
           (160, 160, 160)]                                                                # gloves, emblem, lenses
T_GLOW = {(9, 12), (10, 12), (13, 12), (14, 12), (23, 22), (22, 38)}  # mask lenses and chest emblem
HEAD_ROWS = 16  # rows 0-15 hold the head and hat layers: they become the mask, not the suit


def _shades(top, family):
    """Scale a corps color by the template family's own light-to-dark ratios."""
    ref = max(family[0])
    return [tuple(max(0, min(255, round(v * max(f) / ref))) for v in top) for f in family]


def _families(corps, rgb, design):
    """(primary, base, light) shade lists for a corps and design."""
    if corps == "green":
        primary = list(T_PRIMARY)  # the template is the Green Lantern uniform
    elif corps == "black":
        primary = _shades((112, 116, 128), T_PRIMARY)
    elif corps == "white":
        primary = _shades((246, 248, 252), T_PRIMARY)
    else:
        primary = _shades(rgb, T_PRIMARY)
    base, light = list(T_BASE), list(T_LIGHT)
    if corps == "black":
        base = _shades((20, 20, 24), T_BASE)
    if corps == "white":
        base = _shades((200, 205, 216), T_BASE)
    if design == "shadow":   # pitch-black under-suit, gloves in the corps color
        base = _shades((24, 24, 28) if corps != "black" else (10, 10, 12), T_BASE)
        light = [primary[min(i, 4)] for i in range(len(T_LIGHT))]
    if design == "classic":  # the under-suit takes a deep shade of the corps color
        deep = tuple(int(v * 0.32) for v in (primary[0] if corps != "white" else (120, 128, 146)))
        base = _shades(deep, T_BASE)
    return primary, base, light


def _recolor(img, corps, rgb, design):
    primary, base, light = _families(corps, rgb, design)
    mapping = {}
    for src, dst in zip(T_PRIMARY, primary):
        mapping[src] = dst
    for src, dst in zip(T_BASE, base):
        mapping[src] = dst
    for src, dst in zip(T_LIGHT, light):
        mapping[src] = dst
    out = Image.new("RGBA", img.size, CLEAR)
    glow = Image.new("RGBA", img.size, CLEAR)
    p = palette(corps, rgb)
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            c = img.getpixel((x, y))
            if c[3] == 0:
                continue
            out.putpixel((x, y), mapping.get(c[:3], c[:3]) + (255,))
            if (x, y) in T_GLOW:
                glow.putpixel((x, y), (255, 255, 255, 255) if corps != "black" else p["glow"])
    return out, glow


def _to_slim(img):
    """Convert 4-pixel-wide arms to the 3-pixel slim layout by dropping one middle column."""
    out = img.copy()
    for u, v in ((40, 16), (40, 32), (32, 48), (48, 48)):  # right arm, right sleeve, left arm, left sleeve
        out.paste(CLEAR, (u, v, u + 16, v + 16))
        src = img.crop((u, v, u + 16, v + 16))

        def face(sx, sy, w, h, dx, dy, drop=True):
            region = src.crop((sx, sy, sx + w, sy + h))
            if drop and w == 4:
                cols = [region.crop((i, 0, i + 1, h)) for i in (0, 1, 3)]
                region = Image.new("RGBA", (3, h), CLEAR)
                for i, col in enumerate(cols):
                    region.paste(col, (i, 0))
            out.paste(region, (u + dx, v + dy))

        face(4, 0, 4, 4, 4, 0)            # top
        face(8, 0, 4, 4, 7, 0)            # bottom
        face(0, 4, 4, 12, 0, 4, False)    # outer side
        face(4, 4, 4, 12, 4, 4)           # front
        face(8, 4, 4, 12, 7, 4, False)    # inner side
        face(12, 4, 4, 12, 11, 4)         # back
    return out


def suit(corps, rgb, design, slim):
    """(suit, glow) 64x64 textures for suit_model: the template recolored, without its head."""
    tpl = Image.open(TEMPLATE).convert("RGBA")
    tpl.paste(CLEAR, (0, 0, 64, HEAD_ROWS))
    if slim:
        tpl = _to_slim(tpl)
    return _recolor(tpl, corps, rgb, design)


def corps_mask(corps, rgb):
    """(mask, glow): the template's own mask (head rows only), recolored."""
    tpl = Image.open(TEMPLATE).convert("RGBA")
    tpl.paste(CLEAR, (0, HEAD_ROWS, 64, 64))
    return _recolor(tpl, corps, rgb, "uniform")


def mask_painter(corps, mask):
    """Masks live on the head only. Eyes are on row 4 at x 1-2 and 5-6 of the face."""
    def paint(part, layer, f, x, y, w, h):
        if part != "head" or mask == "none":
            return None
        eye = f == "front" and y == 4 and x in (1, 2, 5, 6)
        near_front = (f == "right" and x >= 6) or (f == "left" and x <= 1)
        if mask == "domino":
            if layer != "inner" or eye:
                return None
            if f == "front" and y in (3, 4):
                return "main"
            if near_front and y in (3, 4):
                return "dark"
            return None
        if mask == "goggles":  # a raised frame with lenses, like the White Lantern reference
            if layer != "outer":
                return None
            if f == "front" and 3 <= y <= 5:
                if y == 4 and x in (1, 2, 5, 6):
                    return "line"  # glowing lenses
                return "main"
            if f in ("right", "left") and y == 4:
                return "dark"  # strap
            return None
        if mask == "deathly":  # undead face paint: pale skin, dark sockets around the eyes, grey lips
            if layer != "inner" or eye:
                return None
            if f == "front":
                if y in (3, 4) and x in (0, 1, 2, 3, 4, 5, 6, 7) and (y == 3 and x in (1, 2, 5, 6) or y == 4):
                    return "socket"
                if y == 6 and 2 <= x <= 5:
                    return "lips"
                return "pale" if y >= 2 else None
            if f in ("right", "left") and 2 <= y <= 7 and near_front:
                return "pale"
            return None
        if mask == "cowl":  # covers the forehead and frames the eyes, with a jewel
            if layer != "inner" or eye:
                return None
            if f == "front":
                if y == 1 and x in (3, 4):
                    return "gem"
                if y <= 3 or (y == 4 and x in (0, 3, 4, 7)) or (y == 5 and x in (0, 7)):
                    return "main"
                return None
            if f in ("right", "left") and y <= 5:
                return "main" if near_front or y <= 2 else None
            if f == "top":
                return "main" if y >= 4 else None
            return None
    return paint


def _paint_layers(corps, rgb, painter, slim):
    p = palette(corps, rgb)
    colors = {**p, "line": p["glow"], "gem": p["glow"],
              "pale": (196, 200, 204, 255), "socket": (34, 32, 38, 255), "lips": (80, 78, 88, 255)}
    imgs = (Image.new("RGBA", (64, 64), CLEAR), Image.new("RGBA", (64, 64), CLEAR))
    for part, (inner, outer, w, h, d) in PARTS.items():
        if slim and part.endswith("arm"):
            w = 3
        for layer, (u, v) in (("inner", inner), ("outer", outer)):
            paint_box(imgs, colors, u, v, w, h, d,
                      lambda f, x, y, fw, fh, part=part, layer=layer: painter(part, layer, f, x, y, fw, fh))
    return imgs


def mask(corps, rgb, mask_id):
    """(mask, glow) 64x64 textures for the head of suit_model."""
    if mask_id == "corps":
        return corps_mask(corps, rgb)
    return _paint_layers(corps, rgb, mask_painter(corps, mask_id), False)


def suit_model(slim):
    """Two-layer humanoid model that sits just over the skin (inner) and over the
    jacket layer (outer), so suits get raised armor like a hand-made skin's second layer."""
    aw = 3 if slim else 4

    def part(offset, inner_uv, outer_uv, origin, dims):
        return {"part_pose": {"offset": offset, "rotation": [0, 0, 0]}, "children": {}, "cubes": [
            {"origin": origin, "dimensions": dims, "texture_offset": list(inner_uv), "deformation": [0.04] * 3},
            {"origin": origin, "dimensions": dims, "texture_offset": list(outer_uv), "deformation": [0.3] * 3},
        ]}

    return {
        "texture_width": 64, "texture_height": 64,
        "mesh": {
            "head": part([0, 0, 0], (0, 0), (32, 0), [-4, -8, -4], [8, 8, 8]),
            "hat": {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "cubes": [], "children": {}},
            "body": part([0, 0, 0], (16, 16), (16, 32), [-4, 0, -2], [8, 12, 4]),
            "right_arm": part([-5, 2.5 if slim else 2, 0], (40, 16), (40, 32), [-aw + 1, -2, -2], [aw, 12, 4]),
            "left_arm": part([5, 2.5 if slim else 2, 0], (32, 48), (48, 48), [-1, -2, -2], [aw, 12, 4]),
            "right_leg": part([-1.9, 12, 0], (0, 16), (0, 32), [-2, 0, -2], [4, 12, 4]),
            "left_leg": part([1.9, 12, 0], (16, 48), (0, 48), [-2, 0, -2], [4, 12, 4]),
        },
    }


def slot_icon(corps, rgb, kind="suit"):
    """16x16 icon for the corps' suit/mask slots in the accessories menu."""
    p = palette(corps, rgb)
    img = Image.new("RGBA", (16, 16), CLEAR)
    if kind == "mask":
        d = ImageDraw.Draw(img)
        d.rectangle((1, 5, 14, 9), fill=p["main"])
        for x0 in (3, 9):
            d.rectangle((x0, 6, x0 + 3, 8), fill=CLEAR)
        return img
    for y, row in enumerate(LOGOS[corps]):
        for x, ch in enumerate(row):
            if ch == "#":
                img.putpixel((2 + x, 2 + y), p["glow"])
    return img


# --- ring worn on the hand ------------------------------------------------------------------

# Model UVs are divided by (texture size x texture_scale), so 0.1 makes each model unit cover
# 10 texture pixels: the 1.2-unit signet face shows a 12-pixel picture. texture_offset is in
# model units (integers), so the band's strip starts 30 pixels down.
RING_TEX_SCALE = 0.1
RING_TEX = 64


def ring_model(slim, left=False):
    """The ring on the hand, where the Green Lantern mod showcase wears it: a signet with the
    corps logo on the outside of the hand, over the base of the fingers (y 8.3-9.5 of the arm,
    which runs from the shoulder at -2 to the fingertips at 10), and a thin band wrapping across
    the front of the hand around the index finger. Both sit just outside the suit's outer layer
    (0.3 beyond the arm), so gloves never hide them. The first ring you wear shows on the right
    hand, a second one on the left."""
    aw = 3 if slim else 4
    empty = {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "cubes": [], "children": {}}
    scale = [RING_TEX_SCALE, RING_TEX_SCALE]
    if left:
        outer = aw - 1  # +x side of the left arm box (-1 .. aw-1)
        signet, band = [outer + 0.3, 8.3, -2.5], [outer - 0.8, 8.75, -2.5]
    else:
        outer = 1 - aw  # -x side of the right arm box (1-aw .. 1)
        signet, band = [outer - 0.5, 8.3, -2.5], [outer - 0.5, 8.75, -2.5]
    arm = {
        "part_pose": {"offset": [5 if left else -5, 2.5 if slim else 2, 0], "rotation": [0, 0, 0]},
        "cubes": [{"origin": signet, "dimensions": [0.2, 1.2, 1.2], "texture_offset": [0, 0], "texture_scale": scale},
                  {"origin": band, "dimensions": [1.3, 0.3, 0.2], "texture_offset": [0, 3], "texture_scale": scale}],
        "children": {},
    }
    mesh = {part: empty for part in ("head", "hat", "body", "right_arm", "left_arm", "right_leg", "left_leg")}
    mesh["left_arm" if left else "right_arm"] = arm
    return {"texture_width": RING_TEX, "texture_height": RING_TEX, "mesh": mesh}


def ring_textures(corps, rgb):
    """(metal, glow) 64x64 textures for ring_model. The signet's outer faces are the 12x12
    squares at (0, 12) (right hand) and (14, 12) (left hand); the band is the strip at y 30-35."""
    p = palette(corps, rgb)
    metal = Image.new("RGBA", (RING_TEX, RING_TEX), CLEAR)
    glow = Image.new("RGBA", (RING_TEX, RING_TEX), CLEAR)
    d = ImageDraw.Draw(metal)
    d.rectangle((0, 0, 27, 23), fill=p["metal_dark"])          # signet edges
    d.rectangle((0, 30, 29, 34), fill=p["metal"])              # band
    d.line((0, 32, 29, 32), fill=shade(p["metal"][:3], 1.3))   # its shine
    for x0 in (0, 14):
        d.rectangle((x0, 12, x0 + 11, 23), fill=p["disc"])
        d.rectangle((x0, 12, x0 + 11, 23), outline=p["main"])
        for y, row in enumerate(LOGOS[corps]):
            for x, ch in enumerate(row):
                if ch == "#":
                    metal.putpixel((x0 + x, 12 + y), p["glow"])
                    glow.putpixel((x0 + x, 12 + y), p["glow"])
    return metal, glow


# --- items ---

def ring_item(corps, rgb):
    """32x32 inventory icon: a chunky band with an octagonal face showing the corps logo."""
    p = palette(corps, rgb)
    img = Image.new("RGBA", (32, 32), CLEAR)
    d = ImageDraw.Draw(img)
    metal, metal_dark, metal_light = p["metal"], p["metal_dark"], shade(p["metal"][:3], 1.3)
    # band (seen at an angle) with light strips
    d.ellipse((3, 14, 28, 30), fill=metal_dark)
    d.ellipse((5, 15, 26, 29), fill=metal)
    d.ellipse((9, 18, 22, 27), fill=CLEAR)
    for x in (6, 25):
        d.line((x, 21, x, 24), fill=p["glow"])
    # octagonal face
    o = [(10, 1), (21, 1), (28, 8), (28, 18), (21, 25), (10, 25), (3, 18), (3, 8)]
    d.polygon(o, fill=metal_dark)
    d.polygon([(11, 3), (20, 3), (26, 9), (26, 17), (20, 23), (11, 23), (5, 17), (5, 9)], fill=p["main"])
    d.polygon([(12, 5), (19, 5), (24, 10), (24, 16), (19, 21), (12, 21), (7, 16), (7, 10)], fill=p["disc"])
    for y, row in enumerate(LOGOS[corps]):
        for x, ch in enumerate(row):
            if ch == "#":
                img.putpixel((10 + x, 8 + y), p["glow"])
    d.line((11, 2, 20, 2), fill=metal_light)
    return img


# --- power battery lantern ---------------------------------------------------------------

def battery_textures(corps, rgb):
    """16x16 block textures for the lantern: painted metal, a lighter trim, translucent glowing
    glass, the logo core and the wire handle."""
    p = palette(corps, rgb)
    metal = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            edge = x in (0, 15) or y in (0, 15)
            hi = (x + y) % 7 == 0
            c = p["dark"] if edge else (p["light"] if hi else p["main"])
            metal.putpixel((x, y), c)
    trim = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            trim.putpixel((x, y), p["light"] if y % 4 else p["main"])
    glass = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            edge = x in (0, 15) or y in (0, 15)
            streak = (x - y) % 9 == 0
            c = p["glow"][:3]
            glass.putpixel((x, y), c + ((230,) if edge else (200,) if streak else (120,)))
    core = Image.new("RGBA", (16, 16), mix(p["disc"], p["main"], 0.25))
    d = ImageDraw.Draw(core)
    d.rectangle((0, 0, 15, 15), outline=p["light"])
    for y, row in enumerate(LOGOS[corps]):
        for x, ch in enumerate(row):
            if ch == "#":
                core.putpixel((2 + x, 2 + y), WHITE if corps not in ("white",) else p["symbol"])
    handle_rgb = {"white": (222, 178, 76), "black": (185, 190, 200)}.get(corps, (238, 240, 236))
    handle = Image.new("RGBA", (16, 16), handle_rgb + (255,))
    ear = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            r = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** 0.5
            ear.putpixel((x, y), WHITE if r < 3 else (p["glow"] if r < 6 else p["light"]))
    return {"metal": metal, "trim": trim, "glass": glass, "core": core, "handle": handle, "ear": ear}


def battery_model(corps):
    """The Power Battery, after the lantern in the Green Lantern mod showcase: a small lantern
    standing on a foot, a translucent glowing chamber with the corps logo inside, corner posts,
    two glowing side ears, a flared cap and a thin wire handle on top."""
    t = lambda name: f"greenlantern:block/{corps}_battery_{name}"  # noqa: E731
    bright = {"block_light": 15, "sky_light": 15}
    faces6 = ("north", "south", "east", "west", "up", "down")

    def cube(frm, to, tex, glow=False, faces=faces6):
        e = {"from": frm, "to": to, "faces": {f: {"texture": f"#{tex}"} for f in faces}}
        if tex in ("core", "ear", "glass"):  # the whole picture on each face, not a slice of it
            for face in e["faces"].values():
                face["uv"] = [0, 0, 16, 16]
        if glow:
            e["shade"] = False
            e["forge_data"] = bright
        return e

    elements = [
        # foot and base
        cube([5.5, 0, 5.5], [10.5, 1, 10.5], "metal"),
        cube([4.5, 1, 4.5], [11.5, 2.5, 11.5], "metal"),
        cube([4.5, 2.5, 4.5], [11.5, 3.5, 11.5], "trim"),
        # the glowing core with the logo, inside a glass chamber
        cube([5.5, 4, 5.5], [10.5, 9, 10.5], "core", glow=True),
        cube([4.6, 3.5, 4.6], [11.4, 9.5, 11.4], "glass", glow=True),
        # corner posts
        cube([4, 3.5, 4], [5, 9.5, 5], "metal"),
        cube([11, 3.5, 4], [12, 9.5, 5], "metal"),
        cube([4, 3.5, 11], [5, 9.5, 12], "metal"),
        cube([11, 3.5, 11], [12, 9.5, 12], "metal"),
        # side ears with glowing lenses
        cube([1.5, 5, 6.5], [4, 8, 9.5], "metal"),
        cube([1.2, 5.5, 7], [1.5, 7.5, 9], "ear", glow=True),
        cube([12, 5, 6.5], [14.5, 8, 9.5], "metal"),
        cube([14.5, 5.5, 7], [14.8, 7.5, 9], "ear", glow=True),
        # cap
        cube([4.5, 9.5, 4.5], [11.5, 10.5, 11.5], "trim"),
        cube([5, 10.5, 5], [11, 11.5, 11], "metal"),
        cube([6, 11.5, 6], [10, 12.5, 10], "metal"),
        cube([7, 12.5, 7], [9, 13.5, 9], "trim"),
        # wire handle
        cube([5.5, 11, 7.7], [6, 15.2, 8.3], "handle"),
        cube([10, 11, 7.7], [10.5, 15.2, 8.3], "handle"),
        cube([5.5, 15.2, 7.7], [10.5, 15.7, 8.3], "handle"),
    ]
    return {
        "parent": "minecraft:block/block",
        "render_type": "minecraft:translucent",
        "textures": {"particle": t("metal"), **{n: t(n) for n in ("metal", "trim", "glass", "core", "handle", "ear")}},
        "elements": elements,
        "display": {
            "thirdperson_righthand": {"rotation": [0, 45, 0], "translation": [0, 1.5, 1], "scale": [0.5, 0.5, 0.5]},
            "thirdperson_lefthand": {"rotation": [0, 45, 0], "translation": [0, 1.5, 1], "scale": [0.5, 0.5, 0.5]},
            "firstperson_righthand": {"rotation": [0, 45, 0], "translation": [0, 2, 0], "scale": [0.5, 0.5, 0.5]},
            "firstperson_lefthand": {"rotation": [0, 45, 0], "translation": [0, 2, 0], "scale": [0.5, 0.5, 0.5]},
            "gui": {"rotation": [20, 225, 0], "translation": [0, 0.5, 0], "scale": [0.8, 0.8, 0.8]},
            "ground": {"rotation": [0, 0, 0], "translation": [0, 3, 0], "scale": [0.5, 0.5, 0.5]},
            "fixed": {"rotation": [0, 0, 0], "translation": [0, 0, 0], "scale": [0.8, 0.8, 0.8]},
        },
    }


def logo_texture(corps_colors):
    """128x128 mod logo: the emotional spectrum around the lantern symbol."""
    img = Image.new("RGBA", (128, 128), (10, 12, 14, 255))
    d = ImageDraw.Draw(img)
    n = len(corps_colors)
    for i, rgb in enumerate(corps_colors):
        a = 360 / n
        d.pieslice((6, 6, 122, 122), i * a - 90, (i + 1) * a - 90, fill=tuple(rgb) + (255,))
    d.ellipse((22, 22, 106, 106), fill=(10, 12, 14, 255))
    for y, row in enumerate(LOGOS["green"]):
        for x, ch in enumerate(row):
            if ch == "#":
                d.rectangle((31 + x * 6, 31 + y * 6, 36 + x * 6, 36 + y * 6), fill=(240, 255, 240, 255))
    return img


# --- hard-light constructs (3D item models shown by display entities) --------------------

def _box(frm, to):
    return {"from": frm, "to": to, "faces": {f: {"texture": "#0", "uv": [0, 0, 16, 16]}
                                             for f in ("north", "south", "east", "west", "up", "down")}}


def construct_shapes():
    """Shape name -> list of elements in a 16x16x16 box, centered on (8, 8, 8). Shapes face -z:
    an item_display turns its item half a turn, so a model's -z side faces the entity's facing
    direction (the fist's knuckles sit at low z for that reason)."""
    fist = [
        _box([3, 3, 5], [13, 11, 13]),     # back of the hand
        _box([3, 11, 4], [5.4, 14, 11]),   # four curled fingers
        _box([5.6, 11, 4], [8, 14.5, 11]),
        _box([8.2, 11, 4], [10.6, 14.5, 11]),
        _box([10.8, 11, 4], [13, 14, 11]),
        _box([3, 9, 2], [13, 11.5, 5]),    # knuckle ridge
        _box([12.5, 5, 6], [15, 10, 11]),  # thumb
        _box([5, 0, 6], [11, 3, 12]),      # wrist
    ]
    hammer = [
        _box([7, 0, 7], [9, 10, 9]),       # handle
        _box([2, 10, 4], [14, 16, 12]),    # head
        _box([1, 11, 5], [2, 15, 11]),     # striking faces
        _box([14, 11, 5], [15, 15, 11]),
    ]
    cage = []
    for x, z in ((1, 1), (14, 1), (1, 14), (14, 14), (7.5, 1), (7.5, 14), (1, 7.5), (14, 7.5)):
        cage.append(_box([x, 0, z], [x + 1, 16, z + 1]))  # bars
    cage += [_box([1, 0, 1], [15, 1, 15]), _box([1, 15, 1], [15, 16, 15])]  # floor and roof frame
    wall = [
        _box([0, 0, 7], [16, 16, 9]),      # slab
        _box([0, 0, 6.5], [16, 1, 9.5]), _box([0, 15, 6.5], [16, 16, 9.5]),  # frame
        _box([0, 0, 6.5], [1, 16, 9.5]), _box([15, 0, 6.5], [16, 16, 9.5]),
        _box([5, 5, 6], [11, 11, 10]),     # boss in the middle
    ]
    claw = [
        _box([7, 0, 7], [9, 8, 9]),        # shaft
        _box([3, 8, 7], [13, 10, 9]),      # crossbar
        _box([3, 10, 7], [5, 15, 9]), _box([3.5, 15, 7.5], [4.5, 16, 8.5]),   # three hooked prongs
        _box([7, 10, 7], [9, 16, 9]),
        _box([11, 10, 7], [13, 15, 9]), _box([11.5, 15, 7.5], [12.5, 16, 8.5]),
    ]
    crystal = [
        _box([6, 0, 6], [10, 14, 10]), _box([7, 14, 7], [9, 16, 9]),          # central spire
        _box([2, 0, 3], [5, 9, 6]), _box([2.8, 9, 3.8], [4.2, 11, 5.2]),        # side shards
        _box([11, 0, 9], [14, 10, 12]), _box([11.8, 10, 9.8], [13.2, 12, 11.2]),
        _box([9, 0, 2], [11, 6, 4]), _box([4, 0, 11], [7, 7, 14]),
    ]
    spike = [_box([5.5, 0, 5.5], [10.5, 6, 10.5]), _box([6.5, 6, 6.5], [9.5, 11, 9.5]),
             _box([7.25, 11, 7.25], [8.75, 15, 8.75]), _box([7.6, 15, 7.6], [8.4, 16, 8.4])]
    hand = [_box([3, 2, 6], [13, 10, 10]),                       # palm, reaching out
            _box([5, -1, 6.5], [11, 2, 9.5]),                    # wrist
            _box([13, 4, 6.5], [15.5, 9, 9.5]), _box([14.5, 9, 6.5], [16, 11, 9.5])]   # thumb
    for x0, x1 in ((3, 5.2), (5.6, 7.8), (8.2, 10.4), (10.8, 13)):  # grasping fingers
        hand += [_box([x0, 10, 6.5], [x1, 15, 9.5]), _box([x0, 15, 9.5], [x1, 16.5, 12.5])]
    # the train (and the grasping hand above) are built facing +z, then mirrored to face -z; the
    # train is lifted 8 units so its wheels sit at the display's feet
    train = [_box([2, 0, -4], [14, 2, 20]),                       # chassis
             _box([3, 2, -4], [13, 12, 4]), _box([2, 12, -5], [14, 13, 5]),    # cab and roof
             _box([4, 2, 4], [12, 10, 18]),                      # boiler
             _box([6.5, 10, 13], [9.5, 15, 16]),                 # smokestack
             _box([3, 0, 18], [13, 3, 21]),                      # cowcatcher
             _box([6, 5, 18], [10, 8, 18.5])]                    # headlamp
    for z in (-2, 6, 14):
        train += [_box([1, -2, z], [2, 2, z + 4]), _box([14, -2, z], [15, 2, z + 4])]  # wheels
    train = [_moved(_mirrored_z(e), dy=8) for e in train]
    hand = [_mirrored_z(e) for e in hand]
    ball = [_box([3, 3, 3], [13, 13, 13]), _box([5, 1, 5], [11, 15, 11]),
            _box([1, 5, 5], [15, 11, 11]), _box([5, 5, 1], [11, 11, 15])]
    shapes = {"fist": fist, "hammer": hammer, "cage": cage, "wall": wall, "claw": claw, "crystal": crystal,
              "spike": spike, "hand": hand, "train": train, "ball": ball}
    for elements in shapes.values():  # hard light glows wherever it is drawn (displays, projectiles)
        for e in elements:
            e["shade"] = False
            e["forge_data"] = {"block_light": 15, "sky_light": 15}
    return shapes


def _mirrored_z(e):
    e = dict(e)
    e["from"], e["to"] = [e["from"][0], e["from"][1], 16 - e["to"][2]], [e["to"][0], e["to"][1], 16 - e["from"][2]]
    return e


def _moved(e, dy):
    e = dict(e)
    e["from"], e["to"] = [e["from"][0], e["from"][1] + dy, e["from"][2]], [e["to"][0], e["to"][1] + dy, e["to"][2]]
    return e


# the cannonball is drawn as a projectile's GROUND item, centered on its feet: lift it into its hitbox
SHAPE_DISPLAY = {"ball": {"ground": {"rotation": [0, 0, 0], "translation": [0, 8, 0], "scale": [1, 1, 1]}}}


def _glow_box(frm, to, angle=-45):
    """A bright hard-light box, rotated about the model center like a handheld item's diagonal."""
    e = _box(frm, to)
    e["shade"] = False
    e["forge_data"] = {"block_light": 15, "sky_light": 15}
    if angle:
        e["rotation"] = {"angle": angle, "axis": "z", "origin": [8, 8, 8]}
    return e


# Display transforms of vanilla item/handheld (with item/generated), for 3D models laid out in
# the same plane as a handheld sprite: the grip at the bottom left, the tip at the top right.
HANDHELD_DISPLAY = {
    "thirdperson_righthand": {"rotation": [0, -90, 55], "translation": [0, 4.0, 0.5], "scale": [0.85, 0.85, 0.85]},
    "thirdperson_lefthand": {"rotation": [0, 90, -55], "translation": [0, 4.0, 0.5], "scale": [0.85, 0.85, 0.85]},
    "firstperson_righthand": {"rotation": [0, -90, 25], "translation": [1.13, 3.2, 1.13], "scale": [0.68, 0.68, 0.68]},
    "firstperson_lefthand": {"rotation": [0, 90, -25], "translation": [1.13, 3.2, 1.13], "scale": [0.68, 0.68, 0.68]},
    "ground": {"rotation": [0, 0, 0], "translation": [0, 2, 0], "scale": [0.5, 0.5, 0.5]},
    "head": {"rotation": [0, 180, 0], "translation": [0, 13, 7], "scale": [1, 1, 1]},
    "fixed": {"rotation": [0, 180, 0], "translation": [0, 0, 0], "scale": [1, 1, 1]},
    "gui": {"rotation": [0, 0, 0], "translation": [0, 0, 0], "scale": [0.85, 0.85, 0.85]},
}
# vanilla shield.json / shield_blocking.json; the plate is laid out like the shield's builtin model
SHIELD_DISPLAY = {
    "thirdperson_righthand": {"rotation": [0, 90, 0], "translation": [10, 6, -4], "scale": [1, 1, 1]},
    "thirdperson_lefthand": {"rotation": [0, 90, 0], "translation": [10, 6, 12], "scale": [1, 1, 1]},
    "firstperson_righthand": {"rotation": [0, 180, 5], "translation": [-10, 2, -10], "scale": [1.25, 1.25, 1.25]},
    "firstperson_lefthand": {"rotation": [0, 180, 5], "translation": [10, 0, -10], "scale": [1.25, 1.25, 1.25]},
    "gui": {"rotation": [15, -25, -5], "translation": [2, 3, 0], "scale": [0.65, 0.65, 0.65]},
    "fixed": {"rotation": [0, 180, 0], "translation": [-2, 4, -5], "scale": [0.5, 0.5, 0.5]},
    "ground": {"rotation": [0, 0, 0], "translation": [4, 4, 2], "scale": [0.25, 0.25, 0.25]},
}
SHIELD_BLOCKING_DISPLAY = {
    **SHIELD_DISPLAY,
    "thirdperson_righthand": {"rotation": [45, 135, 0], "translation": [3.51, 11, -2], "scale": [1, 1, 1]},
    "thirdperson_lefthand": {"rotation": [45, 135, 0], "translation": [13.51, 3, 5], "scale": [1, 1, 1]},
    "firstperson_righthand": {"rotation": [0, 180, -5], "translation": [-15, 5, -11], "scale": [1.25, 1.25, 1.25]},
    "firstperson_lefthand": {"rotation": [0, 180, -5], "translation": [5, 5, -11], "scale": [1.25, 1.25, 1.25]},
}


def held_construct_models():
    """Item -> (elements, display) for the constructs you hold. Weapons are built upright along
    +y (grip at the bottom), then turned -45 degrees so they lie like a handheld sprite."""
    g = _glow_box
    sword = [g([7, -3, 7], [9, -1, 9]), g([7.5, -1, 7.5], [8.5, 4, 8.5]), g([4.5, 4, 7], [11.5, 5.5, 9]),
             g([7, 5.5, 7.5], [9, 17, 8.5]), g([7.5, 17, 7.6], [8.5, 19, 8.4]), g([7.8, 6, 7.3], [8.2, 16, 8.7])]
    mace = [g([7.5, -3, 7.5], [8.5, 8, 8.5]), g([7, 7, 7], [9, 8.5, 9]), g([5, 8.5, 5], [11, 14.5, 11]),
            g([3.8, 10.5, 7.4], [5, 12.5, 8.6]), g([11, 10.5, 7.4], [12.2, 12.5, 8.6]),
            g([7.4, 14.5, 7.4], [8.6, 16, 8.6]), g([7.4, 10.5, 3.8], [8.6, 12.5, 5]), g([7.4, 10.5, 11], [8.6, 12.5, 12.2])]
    axe = [g([7.5, -3, 7.5], [8.5, 16, 8.5]), g([8.5, 9, 7.6], [12.5, 15.5, 8.4]), g([12.5, 8, 7.7], [13.6, 16.5, 8.3]),
           g([5, 11, 7.7], [7.5, 13, 8.3]), g([7, 15, 7], [9, 16.5, 9])]
    drill = [g([7.5, -3, 7.5], [8.5, 6, 8.5]), g([5.5, 6, 5.5], [10.5, 10, 10.5]), g([6.5, 10, 6.5], [9.5, 13, 9.5]),
             g([7, 13, 7], [9, 16, 9]), g([7.5, 16, 7.5], [8.5, 18.5, 8.5]), g([5.2, 7, 7.5], [5.5, 9, 8.5])]
    gatling = [g([7.5, -2, 7], [9, 3, 9]), g([6, 3, 6], [10, 8, 10]),
               g([6.5, 8, 7], [7.5, 18, 8]), g([8.5, 8, 7], [9.5, 18, 8]), g([7.5, 8, 8.2], [8.5, 18, 9.2]),
               g([7.5, 8, 5.8], [8.5, 18, 6.8]), g([5.8, 15, 5.8], [10.2, 16, 10.2]), g([5.8, 10, 5.8], [10.2, 11, 10.2])]
    claws = [g([7, -2, 7], [9, 4, 9]), g([5, 4, 7], [11, 6, 9]),
             g([5.2, 6, 7.6], [6.2, 16, 8.4]), g([7.5, 6, 7.6], [8.5, 18, 8.4]), g([9.8, 6, 7.6], [10.8, 16, 8.4])]
    staff = [g([7.5, -8, 7.5], [8.5, 17, 8.5]), g([6, 17, 7.5], [10, 18, 8.5]), g([6, 18, 7.5], [7, 22, 8.5]),
             g([9, 18, 7.5], [10, 22, 8.5]), g([6, 22, 7.5], [10, 23, 8.5]), g([7, 18.5, 7], [9, 21, 9]),
             g([7, -9, 7], [9, -8, 9])]
    shield = [g([-6, -11, 1], [6, 11, 2], 0), g([-1, -3, -5], [1, 3, 1], 0),
              g([-6.5, -11.5, 0.8], [6.5, -10.5, 2.2], 0), g([-6.5, 10.5, 0.8], [6.5, 11.5, 2.2], 0),
              g([-6.5, -10.5, 0.8], [-5.5, 10.5, 2.2], 0), g([5.5, -10.5, 0.8], [6.5, 10.5, 2.2], 0),
              g([-2.5, -2.5, 2], [2.5, 2.5, 2.6], 0)]
    return {"construct_sword": (sword, HANDHELD_DISPLAY), "construct_mace": (mace, HANDHELD_DISPLAY),
            "construct_axe": (axe, HANDHELD_DISPLAY), "construct_drill": (drill, HANDHELD_DISPLAY),
            "construct_gatling": (gatling, HANDHELD_DISPLAY), "construct_claws": (claws, HANDHELD_DISPLAY),
            "construct_staff": (staff, {**HANDHELD_DISPLAY, "gui": {"rotation": [0, 0, 0], "translation": [0, 0, 0],
                                                                  "scale": [0.6, 0.6, 0.6]}}),
            "construct_shield": (shield, SHIELD_DISPLAY)}


def construct_block_texture(corps, rgb, hardlight=False):
    """Placeable construct blocks: a bright frame around soft light. Hard-light walls (barrier,
    dome, bridge) get a lattice so they read as a force field."""
    p = palette(corps, rgb)
    img = Image.new("RGBA", (16, 16))
    dark = corps == "black"
    for y in range(16):
        for x in range(16):
            edge = x in (0, 15) or y in (0, 15)
            inner = x in (1, 14) or y in (1, 14)
            lattice = hardlight and ((x + y) % 5 == 0 or (x - y) % 5 == 0)
            if dark:
                c, a = ((190, 196, 210), 235) if edge or lattice else ((24, 24, 30), 190)
            elif edge:
                c, a = p["light"][:3], 240
            elif inner or lattice:
                c, a = p["glow"][:3], 200
            else:
                c, a = p["main"][:3], 110 if hardlight else 140
            img.putpixel((x, y), c + (a,))
    return img


def construct_block_model(texture):
    bright = {"block_light": 15, "sky_light": 15}
    return {
        "parent": "minecraft:block/block",
        "render_type": "minecraft:translucent",
        "textures": {"all": texture, "particle": texture},
        "elements": [{"from": [0, 0, 0], "to": [16, 16, 16], "shade": False, "forge_data": bright,
                      "faces": {d: {"texture": "#all", "cullface": d}
                                for d in ("north", "south", "east", "west", "up", "down")}}],
    }


def scuba_model():
    """Scuba Gear: a hard-light diving bubble around the head and an air tank on the back."""
    empty = {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "cubes": [], "children": {}}
    mesh = {part: empty for part in ("hat", "right_arm", "left_arm", "right_leg", "left_leg")}
    mesh["head"] = {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "children": {},
                    "cubes": [{"origin": [-5, -9.5, -5], "dimensions": [10, 10, 10], "texture_offset": [0, 0]}]}
    mesh["body"] = {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "children": {},
                    "cubes": [{"origin": [-3, 1, 2.6], "dimensions": [6, 7, 3], "texture_offset": [0, 20]},
                              {"origin": [-1, -1, 3.1], "dimensions": [2, 2, 2], "texture_offset": [20, 20]}]}
    return {"texture_width": 64, "texture_height": 32, "mesh": mesh}


def scuba_texture(corps, rgb):
    p = palette(corps, rgb)
    img = Image.new("RGBA", (64, 32), CLEAR)
    for y in range(20):
        for x in range(40):  # the bubble: faint glass with bright rims
            u, v = x % 10, y % 10
            rim = u in (0, 9) or v in (0, 9)
            img.putpixel((x, y), p["glow"][:3] + ((200,) if rim else (60,)))
    for y in range(20, 30):
        for x in range(18):  # the tank: solid light with bands
            band = (y - 20) % 4 == 0
            img.putpixel((x, y), (p["light"] if band else p["main"])[:3] + (230,))
    for y in range(20, 24):
        for x in range(20, 28):  # valve
            img.putpixel((x, y), p["metal"][:3] + (255,))
    return img


DIGITS = {"1": [".#.", "##.", ".#.", ".#.", "###"], "2": ["##.", "..#", ".#.", "#..", "###"],
          "3": ["##.", "..#", ".#.", "..#", "##."], "4": ["#.#", "#.#", "###", "..#", "..#"],
          "5": ["###", "#..", "##.", "..#", "##."]}


def construct_slot_icon(corps, rgb, n):
    """16x16 icon for Construct n on the ability bar: a hard-light diamond with the slot number."""
    p = palette(corps, rgb)
    img = Image.new("RGBA", (16, 16), CLEAR)
    d = ImageDraw.Draw(img)
    d.polygon([(8, 0), (15, 7), (8, 15), (1, 7)], fill=p["dark"], outline=p["glow"])
    d.polygon([(8, 3), (12, 7), (8, 12), (4, 7)], fill=p["main"])
    for y, row in enumerate(DIGITS[str(n)]):
        for x, ch in enumerate(row):
            if ch == "#":
                img.putpixel((7 + x, 5 + y), WHITE)
    return img


def construct_texture(corps, rgb):
    """Translucent hard light: bright edges, softer middle. Black Lantern constructs are
    corrupted: near-black with pale cracks running through them."""
    p = palette(corps, rgb)
    if corps == "black":
        img = Image.new("RGBA", (16, 16))
        for y in range(16):
            for x in range(16):
                crack = (x * 3 + y * 5) % 13 == 0 or (x - y) % 11 == 0
                edge = x in (0, 15) or y in (0, 15)
                c = (190, 196, 210) if crack else ((70, 72, 82) if edge else (24, 24, 30))
                img.putpixel((x, y), c + (235 if edge or crack else 205,))
        return img
    img = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            edge = x in (0, 15) or y in (0, 15)
            c = p["light"] if edge else (p["glow"] if (x + y) % 6 == 0 else p["main"])
            img.putpixel((x, y), c[:3] + ((235,) if edge else (170,)))
    return img


def rage_overlay():
    """256x256 screen overlay: a pulsing-red vignette for Red Lantern rage."""
    img = Image.new("RGBA", (256, 256))
    for y in range(256):
        for x in range(256):
            r = (((x - 127.5) / 127.5) ** 2 + ((y - 127.5) / 127.5) ** 2) ** 0.5
            a = max(0.0, min(1.0, (r - 0.55) / 0.6))
            img.putpixel((x, y), (190, 10, 15, int(170 * a)))
    return img


def menu_background(corps, rgb):
    """16x16 tile for the powers menu: dark stone with a faint corps-colored grid."""
    p = palette(corps, rgb)
    img = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            base = mix((18, 19, 22), p["main"], 0.12)
            if x == 0 or y == 0:
                base = mix((18, 19, 22), p["main"], 0.35)
            n = ((x * 7 + y * 13) % 5) * 2
            img.putpixel((x, y), tuple(min(255, v + n) for v in base[:3]) + (255,))
    return img
