"""The Spectrum Bond: two of the nine spectrum rings worn at once (A New Corps' Lantern Ring slot holds two).

While a player wears two, the datapack grants final_lanterns:spectrum_bond. Each ring keeps its own A New Corps power
and bar; the bond adds one more bar, a skill tree about wielding two lights, and a merged suit:

- Twin Beam: both rings' beams at once, one from each hand (each paid by its own ring).
- Twin Constructs: one construct wheel with both corps' construct weapons.
- Spectrum Fusion: a burst that fuses the two emotions (every pair has its own), then Fusion Mastery.
- Prismatic Shield: Resistance II in both colors while it's up (both rings pay).
- Spectrum Overload: the ultimate, both rings unleashed at once.
- Harmony: Shared Light (charge flows to the emptier ring), Twin Lanterns (recharging one ring at its lantern fills
  both) and Resonance (both regain charge on their own).
- Body: Dual Vitality, Twin Strength, Spectrum Flight.
- Merged suits in the accessories menu (Spectrum Suit slot): both corps' A New Corps suits split down the middle or
  at the belt; "Own Suits" keeps each ring's own.

The first of the two rings in common.CORPS order is the right-hand ring (gl_p1_<corps>), the other the left (gl_p2_).
"""
import hashlib
import json
import math
from pathlib import Path

from PIL import Image

import entities
import hosts
from common import CORPS, NS, TARGETS, burst, hexcolor, sound, tellraw

BASE = Path(__file__).resolve().parent.parent / "base"
BOND = f"{NS}:spectrum_bond"
ORDER = list(CORPS)
RGB = (235, 240, 255)  # the bond's own color: every light at once
COSTS = {"fusion": 125, "fusion_mastered": 75, "overload": 400}
FUSION_COOLDOWN, MASTERED_COOLDOWN, OVERLOAD_COOLDOWN = 600, 300, 1200
OVERLOAD_RADIUS = 12
SHARED_FLOW = 20  # charge a second from the fuller ring into the emptier one
RESONANCE = 1     # charge a tick each ring regains
SUIT_SLOT = f"{NS}:spectrum_suit"
OWN_SUITS = f"{NS}:spectrum_suit_own"
DESIGNS = [("split", "Split Light"), ("split_reversed", "Split Light (Reversed)"), ("halves", "Above and Below"),
           ("halves_reversed", "Above and Below (Reversed)")]

FUSION_NAMES = {
    ("green", "yellow"): "Will Over Fear", ("green", "red"): "Righteous Fury", ("green", "orange"): "Unbreakable Grasp",
    ("green", "blue"): "Hope Ignites Will", ("green", "violet"): "Heart's Resolve", ("green", "indigo"): "Steadfast Mercy",
    ("green", "white"): "Emerald Dawn", ("green", "black"): "Brightest Day, Blackest Night",
    ("yellow", "red"): "Terror and Fury", ("yellow", "orange"): "Greed for Terror", ("yellow", "blue"): "Courage Under Fear",
    ("yellow", "violet"): "Love's Dread", ("yellow", "indigo"): "Empathic Terror", ("yellow", "white"): "Fear of Life",
    ("yellow", "black"): "Dread of the Grave",
    ("red", "orange"): "Burning Greed", ("red", "blue"): "Rage Tempered by Hope", ("red", "violet"): "Crimson Passion",
    ("red", "indigo"): "Rage Understood", ("red", "white"): "Blood of Life", ("red", "black"): "Blood and Bone",
    ("orange", "blue"): "Hope Hoarded", ("orange", "violet"): "Covetous Heart", ("orange", "indigo"): "Shared Fortune",
    ("orange", "white"): "Abundance", ("orange", "black"): "Hoard of the Dead",
    ("blue", "violet"): "Hopeful Heart", ("blue", "indigo"): "Gentle Light", ("blue", "white"): "Radiant Hope",
    ("blue", "black"): "Hope in Darkness",
    ("violet", "indigo"): "Tender Embrace", ("violet", "white"): "Love Eternal", ("violet", "black"): "Love Beyond Death",
    ("indigo", "white"): "Mercy of Life", ("indigo", "black"): "Last Rites",
    ("white", "black"): "Life and Death",
}
PAIRS = [(a, b) for i, a in enumerate(ORDER) for b in ORDER[i + 1:]]

