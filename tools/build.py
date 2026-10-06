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
        else:
            for tex in load(model).get("textures", {}).values():
                ns, _, p = tex.partition(":")
                check_ref("texture", f"{ns}:textures/{p}.png", model.name)
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

    for path in (SRC / "data" / NS / "palladium" / "item_powers").glob("*.json"):
        ip = load(path)
        check_ref("item", ip["item"], path.name)
        for p in ip["power"] if isinstance(ip["power"], list) else [ip["power"]]:
            check_ref("power", p, path.name)

    # client resources
    for path in (SRC / "assets" / NS / "palladium" / "render_layers").glob("*.json"):
        tex = load(path)["texture"]
        for t in tex.values() if isinstance(tex, dict) else [tex]:
            check_ref("texture", t, path.name)

    for path in (SRC / "data" / NS / "recipes").glob("*.json"):
        recipe = load(path)
        check_ref("item", recipe["result"]["item"], path.name)
        for ing in recipe.get("key", {}).values():
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
