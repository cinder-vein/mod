"""Bodies of the avarice, hope and love entities: Ophidian (orange serpent dragon), Adara (blue bird of hope) and
the Predator (violet stalking beast). Built from boxes; long limbs and curves are chains of rotated segments."""
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


def shift(els, dx=0.0, dy=0.0, dz=0.0):
    d = (dx, dy, dz)
    for e in els:
        e["from"] = [_r(c + d[i]) for i, c in enumerate(e["from"])]
        e["to"] = [_r(c + d[i]) for i, c in enumerate(e["to"])]
        if "rotation" in e:
            e["rotation"]["origin"] = [_r(c + d[i]) for i, c in enumerate(e["rotation"]["origin"])]
    return els


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
# Ophidian: orange serpent dragon. Coiled S-body on the ground, a raised cobra neck with a hood, an open fanged maw.
def ophidian():
    els = []
    # coiled body, from the neck base back to the tail tip (S-curves on the ground), dorsal frills on some segments
    path = [(45, 6, 7.5), (67.5, 5, 7.5), (45, 4, 7), (0, 3, 7), (-45, 4, 6.5), (-67.5, 5, 6.5), (-90, 5, 6),
            (-67.5, 5, 5.5), (-45, 4, 5), (0, 3, 4.5), (45, 4, 4), (67.5, 4, 3), (90, 4, 2)]
    p = [8, 0, 0.5]
    for i, (ang, length, t) in enumerate(path):
        el, end = seg([p[0], t / 2, p[2]], "y", ang, length, t, t, ext=t * 0.22)
        els.append(el)
        if i in (1, 4, 7, 10):
            els.append(seg([p[0], t + 1.1, p[2]], "y", ang, length * 0.7, 0.6, 2.2)[0])
        p = end
    # raised neck: leans forward, then rises straight
    neck, top = chain([8, 3.5, 0.5], "x", [(-22.5, 10, 6.5, 6.5), (0, 10, 6, 6)], ext=1.2)
    els += neck
    nz = top[2]
    els.append(box([6, 12, nz - 3.4], [10, 21, nz - 2.9]))  # belly scutes
    # cobra hood around the upper neck, its sides curving forward
    hz = nz + 1.5
    els.append(box([0, 7, hz - 1], [16, 22, hz + 1]))
    els.append(box([3, 4.5, hz - 0.8], [13, 7, hz + 0.8]))
    els.append(box([2.5, 22, hz - 0.8], [13.5, 24, hz + 0.8]))
    lobe, end = seg([0.5, 14.5, hz], "y", -112.5, 3.5, 1.8, 13)
    els += both([lobe, seg(end, "y", -135, 2.5, 1.5, 8.5)[0]])
    els += both(box([2.5, 14, hz + 0.9], [5.5, 18, hz + 1.4], "#1"))  # spectacle markings on the back
    # head
    els.append(box([4.5, 21, nz - 6], [11.5, 26.5, nz + 1.5]))  # cranium
    els += both(box([4, 25.6, nz - 6.4], [7, 27.6, nz - 1.5], rot=r("x", 22.5, [5.5, 25.6, nz - 1.5])))  # brows
    els += both(box([3.8, 23.6, nz - 5.6], [5, 25.2, nz - 3.4], "#1"))  # eyes
    jaw_up = r("x", 22.5, [8, 23, nz - 5.5])
    jaw_lo = r("x", -22.5, [8, 22.6, nz - 5.5])
    els.append(box([5.2, 23, nz - 12], [10.8, 26, nz - 5.5], rot=jaw_up))  # upper jaw
    els.append(box([6, 25.6, nz - 11.6], [10, 26.8, nz - 6], rot=jaw_up))  # snout ridge
    els.append(box([5.6, 20.6, nz - 11], [10.4, 22.6, nz - 5.5], rot=jaw_lo))  # lower jaw
    els.append(box([6.2, 21.6, nz - 7.5], [9.8, 23.6, nz - 5], "#1"))  # glowing throat
    els += both(box([5.5, 20.6, nz - 11.6], [6.7, 23.2, nz - 10.4], "#1", rot=jaw_up))  # upper fangs
    els += both(box([6, 22.2, nz - 10.6], [7, 24, nz - 9.6], "#1", rot=jaw_lo))  # lower fangs
    els += both(seg([5.6, 26, nz + 0.5], "x", 67.5, 6.5, 1.6, 1.6)[0])  # swept-back horns
    els += both(box([3.2, 20.5, nz - 3.5], [4.4, 25, nz + 2.5], rot=r("y", -22.5, [4.4, 22, nz - 3.5])))  # frills
    return els


