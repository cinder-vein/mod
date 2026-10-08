"""Builds Final Lanterns into src/.

    python3 -I tools/import_anc.py <a_new_corps zip>   # only when A New Corps itself changes: refreshes base/
    python3 tools/gen_final.py                         # base/ + our systems -> src/
    python3 tools/build.py                             # validates and packages the jar

Final Lanterns is based on A New Corps: its rings, powers, suits, models and icons are base/ (A New Corps renamed
into the final_lanterns namespace). This script copies base/ into src/, patches the few A New Corps files our
systems hook into, and adds our systems on top:

- emotions (with a random 10 000-15 000 start), the Emotional Spectrum menu and its quests (emotions.py);
- ring binding, recall, ring offers, corps leaders and admin tools (systems.py);
- the nine emotional spectrum entities (entities.py), their hosts' powers and suits (hosts.py) and the hard-light
  constructs they form (hardlight.py).

A file we generate never silently replaces an A New Corps file: main() stops if one would (the lang file and the
load/tick function tags are merged instead).
"""
import json
import shutil
from pathlib import Path

import emotions
import entities
import check
import entity_models
import hardlight
import hosts
import icons
import spectrum
import suit_free
import systems
from common import CORPS, HOSTILE_PREY, NOT_CREATURES, NS

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
BASE = ROOT / "base"
VERSION = "1.3.0"
MERGED = {f"assets/{NS}/lang/en_us.json", "data/minecraft/tags/functions/load.json",
          "data/minecraft/tags/functions/tick.json", "pack.mcmeta"}
PATCHED = set()  # A New Corps files deliberately rewritten (see patch_base)
written = {}


def write(rel, data):
    _claim(rel)
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(rel, text):
    _claim(rel)
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def save(img, rel):
    _claim(rel)
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def _claim(rel):
    if rel in written:
        raise SystemExit(f"generated twice: {rel}")
    if (BASE / rel).exists() and rel not in MERGED and rel not in PATCHED:
        raise SystemExit(f"would overwrite the A New Corps file {rel}")
    written[rel] = True


def base_json(rel):
    return json.loads((BASE / rel).read_text(encoding="utf-8"))


def patch(rel, data_or_text):
    PATCHED.add(rel)
    (write_text if isinstance(data_or_text, str) else write)(rel, data_or_text)


# --- A New Corps files our systems hook into ----------------------------------------------------