FOES = TARGETS.format(r=10) + "]"
FRIENDS = "@a[distance=..10]"
# each corps' share of a fusion (run as the bearer, tagged gl_user)
SIGNATURE = {
    "green": [f"execute as {FOES} run damage @s 8 minecraft:player_attack by @p[tag=gl_user]",
              f"effect give {FOES} minecraft:levitation 1 3 true"],
    "yellow": [f"effect give {FOES} minecraft:{x} 8 {a} true" for x, a in
               (("darkness", 0), ("slowness", 2), ("weakness", 1))],
    "red": [f"execute as {FOES} run data merge entity @s {{Fire:100s}}", f"effect give {FOES} minecraft:wither 5 1 true"],
    "orange": [f"execute rotated ~ 0 positioned ^ ^ ^2 run tp {TARGETS.format(r=12)},type=!minecraft:player] ~ ~ ~",
               f"effect give {FOES} minecraft:weakness 8 1 true"],
    "blue": [f"effect give {FRIENDS} minecraft:regeneration 10 1 true",
             f"effect give {FRIENDS} minecraft:resistance 10 0 true"],
    "violet": [f"effect give {FOES} minecraft:weakness 10 3 true", f"effect give {FOES} minecraft:slowness 10 1 true",
               f"execute at {FOES} run particle minecraft:heart ~ ~2 ~ 0.3 0.3 0.3 0 2 force"],
    "indigo": [f"effect give {FRIENDS} minecraft:instant_health 1 0 true",
               f"effect give {FOES} minecraft:weakness 10 254 true"],
    "white": [f"effect give {FRIENDS} minecraft:absorption 30 2 true",
              "effect give @e[distance=..10,type=!minecraft:item,type=!minecraft:experience_orb] "
              "minecraft:instant_health 1 1 true"],
    "black": [f"effect give {FOES} minecraft:wither 8 1 true", f"effect give {FOES} minecraft:darkness 8 0 true",
              "particle minecraft:soul ~ ~1 ~ 4 1 4 0.02 80 force"],
}


def fx(c):
    return CORPS[c]["color"] if c != "black" else (150, 155, 170)


def power(c):
    return f"{NS}:{CORPS[c]['power']}"


def bar_ref(c):
    return f"{power(c)}#{CORPS[c]['bar']}"


def has_power(c):
    return {"type": "palladium:has_power", "power": power(c)}


def NOT(*conds):
    return {"type": "palladium:not", "conditions": list(conds)}


def OR(*conds):
    return {"type": "palladium:or", "conditions": list(conds)}


def AND(*conds):
    return {"type": "palladium:and", "conditions": list(conds)}


def right_hand(c):
    """c is the first of the worn rings (the right hand): nothing earlier in ORDER is worn."""
    before = [has_power(x) for x in ORDER[:ORDER.index(c)]]
    return [has_power(c), *([NOT(OR(*before))] if before else [])]


def left_hand(c):
    before = [has_power(x) for x in ORDER[:ORDER.index(c)]]
    return [has_power(c), OR(*before)] if before else [{"type": "palladium:false"}]


def bond(a, b):
    """True while rings a and b are the two worn (only two Lantern Ring slots, so exactly one pair matches)."""
    return [has_power(a), has_power(b)]


def charge(c, amount):
    return {"type": "palladium:energy_bar", "power": power(c), "energy_bar": CORPS[c]["bar"], "min": amount}


def construct_items():
    """{corps: [(item, name, offhand?)]}: each corps' A New Corps construct weapons (the same as its entity host's)."""
    return {e.corps: hosts.WHEEL_ITEMS[e.key] for e in entities.ENTITIES}


DUAL_NODES = [  # key, name, description, icon (an item, or glyph:<name>), position, parent, XP levels
    ("twin_beam", "Twin Beam", "Hold to fire both rings' beams at once, one from each hand. Each ring pays for its own.",
     "glyph:twin_beam", (-1, 1), "bond_root", 5),
    ("twin_constructs", "Twin Constructs", "One construct wheel with both corps' construct weapons.",
     "glyph:constructs", (-1, 2), "twin_beam", 10),
    ("prismatic", "Prismatic Shield", "Toggle: Resistance II and a shield of both colors. Each ring pays 1 charge a "
     "tick.", "glyph:prismatic", (-1, 3), "twin_constructs", 12),
    ("fusion", "Spectrum Fusion", "Fuse both emotions in one burst around you: every pair of corps has its own fusion. "
     f"Costs {COSTS['fusion']} charge from each ring, every 30 seconds.", "glyph:fusion", (1, 1), "bond_root", 8),
    ("fusion_mastery", "Fusion Mastery", f"Spectrum Fusion recharges in 15 seconds and costs {COSTS['fusion_mastered']} "
     "from each ring.", "minecraft:nether_star", (1, 2), "fusion", 15),
    ("overload", "Spectrum Overload", f"Ultimate: unleash both rings at once. Everything within {OVERLOAD_RADIUS} blocks "
     "takes heavy damage and is thrown into the air, and you gain Strength II, Resistance II and Speed II for 15 "
     f"seconds. Costs {COSTS['overload']} charge from each ring, once a minute.", "glyph:overload", (1, 3),
     "fusion_mastery", 30),
    ("shared_light", "Shared Light", f"Every second, up to {SHARED_FLOW} charge flows from the fuller ring into the "
     "emptier one.", "minecraft:glowstone_dust", (-3, 1), "bond_root", 5),
    ("twin_lanterns", "Twin Lanterns", "Recharging either ring at its lantern fills both rings.", "minecraft:lantern",
     (-3, 2), "shared_light", 10),
    ("resonance", "Resonance", f"The two lights feed each other: both rings regain {RESONANCE * 20} charge a second.",
     "minecraft:amethyst_shard", (-3, 3), "twin_lanterns", 15),
    ("dual_vitality", "Dual Vitality", "+10 hearts.", "minecraft:golden_apple", (3, 1), "bond_root", 8),
    ("twin_strength", "Twin Strength", "+3 attack and punch damage.", "minecraft:netherite_sword", (3, 2),
     "dual_vitality", 12),
    ("spectrum_flight", "Spectrum Flight", "Fly faster on two lights (with either ring's flight).", "minecraft:elytra",
     (3, 3), "twin_strength", 12),
]
TAGGED_NODES = ["shared_light", "twin_lanterns"]  # skills the datapack carries out (tagged gl_dn_<node>)


