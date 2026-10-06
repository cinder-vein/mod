"""Textures and models for the Lantern Corps, drawn in code.

Used by gen_corps.py. Every corps gets the same shapes in its own colors,
with its own logo. Replace any generated PNG with hand-drawn art if you like,
but it will be overwritten the next time gen_corps.py runs unless you remove
that step there.
"""
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
        "main": shade(rgb, 1.0), "light": shade(rgb, 1.3), "dark": shade(rgb, 0.62), "deep": shade(rgb, 0.38),
        "trim": (22, 24, 27, 255), "trim2": (40, 43, 48, 255), "symbol": WHITE, "glow": shade(rgb, 1.4),
        "disc": (14, 15, 17, 255), "gold": GOLD, "metal": (110, 114, 122, 255), "metal_dark": (60, 63, 70, 255),
    }
    if corps == "white":  # white plates on black, glowing white symbol on a dark disc
        p.update(main=(232, 236, 242, 255), light=(255, 255, 255, 255), dark=(178, 184, 196, 255),
                 deep=(130, 136, 148, 255), symbol=(255, 255, 255, 255), glow=(255, 255, 255, 255),
                 disc=(52, 58, 70, 255), metal=(225, 228, 235, 255), metal_dark=(170, 175, 186, 255))
    if corps == "black":  # black and charcoal, pale glowing symbol and bones
        p.update(main=(58, 60, 68, 255), light=(92, 95, 105, 255), dark=(36, 37, 42, 255), deep=(16, 16, 18, 255),
                 trim=(14, 14, 16, 255), trim2=(28, 29, 33, 255), symbol=(225, 230, 240, 255),
                 glow=(215, 222, 235, 255), disc=(6, 6, 8, 255), metal=(50, 52, 58, 255), metal_dark=(28, 29, 33, 255))
    return p


# --- suits ---------------------------------------------------------------------------------
# A suit is a skin overlay drawn at 2x (128x128). It leaves the head open except for an
# optional mask or hood, so the wearer's face and hair stay visible. Painters return a
# palette key; keys in GLOWING are also drawn into a full-bright glow layer.

S = 2  # pixels per skin texel
GLOWING = {"line", "symbol", "gem"}

# Suit designs per corps: (id, name). The first one is the default.
STANDARD = [("corps", "Corps Uniform"), ("classic", "Classic"), ("armored", "Armored")]
DESIGNS = {c: list(STANDARD) for c in LOGOS}
DESIGNS["violet"] = [("gown", "Sapphire Gown")] + STANDARD
DESIGNS["indigo"] = [("robes", "Tribal Robes")] + STANDARD
DESIGNS["black"] = [("risen", "Risen")] + STANDARD


def box_faces(u, v, w, h, d):
    return {
        "top": (u + d, v, w, d), "bottom": (u + d + w, v, w, d), "right": (u, v + d, d, h),
        "front": (u + d, v + d, w, h), "left": (u + d + w, v + d, d, h), "back": (u + d + w + d, v + d, w, h),
    }


def paint_box(imgs, colors, u, v, w, h, d, painter):
    """painter(face, x, y, face_w, face_h) -> palette key or None, per hi-res pixel."""
    suit, glow = imgs
    for face, (fx, fy, fw, fh) in box_faces(u, v, w, h, d).items():
        fw, fh = fw * S, fh * S
        for y in range(fh):
            for x in range(fw):
                key = painter(face, x, y, fw, fh)
                if key is None:
                    continue
                pos = (fx * S + x, fy * S + y)
                suit.putpixel(pos, colors[key])
                if key in GLOWING:
                    glow.putpixel(pos, colors["glow"] if key != "symbol" else colors["symbol"])


def logo_at(logo, x, y, ox, oy):
    lx, ly = x - ox, y - oy
    return 0 <= ly < len(logo) and 0 <= lx < len(logo[0]) and logo[ly][lx] == "#"


def chest(logo, x, y):
    """The logo on a disc in the middle of the chest, or None outside the disc."""
    if (x - 7.5) ** 2 + (y - 8.5) ** 2 <= 6.4 ** 2:
        return "symbol" if logo_at(logo, x, y, 2, 3) else "disc"
    return None