# ---------------------------------------------------------------------------------------------------------------
# Adara: blue bird of hope. Raised gull wings with stepped feathers, a long fanned tail, a glowing heart-core.
def adara():
    els = []
    els.append(box([4.5, 6.2, -1.5], [11.5, 12.4, 10]))  # body
    els.append(box([4.8, 5, -4], [11.2, 12, 3.5]))  # breast
    els.append(box([5.6, 7.4, 9], [10.4, 11, 14]))  # rump
    els.append(box([6.3, 7.3, -4.8], [9.7, 10.7, -3.7], "#1", rot=r("z", 45, [8, 9, -4.2])))  # core
    neck, ntop = chain([8, 10.5, -2], "x", [(-22.5, 5.5, 4, 4)], ext=0.8)
    els += neck
    hy, hz = ntop[1], ntop[2]
    els.append(box([5.3, hy - 1.8, hz - 5], [10.7, hy + 3.2, hz + 1]))  # head
    els.append(box([6.7, hy - 0.4, hz - 8], [9.3, hy + 1.6, hz - 5]))  # beak
    els.append(box([7.2, hy - 0.6, hz - 9.2], [8.8, hy + 0.9, hz - 7.7], rot=r("x", -22.5, [8, hy + 0.4, hz - 7.9])))
    els += both(box([4.9, hy + 0.6, hz - 4.3], [5.8, hy + 2, hz - 2.8], "#1"))  # eyes
    els.append(seg([8, hy + 2.5, hz - 1.5], "x", 45, 6, 1.2, 1.4)[0])  # crest plumes
    els.append(seg([8, hy + 2.2, hz + 0.3], "x", 67.5, 5, 1, 1.2)[0])
    # tail: three long streamers over a fan of shorter feathers
    els.append(box([6.2, 8.4, 12], [9.8, 9.6, 32]))
    for ang, length, w, y in ((22.5, 17, 2.8, 8.8), (-22.5, 17, 2.8, 8.8), (45, 10, 2.6, 8.2), (-45, 10, 2.6, 8.2)):
        els.append(seg([8, y, 12.5], "y", ang, length, w, 1.1)[0])
    els += both(box([6, 4.6, 5], [7.2, 6.6, 8]))  # tucked legs
    # right wing: inner wing raised 22.5 degrees from the shoulder, outer hand level with fanned primaries
    wing = []
    sh = [11, 10.5, 1]
    inner = r("z", 22.5, sh)
    wing.append(box([10.5, 9.5, -2], [22, 12, 1.5], rot=inner))  # leading edge (arm)
    wing.append(box([10.5, 9.8, 1.5], [22, 11.6, 6], rot=inner))  # coverts
    for x0, back in ((10.5, 13.5), (13.4, 15), (16.3, 16), (19.2, 15.5)):
        wing.append(box([x0 + 0.15, 10, 5.5], [x0 + 2.75, 11.2, back], rot=inner))  # secondaries
    wx = sh[0] + 11 * math.cos(math.radians(22.5)) - 0.6  # wrist
    wy = sh[1] + 11 * math.sin(math.radians(22.5))
    wing.append(box([wx, wy - 1.1, -1.6], [31.5, wy + 1.1, 1.5]))  # hand leading edge
    wing.append(box([wx, wy - 0.8, 1.5], [29, wy + 0.8, 6]))  # hand coverts
    for ang, z0, x0, length in ((90, 3.5, wx + 1, 10), (67.5, 5, wx + 0.5, 10.5), (45, 6, wx - 0.3, 10),
                                (22.5, 6, wx - 1.6, 9)):
        wing.append(seg([x0, wy, z0], "y", ang, length, 2.4, 0.9, ext=0.4)[0])  # primaries
    els += both(wing)
    return els


