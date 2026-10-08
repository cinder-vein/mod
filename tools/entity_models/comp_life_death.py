"""Bodies of the compassion, life and death entities: the Proselyte (indigo octopus), the Life Entity (white winged
being of light) and Nekron (black skeletal lord). Built from boxes; limbs, tentacles and curves are chains of rotated
segments. Every model faces -z, is centered on x=8 and is mirror-symmetric where it should be."""
import math

FACES = ("north", "south", "east", "west", "up", "down")
ANGLES = (-45, -22.5, 0, 22.5, 45)
AXES = {"x": (1, 2), "y": (2, 0), "z": (0, 1)}  # rotation axis -> (u, v): a positive angle turns u toward v


def _r(v):
    return round(v + 0.0, 3)


def box(frm, to, tex="#0", rot=None):
    el = {"from": [_r(v) for v in frm], "to": [_r(v) for v in to],
          "faces": {f: {"texture": tex, "uv": [0, 0, 16, 16]} for f in FACES}}
    if rot:
        el["rotation"] = rot
    return el


def r(axis, angle, origin):
    assert angle in ANGLES, angle
    return {"origin": [_r(v) for v in origin], "axis": axis, "angle": angle}


def seg(p0, axis, ang, length, w, h, tex="#0", ext=0.0, base=None):
    """A bar starting at p0 (center of its start cross-section), heading in the plane across `axis` at `ang` degrees
    (measured from the plane's u toward v; a multiple of 22.5). w is its width in that plane, h its size along `axis`.
    ext lengthens both ends (to close joints). Returns (element, end point)."""
    u, v = AXES[axis]
    a = math.radians(ang)
    end = list(p0)
    end[u] += length * math.cos(a)
    end[v] += length * math.sin(a)
    ang = (ang + 180) % 360 - 180
    if base is None:
        base = {0: 0, 1: 90, 2: 180, -1: -90, -2: 180}[round(ang / 90.0)]
    rot = (ang - base + 180) % 360 - 180
    assert rot in ANGLES, (ang, rot)
    k, sign = {0: (u, 1), 90: (v, 1), 180: (u, -1), -90: (v, -1)}[base]
    j = v if k == u else u
    ax = "xyz".index(axis)
    lo, hi = list(p0), list(p0)
    s0, s1 = p0[k] - ext * sign, p0[k] + (length + ext) * sign
    lo[k], hi[k] = min(s0, s1), max(s0, s1)
    lo[j], hi[j] = p0[j] - w / 2, p0[j] + w / 2
    lo[ax], hi[ax] = p0[ax] - h / 2, p0[ax] + h / 2
    rot = rot + 0.0 if rot % 1 else int(rot)
    el = box(lo, hi, tex, r(axis, rot, p0) if rot else None)
    return el, end


def chain(p0, axis, steps, tex="#0", ext=0.0):
    """steps: [(ang, length, w, h)] joined end to start. Returns (elements, end point)."""
    out, p = [], p0
    for ang, length, w, h in steps:
        el, p = seg(p, axis, ang, length, w, h, tex, ext)
        out.append(el)
    return out, p


def mirror(el):
    """The same element mirrored across x = 8."""
    m = {"from": [_r(16 - el["to"][0]), el["from"][1], el["from"][2]],
         "to": [_r(16 - el["from"][0]), el["to"][1], el["to"][2]],
         "faces": dict(el["faces"])}
    m["faces"]["east"], m["faces"]["west"] = el["faces"]["west"], el["faces"]["east"]
    if "rotation" in el:
        ro = el["rotation"]
        o = ro["origin"]
        ang = ro["angle"] if ro["axis"] == "x" else -ro["angle"]
        m["rotation"] = {"origin": [_r(16 - o[0]), o[1], o[2]], "axis": ro["axis"], "angle": ang}
    return m


def both(els):
    els = els if isinstance(els, list) else [els]
    return els + [mirror(e) for e in els]