def glyph(name, fallback):
    return hosts.glyph_icon(name, "bond", RGB, fallback)


def unlocked(ability):
    return {"type": "palladium:ability_unlocked", "ability": ability}


def enabled(ability):
    return {"type": "palladium:ability_enabled", "ability": ability}


def power_json(lang):
    abilities = {}

    def tr(key, english):
        lang[f"ability.{NS}.bond.{key}"] = english
        return {"translate": f"ability.{NS}.bond.{key}"}

    def hidden(key, ability):
        abilities[key] = {**ability, "hidden": True, "hidden_in_bar": True}

    def bar(key, ability, name, icon, index, desc=None):
        abilities[key] = {**ability, "title": tr(key.split("__")[0], name), "icon": icon, "bar_color": "white",
                          "hidden": True, "hidden_in_bar": False, "list_index": index}
        if desc:
            abilities[key]["description"] = tr(key.split("__")[0] + ".description", desc)

    abilities["bond_root"] = {
        "type": "palladium:dummy", "title": tr("bond_root", "Spectrum Bond"),
        "description": tr("bond_root.description", "Two rings, two emotions, one light. While you wear two spectrum "
                          "rings, the Spectrum Bond adds this bar and this skill tree; each ring keeps its own. Choose "
                          "a merged suit in the accessories menu (Spectrum Suit)."),
        "icon": "minecraft:nether_star", "hidden_in_bar": True, "gui_position": [0, 0]}
    for key, name, desc, icon, pos, parent, xp in DUAL_NODES:
        if icon.startswith("glyph:"):
            icon = glyph(icon[6:], "minecraft:nether_star")
        abilities[f"skill_{key}"] = {
            "type": "palladium:dummy", "title": tr(key, name), "description": tr(key + ".description",
                                                                                  desc + f" Costs {xp} XP levels."),
            "icon": icon, "hidden_in_bar": True, "gui_position": list(pos),
            "conditions": {"unlocking": [unlocked(parent if parent == "bond_root" else f"skill_{parent}"),
                                         {"type": "palladium:experience_level_buyable", "xp_level": xp}]}}
    for key in TAGGED_NODES:
        hidden(f"tag_{key}", {**hosts.command(every=[f"tag @s add gl_dn_{key}"]),
                              "conditions": {"unlocking": unlocked(f"skill_{key}")}})

    # --- Twin Beam: each corps' A New Corps beam, the right-hand ring's from the right arm, the left's from the left
    bar("twin_beam", {"type": "palladium:dummy", "conditions": {"unlocking": unlocked("skill_twin_beam"),
                                                                 "enabling": [{"type": "palladium:held"}]}},
        "Twin Beam", glyph("twin_beam", "minecraft:end_rod"), 0, "Hold: both rings' beams at once.")
    hidden("twin_aim", {"type": "palladium:aim", "time": 1, "arm": "both",
                        "conditions": {"enabling": enabled("twin_beam")}})
    for c in ORDER:
        beam = hosts.anc_ability(c, CORPS[c]["beam"])
        for k in ("title", "description", "gui_position", "list_index", "icon", "bar_color"):
            beam.pop(k, None)
        beam["energy_bar_usage"] = {"energy_bar": bar_ref(c), "amount": beam.get("energy_bar_usage", {}).get("amount", 5)}
        left = left_beam(beam["energy_beam"])
        for side, hand, beam_id in (("r", right_hand(c), beam["energy_beam"]), ("l", left_hand(c), left)):
            hidden(f"beam_{side}_{c}", {**beam, "energy_beam": beam_id, "conditions": {
                "unlocking": hand, "enabling": [enabled("twin_beam"), charge(c, 5)]}})

    # --- Twin Constructs: one wheel per pair, sharing each corps' construct abilities
    items = construct_items()
    children = {}
    for c in ORDER:
        children[c] = []
        for n, item in enumerate(items[c]):
            iid, iname, offhand = item[0], item[1], len(item) > 2
            nbt = f"{{CustomTag:{c},fl_bond:1b}}"
            give = (f"item replace entity @s weapon.offhand with {NS}:{iid}{nbt}" if offhand else
                    f"give @s {NS}:{iid}{nbt} {hosts.ARROW_COUNT if iid == 'lovearrow' else 1}")
            enabling = [hosts.key_action(30, empty_hand=not offhand)]
            if offhand:
                enabling.append({"type": "palladium:empty_slot", "slot": "offhand"})
            key = f"cx_{c}_{n}"
            children[c].append(key)
            hidden(key, {**hosts.command(first=[give, sound("minecraft:block.beacon.power_select", 1.8)]),
                         "title": tr(f"cx_{iid}", iname), "icon": f"{NS}:{iid}", "list_index": 1,
                         "conditions": {"unlocking": [unlocked("skill_twin_constructs"), has_power(c)],
                                        "enabling": enabling}})
    for a, b in PAIRS:
        bar(f"twin_constructs__{a}_{b}", {
            "type": "palladium:ability_wheel", "abilities": children[a] + children[b], "texture": "null",
            "disable_mouse_scrolling": False,
            "conditions": {"unlocking": [unlocked("skill_twin_constructs"), *bond(a, b)],
                           "enabling": [{"type": "palladium:held"}]}},
            "Twin Constructs", glyph("constructs", "minecraft:emerald"), 1, "Hold: both corps' construct weapons.")

    # --- Spectrum Fusion (two strengths) and Spectrum Overload: one per pair, paid by both rings
    for a, b in PAIRS:
        for key, cost, cooldown, mastered in (("fusion", COSTS["fusion"], FUSION_COOLDOWN, False),
                                              ("fusion_mastered", COSTS["fusion_mastered"], MASTERED_COOLDOWN, True)):
            unlock = [unlocked("skill_fusion"), *bond(a, b), charge(a, cost), charge(b, cost),
                      unlocked("skill_fusion_mastery") if mastered else NOT(unlocked("skill_fusion_mastery"))]
            bar(f"fusion__{key}_{a}_{b}", {
                **hosts.command(first=["tag @s add gl_user", f"function {NS}:bond/fusion/{a}_{b}",
                                       "tag @s remove gl_user"]),
                "energy_bar_usage": [{"energy_bar": bar_ref(a), "amount": cost},
                                     {"energy_bar": bar_ref(b), "amount": cost}],
                "conditions": {"unlocking": unlock, "enabling": hosts.action(cooldown)}},
                "Spectrum Fusion", glyph("fusion", "minecraft:nether_star"), 2,
                "Fuse both emotions in one burst around you.")
        cost = COSTS["overload"]
        bar(f"overload__{a}_{b}", {
            **hosts.command(first=["tag @s add gl_user", f"function {NS}:bond/overload/{a}_{b}", "tag @s remove gl_user"]),
            "energy_bar_usage": [{"energy_bar": bar_ref(a), "amount": cost}, {"energy_bar": bar_ref(b), "amount": cost}],
            "conditions": {"unlocking": [unlocked("skill_overload"), *bond(a, b), charge(a, cost), charge(b, cost)],
                           "enabling": hosts.action(OVERLOAD_COOLDOWN)}},
            "Spectrum Overload", glyph("overload", "minecraft:nether_star"), 4,
            f"Ultimate: both rings unleashed at once. Costs {cost} charge from each ring.")

    # --- Prismatic Shield: a toggle, each worn ring pays a charge a tick
    bar("prismatic", {**hosts.command(first=["tag @s add gl_prism"], last=["tag @s remove gl_prism"]),
                      "conditions": {"unlocking": unlocked("skill_prismatic"), "enabling": hosts.toggle()}},
        "Prismatic Shield", glyph("prismatic", "minecraft:shield"), 3,
        "Toggle: Resistance II while both rings hold charge.")
    for c in ORDER:
        hidden(f"prismatic_{c}", {"type": "palladium:dummy", "energy_bar_usage": {"energy_bar": bar_ref(c), "amount": 1},
                                  "conditions": {"unlocking": has_power(c),
                                                 "enabling": [enabled("prismatic"), charge(c, 1)]}})
        hidden(f"resonance_{c}", {"type": "palladium:dummy",
                                  "energy_bar_usage": {"energy_bar": bar_ref(c), "amount": -RESONANCE},
                                  "conditions": {"unlocking": [unlocked("skill_resonance"), has_power(c)]}})
    hidden("prismatic_resist", {**hosts.command(first=["effect give @s minecraft:resistance 2 1 true"]),
                                "conditions": {"enabling": [enabled("prismatic"), hosts.interval(20)]}})

    # --- the body
    def attr(key, attribute, amount, node):
        hidden(key, {"type": "palladium:attribute_modifier", "attribute": attribute, "amount": amount, "operation": 0,
                     "uuid": "6c7abead-1a2b-4c3d-8e4f-" + hashlib.md5(f"bond.{key}".encode()).hexdigest()[:12],
                     "conditions": {"unlocking": unlocked(f"skill_{node}")}})

    attr("dual_vitality", "minecraft:generic.max_health", 20, "dual_vitality")
    attr("twin_strength", "minecraft:generic.attack_damage", 3, "twin_strength")
    attr("twin_strength_fists", "palladium:punch_damage", 3, "twin_strength")
    attr("spectrum_flight", "palladium:flight_speed", 0.5, "spectrum_flight")

    # --- the Emotional Spectrum menu, and the merged suit
    bar("emotions", {**hosts.command(first=[f"function {NS}:emotion/menu"]), "conditions": {"enabling": hosts.action(20)}},
        "Emotional Spectrum", glyph("emotional_sight", "minecraft:nether_star"), 5,
        "Your emotions, what raised them, and their quests.")
    either_suit = OR(*[{"type": "palladium:ability_enabled", "power": power(c), "ability": CORPS[c]["power"]}
                       for c in ORDER])
    hidden("spectrum_suit", {"type": "palladium:render_layer_by_accessory_slot", "accessory_slot": SUIT_SLOT,
                             "default_layer": f"{NS}:spectrum/{DESIGNS[0][0]}", "conditions": {"enabling": either_suit}})
    hidden("spectrum_suit_skin", {"type": "palladium:hide_body_part", "body_parts": [
        "right_arm_overlay", "left_arm_overlay", "right_leg_overlay", "left_leg_overlay", "chest_overlay",
        "head_overlay"], "affects_first_person": True, "conditions": {"enabling": [either_suit, merged_suit()]}})
    return {"name": {"translate": f"power.{NS}.spectrum_bond"}, "icon": "minecraft:nether_star",
            "background": "minecraft:textures/block/white_concrete.png", "gui_display_type": "tree",
            "primary_color": hexcolor(RGB), "secondary_color": "#3A3D46", "persistent_data": True,
            "abilities": abilities}


