"""Bodies of the willpower, fear and rage entities: Ion (space whale), Parallax (insectoid parasite) and
The Butcher (demon bull). Every model faces -z, is centered on x=8 and is built mirror-symmetric where it should be."""
import math

FACES = ("north", "south", "east", "west", "up", "down")


def box(frm, to, tex="#0", rot=None):
    el = {"from": [round(v, 3) for v in frm], "to": [round(v, 3) for v in to],
          "faces": {f: {"texture": tex, "uv": [0, 0, 16, 16]} for f in FACES}}
    if rot:
        el["rotation"] = rot
    return el


def r(axis, angle, origin):
    return {"origin": list(origin), "axis": axis, "angle": angle}


def mirror(el):
    """The same element mirrored across the x=8 plane (rotations about y and z flip their sense)."""
    a, b = el["from"], el["to"]
    out = box([16 - b[0], a[1], a[2]], [16 - a[0], b[1], b[2]])
    out["faces"] = el["faces"]
    if "rotation" in el:
        rt = el["rotation"]
        o = rt["origin"]
        out["rotation"] = {"origin": [16 - o[0], o[1], o[2]], "axis": rt["axis"],
                           "angle": rt["angle"] if rt["axis"] == "x" else -rt["angle"]}
    return out


def pair(frm, to, tex="#0", rot=None):
    """An element on the low-x side plus its mirror image on the high-x side."""
    el = box(frm, to, tex, rot)
    return [el, mirror(el)]


def lowest_point(el):
    """Lowest y of an element's corners after its rotation."""
    a, b = el["from"], el["to"]
    rt = el.get("rotation")
    low = None
    for x in (a[0], b[0]):
        for y in (a[1], b[1]):
            for z in (a[2], b[2]):
                if rt:
                    o, ang = rt["origin"], math.radians(rt["angle"])
                    px, py, pz = x - o[0], y - o[1], z - o[2]
                    if rt["axis"] == "x":
                        py = py * math.cos(ang) - pz * math.sin(ang)
                    elif rt["axis"] == "z":
                        py = px * math.sin(ang) + py * math.cos(ang)
                    y = py + o[1]
                low = y if low is None else min(low, y)
    return low


def lift_for(elements, scale):
    """Raise the display so the lowest point of the model sits at the entity's feet."""
    low = min(lowest_point(e) for e in elements)
    return round((8 - low) * scale / 16, 2)


# ---------------------------------------------------------------- Ion: a serene space whale
def ion():
    e = []
    # body core: per segment a wide+short and a narrow+tall box give a rounded cross-section
    segs = [  # z0, z1, half width, belly y, back y
        (-16, -11, 3.5, 2.5, 8.5),
        (-11, -5, 5.5, 1.5, 10.5),
        (-5, 3, 7.0, 1.0, 14.0),
        (3, 10, 6.75, 1.5, 14.0),
        (10, 13, 5.5, 3.5, 13.5),
        (13, 17, 4.0, 5.0, 11.5),
        (17, 21, 2.5, 6.5, 10.0),
    ]
    for z0, z1, hw, yb, yt in segs:
        e.append(box([8 - hw, yb + 1.0, z0], [8 + hw, yt - 1.25, z1]))
        e.append(box([8 - hw + 1.0, yb, z0], [8 + hw - 1.0, yt, z1]))
    e.append(box([6.5, 7.0, 21], [9.5, 10.0, 29.5]))  # tail stock
    # smooth slopes laid over the steps: the forehead down to the snout, the back and belly into the tail stock
    e.append(box([3.5, 12.5, -15], [12.5, 14.0, -3], rot=r("x", -22.5, [8, 14, -3])))
    e += pair([1.25, 2.5, -12], [2.75, 10.5, -3], rot=r("y", -22.5, [1.25, 6, -3]))  # cheeks taper the head
    e.append(box([5.0, 12.0, 12], [11.0, 13.5, 22], rot=r("x", 22.5, [8, 13.5, 12])))
    e.append(box([4.5, 1.5, 8], [11.5, 3.0, 21], rot=r("x", -22.5, [8, 1.5, 8])))
    # flukes: broad horizontal blades swept back from the tail stock, notched in the middle
    sweep = r("y", 22.5, [8, 8.5, 27])
    e += pair([0, 8.0, 26], [8, 9.25, 31], rot=sweep)
    e += pair([-7, 8.0, 26.75], [1, 9.25, 30], rot=sweep)
    # long pectoral fins, swept back
    fin = r("y", 22.5, [2, 3.5, -4])
    e += pair([-3, 3.0, -4], [2.5, 4.25, 2], rot=fin)
    e += pair([-10, 3.0, -2], [-2, 4.25, 2.5], rot=fin)
    # low dorsal fin
    e.append(box([7.0, 11.5, 13], [9.0, 14.5, 17], rot=r("x", 22.5, [8, 11.5, 17])))
    # small calm eyes low on the head, just above the corner of the jaw
    e += pair([1.3, 5.25, -8.5], [2.4, 7.0, -6.25], "#1")
    # lower jaw, a touch wider than the snout, for a whale's mouth line
    e.append(box([4.0, 2.0, -16], [12.0, 4.0, -9]))
    # bioluminescent photophores along the lower flanks, spots along the back, and a glowing blowhole
    for z0, xs, y0 in ((-3.5, 1.0, 4.6), (0.0, 1.0, 4.6), (3.5, 1.25, 4.6), (7.0, 1.25, 4.6), (10.75, 2.5, 5.2),
                       (14.25, 4.0, 6.4)):
        e += pair([xs - 0.5, y0, z0], [xs + 0.5, y0 + 1.2, z0 + 1.5], "#1")
    for z0 in (2.5, 7.0):
        e += pair([4.5, 13.6, z0], [6.0, 14.4, z0 + 1.5], "#1")
    e.append(box([7.0, 13.6, -2], [9.0, 14.4, 0.5], "#1"))
    return e


