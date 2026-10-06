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


def palette(corps, rgb):
    p = {
        "main": shade(rgb, 1.0), "light": shade(rgb, 1.3), "dark": shade(rgb, 0.62), "deep": shade(rgb, 0.38),
        "trim": (22, 24, 27, 255), "trim2": (36, 39, 44, 255), "symbol": WHITE, "glow": shade(rgb, 1.4),
        "disc": (14, 15, 17, 255),
    }
    if corps == "white":  # white suit, silver trim, glowing white symbol on a dark disc
        p.update(main=(232, 236, 242, 255), light=(255, 255, 255, 255), dark=(178, 184, 196, 255),
                 deep=(130, 136, 148, 255), trim=(200, 206, 216, 255), trim2=(188, 194, 206, 255),
                 symbol=(255, 255, 255, 255), glow=(255, 255, 255, 255), disc=(52, 58, 70, 255))
    if corps == "black":  # black suit, grey trim, pale glowing symbol
        p.update(main=(34, 35, 40, 255), light=(70, 72, 80, 255), dark=(22, 22, 26, 255), deep=(12, 12, 14, 255),
                 trim=(58, 60, 68, 255), trim2=(66, 68, 76, 255), symbol=(225, 230, 240, 255),
                 glow=(225, 232, 245, 255), disc=(8, 8, 10, 255))
    return p


# --- full-body uniform (skin replacement, 128x128 = 2x the vanilla skin layout) --------

S = 2  # pixels per skin texel


def box_faces(u, v, w, h, d):
    return {
        "top": (u + d, v, w, d), "bottom": (u + d + w, v, w, d), "right": (u, v + d, d, h),
        "front": (u + d, v + d, w, h), "left": (u + d + w, v + d, d, h), "back": (u + d + w + d, v + d, w, h),
    }


def paint_box(img, u, v, w, h, d, painter):
    """painter(face, x, y, face_w, face_h) is called per hi-res pixel."""
    for face, (fx, fy, fw, fh) in box_faces(u, v, w, h, d).items():
        fw, fh = fw * S, fh * S
        for y in range(fh):
            for x in range(fw):
                col = painter(face, x, y, fw, fh)
                if col is not None:
                    img.putpixel((fx * S + x, fy * S + y), col)


def logo_at(logo, x, y, ox, oy):
    lx, ly = x - ox, y - oy
    return 0 <= ly < len(logo) and 0 <= lx < len(logo[0]) and logo[ly][lx] == "#"