def blob(c, size, k, tex="#0"):
    """A rounded block: three overlapping boxes, each inset by k on two of its three axes."""
    out = []
    for keep in range(3):
        lo = [c[i] - size[i] / 2 + (0 if i == keep else k) for i in range(3)]
        hi = [c[i] + size[i] / 2 - (0 if i == keep else k) for i in range(3)]
        out.append(box(lo, hi, tex))
    return out


def corners(el):
    """The element's 8 corners after its rotation."""
    a, b = el["from"], el["to"]
    pts = [[(a, b)[i >> k & 1][k] for k in range(3)] for i in range(8)]
    ro = el.get("rotation")
    if not ro:
        return pts
    u, v = AXES[ro["axis"]]
    c, s = math.cos(math.radians(ro["angle"])), math.sin(math.radians(ro["angle"]))
    o = ro["origin"]
    out = []
    for p in pts:
        q = list(p)
        du, dv = p[u] - o[u], p[v] - o[v]
        q[u], q[v] = o[u] + du * c - dv * s, o[v] + du * s + dv * c
        out.append(q)
    return out


def extent(elements, axis):
    vals = [p["xyz".index(axis)] for e in elements for p in corners(e)]
    return min(vals), max(vals)


def check(elements):
    for e in elements:
        for c in e["from"] + e["to"]:
            assert -16 <= c <= 32, (c, e["from"], e["to"])
        if "rotation" in e:
            assert e["rotation"]["angle"] in ANGLES and e["rotation"]["axis"] in "xyz", e
    return elements


# ---------------------------------------------------------------------------------------------------------------
# The Proselyte: indigo octopus. A bulbous mantle swept back over one huge eye, eight thick curling arms.
def _arm_angle(out, theta):
    """The chain angle for a direction theta degrees above the outward horizontal, for an arm reaching `out`
    (one of "-z", "+z", "-x"). Returns (axis, angle)."""
    t = math.radians(theta)
    if out == "-z":
        axis, a = "x", math.atan2(-math.cos(t), math.sin(t))  # axis x: (y, z)
    elif out == "+z":
        axis, a = "x", math.atan2(math.cos(t), math.sin(t))
    else:
        axis, a = "z", math.atan2(math.sin(t), -math.cos(t))  # axis z: (x, y)
    return axis, round(math.degrees(a) / 22.5) * 22.5


def proselyte():
    els = []
    # head: a rounded block (two crossed boxes) carrying the eye; above and behind it the wider mantle bulb
    els.append(box([0.5, 9.5, 2], [15.5, 20.5, 14]))
    els.append(box([2.5, 9.5, 0], [13.5, 20.5, 14]))
    els.append(box([0, 18, 5], [16, 28.5, 17]))
    els.append(box([2.5, 18, 2.5], [13.5, 28.5, 19.5]))
    els.append(box([2.5, 16.5, 5], [13.5, 30, 17]))
    els.append(box([4, 29, 7], [12, 31.8, 15.5]))
    # one huge eye, rounded: a white-hot iris with a slit pupil, a heavy brow and a lower lid
    els.append(box([3.5, 12.5, -0.7], [12.5, 19.5, 1], "#1"))
    els.append(box([4.5, 11.5, -0.5], [11.5, 20.5, 1], "#1"))
    els.append(box([7.1, 12.1, -1.1], [8.9, 19.9, 0]))  # pupil
    els.append(box([2, 20, -1.3], [14, 22.2, 4]))  # brow
    els.append(box([4, 10.4, -0.9], [12, 11.6, 2]))  # lower lid
    # webbing between the arm roots: an octagonal skirt under the mantle
    els.append(box([1.5, 7, 1.5], [14.5, 10, 14.5]))
    els.append(box([2.5, 7.2, 2.5], [13.5, 9.8, 13.5], rot=r("y", 45, [8, 8.5, 8])))
    # eight arms: a thick root splaying out of the skirt, then a droop, a reach out and a tip curling up and back
    # in. Front and back pairs reach out low and long, side pairs droop and curl; each curls in its own plane.
    reach = [(-22.5, 5.5, 3.6), (-45, 4, 2.8), (22.5, 4, 2.1), (90, 2.5, 1.4)]
    trail = [(-45, 6, 3.6), (-22.5, 6.5, 2.8), (22.5, 4.5, 2.1), (90, 3, 1.4)]
    droop = [(-67.5, 7, 3.6), (-22.5, 5, 2.8), (45, 4, 2.1), (112.5, 2.5, 1.3)]
    spread = [(-45, 6, 3.6), (-45, 4.5, 2.8), (0, 4, 2.1), (67.5, 3, 1.4)]
    arms = (  # base, root angle about y, outward direction, profile
        ([4.5, 8.5, 3.0], -135, "-z", reach),
        ([4.5, 8.5, 13.0], -45, "+z", trail),
        ([3.0, 8.5, 4.5], -135, "-x", droop),
        ([3.0, 8.5, 11.5], -45, "-x", spread),
    )
    for base, root_ang, out, profile in arms:
        arm = []
        el, p = seg(base, "y", root_ang, 4.5, 4.2, 4.2, ext=1)
        arm.append(el)
        for theta, length, w in profile:
            axis, ang = _arm_angle(out, theta)
            el, p = seg(p, axis, ang, length, w, w, ext=0.7)
            arm.append(el)
        els += both(arm)
    return els