def patch_base(lang):
    # Its load function had a stray comma (a parse error stops the whole function) and a selector option that
    # vanilla can't parse; every player gets the base power in either case.
    load = (BASE / f"data/{NS}/functions/load.mcfunction").read_text(encoding="utf-8").splitlines()
    load = [line.rstrip(",") for line in load if "palladium.power=" not in line]
    patch(f"data/{NS}/functions/load.mcfunction", "\n".join(load) + "\n")
    # Its ring-sacrifice counter picked a color with a selector option vanilla can't parse (which stops the whole
    # function, counter included): one gold message instead.
    sac = (BASE / f"data/{NS}/functions/sacrifice.mcfunction").read_text(encoding="utf-8").splitlines()
    sac = [line for line in sac if "palladium.power=" not in line] + [
        'title @s actionbar [{"text":"Rings Sacrificed ","color":"gold","bold":true},{"score":{"name":"@s",'
        '"objective":"rings_sacrificed"},"color":"gold","bold":true},{"text":"/10 ","color":"gold","bold":true}]']
    patch(f"data/{NS}/functions/sacrifice.mcfunction", "\n".join(sac) + "\n")
    # Sacrificing ten rings to the yellow lantern no longer makes a second Parallax: our Parallax takes you, if free.
    patch(f"data/{NS}/functions/ring_sacrifice.mcfunction", "\n".join([
        f"execute as @a[scores={{rings_sacrificed=10..}}] at @s run function {NS}:entity/parallax/sacrifice",
        "scoreboard players reset @a[scores={rings_sacrificed=10..}] rings_sacrificed"]) + "\n")
    # Each of the nine rings: a marker our systems read (gl_<corps> while its power is on you), and the Emotional
    # Spectrum menu on its ability bar.
    for c, data in CORPS.items():
        rel = f"data/{NS}/palladium/powers/{data['power']}.json"
        power = base_json(rel)
        abilities = power["abilities"]
        used = {a.get("list_index") for a in abilities.values() if isinstance(a.get("list_index"), int)}
        top = max(i for i in used if i is not None)
        free = [i for i in range(5, 30) if i not in used and i // 5 <= top // 5]
        index = free[-1] if free else (top // 5 + 1) * 5
        abilities["fl_marker"] = {
            "type": "palladium:command", "hidden": True, "hidden_in_bar": True, "first_tick_commands": [],
            "commands": [f"tag @s add gl_{c}", f"scoreboard players set @s gl_t_{c} 3"], "last_tick_commands": []}
        abilities["fl_emotions"] = {
            "type": "palladium:command", "title": {"translate": f"ability.{NS}.emotional_spectrum"},
            "description": {"translate": f"ability.{NS}.emotional_spectrum.description"},
            "icon": hosts.glyph_icon("emotional_sight", c, data["color"], "minecraft:nether_star"),
            "bar_color": "white", "hidden": True, "hidden_in_bar": False, "list_index": index,
            "first_tick_commands": [f"function {NS}:emotion/menu"], "commands": [], "last_tick_commands": [],
            "conditions": {"enabling": [{"type": "palladium:action", "cooldown": 20, "key_type": "key_bind"}]}}
        suit_free.free_from_suit(power, f"{NS}:{data['power']}")
        patch(rel, spectrum.patch_ring(c, power))
    # Every other A New Corps ring too: its abilities work while it's worn, suit or no suit (the suit is just a look)
    ours = {data["power"] for data in CORPS.values()}
    for path in sorted((BASE / f"data/{NS}/palladium/powers").glob("*.json")):
        power = json.loads(path.read_text(encoding="utf-8"))
        if path.stem not in ours and power.get("energy_bars") and suit_free.free_from_suit(power, f"{NS}:{path.stem}"):
            patch(f"data/{NS}/palladium/powers/{path.name}", power)
    lang[f"ability.{NS}.emotional_spectrum"] = "Emotional Spectrum"
    lang[f"ability.{NS}.emotional_spectrum.description"] = "Your emotions, what raised them, and their quests."
    # Orange had no ring-forging animation of its own (the hosts' Forge Ring uses one per color)
    forge = base_json(f"data/{NS}/palladium/powers/ring_construction/green_lantern.json")
    text = json.dumps(forge).replace("ring_construction/green_ring", "ring_construction/orange_ring")
    text = text.replace("minecraft:dust 0 1 0.5", "minecraft:dust 1 0.5 0.05")
    write(f"data/{NS}/palladium/powers/ring_construction/orange_lantern.json", json.loads(text))
    write_text(f"data/{NS}/functions/orangelanternconstruction.mcfunction", "\n".join([
        'execute positioned ^ ^ ^ run summon minecraft:armor_stand ~ ~ ~ {Tags:["ring_construction_energy"],'
        'Invisible:1b,Invulnerable:1b}',
        f"superpower add {NS}:ring_construction/orange_lantern @e[tag=ring_construction_energy]",
        "tag @e[tag=ring_construction_energy] remove ring_construction_energy"]) + "\n")


# --- the entities' bodies, lanterns and the hidden power every player carries ----------------------

def entity_assets(lang):
    models = entity_models.load()
    write(f"addon/{NS}/items/entity_body.json", {"type": "palladium:default", "max_stack_size": 1})
    lang[f"item.{NS}.entity_body"] = "Emotional Entity"
    overrides = []
    for i, e in enumerate(entities.ENTITIES, 1):
        elements = models.get(e.key, {}).get("elements") or [hardlight._box([2, 2, 2], [14, 14, 14])]
        write(f"assets/{NS}/models/item/entity_body_{e.key}.json", {
            "textures": {"0": f"{NS}:item/construct/{e.corps}", "1": f"{NS}:item/construct/glow",
                         "particle": f"{NS}:item/construct/{e.corps}"},
            "elements": elements})
        overrides.append({"predicate": {"custom_model_data": i}, "model": f"{NS}:item/entity_body_{e.key}"})
    write(f"assets/{NS}/models/item/entity_body.json", {
        "parent": f"{NS}:item/entity_body_{entities.ENTITIES[0].key}", "overrides": overrides})
    # the Entity Lantern: a corps' lantern with an entity sealed inside (looks like that corps' lantern)
    write(f"addon/{NS}/items/entity_lantern.json", {"type": "palladium:default", "max_stack_size": 1, "rarity": "epic",
                                                    "is_fire_resistant": True})
    lang[f"item.{NS}.entity_lantern"] = "Entity Lantern"
    write(f"assets/{NS}/models/item/entity_lantern.json", {
        "parent": CORPS["green"]["battery_model"],
        "overrides": [{"predicate": {"custom_model_data": i}, "model": CORPS[e.corps]["battery_model"]}
                      for i, e in enumerate(entities.ENTITIES, 1)]})
    write(f"data/{NS}/tags/items/power_batteries.json", {"replace": False, "values": [
        CORPS[c]["battery"] for c in CORPS]})
    return models


def spirit_power():
    """final_lanterns:emotional_spectrum: a hidden power every player has. It answers chat phrases without KubeJS,
    through Palladium's own chat conditions (calling your ring, answering a ring's offer, the Emotional Spectrum
    menu, releasing your entity), and right-clicks with an Entity Lantern."""
    abilities = {}
    phrases = {**systems.chat_phrases(CORPS), "i release you": "entity/release_ask", "i release you!": "entity/release_ask"}
    abilities["lantern_use"] = {
        **hosts.command(first=[f"function {NS}:entity/lantern_use"]), "hidden": True, "hidden_in_bar": True,
        "conditions": {"unlocking": {"type": "palladium:item_in_slot", "item": {"item": f"{NS}:entity_lantern"},
                                     "slot": "mainhand"},
                       "enabling": {"type": "palladium:action", "key_type": "right_click", "cooldown": 20}}}
    for n, (phrase, function) in enumerate(sorted(phrases.items())):
        abilities[f"chat_{n}"] = {
            **hosts.command(first=[f"function {NS}:{function}"]), "hidden": True, "hidden_in_bar": True,
            "conditions": {"enabling": {"type": "palladium:chat_action", "chat_message": phrase, "cooldown": 20}}}
    return {"name": {"translate": f"power.{NS}.emotional_spectrum"}, "icon": "minecraft:nether_star", "hidden": True,
            "abilities": abilities}


def mods_toml():
    return f'''# Data-only Forge mod: no Java code, so it uses Forge's low-code loader.
# Palladium loads every mod jar as an addon pack, which is how the "addon/" folder in this jar gets loaded.
modLoader="lowcodefml"
loaderVersion="[47,)"
license="All rights reserved"

[[mods]]
modId="{NS}"
version="{VERSION}"
displayName="Final Lanterns"
authors="cinder-vein"
logoFile="pack.png"
description=\'\'\'
The Lantern Corps of the emotional spectrum, and the entities behind it.
Based on A New Corps.
\'\'\'
''' + "".join(f'''
[[dependencies.{NS}]]
    modId="{mod}"
    mandatory=true
    versionRange="{versions}"
    ordering="{ordering}"
    side="BOTH"
''' for mod, versions, ordering in (("forge", "[47,)", "NONE"), ("minecraft", "[1.20.1,1.20.2)", "NONE"),
                                    ("palladium", "[4.0.0,)", "AFTER"), ("geckolib", "*", "NONE"),
                                    ("gravecore", "[1.2.1,)", "NONE"), ("curios", "*", "NONE"),
                                    ("kubejs", "*", "NONE")))


def main():
    shutil.rmtree(SRC, ignore_errors=True)
    shutil.copytree(BASE, SRC)
    lang = {}
    patch_base(lang)

    load, tick, second, fn = ["scoreboard objectives add gl_life dummy"], [], [], {}

    def merge(parts):
        p_load, p_tick, p_second, p_fn = parts
        load.extend(p_load)
        tick.extend(p_tick)
        second.extend(p_second)
        for path, lines in p_fn.items():
            if path in fn:
                raise SystemExit(f"function defined twice: {path}")
            fn[path] = lines

    # ring markers: gl_<corps> lasts while that ring's power keeps refreshing it; gl_ring while any does
    for c in CORPS:
        load.append(f"scoreboard objectives add gl_t_{c} dummy")
        tick += [f"scoreboard players add @a[tag=gl_{c}] gl_t_{c} 0",
                 f"scoreboard players remove @a[scores={{gl_t_{c}=1..}}] gl_t_{c} 1",
                 f"tag @a[tag=gl_{c},scores={{gl_t_{c}=..0}}] remove gl_{c}"]
    tick += ["tag @a[tag=gl_ring] remove gl_ring"] + [f"tag @a[tag=gl_{c}] add gl_ring" for c in CORPS]

    s_load, s_tick, s_fn = systems.generate(CORPS, write, write_text)
    s_second = s_fn.pop("second")  # systems' once-a-second function is the one everything shares
    merge((s_load, s_tick, [], s_fn))
    e_load, e_tick, e_second, e_fn, e_files = emotions.generate()
    merge((e_load, e_tick, e_second, e_fn))
    n_load, n_tick, n_second, n_fn, n_files = entities.generate(entities.body_sizes(entity_models.load()))
    merge((n_load, n_tick, n_second, n_fn))
    h_fn, h_load, h_second = hosts.functions()
    merge((h_load, [], h_second, h_fn))
    merge(([], hardlight.tick_lines(), [], hardlight.world_constructs()))
    merge(spectrum.generate())
    c_load, c_tick, c_fn = check.generate()
    merge((c_load, c_tick, [], c_fn))
    second.append(f"superpower add {NS}:emotional_spectrum @a")
    fn["second"] = s_second + second
    for path, data in {**e_files, **n_files}.items():
        write(f"data/{NS}/{path}", data)
    tick.insert(0, "# Generated by tools/gen_final.py")
    fn["fl/tick"] = tick
    fn["fl/load"] = load
    for path, lines in fn.items():
        write_text(f"data/{NS}/functions/{path}.mcfunction", "\n".join(lines) + "\n")

    # Every entry optional: a function tag with one missing function (one that failed to load, say) is dropped whole,
    # which would stop A New Corps' tick and ours together.
    for rel, value in (("data/minecraft/tags/functions/load.json", f"{NS}:fl/load"),
                       ("data/minecraft/tags/functions/tick.json", f"{NS}:fl/tick")):
        tag = base_json(rel)
        tag["values"] = [{"id": v, "required": False} if isinstance(v, str) else v for v in tag["values"] + [value]]
        write(rel, tag)
    write(f"data/{NS}/tags/entity_types/not_creatures.json", {"replace": False, "values": [
        t if t.startswith("minecraft:") else {"id": t, "required": False} for t in NOT_CREATURES]})
    write(f"data/{NS}/tags/entity_types/hostile_prey.json", {"replace": False, "values": HOSTILE_PREY})

    items = hardlight.item_files(write, save, lang)
    entity_assets(lang)
    hosts.assets(write, lang)
    spectrum.assets(write, save, lang)
    write(f"data/{NS}/palladium/powers/emotional_spectrum.json", spirit_power())
    lang[f"power.{NS}.emotional_spectrum"] = "Emotional Spectrum"
    for name, (glyph, rgb) in sorted(hosts.ICONS.items()):
        save(icons.render(glyph, rgb), f"assets/{NS}/textures/gui/ability/{name}")
    print(f"{len(items)} construct shapes, {len(entities.ENTITIES)} entities, {len(fn)} functions")

    # mod metadata, the logo, and our translations merged into A New Corps' own
    write_text("META-INF/mods.toml", mods_toml())
    pack = base_json("pack.mcmeta")
    pack["pack"].update({"id": NS, "description": "Final Lanterns (based on A New Corps)", "version": VERSION})
    # two Lantern Ring slots, for the Spectrum Bond (Palladium registers this slot from here)
    pack["custom"]["curios"]["lantern_rings"]["size"] = 2
    write("pack.mcmeta", pack)
    shutil.copyfile(ROOT / "tools/templates/logo.png", SRC / "pack.png")
    base_lang = base_json(f"assets/{NS}/lang/en_us.json")
    clash = sorted(k for k in lang if k in base_lang and base_lang[k] != lang[k])
    if clash:
        raise SystemExit(f"translations that would replace A New Corps' own: {clash[:5]}")
    write(f"assets/{NS}/lang/en_us.json", {**base_lang, **lang})

    # The KubeJS script again, to copy into the game's kubejs folder by hand if Palladium doesn't load it from the
    # jar (/ring or /lantern "unknown command" with KubeJS installed).
    shutil.rmtree(ROOT / "kubejs", ignore_errors=True)
    dest = ROOT / "kubejs/server_scripts/lantern_commands.js"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC / f"data/{NS}/kubejs_scripts/lantern_commands.js", dest)


if __name__ == "__main__":
    main()
