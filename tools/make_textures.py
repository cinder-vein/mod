"""Generates every texture in the pack.

The art is drawn in code so it can be tweaked and regenerated:

    python3 tools/make_textures.py

Swap any PNG for hand-drawn art later; nothing else depends on this script.
"""
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent / "src" / "assets" / "greenlantern" / "textures"

CLEAR = (0, 0, 0, 0)
GREEN = (46, 200, 70, 255)
GREEN_LIGHT = (90, 240, 110, 255)
GREEN_DARK = (22, 120, 40, 255)
GREEN_DEEP = (12, 70, 24, 255)
BLACK = (24, 26, 28, 255)
BLACK_LIGHT = (44, 48, 52, 255)
WHITE = (240, 255, 240, 255)
GLOW = (120, 255, 140, 255)
GOLD = (210, 170, 60, 255)

# The Green Lantern Corps emblem as it sits on the chest: "W" is the symbol,
# "B" the black disc behind it (8x5, drawn from row 1 of the chest).
EMBLEM = [
    "BWWWWWWB",
    "BBWBBWBB",
    "BWBBBBWB",
    "BBWBBWBB",
    "BWWWWWWB",
]


# --- player skin layout helpers ------------------------------------------------

def box_faces(u, v, w, h, d):
    """Texture rectangles (x, y, width, height) of a Minecraft model box."""
    return {
        "top": (u + d, v, w, d),
        "bottom": (u + d + w, v, w, d),
        "right": (u, v + d, d, h),
        "front": (u + d, v + d, w, h),
        "left": (u + d + w, v + d, d, h),
        "back": (u + d + w + d, v + d, w, h),
    }


def paint_box(img, u, v, w, h, d, painter):
    """Calls painter(face, x, y, face_width, face_height) for every pixel of the box."""
    for face, (fx, fy, fw, fh) in box_faces(u, v, w, h, d).items():
        for y in range(fh):
            for x in range(fw):
                color = painter(face, x, y, fw, fh)
                if color is not None:
                    img.putpixel((fx + x, fy + y), color)


def head(face, x, y, w, h):
    # Domino mask across the eyes (rows 3-4), wrapping around the sides of the head.
    if y not in (3, 4):
        return None
    if face == "front":
        return GREEN_DARK if y == 3 or x in (0, 3, 4, 7) else None  # eye holes
    if face == "right" and x >= 5:  # strip next to the face
        return GREEN_DARK
    if face == "left" and x <= 2:
        return GREEN_DARK
    return None


def body(face, x, y, w, h):
    if face == "top":
        return GREEN
    if face == "bottom":
        return BLACK
    if face in ("right", "left"):
        return BLACK if y >= 2 else GREEN
    if face == "front":
        # emblem circle sits on a black disc in the chest
        ey, ex = y - 1, x
        if 0 <= ey < len(EMBLEM):
            return WHITE if EMBLEM[ey][ex] == "W" else BLACK
        if y == 0:
            return GREEN_LIGHT
        if y >= 10:
            return BLACK  # belt
        return GREEN if 1 < x < 6 else BLACK
    if face == "back":
        if y >= 10:
            return BLACK
        return GREEN if 1 < x < 6 else BLACK
    return None


def arm(face, x, y, w, h):
    if face == "top":
        return GREEN
    if face == "bottom":
        return GREEN_DARK
    if y >= h - 4:  # gloves
        return GREEN_DARK if y == h - 4 else GREEN
    if y < 3:  # shoulders
        return GREEN
    return BLACK if (x + y) % 7 else BLACK_LIGHT


def leg(face, x, y, w, h):
    if face == "top":
        return GREEN
    if face == "bottom":
        return GREEN_DEEP
    if y >= h - 4:  # boots
        return GREEN_DARK if y == h - 4 else GREEN
    if face in ("right", "left"):
        return BLACK
    return GREEN if 0 < x < w - 1 else BLACK