# ---------------------------------------------------------------------------------------------------------------
# The Life Entity: white winged being of light. A slender upright body, great arched wings with a curtain of
# feathers, a long flowing tail, a white-hot core on the breast and a halo above the head.
def life():
    els = []
    # slender upright body leaning forward, a full rounded breast carrying the white-hot core
    torso, chest = chain([8, 9, 9.5], "x", [(-22.5, 10, 4, 3.4)], ext=1)
    els += torso
    els.append(box([4.6, 13, 3.5], [11.4, 19, 8.5]))
    els.append(box([5.4, 12, 2.8], [10.6, 20, 8]))
    els.append(box([6.2, 13.9, 2.3], [9.8, 17.5, 3.3], "#1", rot=r("z", 45, [8, 15.7, 2.8])))  # core
    # slender neck rising up and forward; a small bird's head with a hooked beak and swept-back crest plumes
    neck, top = chain([8, chest[1], chest[2]], "x", [(-22.5, 4, 2.6, 2.6), (0, 3, 2.4, 2.4)], ext=0.8)
    els += neck
    hy, hz = top[1], top[2]
    els.append(box([5.9, hy - 1.4, hz - 3.4], [10.1, hy + 2.4, hz + 1.4]))  # head
    els.append(box([7.1, hy - 0.7, hz - 6.5], [8.9, hy + 1.0, hz - 3.2], rot=r("x", -22.5, [8, hy, hz - 3.2])))  # beak
    els += both(box([5.5, hy + 0.3, hz - 3.0], [6.2, hy + 1.5, hz - 1.6], "#1"))  # eyes
    els.append(seg([8, hy + 1.6, hz], "x", 90, 6.5, 1.4, 1.6)[0])  # crest plumes streaming back
    els.append(seg([8, hy + 0.6, hz + 1], "x", 112.5, 6, 1.1, 1.3)[0])
    # halo: a white-hot octagonal ring floating above the head
    cx, cy, cz, rad = 8, hy + 5, hz - 0.8, 4
    side = rad * math.tan(math.radians(22.5)) * 2 + 0.6
    for rot in (None, r("y", 45, [cx, cy, cz])):
        for s in (-1, 1):
            els.append(box([cx - side / 2, cy - 0.5, cz + s * rad - 0.5], [cx + side / 2, cy + 0.5, cz + s * rad + 0.5],
                           "#1", rot))
            els.append(box([cx + s * rad - 0.5, cy - 0.5, cz - side / 2], [cx + s * rad + 0.5, cy + 0.5, cz + side / 2],
                           "#1", rot))
    # long flowing tail: a central streamer sweeping down and back and curling up, and two side ribbons that
    # part from it before flowing back
    tail, _ = chain([8, 9.5, 10], "x", [(157.5, 5, 1.4, 3.2), (135, 5.5, 1.2, 3), (112.5, 6, 1.1, 2.8),
                                        (90, 4.5, 1, 2.5), (67.5, 3.5, 0.9, 2.2)], ext=0.5)
    els += tail
    side_tail, p = chain([7, 10, 10.5], "z", [(-135, 4.5, 2.2, 1.2)], ext=0.5)
    side_tail += chain(p, "x", [(135, 5.5, 1, 2.2), (112.5, 5, 0.9, 2), (90, 4, 0.8, 1.8)], ext=0.5)[0]
    els += both(side_tail)
    # wings: a great arch rising from the shoulder above the head, swept a little back; a solid panel of
    # secondaries hangs from its inner half, long primaries fan down and out from its outer half
    wing, pts = [], [[10.5, 17.5]]
    for i, (ang, length, w, h) in enumerate(((67.5, 6, 3, 3.4), (45, 6, 2.8, 3.2), (22.5, 5, 2.6, 3),
                                             (-22.5, 5, 2.2, 2.6), (-67.5, 5, 1.8, 2))):
        el, end = seg([pts[-1][0], pts[-1][1], 6.5 + 1 * i], "z", ang, length, w, h, ext=0.6)
        wing.append(el)
        pts.append(end)

    def under(x):  # a point just under the arch's top at x
        for a, b in zip(pts, pts[1:]):
            if a[0] <= x <= b[0]:
                return a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0]) - 0.8
        return pts[-1][1]

    for x0, z0, ang, low, w in ((12.2, 7, -90, 17, 3.4), (14.6, 7.3, -90, 15.8, 3.4), (17.4, 7.6, -90, 14.6, 3.4),
                                (20.4, 8.2, -90, 13.2, 3.2), (23.2, 9, -67.5, 11.8, 2.6),
                                (25.8, 9.8, -67.5, 11, 2.4), (27.6, 10.6, -45, 12.5, 2.2)):
        y0 = under(x0)  # each feather hangs from the arch down to its tip height `low`
        length = (y0 - low) / -math.sin(math.radians(ang))
        wing.append(seg([x0, y0, z0], "z", ang, length, w, 0.8, base=-90)[0])
    els += both(wing)
    return els