def uniform(corps, rgb, slim):
    """Returns (suit, glow) textures. The suit replaces the whole skin."""
    p = palette(corps, rgb)
    logo = LOGOS[corps]
    suit = Image.new("RGBA", (64 * S, 64 * S), CLEAR)
    glow = Image.new("RGBA", (64 * S, 64 * S), CLEAR)

    def head(face, x, y, w, h):
        if face == "top":
            return p["main"] if 2 < x < w - 3 else p["dark"]
        if face == "bottom":
            return p["dark"]
        mask = 6 <= y <= 9
        if face == "front":
            if mask:
                return WHITE if y in (7, 8) and (3 <= x <= 5 or 10 <= x <= 12) else p["trim"]
            if y >= 14:
                return p["dark"]
            return p["main"]
        if face in ("right", "left"):
            near_face = x >= w - 6 if face == "right" else x <= 5
            if mask and near_face:
                return p["trim"]
            return p["main"] if y < 13 else p["dark"]
        return p["main"] if 4 < x < w - 5 else p["dark"]  # back

    def body(face, x, y, w, h):
        if face == "top":
            return p["main"]
        if face == "bottom":
            return p["trim"]
        if y >= 20:  # belt
            return p["light"] if face == "front" and 6 <= x <= 9 and y in (21, 22) else p["trim"]
        if face in ("right", "left"):
            return p["main"] if 3 <= x <= 4 else p["trim"]
        if face == "front":
            if y <= 1:
                return p["light"]
            cx, cy = 7.5, 8
            if (x - cx) ** 2 + (y - cy) ** 2 <= 6.8 ** 2:  # disc behind the logo
                return p["symbol"] if logo_at(logo, x, y, 2, 3) else p["disc"]
            return p["main"] if 3 <= x <= 12 else p["trim"]
        return p["main"] if 3 <= x <= 12 else p["trim"]  # back

    def arm(face, x, y, w, h):
        if face == "top":
            return p["main"]
        if face == "bottom":
            return p["dark"]
        if y < 6:
            return p["main"] if y != 5 else p["dark"]  # shoulder
        if y >= 17:  # glove
            return p["dark"] if y == 17 or y == h - 1 else p["main"]
        return p["trim2"] if (x + y) % 9 == 0 else p["trim"]

    def leg(face, x, y, w, h):
        if face == "top":
            return p["main"]
        if face == "bottom":
            return p["deep"]
        if y >= 16:  # boot
            return p["dark"] if y == 16 else (p["deep"] if y >= h - 2 else p["main"])
        if face in ("right", "left"):
            return p["main"] if 3 <= x <= 4 else p["trim"]
        return p["main"] if 1 <= x <= w - 2 else p["trim"]

    def eyes(face, x, y, w, h):
        return WHITE if face == "front" and y in (7, 8) and (3 <= x <= 5 or 10 <= x <= 12) else None

    def emblem(face, x, y, w, h):
        return p["glow"] if face == "front" and 2 <= y <= 14 and logo_at(logo, x, y, 2, 3) else None

    aw = 3 if slim else 4
    for img, parts in ((suit, (head, body, arm, leg)), (glow, (eyes, emblem, None, None))):
        h_, b_, a_, l_ = parts
        paint_box(img, 0, 0, 8, 8, 8, h_)
        paint_box(img, 16, 16, 8, 12, 4, b_)
        if a_:
            paint_box(img, 40, 16, aw, 12, 4, a_)
            paint_box(img, 32, 48, aw, 12, 4, a_)
            paint_box(img, 0, 16, 4, 12, 4, l_)
            paint_box(img, 16, 48, 4, 12, 4, l_)
    return suit, glow


# --- ring worn on the hand (model layer + 32x32 textures) ------------------------------

def ring_model(slim):
    """A band around the right hand with a face plate on the back of the hand."""
    w = 3 if slim else 4
    x0 = -2 if slim else -3  # outer edge of the right arm
    empty = {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "cubes": [], "children": {}}
    return {
        "texture_width": 32,
        "texture_height": 32,
        "mesh": {
            "head": empty, "hat": empty, "body": empty, "left_arm": empty, "right_leg": empty, "left_leg": empty,
            "right_arm": {
                "part_pose": {"offset": [-5, 2 if not slim else 2.5, 0], "rotation": [0, 0, 0]},
                "cubes": [
                    {"origin": [x0, 7, -2], "dimensions": [w, 1, 4], "texture_offset": [0, 0],
                     "deformation": [0.35, 0.05, 0.35]},
                    {"origin": [x0 - 0.9, 6, -1.5], "dimensions": [1, 3, 3], "texture_offset": [0, 8],
                     "deformation": [0.05, 0.05, 0.05]},
                ],
                "children": {},
            },
        },
    }


def ring_textures(corps, rgb):
    """(band, gem) 32x32 textures for ring_model: band is metal, gem is the glowing face."""
    p = palette(corps, rgb)
    band = Image.new("RGBA", (32, 32), CLEAR)
    gem = Image.new("RGBA", (32, 32), CLEAR)
    metal, metal_dark = (120, 124, 130, 255), (78, 82, 88, 255)
    if corps == "white":
        metal, metal_dark = (225, 228, 235, 255), (180, 185, 195, 255)
    if corps == "black":
        metal, metal_dark = (50, 52, 58, 255), (30, 31, 35, 255)
    for x in range(16):  # band box: 4 wide, 1 tall, 4 deep -> region 16x5
        for y in range(5):
            band.putpixel((x, y), metal if (x + y) % 3 else metal_dark)
    for x in range(16):
        if x % 4 == 1:
            gem.putpixel((x, 4), p["glow"])  # light strips on the band
    # face plate box: 1 wide, 3 tall, 3 deep -> its side faces sit at y 11..13
    for x in range(8):
        for y in range(8, 14):
            band.putpixel((x, y), metal_dark)
    for x in range(8):
        for y in range(11, 14):
            gem.putpixel((x, y), WHITE if y == 12 and x in (1, 5) else p["glow"])
    return band, gem


