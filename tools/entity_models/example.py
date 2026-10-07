"""Format example only (not a real entity)."""


def box(frm, to, tex="#0", rot=None):
    el = {"from": frm, "to": to, "faces": {f: {"texture": tex, "uv": [0, 0, 16, 16]}
                                           for f in ("north", "south", "east", "west", "up", "down")}}
    if rot:
        el["rotation"] = rot
    return el


MODELS = {}  # e.g. {"ion": {"elements": [box([0, 4, -8], [16, 12, 24]), ...], "scale": 4.0, "lift": 0.0}}
