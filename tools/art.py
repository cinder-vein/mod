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
DESIGNS = {c: [("armored", "Corps Armor"), ("classic", "Classic"), ("stealth", "Stealth")] for c in LOGOS}

# Mask designs (id, name); "none" removes the mask. DEFAULT_MASK is used until one is picked.
MASKS = [("domino", "Domino Mask"), ("goggles", "Lens Goggles"), ("cowl", "Gem Cowl"), ("none", "No Mask")]
MASK_EXTRAS = {"black": [("deathly", "Deathly Pallor")]}  # corps-only masks
DEFAULT_MASK = {c: "domino" for c in LOGOS}
DEFAULT_MASK.update(violet="cowl", white="goggles", indigo="none", black="none")

# Texture offsets of the standard skin layout: part -> (inner uv, outer uv, w, h, d)
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


def emblem(corps, x, y, ox=1, oy=1, bg="main"):
    """Chest emblem pixels: "symbol" on the logo, `bg` around it, None outside."""
    m = MINI[corps]
    lx, ly = x - ox, y - oy
    if 0 <= ly < len(m) and 0 <= lx < len(m[0]):
        return "symbol" if m[ly][lx] == "#" else bg
    return None


def design_armored(corps):
    """Black under-suit with raised corps-colored armor: shoulder pads, a chest plate
    carrying the emblem, gauntlets, knee guards and boots. Hands stay bare."""
    tassets = corps == "violet"

    def paint(part, layer, f, x, y, w, h):
        if part == "head":
            return None
        if layer == "inner":
            if part == "body":
                if f == "top":
                    return "main"
                if f == "front":
                    if y == 9:
                        return "trim2"  # belt
                    return "main" if 2 <= x <= 5 and y < 9 else "trim"
                return "trim2" if y == 9 else "trim"
            if part.endswith("arm"):
                if y == h - 1 and f not in ("top", "bottom"):
                    return None  # bare hand
                if f == "bottom":
                    return None
                return "main" if 7 <= y <= 9 else "trim"
            if part.endswith("leg"):
                if y >= 9 or f == "bottom":
                    return "dark" if y == 9 else "main"  # boots
                if tassets and f == "front" and y <= 5:
                    return "main"
                return "trim"
        # outer layer: armor pieces
        if part == "body":
            if f == "front":
                e = emblem(corps, x, y)
                if e:
                    return e
                if y == 0 and 1 <= x <= 6:
                    return "light"
                if y == 6 and 2 <= x <= 5 or y == 7 and 3 <= x <= 4:
                    return "main"  # plate narrows to a point
                if y == 10 and 3 <= x <= 4:
                    return "light"  # buckle
                return None
            if f == "back" and y <= 4 and 1 <= x <= 6:
                return "main"
            if f == "top":
                return "main"
            return None
        if part.endswith("arm"):
            if f == "top" or (y <= 2 and f != "bottom"):
                return "light" if y == 0 and f != "top" else "main"  # shoulder pad
            if 7 <= y <= 9 and f != "bottom":
                return "dark" if y == 7 else "main"  # gauntlet
            return None
        if part.endswith("leg"):
            if 4 <= y <= 6 and f == "front":
                return "main"  # knee guard
            if y in (8, 9) and f not in ("top", "bottom"):
                return "light" if y == 8 else "main"  # boot cuff
            if tassets and f in ("front", "right", "left") and y <= 3:
                return "main" if y < 3 else "dark"
            return None

    return paint


def design_classic(corps):
    """The comic-book look: corps color with black sides, full gloves and boots."""
    def paint(part, layer, f, x, y, w, h):
        if part == "head":
            return None
        if layer == "outer":
            if part == "body" and f == "front":
                e = emblem(corps, x, y)
                return e
            return None
        if part == "body":
            if f == "top":
                return "main"
            if y == 9:
                return "trim2"
            if f in ("front", "back"):
                return "main" if 1 <= x <= 6 else "trim"
            return "trim"
        if part.endswith("arm"):
            if y <= 2 or f == "top":
                return "main"
            if y >= 8:
                return "dark" if y == 8 else "main"  # gloves
            return "trim"
        if part.endswith("leg"):
            if y >= 9 or f == "bottom":
                return "dark" if y == 9 else "main"
            if f in ("right", "left"):
                return "trim"
            return "main"
    return paint