def uniform(slim):
    img = Image.new("RGBA", (64, 64), CLEAR)
    arm_w = 3 if slim else 4
    paint_box(img, 0, 0, 8, 8, 8, head)
    paint_box(img, 16, 16, 8, 12, 4, body)
    paint_box(img, 40, 16, arm_w, 12, 4, arm)  # right arm
    paint_box(img, 32, 48, arm_w, 12, 4, arm)  # left arm
    paint_box(img, 0, 16, 4, 12, 4, leg)  # right leg
    paint_box(img, 16, 48, 4, 12, 4, leg)  # left leg
    return img


def uniform_glow(slim):
    """Full-bright parts: the mask's eyes, the emblem and the ring."""
    img = Image.new("RGBA", (64, 64), CLEAR)

    def eyes(face, x, y, w, h):
        if face == "front" and y == 4 and x in (1, 2, 5, 6):
            return WHITE
        return None

    def emblem(face, x, y, w, h):
        ey = y - 1
        if face == "front" and 0 <= ey < len(EMBLEM) and EMBLEM[ey][x] == "W":
            return GLOW
        return None

    def ring(face, x, y, w, h):
        # a band around the right hand's fingers
        if face in ("front", "right", "left", "back") and y == h - 2:
            return GLOW
        return None

    arm_w = 3 if slim else 4
    paint_box(img, 0, 0, 8, 8, 8, eyes)
    paint_box(img, 16, 16, 8, 12, 4, emblem)
    paint_box(img, 40, 16, arm_w, 12, 4, ring)
    return img


# --- items ---------------------------------------------------------------------

def from_rows(rows, palette):
    img = Image.new("RGBA", (16, 16), CLEAR)
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in palette:
                img.putpixel((x, y), palette[ch])
    return img


RING = [
    "................",
    "................",
    ".....GGGGGG.....",
    "....GLLLLLLG....",
    "....GLWWWWLG....",
    "....GWLLLLWG....",
    "....GWLLLLWG....",
    "....GLWWWWLG....",
    "....GGLLLLGG....",
    ".....DGGGGD.....",
    "....D......D....",
    "...D........D...",
    "...D........D...",
    "....D......D....",
    ".....DDDDDD.....",
    "................",
]

BATTERY = [
    "......YYYY......",
    ".....Y....Y.....",
    "....DDDDDDDD....",
    "...DGGGGGGGGD...",
    "...DGLLLLLLGD...",
    "...DGLWWWWLGD...",
    "...DGWLLLLWGD...",
    "...DGWLLLLWGD...",
    "...DGLWWWWLGD...",
    "...DGLLLLLLGD...",
    "...DGGGGGGGGD...",
    "....DDDDDDDD....",
    "...SSSSSSSSSS...",
    "..SBBBBBBBBBBS..",
    "..SSSSSSSSSSSS..",
    "................",
]


def logo():
    size = 128
    img = Image.new("RGBA", (size, size), (10, 20, 12, 255))
    draw = ImageDraw.Draw(img)
    for r in range(60, 0, -4):  # soft green glow, brighter towards the centre
        t = 1 - r / 60
        draw.ellipse((64 - r, 64 - r, 64 + r, 64 + r), fill=(int(10 + 40 * t), int(20 + 140 * t), int(12 + 50 * t), 255))
    draw.rectangle((20, 26, 108, 38), fill=GLOW)
    draw.rectangle((20, 90, 108, 102), fill=GLOW)
    draw.ellipse((34, 34, 94, 94), outline=GLOW, width=10)
    return img


def main():
    palette = {
        "G": GREEN, "L": GREEN_LIGHT, "D": GREEN_DARK, "W": WHITE,
        "Y": GOLD, "S": BLACK_LIGHT, "B": BLACK,
    }
    (ROOT / "item").mkdir(parents=True, exist_ok=True)
    (ROOT / "models").mkdir(parents=True, exist_ok=True)
    from_rows(RING, palette).save(ROOT / "item" / "green_lantern_ring.png")
    from_rows(BATTERY, palette).save(ROOT / "item" / "power_battery.png")
    uniform(False).save(ROOT / "models" / "uniform.png")
    uniform(True).save(ROOT / "models" / "uniform_slim.png")
    uniform_glow(False).save(ROOT / "models" / "uniform_glow.png")
    uniform_glow(True).save(ROOT / "models" / "uniform_glow_slim.png")
    logo().save(ROOT.parent.parent.parent / "pack.png")


if __name__ == "__main__":
    main()