def merged_suit():
    """True while the bond's merged suit replaces each ring's own (anything but Own Suits picked)."""
    return AND({"type": "palladium:has_power", "power": BOND},
               NOT({"type": "palladium:accessory_selected", "accessory_slot": SUIT_SLOT, "accessory": OWN_SUITS}))


LEFT_BEAMS = {}  # left-arm beam id -> json


def left_beam(beam_id):
    """A copy of an A New Corps beam fired from the left arm (beams from the head stay as they are)."""
    ns, _, path = beam_id.partition(":")
    data = json.loads((BASE / f"assets/{ns}/palladium/energy_beams/{path}.json").read_text(encoding="utf-8"))
    parts = data if isinstance(data, list) else [data]
    if not any(p.get("body_part") == "right_arm" for p in parts):
        return beam_id
    for p in parts:
        if p.get("body_part") == "right_arm":
            p["body_part"] = "left_arm"
            if isinstance(p.get("offset"), list) and p["offset"]:
                p["offset"][0] = -p["offset"][0]
    LEFT_BEAMS[f"{NS}:fl_left/{path}"] = data
    return f"{NS}:fl_left/{path}"


def patch_ring(c, power):
    """Hides a ring's own suit and mask while the bond's merged suit is worn."""
    slots = {f"{NS}:{CORPS[c]['power']}", f"{NS}:{CORPS[c]['power']}masks"}
    for ab in power["abilities"].values():
        if ab.get("type") == "palladium:render_layer_by_accessory_slot" and ab.get("accessory_slot") in slots:
            conds = ab.setdefault("conditions", {})
            enabling = conds.get("enabling", [])
            enabling = enabling if isinstance(enabling, list) else [enabling]
            conds["enabling"] = enabling + [NOT(merged_suit())]
    return power


