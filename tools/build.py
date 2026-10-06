"""Validates the pack and packages it as a Forge mod jar.

    python3 tools/build.py

Output: dist/greenlantern-<version>-forge-1.20.1.jar
The same file also works as a Palladium addon pack (drop it in .minecraft/addonpacks).
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
NS = "greenlantern"

errors = []


def err(msg):
    errors.append(msg)


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001 - report every broken file
        err(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
        return None


def walk(node):
    """Yields every dict nested anywhere inside node."""
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)


def exists(kind, rl):
    ns, _, path = rl.partition(":")
    if ns != NS:
        return True  # vanilla / palladium ids are checked by the game
    places = {
        "item": [SRC / "addon" / ns / "items" / f"{path}.json"],
        "power": [SRC / "data" / ns / "palladium" / "powers" / f"{path}.json"],
        "render_layer": [SRC / "assets" / ns / "palladium" / "render_layers" / f"{path}.json"],
        "energy_beam": [SRC / "assets" / ns / "palladium" / "energy_beams" / f"{path}.json"],
        "emitter": [SRC / "assets" / ns / "palladium" / "particle_emitters" / f"{path}.json"],
        "trail": [SRC / "assets" / ns / "palladium" / "trails" / f"{path}.json"],
        "creative_tab": [SRC / "addon" / ns / "creative_mode_tabs" / f"{path}.json"],
        "texture": [SRC / "assets" / ns / path],
    }[kind]
    return any(p.exists() for p in places)


def check_ref(kind, rl, where):
    if not exists(kind, rl):
        err(f"{where}: unknown {kind} '{rl}'")


def validate():
    for path in SRC.rglob("*.json"):
        load(path)
    if errors:
        return

    lang = load(SRC / "assets" / NS / "lang" / "en_us.json")

    def check_lang(node, where):
        for obj in walk(node):
            key = obj.get("translate")
            if key and key not in lang:
                err(f"{where}: missing translation '{key}'")

    # items + creative tabs
    for path in (SRC / "addon" / NS / "items").glob("*.json"):
        if path.name.startswith("_"):
            continue
        item = load(path)
        rl = f"{NS}:{path.stem}"
        if f"item.{NS}.{path.stem}" not in lang:
            err(f"{path.name}: missing item name translation")
        model = SRC / "assets" / NS / "models" / "item" / path.name
        if not model.exists():
            err(f"{path.name}: missing item model")
        tabs = item.get("creative_mode_tab", [])
        for tab in tabs if isinstance(tabs, list) else [tabs]:
            check_ref("creative_tab", tab if isinstance(tab, str) else tab["tab"], rl)
        check_lang(item, path.name)
    for path in (SRC / "addon" / NS / "creative_mode_tabs").glob("*.json"):
        tab = load(path)
        check_ref("item", tab["icon"], path.name)
        for i in tab.get("items", []):
            check_ref("item", i, path.name)
        if f"itemGroup.{NS}.{path.stem}" not in lang:
            err(f"{path.name}: missing creative tab translation")

    # powers
    for path in (SRC / "data" / NS / "palladium" / "powers").glob("*.json"):
        power = load(path)
        where = f"power {path.stem}"
        abilities = power.get("abilities", {})
        uuids = {}
        bars = power.get("energy_bars", {})
        check_lang(power, where)
        if isinstance(power.get("icon"), str):
            check_ref("item", power["icon"], where)
        for name, ab in abilities.items():
            w = f"{where}/{name}"
            if isinstance(ab.get("icon"), str):
                check_ref("item", ab["icon"], w)
            if "render_layer" in ab:
                check_ref("render_layer", ab["render_layer"], w)
            if "energy_beam" in ab:
                check_ref("energy_beam", ab["energy_beam"], w)
            if ab.get("type") == "palladium:command" and "commands" not in ab:
                err(f"{w}: command ability must set 'commands' (Palladium defaults to 'say Hello World')")
            if ab.get("type") == "palladium:skin_change":
                for t in ab["texture"].values() if isinstance(ab["texture"], dict) else [ab["texture"]]:
                    check_ref("texture", t, w)
            if ab.get("type") == "palladium:gui_overlay":
                check_ref("texture", ab["texture"], w)
            for key in ("first_tick_commands", "commands", "last_tick_commands"):
                for cmd in ab.get(key, []):
                    for item in __import__("re").findall(r'id:"(%s:[a-z_]+)"' % NS, cmd):
                        check_ref("item", item, w)
            if "default_layer" in ab:
                check_ref("render_layer", ab["default_layer"], w)
            if "accessory_slot" in ab:
                ns, _, slot = ab["accessory_slot"].partition(":")
                if not (SRC / "addon" / ns / "accessory_slots" / f"{slot}.json").exists():
                    err(f"{w}: unknown accessory slot {ab['accessory_slot']}")
            if "trail" in ab:
                check_ref("trail", ab["trail"], w)
            if ab.get("type") == "palladium:ability_wheel":
                for sub in ab["abilities"]:
                    if sub not in abilities:
                        err(f"{w}: wheel references unknown ability '{sub}'")
            if ab.get("type") == "palladium:attribute_modifier":
                uuids.setdefault(ab["uuid"], []).append(w)
            for e in ab.get("emitter", []):
                check_ref("emitter", e, w)
            usages = ab.get("energy_bar_usage", [])
            for u in usages if isinstance(usages, list) else [usages]:
                if u["energy_bar"] not in bars:
                    err(f"{w}: unknown energy bar '{u['energy_bar']}'")
            for cond in walk(ab.get("conditions", {})):
                if "ability" in cond and cond["ability"] not in abilities:
                    err(f"{w}: condition references unknown ability '{cond['ability']}'")
                if cond.get("type") == "palladium:energy_bar" and cond["energy_bar"] not in bars:
                    err(f"{w}: unknown energy bar '{cond['energy_bar']}'")
                item = cond.get("item")
                if isinstance(item, dict) and "item" in item:
                    check_ref("item", item["item"], w)
            for key in ("first_tick_commands", "commands", "last_tick_commands"):
                for cmd in ab.get(key, []):
                    if cmd.startswith("/"):
                        err(f"{w}: commands must not start with '/'")
                    for k in re.findall(r'"translate\\":\\"([^"\\]+)', json.dumps(cmd)):
                        if k not in lang:
                            err(f"{w}: missing translation '{k}'")

        for u, users in uuids.items():
            if len(users) > 1:
                err(f"{where}: attribute uuid {u} used by {users}")

    for path in (SRC / "data" / NS / "palladium" / "item_powers").glob("*.json"):
        ip = load(path)
        check_ref("item", ip["item"], path.name)
        for p in ip["power"] if isinstance(ip["power"], list) else [ip["power"]]:
            check_ref("power", p, path.name)

    # client resources
    for path in (SRC / "assets" / NS / "palladium" / "render_layers").glob("*.json"):
        for layer in walk(load(path)):
            tex = layer.get("texture")
            for t in tex.values() if isinstance(tex, dict) else [tex] if tex else []:
                check_ref("texture", t, path.name)

    for path in (SRC / "addon" / NS / "accessory_slots").glob("*.json"):
        check_ref("texture", load(path)["icon"], path.name)
        if f"accessory_slot.{NS}.{path.stem}" not in lang:
            err(f"accessory slot {path.stem}: missing translation")
    for path in (SRC / "addon" / NS / "accessories").glob("*.json"):
        acc = load(path)
        check_ref("render_layer", acc["render_layer"], path.name)
        ns, _, slot = acc["slot"].partition(":")
        if not (SRC / "addon" / ns / "accessory_slots" / f"{slot}.json").exists():
            err(f"accessory {path.stem}: unknown slot {acc['slot']}")
        if f"accessory.{NS}.{path.stem}" not in lang:
            err(f"accessory {path.stem}: missing translation")

    for path in (SRC / "assets" / NS / "blockstates").glob("*.json"):
        if not (SRC / "addon" / NS / "blocks" / path.name).exists():
            err(f"blockstate {path.name}: no matching block")
        for variant in load(path)["variants"].values():
            ns, _, p = variant["model"].partition(":")
            if not (SRC / "assets" / ns / "models" / f"{p}.json").exists():
                err(f"blockstate {path.name}: missing model {variant['model']}")
    for path in (SRC / "addon" / NS / "blocks").glob("*.json"):
        if not (SRC / "assets" / NS / "blockstates" / path.name).exists():
            err(f"block {path.stem}: missing blockstate")
        if not (SRC / "data" / NS / "loot_tables" / "blocks" / path.name).exists():
            err(f"block {path.stem}: missing loot table")
        if f"block.{NS}.{path.stem}" not in lang:
            err(f"block {path.stem}: missing translation")
    for path in (SRC / "assets" / NS / "models").rglob("*.json"):
        model = load(path)
        for o in model.get("overrides", []):
            ns, _, m = o["model"].partition(":")
            if not (SRC / "assets" / ns / "models" / f"{m}.json").exists():
                err(f"model {path.name}: missing override model {o['model']}")
        parent = model.get("parent", "")
        if parent.startswith(NS + ":") and not (SRC / "assets" / NS / "models" / f"{parent.split(':')[1]}.json").exists():
            err(f"model {path.name}: missing parent {parent}")
        for tex in model.get("textures", {}).values():
            if not tex.startswith("#"):
                ns, _, p = tex.partition(":")
                check_ref("texture", f"{ns}:textures/{p}.png", path.name)
    for path in (SRC / "assets" / NS / "palladium" / "render_layers").glob("*.json"):
        layer = load(path)
        ml = layer.get("model_layer")
        for m in (ml.values() if isinstance(ml, dict) else [ml] if ml else []):
            ns, _, rest = m.partition(":")
            model, _, layer_name = rest.partition("#")
            if ns == NS and not (SRC / "assets" / ns / "palladium" / "model_layers" / layer_name / f"{model}.json").exists():
                err(f"{path.name}: missing model layer {m}")

    for path in (SRC / "data" / NS / "recipes").glob("*.json"):
        recipe = load(path)
        check_ref("item", recipe["result"]["item"], path.name)
        for ing in [*recipe.get("key", {}).values(), *recipe.get("ingredients", [])]:
            if "item" in ing:
                check_ref("item", ing["item"], path.name)

    for obj in walk(load(SRC / "data" / "curios" / "tags" / "items" / "ring.json")):
        for v in obj.get("values", []):
            check_ref("item", v, "curios ring tag")


def version():
    return json.loads((SRC / "pack.mcmeta").read_text())["pack"]["version"]


def package():
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{NS}-{version()}-forge-1.20.1.jar"
    files = sorted(p for p in SRC.rglob("*") if p.is_file())
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as jar:
        for p in files:
            info = zipfile.ZipInfo(p.relative_to(SRC).as_posix(), date_time=(2024, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            jar.writestr(info, p.read_bytes())
    return out, len(files)


if __name__ == "__main__":
    validate()
    if errors:
        print("Validation failed:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    out, n = package()
    print(f"OK - packaged {n} files into {out.relative_to(ROOT)}")