# ---------------------------------------------------------------------------------------------------------------
# The Predator: violet stalking beast. Hunched, digitigrade legs, long clawed arms, skull head, crystal heart, spines.
def predator():
    els = []
    # legs: toes forward, hock raised behind, knee forward, hip back
    lx = 5.2
    leg = [box([lx - 1.5, 0, -4], [lx + 1.5, 1.5, 1])]  # foot
    for dx in (-1, 1):
        leg.append(seg([lx + dx, 0.6, -4], "x", -112.5, 2.5, 0.8, 0.8)[0])  # toe claws
    legs, hip = chain([lx, 1, 0], "x", [(45, 5.5, 2.4, 2.4), (-22.5, 6.5, 2.8, 2.8), (45, 5, 3.8, 3.8)], ext=1)
    leg += legs
    els += both(leg)
    hy, hz = hip[1], hip[2]
    els.append(box([4.2, hy - 1.5, hz - 2.2], [11.8, hy + 2, hz + 2]))  # pelvis
    # hunched spine: a narrow waist, then a deep chest leaning forward
    a1, a2, l1, l2 = -22.5, -45, 5, 9
    torso, sh = chain([8, hy + 1, hz], "x", [(a1, l1, 4, 4.5), (a2, l2, 6.5, 9)], ext=1.2)
    els += torso
    sy, sz = sh[1], sh[2]

    def along(t, off):  # a point t along the chest axis, off out from its back (+) or front (-)
        c = math.radians(a2)
        y0 = hy + 1 + l1 * math.cos(math.radians(a1)) + t * math.cos(c)
        z0 = hz + l1 * math.sin(math.radians(a1)) + t * math.sin(c)
        return y0 - off * math.sin(c), z0 + off * math.cos(c)

    # crystal heart on the chest front
    cy, cz = along(4.5, -3.6)
    els.append(box([6.1, cy - 1.9, cz - 1.9], [9.9, cy + 1.9, cz + 1.9], "#1", rot=r("y", 45, [8, cy, cz])))
    els.append(box([6.6, cy - 2.7, cz - 1.3], [9.4, cy + 2.7, cz + 1.3], "#1", rot=r("z", 45, [8, cy, cz])))
    # ribs wrapping the chest sides
    for t in (3, 5.5):
        ry, rz = along(t, -0.5)
        els.append(box([3, ry - 0.6, rz - 3.2], [13, ry + 0.6, rz + 2.2], rot=r("x", -45, [8, ry, rz])))
    # spines along the back, pointing up and back
    for t, length, w in ((8.2, 6.5, 1.6), (5.8, 6, 1.5), (3.4, 5, 1.4), (1, 4, 1.2)):
        py, pz = along(t, 3)
        els.append(seg([8, py, pz], "x", 45, length, w, w, base=90)[0])
    els.append(seg([8, hy + 3.2, hz + 1.3], "x", 67.5, 3, 1.1, 1.1)[0])
    # shoulders
    els += both(box([2, sy - 3.8, sz - 1.5], [6, sy + 0.2, sz + 3]))
    els += both(seg([3.5, sy - 0.5, sz + 1.5], "x", 45, 3.5, 1.3, 1.3)[0])
    # head: thrust forward, low
    neck, nh = chain([8, sy - 1.5, sz], "x", [(-67.5, 4, 3.2, 3.2)], ext=0.8)
    els += neck
    ny, nz = nh[1], nh[2]
    els.append(box([5.2, ny - 2, nz - 5], [10.8, ny + 3.5, nz + 1.5]))  # cranium
    els.append(box([4.8, ny + 2, nz - 5.6], [11.2, ny + 3.3, nz - 3.4]))  # brow ridge
    els.append(box([5.8, ny + 3.4, nz - 3.8], [10.2, ny + 4.4, nz + 1.2]))  # dome
    els += both(box([5.5, ny + 0.2, nz - 5.5], [7.5, ny + 1.9, nz - 4.6], "#1"))  # eyes
    els.append(box([6, ny - 2.5, nz - 8.5], [10, ny + 0.8, nz - 4.5]))  # muzzle
    els.append(box([6.6, ny - 2.3, nz - 9.5], [9.4, ny + 0.2, nz - 8]))  # snout
    els.append(box([6.2, ny - 4.2, nz - 8], [9.8, ny - 2.4, nz - 1.5], rot=r("x", -22.5, [8, ny - 2.4, nz - 1.5])))
    els += both(box([6.6, ny - 4, nz - 9.2], [7.3, ny - 2.2, nz - 8.5], "#1"))  # fangs
    els += both(box([4.6, ny - 1.8, nz - 4.5], [5.6, ny + 0.4, nz - 0.5]))  # cheekbones
    els += both(seg([6.2, ny + 3, nz], "x", 67.5, 6, 1.4, 1.4)[0])  # horns sweeping back
    # long arms: upper arm splayed out and down, forearm reaching forward, claws raised to strike
    arm, elbow = chain([2.6, sy - 2, sz + 0.8], "z", [(-112.5, 9, 2.4, 2.4)], ext=0.8)
    fore, wrist = chain(elbow, "x", [(-135, 8.5, 2, 2)], ext=0.8)
    arm += fore
    wx, wy, wz = wrist
    arm.append(box([wx - 1.5, wy - 1.6, wz - 2.6], [wx + 1.5, wy + 1.2, wz + 0.4], rot=r("x", 45, [wx, wy, wz])))
    for dx in (-1.1, 0, 1.1):
        arm.append(seg([wx + dx, wy - 0.8, wz - 1.8], "x", -112.5, 6, 0.7, 0.7)[0])  # claws
    els += both(arm)
    return shift(els, dz=2.5)


def build(fn, axis, size_blocks):
    """Scale so the creature's extent along `axis` is size_blocks; lift so its underside sits at the entity's feet."""
    elements = check(fn())
    lo, hi = extent(elements, axis)
    scale = round(size_blocks * 16 / (hi - lo), 2)
    return {"elements": elements, "scale": scale, "lift": round((8 - extent(elements, "y")[0]) * scale / 16, 2)}


MODELS = {
    "ophidian": build(ophidian, "z", 6),  # 6 blocks long
    "adara": build(adara, "x", 6),  # 6 blocks wingspan
    "predator": build(predator, "y", 3),  # 3 blocks tall
}