# --- items -----------------------------------------------------------------------------

def ring_item(corps, rgb):
    """32x32 inventory icon: a chunky band with an octagonal face showing the corps logo."""
    p = palette(corps, rgb)
    img = Image.new("RGBA", (32, 32), CLEAR)
    d = ImageDraw.Draw(img)
    metal, metal_dark, metal_light = (110, 114, 122, 255), (60, 63, 70, 255), (160, 164, 172, 255)
    if corps == "white":
        metal, metal_dark, metal_light = (220, 224, 232, 255), (165, 170, 182, 255), (255, 255, 255, 255)
    if corps == "black":
        metal, metal_dark, metal_light = (48, 50, 56, 255), (24, 25, 28, 255), (90, 92, 100, 255)
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


def battery_textures(corps, rgb):
    """16x16 textures for the lantern block: stone, glowing core with logo, light beam."""
    p = palette(corps, rgb)
    stone = Image.new("RGBA", (16, 16))
    base = (64, 66, 72) if corps != "white" else (200, 204, 212)
    if corps == "black":
        base = (34, 35, 40)
    for y in range(16):
        for x in range(16):
            n = ((x * 7 + y * 13) ^ (x * y)) % 5
            edge = x in (0, 15) or y in (0, 15)
            c = tuple(max(0, v - 18) if edge else v - 6 + n * 4 for v in base)
            stone.putpixel((x, y), c + (255,))
    for x in range(2, 14):  # glowing seam
        stone.putpixel((x, 12), p["glow"])
    core = Image.new("RGBA", (16, 16), p["disc"])
    d = ImageDraw.Draw(core)
    d.ellipse((0, 0, 15, 15), outline=p["main"], width=1)
    for y, row in enumerate(LOGOS[corps]):
        for x, ch in enumerate(row):
            if ch == "#":
                core.putpixel((2 + x, 2 + y), p["glow"])
    light = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            light.putpixel((x, y), p["glow"] if 4 <= x <= 11 else p["main"])
    return stone, core, light


def battery_model(corps):
    """A stone shrine with four pillars, a glowing logo core and a beam of light."""
    ns = "greenlantern"
    t = lambda name: f"{ns}:block/{corps}_battery_{name}"  # noqa: E731

    def cube(frm, to, tex, faces=("north", "south", "east", "west", "up", "down")):
        return {"from": frm, "to": to, "faces": {f: {"texture": f"#{tex}"} for f in faces}}

    elements = [
        cube([1, 0, 1], [15, 3, 15], "stone"),
        cube([3, 3, 3], [13, 4, 13], "stone"),
    ]
    for x, z in ((1, 1), (12, 1), (1, 12), (12, 12)):
        elements.append(cube([x, 3, z], [x + 3, 13, z + 3], "stone"))
        elements.append(cube([x + 1, 13, z + 1], [x + 2, 15, z + 2], "light"))
    elements += [
        cube([4, 5, 4], [12, 12, 12], "core", ("north", "south", "east", "west")),
        cube([4, 5, 4], [12, 12, 12], "light", ("up", "down")),
        cube([7, 4, 7], [9, 5, 9], "light"),
        cube([7, 12, 7], [9, 16, 9], "light"),
    ]
    return {
        "parent": "minecraft:block/block",
        "render_type": "minecraft:cutout",
        "textures": {"particle": t("stone"), "stone": t("stone"), "core": t("core"), "light": t("light")},
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