def design_stealth(corps):
    """Black on black with glowing corps-colored seams."""
    def paint(part, layer, f, x, y, w, h):
        if part == "head":
            return None
        if layer == "outer":
            if part == "body" and f == "front":
                return emblem(corps, x, y, bg="disc")
            if part.endswith("arm") and f in ("right", "left") and 1 <= y <= 9 and x == 1:
                return "line"
            return None
        if part == "body":
            if f == "front" and y == 9:
                return "line"
            return "trim2" if f == "top" else "trim"
        if part.endswith("arm"):
            if y == h - 1 and f not in ("top", "bottom"):
                return None
            return "line" if y == 8 and f != "bottom" else "trim"
        if part.endswith("leg"):
            if f == "front" and x in (1, 2) and y <= 8:
                return "line" if x == 1 else "trim"
            return "dark" if y >= 10 else "trim"
    return paint


DESIGN_FUNCS = {"armored": design_armored, "classic": design_classic, "stealth": design_stealth}


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


def suit(corps, rgb, design, slim):
    """(suit, glow) 64x64 textures for suit_model."""
    return _paint_layers(corps, rgb, DESIGN_FUNCS[design](corps), slim)


def mask(corps, rgb, mask_id):
    """(mask, glow) 64x64 textures for the head of suit_model."""
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

# Model UVs are divided by (texture size x texture_scale), so 0.1 makes each model unit of
# the tiny plate cover 10 texture pixels: its 1.2-unit front face shows pixels 2..14.
RING_TEX_SCALE = 0.1


def ring_model(slim):
    """A small square signet plate with the corps logo on the front of the right hand,
    like A New Corps (not a band around the wrist)."""
    x0 = -2 if slim else -3  # outer side of the right arm
    empty = {"part_pose": {"offset": [0, 0, 0], "rotation": [0, 0, 0]}, "cubes": [], "children": {}}
    return {
        "texture_width": 16, "texture_height": 16,
        "mesh": {
            "head": empty, "hat": empty, "body": empty, "left_arm": empty, "right_leg": empty, "left_leg": empty,
            "right_arm": {
                "part_pose": {"offset": [-5, 2.5 if slim else 2, 0], "rotation": [0, 0, 0]},
                "cubes": [{"origin": [x0 + 0.55, 7.0, -2.25], "dimensions": [1.2, 1.2, 0.2],
                           "texture_offset": [0, 0], "texture_scale": [RING_TEX_SCALE, RING_TEX_SCALE]}],
                "children": {},
            },
        },
    }


def ring_textures(corps, rgb):
    """(plate, glow) 16x16 textures for ring_model. The plate's front face covers
    pixels (2..14, 2..14); its edges use the strips around it."""
    p = palette(corps, rgb)
    plate = Image.new("RGBA", (16, 16), p["dark"])
    glow = Image.new("RGBA", (16, 16), CLEAR)
    d = ImageDraw.Draw(plate)
    d.rectangle((2, 2, 13, 13), fill=p["disc"])
    d.rectangle((2, 2, 13, 13), outline=p["main"])
    for y, row in enumerate(LOGOS[corps]):
        for x, ch in enumerate(row):
            if ch == "#":
                glow.putpixel((2 + x, 2 + y), p["glow"])
                plate.putpixel((2 + x, 2 + y), p["glow"])
    return plate, glow


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


# --- hard-light constructs (3D item models shown by display entities) --------------------

def _box(frm, to):
    return {"from": frm, "to": to, "faces": {f: {"texture": "#0", "uv": [0, 0, 16, 16]}
                                             for f in ("north", "south", "east", "west", "up", "down")}}


def construct_shapes():
    """Shape name -> list of elements in a 16x16x16 box, centered on (8, 8, 8)."""
    fist = [
        _box([3, 3, 5], [13, 11, 13]),     # back of the hand
        _box([3, 11, 4], [5.4, 14, 11]),   # four curled fingers
        _box([5.6, 11, 4], [8, 14.5, 11]),
        _box([8.2, 11, 4], [10.6, 14.5, 11]),
        _box([10.8, 11, 4], [13, 14, 11]),
        _box([3, 9, 2], [13, 11.5, 5]),    # knuckle ridge, facing forward
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
    return {"fist": fist, "hammer": hammer, "cage": cage, "wall": wall, "claw": claw, "crystal": crystal}


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