# ---------------------------------------------------------------- Parallax: a demonic insectoid parasite
def parallax():
    e = []
    # head: broad demon skull with an angry V brow, a cluster of burning eyes and a glowing maw
    e.append(box([2.0, 8.5, -12], [14.0, 15.0, -3.5]))
    e.append(box([3.5, 15.0, -11], [12.5, 17.0, -4.5]))  # cranium
    e.append(box([4.0, 6.0, -11.5], [12.0, 8.5, -5]))  # narrow lower face
    e += pair([1.5, 14.0, -13], [8.25, 15.75, -10.5], rot=r("z", -22.5, [8.25, 14.9, -12]))  # brow
    e += pair([3.0, 11.75, -12.6], [7.25, 13.5, -11.5], "#1", r("z", -22.5, [7.25, 12.6, -12]))  # main eyes
    e += pair([4.5, 9.75, -12.5], [6.0, 10.75, -11.5], "#1")  # lower eyes
    e += pair([1.4, 12.0, -10], [2.1, 13.5, -8.0], "#1")  # side eyes
    e.append(box([7.25, 15.5, -11.6], [8.75, 16.75, -10.75], "#1"))  # third eye
    e.append(box([6.25, 6.75, -12.1], [9.75, 7.75, -11.25], "#1"))  # maw
    e += pair([6.25, 4.5, -12], [7.0, 6.75, -11.25])  # fangs
    # sickle mandibles: heavy bases splaying forward and out, hooked tips curling in
    e += pair([2.75, 6.0, -16], [5.5, 8.75, -9.5], rot=r("y", 22.5, [5.5, 7.4, -9.5]))
    e += pair([0.75, 6.5, -16], [6.5, 8.25, -14.25], rot=r("y", -45, [0.75, 7.4, -15]))
    # horn-tendrils: rising off the crown, then whipping back and out over the body, tips drooping
    e += pair([4.0, 16.0, -9], [5.75, 24.0, -7.25], rot=r("x", 45, [4.9, 16, -8.1]))
    e += pair([4.25, 20.75, -3.5], [5.5, 22.0, 18], rot=r("y", -22.5, [4.9, 21.4, -3.5]))
    e += pair([-3.6, 19.0, 15.0], [-2.4, 20.25, 29], rot=r("x", 22.5, [-3.0, 20.25, 15.0]))
    # narrow armoured thorax and waist
    e.append(box([4.5, 9.0, -4.5], [11.5, 14.5, 8]))
    e.append(box([4.0, 13.0, -3.5], [12.0, 16.0, 7]))
    e.append(box([6.5, 10.0, 7.5], [9.5, 13.0, 11.5]))
    for z0 in (-1.0, 3.5):  # carapace spikes
        e.append(box([7.0, 15.0, z0], [9.0, 19.5, z0 + 2], rot=r("x", 45, [8, 15, z0 + 1])))
    # big segmented gaster, raised behind like a sting
    lift_up = r("x", -22.5, [8, 11.5, 11])
    for z0, z1, hw, y0, y1 in ((11, 15, 5.0, 7.5, 16.0), (15, 20, 6.5, 6.5, 17.5), (20, 25, 6.0, 7.0, 17.0),
                               (25, 29, 4.5, 8.0, 15.5), (29, 32, 2.5, 9.5, 13.5)):
        e.append(box([8 - hw, y0, z0], [8 + hw, y1, z1 - 0.3], rot=lift_up))
    # six spindly legs: thigh up and out to a high knee, shin down to the ground
    # (fore legs reach forward, hind legs reach back)
    for z in (-3.0, 1.0, 5.0):
        knee = [-2.9, 18.4, z + 0.5]
        shin = r("x", 22.5, knee) if z < 0 else r("x", -22.5, knee) if z > 3 else r("z", -22.5, knee)
        e += pair([-6.0, 10.5, z], [4.5, 11.5, z + 1], rot=r("z", -45, [4.5, 11, z + 0.5]))
        e += pair([-3.4, -1.5, z], [-2.4, 18.4, z + 1], rot=shin)
    return e


