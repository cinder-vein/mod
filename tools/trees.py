"""Skill trees built the way A New Corps builds its rings' trees.

A New Corps' ring powers lay their tree out on half-steps around the suit node (x from -1 to 1, the strength tree on
the left, defense on the right, health and charge above, the beam and constructs down the middle), give the power its
corps' bar texture and background, and put the real abilities in the tree: an ability is a node you buy with XP, and
once bought it is on the bar. The host powers are copies of their corps' ring power (clone_ring) with the entity's
branches added beside it; the Spectrum Bond's tree uses the same layout with its own abilities.
"""
import copy
import hashlib
import json
import re
from pathlib import Path

import suit_free
from common import CORPS, NS

BASE = Path(__file__).resolve().parent.parent / "base"
STEP = 0.5  # A New Corps' tree spacing (Palladium's grid is 50 pixels a unit)

# What a copy of a ring power leaves out: how the ring's suit looks (its layers, mask, cape, name, the suit-up sound
# and armor swap), and the abilities that need the ring itself on your finger. Looks that come from an effect
# (Willpower Overdrive's skin, the Berserker's) stay.
LOOKS = {"palladium:render_layer_by_accessory_slot", "palladium:name_change", "palladium:restrict_slots"}
EFFECT_LOOKS = {"palladium:render_layer", "palladium:hide_body_part", "palladium:shader_effect"}
RING_SLOTS = {"curios:lantern_rings", "trinkets:hand/ring"}


def ring_json(corps):
    path = BASE / f"data/{NS}/palladium/powers/{CORPS[corps]['power']}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def walk(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v)


def uuid_for(seed):
    h = hashlib.md5(seed.encode()).hexdigest()
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def unlocked(ability):
    return {"type": "palladium:ability_unlocked", "power": "null", "ability": ability}


def enabled(ability):
    return {"type": "palladium:ability_enabled", "power": "null", "ability": ability}


def buy(xp):
    return {"type": "palladium:experience_level_buyable", "xp_level": xp}


KEEP_NAMES = {"accessory_slot", "accessory", "default_layer"}  # the ring's accessory slot keeps its name


def _replace_strings(node, pattern, new):
    if isinstance(node, dict):
        return {k: v if k in KEEP_NAMES else _replace_strings(v, pattern, new) for k, v in node.items()}
    if isinstance(node, list):
        return [_replace_strings(v, pattern, new) for v in node]
    if isinstance(node, str):
        return pattern.sub(new, node)
    return node


def _left_out(ab):
    t = ab.get("type")
    if t in LOOKS:
        return True
    if t in EFFECT_LOOKS:
        return not any(c.get("type") == "palladium:has_effect" for c in walk(ab.get("conditions", {})))
    if t == "palladium:command":
        cmds = [c for k in ("first_tick_commands", "commands", "last_tick_commands") for c in ab.get(k) or []]
        if cmds and all(c.startswith(("pocket ", "playsound final_lanterns:suitup")) for c in cmds):
            return True
    return any(c.get("type") == "palladium:item_in_slot" and c.get("slot") in RING_SLOTS
               for c in walk(ab.get("conditions", {})))


def clone_ring(corps, power_id):
    """A copy of that corps' A New Corps ring power for another power (power_id, "ns:path"): its whole tree, bar,
    background and bar texture, its abilities working without the suit, minus the suit's looks and anything that
    needs the ring itself. Returns (power, suit node key); the suit node becomes the copy's root."""
    power = ring_json(corps)
    ring_id = f"{NS}:{CORPS[corps]['power']}"
    toggle = suit_free.suit_toggles(power)[0]
    suit_free.free_from_suit(power, ring_id)
    kept = {}
    for key, ab in power["abilities"].items():
        if key != toggle and _left_out(ab):
            continue
        for field in ("first_tick_commands", "commands", "last_tick_commands"):
            if field in ab:  # a ring's corps advancement and mastery belong to its bearers
                ab[field] = [c for c in ab[field] or [] if "advancement grant" not in c]
        if ab.get("type") == "palladium:attribute_modifier":  # its own modifiers: wearing the ring too stacks
            ab["uuid"] = uuid_for(f"{power_id}.{key}")
        kept[key] = ab
    # helpers left waiting on a look that was left out (Willpower's Green Machine timer)
    kept = {key: ab for key, ab in kept.items()
            if not any(c.get("type") in ("palladium:ability_enabled", "palladium:ability_unlocked")
                       and c.get("power") in (None, "null") and c.get("ability") in power["abilities"]
                       and c.get("ability") not in kept for c in walk(ab.get("conditions", {})))}
    power["abilities"] = kept
    # everything that named the ring's power (energy bar commands, ability locks, conditions) names the copy
    power = _replace_strings(power, re.compile(re.escape(ring_id) + r"(?![a-z0-9_/])"), power_id)
    return power, toggle


def raise_caps(power, cap=1000000):
    """A New Corps checks some abilities against its bar's top (charge between 0 and 4000): a bigger bar must not
    lock them."""
    for cond in walk(power["abilities"]):
        if cond.get("type") == "palladium:energy_bar" and isinstance(cond.get("max"), (int, float)) \
                and cond["max"] >= 2000:
            cond["max"] = cap


def occupied(power):
    """(min x, max x) of the tree's visible nodes."""
    xs = [ab["gui_position"][0] for ab in power["abilities"].values()
          if ab.get("hidden") is False and isinstance(ab.get("gui_position"), list)]
    return (min(xs), max(xs)) if xs else (0, 0)


def bar_indices(power):
    return {ab.get("list_index") for ab in power["abilities"].values()
            if isinstance(ab.get("list_index"), int) and ab.get("hidden_in_bar") is False}


def free_index(power, start=5):
    used = bar_indices(power)
    i = start
    while i in used:
        i += 1
    return i


def node(title, description, icon, pos, parents, xp=None, ability=None, bar=None, color="white"):
    """A tree node in A New Corps' style: the ability itself (a dummy when it's only a branch or a passive), visible
    in the tree, bought with XP once its parents are; `bar` puts it on the ability bar at that index."""
    ab = copy.deepcopy(ability) if ability else {"type": "palladium:dummy"}
    conds = ab.setdefault("conditions", {})
    own = conds.get("unlocking", [])
    own = own if isinstance(own, list) else [own]
    conds["unlocking"] = [*(unlocked(p) for p in parents), *([buy(xp)] if xp else []), *own]
    ab.update({"title": title, "description": description, "icon": icon, "gui_position": list(pos),
               "hidden": False, "hidden_in_bar": bar is None})
    if bar is not None:
        ab.update({"list_index": bar, "bar_color": color})
    return ab


COLOR_CORPS = {"green": "green", "yellow": "yellow", "red": "red", "orange": "orange", "blue": "blue",
               "pink": "violet"}  # A New Corps' construct tags (CustomTag) -> corps


def ring_constructs(corps):
    """{CustomTag value: construct items} a ring power hands out (its construct wheel)."""
    out = {}
    for ab in ring_json(corps)["abilities"].values():
        for field in ("first_tick_commands", "commands", "last_tick_commands"):
            for c in ab.get(field) or []:
                m = re.search(r"(?:give @s|with) (final_lanterns:[a-z0-9_]+)(\{[^ ]*)?", c)
                t = m and re.search(r'CustomTag:"?([a-z]+)', m[2] or "")
                if t and t[1] in COLOR_CORPS:
                    out.setdefault(t[1], set()).add(m[1])
    return out