# ---------------------------------------------------------------------------------------------------------------
# Nekron: black skeletal lord. A hooded capelet over a ragged robe widening in steps, a pale skull with burning eyes,
# a spiked crown, a bare ribcage and long bony arms hanging down to great claws.
def nekron():
    els = []
    # robe: three steps widening from a narrow waist to the hem, ragged strips hanging below it
    els.append(box([4.5, 11, 5], [11.5, 16.5, 11]))
    els.append(box([3, 6, 4], [13, 11, 12.5]))
    els.append(box([1.5, 1.5, 3], [14.5, 6, 14]))
    els += both(box([1.2, 0, 2.6], [4.4, 2, 5]))  # tattered hem strips
    els += both(box([0.9, 0.4, 6], [2.5, 2, 13.5]))
    els.append(box([6.2, 0.6, 2.6], [9.8, 2, 3.6]))
    els.append(box([4, 0, 13], [12, 2, 14.6]))
    # capelet over the shoulders and back with ragged points, open at the front over a bare ribcage
    els.append(box([3.5, 21, 5], [12.5, 23.5, 11.5]))
    els.append(box([2, 17, 6.5], [14, 21.5, 12]))
    els += both(box([2, 17, 4.6], [4.5, 21.5, 6.5]))
    els += both(box([2, 15, 4.8], [3.4, 17.2, 6.3]))
    els.append(box([6, 15, 5.5], [10, 21.5, 8.5]))  # chest and spine
    els.append(box([7.4, 15.5, 4.5], [8.6, 21, 5.5]))  # sternum
    for y, hw in ((20, 3.2), (18.2, 3.0), (16.4, 2.6)):
        els += both(box([8 - hw, y - 0.45, 4.8], [7.6, y + 0.45, 7.5], "#1", r("z", -22.5, [7.6, y, 6])))  # ribs
    # hood around the head, peaked at the back
    els.append(box([4.5, 21, 4.6], [11.5, 27.8, 11]))
    els += both(box([4.5, 21, 2.4], [5.8, 27.5, 4.6]))  # side flaps framing the face
    els.append(box([4.8, 26.6, 2.4], [11.2, 27.8, 4.6]))  # brow of the hood
    els.append(box([6, 24.5, 8], [10, 28, 12.5], rot=r("x", 22.5, [8, 25.5, 11])))  # peak
    # pale skull: cranium, cheekbones and jaw; dark sockets with burning eyes, nose hole and teeth gap
    els.append(box([6, 23.5, 3], [10, 26.6, 5], "#1"))
    els.append(box([6.4, 22.2, 3.2], [9.6, 23.6, 5], "#1"))
    els.append(box([6.9, 21, 3.4], [9.1, 22.4, 5], "#1"))
    els += both(box([6.2, 24.0, 2.6], [7.6, 25.4, 3.1]))  # sockets
    els += both(box([6.6, 24.4, 2.3], [7.3, 25.1, 2.7], "#1"))  # eyes
    els.append(box([7.6, 22.8, 2.9], [8.4, 23.8, 3.3]))  # nose
    els.append(box([7, 21.9, 3.1], [9, 22.2, 3.5]))  # teeth gap
    # bone-pale spiked crown on the hood's brow: a band, a tall middle spike, flanking spikes leaning outward
    els.append(box([4.2, 27.2, 2.0], [11.8, 28.2, 6.5], "#1"))
    els.append(box([7.25, 27.8, 2.3], [8.75, 32, 3.7], "#1"))
    els += both(box([4.9, 27.8, 2.4], [6.1, 31.3, 3.6], "#1", r("z", 22.5, [5.5, 28, 3])))
    els += both(box([3.7, 27.6, 4.2], [4.7, 30.2, 5.4], "#1", r("z", 45, [4.2, 27.8, 4.8])))
    # long bony arms: a sleeve out from the shoulder, a pale forearm hanging down, a hand with fanned claws
    arm = []
    sleeve, elbow = chain([3.4, 21.5, 8], "z", [(-135, 5.5, 3.4, 3.6)], ext=0.8)
    arm += sleeve
    arm.append(box([elbow[0] - 2, elbow[1] - 3, elbow[2] - 2], [elbow[0] + 2, elbow[1] + 1, elbow[2] + 2]))  # cuff
    fore, wrist = chain(elbow, "z", [(-112.5, 8, 1.2, 1.2)], "#1", ext=0.6)
    arm += fore
    wx, wy, wz = wrist
    arm.append(box([wx - 1.1, wy - 1.8, wz - 1.1], [wx + 1.1, wy + 0.3, wz + 1.1], "#1"))  # hand
    for dx, ang in ((-0.6, -112.5), (0, -90), (0.6, -67.5)):
        arm.append(seg([wx + dx, wy - 1.4, wz], "z", ang, 4.5, 0.6, 0.7, "#1")[0])  # claws
    els += both(arm)
    return els


def build(fn, axis, size_blocks):
    """Scale so the creature's extent along `axis` is size_blocks; lift so its underside sits at the entity's feet."""
    elements = check(fn())
    lo, hi = extent(elements, axis)
    scale = round(size_blocks * 16 / (hi - lo), 2)
    return {"elements": elements, "scale": scale, "lift": round((8 - extent(elements, "y")[0]) * scale / 16, 2)}


MODELS = {
    "proselyte": build(proselyte, "y", 4),  # 4 blocks tall
    "life": build(life, "x", 6),  # 6 blocks wingspan
    "nekron": build(nekron, "y", 3.5),  # 3.5 blocks tall
}