# ---------------------------------------------------------------- The Butcher: a hulking demon bull
def butcher():
    e = []
    # fore legs: thick forearms, shaggy cuffs, cloven hooves
    e += pair([1.0, 7.0, -3.0], [6.5, 17.0, 3.0])
    e += pair([2.0, 2.0, -2.0], [5.75, 7.5, 2.0])
    e += pair([1.5, 5.5, -2.5], [6.25, 8.5, 2.5])
    e += pair([1.75, 0.0, -2.25], [6.0, 2.0, 2.25])
    # hind legs: lean thighs and hocks
    e += pair([2.5, 9.0, 16.0], [6.5, 19.0, 22.5])
    e += pair([3.0, 1.5, 18.0], [6.0, 10.0, 21.0])
    e += pair([2.75, 0.0, 17.75], [6.25, 2.0, 21.25])
    # massive rounded shoulders under a towering hump; the back falls away to small hindquarters
    e.append(box([-1.0, 13.0, -5.0], [17.0, 23.0, 7.0]))
    e.append(box([0.5, 11.5, -4.5], [15.5, 24.5, 6.5]))
    e.append(box([1.5, 9.5, -4.0], [14.5, 14.0, 6.0]))  # deep chest
    # the hump peaks over the shoulders: a slope up from the neck and a long fall to the hips
    e.append(box([2.0, 23.0, -7.0], [14.0, 29.5, 1.0], rot=r("x", -22.5, [8.0, 29.5, 1.0])))
    e.append(box([2.5, 23.5, 1.0], [13.5, 29.5, 14.0], rot=r("x", 22.5, [8.0, 29.5, 1.0])))
    e.append(box([1.0, 22.0, -4.0], [15.0, 26.5, 6.0]))
    e.append(box([2.0, 11.5, 6.0], [14.0, 22.5, 15.0]))  # barrel
    e.append(box([2.5, 11.0, 14.0], [13.5, 21.0, 23.0]))  # hindquarters
    e.append(box([3.5, 10.0, 15.0], [12.5, 22.0, 22.5]))
    # lowered, charging head on a thick neck
    e.append(box([3.0, 11.5, -10.0], [13.0, 21.5, -3.0]))
    e.append(box([3.0, 10.5, -14.0], [13.0, 19.0, -7.5]))  # skull
    e.append(box([3.5, 18.5, -13.0], [12.5, 20.0, -8.0]))  # shaggy crown
    e.append(box([4.5, 9.0, -15.5], [11.5, 14.0, -13.0]))  # muzzle
    e += pair([5.25, 12.25, -16.0], [6.5, 13.25, -15.4], "#1")  # smouldering nostrils
    e += pair([2.5, 16.75, -15.0], [8.25, 18.5, -12.5], rot=r("z", -22.5, [8.25, 17.6, -13.75]))  # scowling brow
    e += pair([3.5, 14.25, -14.6], [7.0, 15.75, -13.6], "#1", r("z", -22.5, [7.0, 15.0, -14.1]))  # burning eyes
    # snarling maw: the jaw hangs open on a furnace glow, fangs bared
    e.append(box([5.0, 6.5, -15.5], [11.0, 9.0, -8.5], rot=r("x", -22.5, [8, 9.0, -8.5])))
    e.append(box([5.5, 7.5, -15.0], [10.5, 9.25, -10.0], "#1"))
    e += pair([4.75, 6.5, -15.75], [6.0, 9.0, -14.75])
    # great horns: out from the skull, then sweeping up and forward
    e += pair([-4.0, 16.0, -12.0], [4.0, 19.0, -9.0], rot=r("z", -22.5, [4.0, 17.5, -10.5]))
    e += pair([-4.75, 19.5, -11.9], [-2.0, 27.5, -9.1], rot=r("x", -45, [-3.4, 19.5, -10.5]))
    # spines raking back along the hump
    for z0 in (-2.5, 0.5, 4.0):
        e.append(box([6.75, 28.0, z0], [9.25, 32.0, z0 + 2.5], rot=r("x", 45, [8, 29.0, z0 + 1.25])))
    # tail lashing down behind
    e.append(box([7.25, 10.0, 22.5], [8.75, 20.0, 24.0], rot=r("x", -22.5, [8.0, 20.0, 23.25])))
    e.append(box([6.75, 7.0, 25.5], [9.25, 11.0, 28.0]))
    return e


def build(fn, length_units, length_blocks):
    elements = fn()
    scale = round(length_blocks * 16 / length_units, 2)
    return {"elements": elements, "scale": scale, "lift": lift_for(elements, scale)}


MODELS = {
    "ion": build(ion, 48, 7.0),
    "parallax": build(parallax, 48, 5.0),
    "butcher": build(butcher, 31, 3.0),
}