# --- merged suits ------------------------------------------------------------------------------------

def skin_side(x, y):
    """Which side of the wearer a pixel of a 64x64 skin-layout texture is on: "R" (their right), "L", or None."""
    if 40 <= x < 56 and 16 <= y < 48:      # right arm and sleeve
        return "R"
    if 32 <= x < 64 and 48 <= y < 64:      # left arm and sleeve
        return "L"
    if 0 <= x < 16 and 16 <= y < 48:       # right leg and trouser
        return "R"
    if 0 <= x < 32 and 48 <= y < 64:       # left leg and trouser
        return "L"

    def box(lx, ly, w, d):  # a box's faces in its own UV block: top/bottom row, then right, front, left, back
        if ly < d:
            for start in (d, d + w):  # top, bottom
                if start <= lx < start + w:
                    return "R" if lx < start + w // 2 else "L"
            return None
        if lx < d:
            return "R"
        if lx < d + w:
            return "R" if lx < d + w // 2 else "L"  # the front, seen from the front: their right is on the left
        if lx < d + w + d:
            return "L"
        if lx < d + w + d + w:
            return "L" if lx < d + w + d + w // 2 else "R"  # the back, seen from behind
        return None

    if 16 <= x < 40 and 16 <= y < 48:      # body and jacket
        return box(x - 16, (y - 16) % 16, 8, 4)
    if y < 16:                             # head and hat
        return box(x % 32, y, 8, 8)
    return None


