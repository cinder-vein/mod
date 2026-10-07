"""Models for the emotional spectrum entities' bodies (see tools/entities.py).

Each module defines MODELS = {entity key: {"elements": [...], "scale": float, "lift": float}}:
- elements: Minecraft item-model elements (from/to within -16..32, optional "rotation" with angle -45/-22.5/0/22.5/45
  on one axis). Faces use texture "#0" (the entity's hard-light texture, colored per entity) or "#1" (white-hot glow,
  for eyes and cores), with "uv" in 0..16.
- The model faces -z (an item_display turns its item half a turn, so -z ends up facing the entity's facing).
- scale: how big the display shows it (1 = one block for the 16-unit box); lift: blocks to raise it by.
"""
import importlib
import pkgutil
from pathlib import Path


def load():
    models = {}
    for info in pkgutil.iter_modules([str(Path(__file__).resolve().parent)]):
        if info.name.startswith(("preview", "example")):
            continue
        mod = importlib.import_module(f"entity_models.{info.name}")
        for key, model in getattr(mod, "MODELS", {}).items():
            if key in models:
                raise ValueError(f"entity model '{key}' defined twice")
            models[key] = model
    return models
