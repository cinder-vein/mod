"""Preview entity models:  python3 tools/entity_models/preview.py out.png [key ...]

Renders each model from four angles with the real per-entity colors (uses the scratchpad software renderer)."""
import sys
from pathlib import Path

from PIL import Image

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, "/tmp/claude-0/-home-user-mod/96fe7e93-da4a-51ab-827c-893c832f9e8b/scratchpad")

import art  # noqa: E402
import render_model  # noqa: E402
from entity_models import load  # noqa: E402

COLORS = {"ion": ("green", (46, 200, 70)), "parallax": ("yellow", (245, 205, 30)), "butcher": ("red", (220, 30, 35)),
          "ophidian": ("orange", (250, 130, 20)), "adara": ("blue", (40, 130, 255)),
          "predator": ("violet", (215, 55, 220)), "proselyte": ("indigo", (105, 60, 230)),
          "life": ("white", (235, 242, 250)), "nekron": ("black", (95, 98, 110))}


def textures(key):
    corps, rgb = COLORS[key]
    glow = Image.new("RGBA", (16, 16), (255, 255, 240, 255))
    return {"0": art.construct_texture(corps, rgb), "1": glow}


def render_key(key, model):
    tex = textures(key)
    render_model.load_tex = lambda rl, tex=tex: tex[rl]  # textures by name
    m = {"elements": model["elements"], "textures": {"0": "0", "1": "1"}}
    views = [render_model.render(m, yaw=y, pitch=p, size=300, bg=(48, 52, 60)) for y, p in
             ((35, -20), (145, -20), (-90, -5), (0, -60))]
    sheet = Image.new("RGB", (1200, 300))
    for i, v in enumerate(views):
        sheet.paste(v, (300 * i, 0))
    return sheet


if __name__ == "__main__":
    models = load()
    keys = sys.argv[2:] or sorted(models)
    rows = [render_key(k, models[k]) for k in keys]
    out = Image.new("RGB", (1200, 300 * len(rows)))
    for i, r in enumerate(rows):
        out.paste(r, (0, 300 * i))
    out.save(sys.argv[1])
    print("rendered", keys)