def legs(x, y):
    return (0 <= x < 16 and 16 <= y < 48) or (0 <= x < 32 and 48 <= y < 64)


def compose(first, second, pick):
    out = Image.new("RGBA", first.size, (0, 0, 0, 0))
    for y in range(first.size[1]):
        for x in range(first.size[0]):
            out.putpixel((x, y), (first if pick(x, y) else second).getpixel((x, y)))
    return out


def default_suit(c, slim):
    """The texture of the corps' default A New Corps suit (its suit slot's default layer)."""
    ring = json.loads((BASE / f"data/{NS}/palladium/powers/{CORPS[c]['power']}.json").read_text(encoding="utf-8"))
    slot = f"{NS}:{CORPS[c]['power']}"
    layer_id = next(a["default_layer"] for a in ring["abilities"].values()
                    if a.get("type") == "palladium:render_layer_by_accessory_slot" and a.get("accessory_slot") == slot)
    ns, _, path = layer_id.partition(":")
    layer = json.loads((BASE / f"assets/{ns}/palladium/render_layers/{path}.json").read_text(encoding="utf-8"))
    first = layer["layers"][0] if layer.get("type") == "palladium:compound" else layer
    tex = first["texture"]["base"] if isinstance(first["texture"], dict) else first["texture"]
    tex = tex.replace("#SLIM", "slim" if slim else "steve")
    tns, _, tpath = tex.partition(":")
    return Image.open(BASE / f"assets/{tns}/{tpath}").convert("RGBA")


def suit_texture(a, b, design, slim):
    ta, tb = default_suit(a, slim), default_suit(b, slim)
    if design.endswith("_reversed"):
        ta, tb = tb, ta
    if design.startswith("split"):
        return compose(ta, tb, lambda x, y: skin_side(x, y) == "R")
    return compose(ta, tb, lambda x, y: not legs(x, y))  # halves: the first above the belt, the second below


def slot_icon():
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    colors = [fx(c) for c in ORDER[:7]]
    for y in range(16):
        for x in range(16):
            d = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** 0.5
            if 4.5 <= d <= 7:
                k = int((math.atan2(y - 7.5, x - 7.5) + math.pi) / (2 * math.pi) * len(colors)) % len(colors)
                img.putpixel((x, y), tuple(colors[k]) + (255,))
    return img


def assets(write, save, lang):
    """The bond's power, its merged suits and their accessory slot, and the left-hand beams."""
    write(f"data/{NS}/palladium/powers/spectrum_bond.json", power_json(lang))
    lang[f"power.{NS}.spectrum_bond"] = "Spectrum Bond"
    for beam_id, data in LEFT_BEAMS.items():
        write(f"assets/{NS}/palladium/energy_beams/{beam_id.partition(':')[2]}.json", data)
    write(f"addon/{NS}/accessory_slots/spectrum_suit.json", {
        "icon": f"{NS}:textures/gui/accessory_slots/spectrum_suit.png",
        "menu_visibility": {"type": "palladium:has_power", "power": BOND}})
    save(slot_icon(), f"assets/{NS}/textures/gui/accessory_slots/spectrum_suit.png")
    lang[f"accessory_slot.{NS}.spectrum_suit"] = "Spectrum Suit"
    model = {"normal": f"{NS}:humanoid", "slim": f"{NS}:humanoid_slim"}
    slim_var = {"SLIM": {"type": "palladium:small_arms", "true_value": "slim", "false_value": "steve"}}
    for design, name in DESIGNS:
        layers = []
        for a, b in PAIRS:
            for slim in (False, True):
                save(suit_texture(a, b, design, slim),
                     f"assets/{NS}/textures/models/spectrum/{'slim' if slim else 'steve'}/{design}_{a}_{b}.png")
            layers.append({"model_layer": model, "conditions": bond(a, b), "texture": {
                "base": f"{NS}:textures/models/spectrum/#SLIM/{design}_{a}_{b}.png", "variables": slim_var}})
        write(f"assets/{NS}/palladium/render_layers/spectrum/{design}.json", {"type": "palladium:compound", "layers": layers})
        write(f"addon/{NS}/accessories/spectrum_suit_{design}.json", {
            "type": "palladium:render_layer", "slot": SUIT_SLOT, "render_layer": f"{NS}:spectrum/{design}",
            "disable_rendering": True})
        lang[f"accessory.{NS}.spectrum_suit_{design}"] = name
    write(f"assets/{NS}/palladium/render_layers/spectrum/own.json", {"type": "palladium:compound", "layers": []})
    write(f"addon/{NS}/accessories/spectrum_suit_own.json", {
        "type": "palladium:render_layer", "slot": SUIT_SLOT, "render_layer": f"{NS}:spectrum/own"})
    lang[f"accessory.{NS}.spectrum_suit_own"] = "Own Suits"