def mask(face, x, y, w, h, key="main"):
    """Domino mask with eye holes, so the wearer's eyes show through."""
    if face == "front" and 6 <= y <= 10:
        if y in (8, 9) and (2 <= x <= 5 or 10 <= x <= 13):
            return None
        return key
    if face == "right" and 7 <= y <= 9 and x >= w - 4:
        return key
    if face == "left" and 7 <= y <= 9 and x <= 3:
        return key
    return None


def design_corps(logo):
    """Black suit with glowing corps lines and plates (the corps-standard look)."""
    def head(f, x, y, w, h):
        return mask(f, x, y, w, h)

    def body(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom" or y >= 22:
            return "trim"
        if 19 <= y <= 21:
            return "main" if f == "front" and 6 <= x <= 9 else "trim2"  # belt and buckle
        if f == "front":
            c = chest(logo, x, y)
            if c:
                return c
            if y <= 1:
                return "dark"
            if 2 <= y <= 14 and (x == round(1 + (y - 2) * 0.45) or x == 14 - round((y - 2) * 0.45)):
                return "line"
            return "main" if x in (0, 15) and y >= 2 else "trim"
        if f == "back":
            return "main" if 2 <= x <= 4 or 11 <= x <= 13 else ("line" if x in (7, 8) and y < 18 else "trim")
        return "main" if x in (3, 4) else "trim"

    def arm(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom":
            return "trim"
        if y < 5:
            return "main"
        if y == 5 or y == 16:
            return "dark"
        if y == 11:
            return "line"
        if 17 <= y <= 21:
            return "main"
        return "trim"

    def leg(f, x, y, w, h):
        if f == "top":
            return "trim2"
        if f == "bottom" or y >= 22:
            return "deep"
        if y >= 17:
            return "dark" if y == 17 else "main"  # boots
        if 9 <= y <= 12 and f == "front":
            return "dark" if y == 9 else "main"  # knee
        if f == "front" and x in (3, 4) and 2 <= y <= 8:
            return "line"
        if f in ("right", "left") and x in (3, 4):
            return "main"
        return "trim"

    return head, body, arm, leg


def design_classic(logo):
    """Mostly corps color with black sides, like the comics."""
    def head(f, x, y, w, h):
        return mask(f, x, y, w, h, "dark")

    def body(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom" or 19 <= y <= 21:
            return "trim"
        if f == "front":
            c = chest(logo, x, y)
            if c:
                return c
            if y <= 1:
                return "light"
        if f in ("front", "back"):
            return "main" if 3 <= x <= 12 else "trim"
        return "main" if y < 4 else "trim"

    def arm(f, x, y, w, h):
        if f == "top" or y < 6:
            return "main"
        if f == "bottom" or y == 16:
            return "dark"
        return "main" if y > 16 else "trim"

    def leg(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom" or y >= 22:
            return "deep"
        if y >= 17:
            return "dark" if y == 17 else "main"
        if f in ("right", "left"):
            return "trim"
        return "trim" if x in (0, w - 1) else "main"

    return head, body, arm, leg


def design_armored(logo):
    """Heavy plates over a black under-suit, no mask."""
    def head(f, x, y, w, h):
        return None

    def body(f, x, y, w, h):
        if f == "top":
            return "light"
        if f == "bottom" or y >= 22:
            return "trim"
        if 18 <= y <= 21:
            return "line" if f == "front" and 7 <= x <= 8 and y in (19, 20) else "trim2"
        if f == "front":
            c = chest(logo, x, y)
            if c:
                return c
            if 2 <= y <= 17 and 1 <= x <= 14:
                if x in (1, 14) or y == 17:
                    return "dark"
                return "line" if y == 15 and 3 <= x <= 12 else "main"
            return "trim"
        if f == "back":
            if 2 <= y <= 16 and 2 <= x <= 13:
                return "dark" if x in (2, 13) or y == 16 else "main"
            return "trim"
        return "dark" if 2 <= y <= 10 else "trim"

    def arm(f, x, y, w, h):
        if f == "top" or y < 6:
            return "light"
        if y == 6 or y in (13, 21):
            return "dark"
        if 14 <= y <= 20:
            return "line" if y == 17 else "main"
        if f == "bottom":
            return "trim"
        return "trim"

    def leg(f, x, y, w, h):
        if f == "top":
            return "trim2"
        if f == "bottom" or y >= 22:
            return "deep"
        if 9 <= y <= 12:
            return "light" if y == 9 else "main"
        if y >= 13:
            return "line" if f == "front" and x in (3, 4) and 14 <= y <= 20 else "main"
        if f == "front" and 1 <= x <= w - 2:
            return "dark"
        return "trim"

    return head, body, arm, leg


def design_gown(logo):
    """Star Sapphire: a flowing gown with gold trim and a jewelled circlet."""
    def head(f, x, y, w, h):
        if y in (2, 3) and f in ("front", "left", "right", "back"):
            return "gem" if f == "front" and 7 <= x <= 8 else "gold"
        return None

    def body(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom":
            return "dark"
        if y in (18, 19):
            return "gold"
        if f == "front":
            c = chest(logo, x, y)
            if c:
                return c
            if y < 14 and (x == round(7.5 - (14 - y) * 0.5) or x == round(7.5 + (14 - y) * 0.5)):
                return "gold"
            if x in (0, 15):
                return "gold"
        return "main" if y < 18 else "dark"

    def arm(f, x, y, w, h):
        if f == "top" or y < 3:
            return "gold" if y == 2 else "main"
        if y in (19, 20):
            return "gold"
        if f == "bottom" or y > 20:
            return "light"
        return "main" if (x + y) % 6 else "dark"

    def leg(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom" or y >= 22:
            return "deep"
        if y in (20, 21):
            return "gold"
        return "dark" if x % 3 == 0 else "main"

    return head, body, arm, leg


def design_robes(logo):
    """Indigo Tribe: hooded robes with a sash. The hood frames the face without covering it."""
    def head(f, x, y, w, h):
        if f == "top" or f == "back":
            return "main" if (x + y) % 5 else "dark"
        if f == "front":
            return "gold" if y == 1 else ("main" if y == 0 else None)
        if f == "right":
            return "main" if x < w - 3 else None
        if f == "left":
            return "main" if x > 2 else None
        return None

    def body(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom":
            return "dark"
        if y in (18, 19):
            return "gold"
        if f == "front":
            c = chest(logo, x, y)
            if c:
                return c
            if abs(x - (y - 2)) <= 1 and y < 18:
                return "light"
        if f == "back" and y < 7:
            return "dark"
        return "main"

    def arm(f, x, y, w, h):
        if y in (18, 19):
            return "gold"
        if y >= 20:
            return "trim2"
        if f == "bottom":
            return "dark"
        return "main" if (x + y) % 7 else "dark"

    def leg(f, x, y, w, h):
        if f == "top":
            return "main"
        if f == "bottom" or y >= 22:
            return "deep"
        if y in (20, 21):
            return "gold"
        return "main" if x % 4 else "dark"

    return head, body, arm, leg


def design_risen(logo):
    """Black Lantern: a dead-black suit with pale glowing bones."""
    corps_head, corps_body, corps_arm, corps_leg = design_corps(logo)

    def head(f, x, y, w, h):
        return None

    def body(f, x, y, w, h):
        if f == "front" and 13 <= y <= 18 and y % 2 == 1 and 2 <= x <= 13 and x not in (7, 8):
            return "line"  # ribs
        if f == "front" and x in (7, 8) and 14 <= y <= 18:
            return "line"  # spine of the ribcage
        return corps_body(f, x, y, w, h)

    def arm(f, x, y, w, h):
        if f == "front" and 6 <= y <= 15 and x == w // 2:
            return "line"
        return corps_arm(f, x, y, w, h)

    def leg(f, x, y, w, h):
        if f == "front" and x in (3, 4) and 2 <= y <= 16 and y not in (9, 10, 11, 12):
            return "line"
        return corps_leg(f, x, y, w, h)

    return head, body, arm, leg


DESIGN_FUNCS = {"corps": design_corps, "classic": design_classic, "armored": design_armored,
                "gown": design_gown, "robes": design_robes, "risen": design_risen}


def suit(corps, rgb, design, slim):
    """Returns (suit, glow) 128x128 overlay textures."""
    p = palette(corps, rgb)
    imgs = (Image.new("RGBA", (64 * S, 64 * S), CLEAR), Image.new("RGBA", (64 * S, 64 * S), CLEAR))
    colors = {**p, "line": p["glow"], "gem": p["glow"]}
    head, body, arm, leg = DESIGN_FUNCS[design](LOGOS[corps])
    aw = 3 if slim else 4
    paint_box(imgs, colors, 0, 0, 8, 8, 8, head)
    paint_box(imgs, colors, 16, 16, 8, 12, 4, body)
    paint_box(imgs, colors, 40, 16, aw, 12, 4, arm)
    paint_box(imgs, colors, 32, 48, aw, 12, 4, arm)
    paint_box(imgs, colors, 0, 16, 4, 12, 4, leg)
    paint_box(imgs, colors, 16, 48, 4, 12, 4, leg)
    return imgs


def slot_icon(corps, rgb):
    """16x16 icon for the corps' suit slot in the accessories menu."""
    p = palette(corps, rgb)
    img = Image.new("RGBA", (16, 16), CLEAR)
    for y, row in enumerate(LOGOS[corps]):
        for x, ch in enumerate(row):
            if ch == "#":
                img.putpixel((2 + x, 2 + y), p["glow"])
    return img


# --- ring worn on the hand ------------------------------------------------------------------

def ring_model(slim):
    """A small signet ring at the knuckles of the right hand (not a bracelet).

    The right arm's outer side is -x; the hand ends at y=10. A thin band shows on
    the front and back of the hand, with a signet plate and glowing gem on the outside.
    """
    w = 3 if slim else 4
    x0 = -2 if slim else -3  # outer side of the right arm
    empty = {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "cubes": [], "children": {}}
    return {
        "texture_width": 16,
        "texture_height": 16,
        "mesh": {
            "head": empty, "hat": empty, "body": empty, "left_arm": empty, "right_leg": empty, "left_leg": empty,
            "right_arm": {
                "part_pose": {"offset": [-5, 2 if not slim else 2.5, 0], "rotation": [0, 0, 0]},
                "cubes": [
                    # band across the front and back of the fingers
                    {"origin": [x0, 8.6, -2.15], "dimensions": [1.4, 0.6, 0.2], "texture_offset": [0, 0]},
                    {"origin": [x0, 8.6, 1.95], "dimensions": [1.4, 0.6, 0.2], "texture_offset": [0, 0]},
                    # signet plate on the outside of the hand
                    {"origin": [x0 - 0.3, 8.2, -1.0], "dimensions": [0.3, 1.4, 2.0], "texture_offset": [0, 4]},
                    # gem
                    {"origin": [x0 - 0.5, 8.5, -0.6], "dimensions": [0.2, 0.8, 1.2], "texture_offset": [0, 10]},
                ],
                "children": {},
            },
        },
    }


def ring_textures(corps, rgb):
    """(band, gem) 16x16 textures for ring_model: metal parts and the glowing gem."""
    p = palette(corps, rgb)
    band = Image.new("RGBA", (16, 16), CLEAR)
    gem = Image.new("RGBA", (16, 16), CLEAR)
    for y in range(10):
        for x in range(16):
            band.putpixel((x, y), p["metal"] if (x + y) % 3 else p["metal_dark"])
    for y in range(10, 16):
        for x in range(16):
            gem.putpixel((x, y), p["glow"])
    return band, gem


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
    """16x16 block textures: stone body, metal frame, glowing lens and the logo plate."""
    p = palette(corps, rgb)
    base = {"white": (206, 210, 218), "black": (30, 31, 36)}.get(corps, tuple(int(36 + v * 0.12) for v in rgb))
    stone = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            n = ((x * 7 + y * 13) ^ (x * y)) % 5
            seam = y % 8 == 7 or (x + (y // 8) * 4) % 8 == 0  # brick-like blocks
            c = tuple(max(0, v - 16) if seam else v - 6 + n * 4 for v in base)
            stone.putpixel((x, y), c + (255,))
    for x in range(16):
        stone.putpixel((x, 3), p["glow"] if x % 4 else stone.getpixel((x, 3)))  # glowing seam
    metal = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            metal.putpixel((x, y), p["metal"] if (x + y) % 4 else p["metal_dark"])
    lens = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            r = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** 0.5
            lens.putpixel((x, y), p["glow"] if r < 2.5 else (p["light"] if r < 5 else (p["main"] if r < 7 else p["dark"])))
    core = Image.new("RGBA", (16, 16), p["disc"])
    d = ImageDraw.Draw(core)
    d.ellipse((0, 0, 15, 15), outline=p["main"], width=1)
    for y, row in enumerate(LOGOS[corps]):
        for x, ch in enumerate(row):
            if ch == "#":
                core.putpixel((2 + x, 2 + y), p["glow"])
    return {"stone": stone, "metal": metal, "lens": lens, "core": core}


def battery_model(corps):
    """The lantern from the reference art: a round stone body on a pedestal, a big glowing
    lens on the front, logo plates on the sides, a carrying arch and a glowing core column."""
    t = lambda name: f"greenlantern:block/{corps}_battery_{name}"  # noqa: E731
    bright = {"block_light": 15, "sky_light": 15}

    def cube(frm, to, tex, faces=("north", "south", "east", "west", "up", "down"), glow=False):
        e = {"from": frm, "to": to, "faces": {f: {"texture": f"#{tex}"} for f in faces}}
        if tex in ("lens", "core"):  # show the whole picture on each face, not a slice of it
            for face in e["faces"].values():
                face["uv"] = [0, 0, 16, 16]
        if glow:
            e["shade"] = False
            e["forge_data"] = bright
        return e

    elements = [
        # pedestal
        cube([3, 0, 3], [13, 1, 13], "stone"),
        cube([4, 1, 4], [12, 2, 12], "stone"),
        # rounded body: two crossed boxes plus a core
        cube([3, 2, 4], [13, 11, 12], "stone"),
        cube([4, 2, 3], [12, 11, 13], "stone"),
        cube([4, 11, 4], [12, 12, 12], "stone"),
        # front lens with a metal rim
        cube([4, 3, 2.5], [12, 10, 3], "metal"),
        cube([5, 4, 2], [11, 9, 2.5], "lens", glow=True),
        # back lens
        cube([5, 4, 13], [11, 9, 13.5], "lens", glow=True),
        # logo plates on both sides
        cube([12.8, 4, 5], [13.4, 10, 11], "core", ("east", "west", "north", "south", "up", "down"), glow=True),
        cube([2.6, 4, 5], [3.2, 10, 11], "core", ("east", "west", "north", "south", "up", "down"), glow=True),
        # glowing core column and cap
        cube([7, 12, 7], [9, 14, 9], "lens", glow=True),
        cube([5.5, 14, 5.5], [10.5, 15, 10.5], "metal"),
        # carrying arch over the top
        cube([1.5, 10.5, 7], [2.5, 13, 9], "metal"),
        cube([2.5, 10.5, 7], [3, 11.5, 9], "metal"),
        cube([2, 13, 7], [4, 14.5, 9], "metal"),
        cube([4, 14.5, 7], [12, 15.5, 9], "metal"),
        cube([12, 13, 7], [14, 14.5, 9], "metal"),
        cube([13.5, 10.5, 7], [14.5, 13, 9], "metal"),
        cube([13, 10.5, 7], [13.5, 11.5, 9], "metal"),
        cube([6.5, 15.5, 6.5], [9.5, 16, 9.5], "stone"),
    ]
    return {
        "parent": "minecraft:block/block",
        "render_type": "minecraft:cutout",
        "textures": {"particle": t("stone"), "stone": t("stone"), "metal": t("metal"), "lens": t("lens"),
                     "core": t("core")},
        "elements": elements,
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