# --- datapack ----------------------------------------------------------------------------------------

def generate():
    """Returns (load, tick, second, functions)."""
    fn, load, tick, second = {}, [], [], []
    load += ["scoreboard objectives add gl_rings dummy", "scoreboard objectives add gl_dc1 dummy",
             "scoreboard objectives add gl_dc2 dummy"]

    # which rings are bonded: gl_<corps> comes from each ring's marker (see gen_final.patch_base)
    tick += ["scoreboard players set @a gl_rings 0"]
    for c in ORDER:
        tick += [f"tag @a[tag=gl_p1_{c}] remove gl_p1_{c}", f"tag @a[tag=gl_p2_{c}] remove gl_p2_{c}"]
    for c in ORDER:
        tick += [f"scoreboard players add @a[tag=gl_{c}] gl_rings 1",
                 f"tag @a[tag=gl_{c},scores={{gl_rings=1}}] add gl_p1_{c}",
                 f"tag @a[tag=gl_{c},scores={{gl_rings=2}}] add gl_p2_{c}"]
    tick += [f"execute as @a[tag=!gl_dual,scores={{gl_rings=2..}}] at @s run function {NS}:bond/bond",
             f"execute as @a[tag=gl_dual,scores={{gl_rings=..1}}] at @s run function {NS}:bond/unbond",
             "scoreboard players add #prism gl_cfg 1",
             "execute if score #prism gl_cfg matches 4.. run scoreboard players set #prism gl_cfg 0",
             f"execute if score #prism gl_cfg matches 0 as @a[tag=gl_prism,tag=gl_dual] at @s run function {NS}:bond/prism"]
    second += [f"execute as @a[tag=gl_dual] run superpower add {BOND} @s",
               f"execute as @a[tag=!gl_dual] run superpower remove {BOND} @s",
               f"execute as @a[tag=gl_dual,tag=gl_dn_shared_light] run function {NS}:bond/shared_light",
               f"execute as @a[tag=gl_dual,tag=gl_dn_twin_lanterns] run function {NS}:bond/twin_lanterns",
               *[f"tag @a remove gl_dn_{k}" for k in TAGGED_NODES],
               "tag @a[tag=gl_prism,tag=!gl_dual] remove gl_prism"]

    hello = []
    for a, b in PAIRS:
        hello.append(f"execute if entity @s[tag=gl_p1_{a},tag=gl_p2_{b}] run function {NS}:bond/hello/{a}_{b}")
        fn[f"bond/hello/{a}_{b}"] = [
            "title @s actionbar " + json.dumps([{"text": "Spectrum Bond: ", "color": "white", "bold": True},
                                                {"text": CORPS[a]["emotion"], "color": hexcolor(fx(a))},
                                                {"text": " + ", "color": "gray"},
                                                {"text": CORPS[b]["emotion"], "color": hexcolor(fx(b))}]),
            burst(fx(a), 1.4, "0.5 1 0.5", 60), burst(fx(b), 1.4, "0.5 1 0.5", 60),
            sound("minecraft:block.beacon.power_select", 1.5)]
    fn["bond/bond"] = [
        f"superpower add {BOND} @s", "tag @s add gl_dual", *hello,
        "execute unless entity @s[tag=gl_bond_seen] run " + tellraw("@s", [
            "", {"text": "Your two rings bond. ", "color": "white", "bold": True},
            {"text": "The Spectrum Bond adds its own bar (Twin Beam, Twin Constructs, Spectrum Fusion, Prismatic Shield, "
                     "Spectrum Overload) and its own skill tree in the powers menu; each ring keeps its own. Pick a "
                     "merged suit in the accessories menu (Spectrum Suit).", "color": "gray"}]),
        "tag @s add gl_bond_seen"]
    fn["bond/unbond"] = [
        f"superpower remove {BOND} @s", "tag @s remove gl_dual", "tag @s remove gl_prism",
        f"clear @s #{NS}:host_constructs{{fl_bond:1b}}",
        "title @s actionbar " + json.dumps({"text": "The Spectrum Bond fades.", "color": "gray"})]

    # reading both rings' charge into #c1 / #c2
    read = ["scoreboard players set #c1 gl_tmp 0", "scoreboard players set #c2 gl_tmp 0"]
    for c in ORDER:
        for n in (1, 2):
            read.append(f"execute if entity @s[tag=gl_p{n}_{c}] store result score #c{n} gl_tmp run "
                        f"energybar value get @s {power(c)} {CORPS[c]['bar']}")
    fn["bond/read"] = read

    def to_ring(n, verb, amount):
        return [f"execute if entity @s[tag=gl_p{n}_{c}] run energybar value {verb} @s {power(c)} {CORPS[c]['bar']} "
                f"{amount}" for c in ORDER]

    small = max(1, SHARED_FLOW // 4)
    fn["bond/shared_light"] = [
        f"function {NS}:bond/read",
        "scoreboard players operation #d gl_tmp = #c1 gl_tmp", "scoreboard players operation #d gl_tmp -= #c2 gl_tmp",
        f"execute if score #d gl_tmp matches {SHARED_FLOW * 2}.. run function {NS}:bond/flow_12",
        f"execute if score #d gl_tmp matches {small * 2}..{SHARED_FLOW * 2 - 1} run function {NS}:bond/flow_12_small",
        f"execute if score #d gl_tmp matches ..-{SHARED_FLOW * 2} run function {NS}:bond/flow_21",
        f"execute if score #d gl_tmp matches -{SHARED_FLOW * 2 - 1}..-{small * 2} run function {NS}:bond/flow_21_small"]
    for name, giver, taker, amount in (("flow_12", 1, 2, SHARED_FLOW), ("flow_12_small", 1, 2, small),
                                       ("flow_21", 2, 1, SHARED_FLOW), ("flow_21_small", 2, 1, small)):
        fn[f"bond/{name}"] = to_ring(giver, "subtract", amount) + to_ring(taker, "add", amount)
    fn["bond/twin_lanterns"] = [  # a ring that jumped by 1 000 or more this second was just recharged: fill the other
        f"function {NS}:bond/read",
        "execute unless score @s gl_dc1 matches 0.. run scoreboard players operation @s gl_dc1 = #c1 gl_tmp",
        "execute unless score @s gl_dc2 matches 0.. run scoreboard players operation @s gl_dc2 = #c2 gl_tmp",
        "scoreboard players operation #j1 gl_tmp = #c1 gl_tmp", "scoreboard players operation #j1 gl_tmp -= @s gl_dc1",
        "scoreboard players operation #j2 gl_tmp = #c2 gl_tmp", "scoreboard players operation #j2 gl_tmp -= @s gl_dc2",
        *[f"execute if score #j1 gl_tmp matches 1000.. run {line}" for line in to_ring(2, "add", 100000)],
        *[f"execute if score #j2 gl_tmp matches 1000.. run {line}" for line in to_ring(1, "add", 100000)],
        f"function {NS}:bond/read",
        "scoreboard players operation @s gl_dc1 = #c1 gl_tmp", "scoreboard players operation @s gl_dc2 = #c2 gl_tmp"]
    fn["bond/prism"] = [line for c in ORDER for line in (
        f"execute if entity @s[tag=gl_p1_{c}] run {burst(fx(c), 1.0, '0.5 0.9 0.5', 6)}",
        f"execute if entity @s[tag=gl_p2_{c}] run {burst(fx(c), 1.0, '0.5 0.9 0.5', 6)}")]

    for a, b in PAIRS:
        name = FUSION_NAMES[(a, b)]
        words = name.split(" ")
        fn[f"bond/fusion/{a}_{b}"] = [
            "title @s times 5 40 10",
            "title @s subtitle " + json.dumps({"text": f"{CORPS[a]['emotion']} + {CORPS[b]['emotion']}", "color": "gray"}),
            "title @s title " + json.dumps([{"text": words[0] + " ", "color": hexcolor(fx(a))},
                                            {"text": " ".join(words[1:]), "color": hexcolor(fx(b))}]),
            burst(fx(a), 2.5, "4 1.5 4", 220), burst(fx(b), 2.5, "4 1.5 4", 220),
            "particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force",
            f"execute as {FOES} run damage @s 8 minecraft:player_attack by @p[tag=gl_user]",
            *SIGNATURE[a], *SIGNATURE[b],
            sound("minecraft:block.beacon.power_select", 0.8), sound("minecraft:entity.illusioner.cast_spell", 1.2)]
        around = TARGETS.format(r=OVERLOAD_RADIUS) + "]"
        fn[f"bond/overload/{a}_{b}"] = [
            burst(fx(a), 3.0, "6 2 6", 400), burst(fx(b), 3.0, "6 2 6", 400),
            "particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force",
            f"execute as {around} run damage @s 24 minecraft:player_attack by @p[tag=gl_user]",
            f"effect give {around} minecraft:levitation 2 4 true",
            *[f"effect give @s minecraft:{x} 15 1 true" for x in ("strength", "resistance", "speed")],
            "title @s times 5 40 10",
            "title @s title " + json.dumps([{"text": "Spectrum ", "color": hexcolor(fx(a))},
                                            {"text": "Overload", "color": hexcolor(fx(b))}]),
            sound("minecraft:entity.generic.explode", 0.6), sound("minecraft:block.beacon.activate", 0.6)]
    return load, tick, second, fn
