"""Generates every Lantern Corps in the pack from the CORPS table below.

    python3 tools/gen_corps.py   # writes the generated files into src/
    python3 tools/build.py       # validates and packages the jar

Each corps gets: a ring (worn on the hand), a placeable Power Battery
lantern, a power with a skill tree (shared upgrades + its own specials),
a full-body uniform, a beam, a flight trail, recipes and translations.

To tweak a corps, edit its entry in CORPS or its specials function and
re-run this script. Art lives in art.py.
"""
import hashlib
import json
import shutil
from pathlib import Path

import art
import constructs
import systems

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
NS = "greenlantern"
BAR = "ring_charge"
BASE_CHARGE = 1000

# --- corps table ------------------------------------------------------------------

# map color of each corps' blocks (Palladium BlockMaterialRegistry ids)
MAP_COLOR = {"green": "minecraft:color_green", "yellow": "minecraft:color_yellow", "red": "minecraft:color_red",
             "orange": "minecraft:color_orange", "blue": "minecraft:color_blue", "violet": "minecraft:color_magenta",
             "indigo": "minecraft:color_purple", "white": "minecraft:snow", "black": "minecraft:color_black"}

CORPS = {
    "green": {
        "name": "Green Lantern", "emotion": "Willpower", "color": (46, 200, 70),
        "empowered_by": "blue", "empowered_name": "Hope Amplified",
        "empowered_desc": "Within 12 blocks of a Blue Lantern your ring recharges fast and you hit harder.",
        "gem": "minecraft:emerald_block", "glass": "minecraft:lime_stained_glass",
        "oath": ["In brightest day, in blackest night,", "No evil shall escape my sight.",
                 "Let those who worship evil's might,", "Beware my power... Green Lantern's light!"],
    },
    "yellow": {
        "name": "Sinestro Corps", "emotion": "Fear", "color": (245, 205, 30),
        "gem": "minecraft:gold_block", "glass": "minecraft:yellow_stained_glass",
        "oath": ["In blackest day, in brightest night,", "Beware your fears made into light.",
                 "Let those who try to stop what's right,", "Burn like my power... Sinestro's might!"],
    },
    "red": {
        "name": "Red Lantern", "emotion": "Rage", "color": (220, 30, 35),
        "health_penalty": 20, "bonus_damage": 4,  # rage: fewer hearts, more strength
        "shapes": {"fist": "claw"},
        "gem": "minecraft:redstone_block", "glass": "minecraft:red_stained_glass",
        "oath": ["With blood and rage of crimson red,", "Ripped from a corpse so freshly dead,",
                 "Together with our hellish hate,", "We'll burn you all... that is your fate!"],
    },
    "orange": {
        "name": "Orange Lantern", "emotion": "Avarice", "color": (250, 130, 20),
        "gem": "minecraft:raw_gold_block", "glass": "minecraft:orange_stained_glass",
        "oath": ["What's mine is mine,", "and mine,", "and mine...", "and mine! And not yours!"],
    },
    "blue": {
        "name": "Blue Lantern", "emotion": "Hope", "color": (40, 130, 255),
        "empowered_by": "green", "empowered_name": "Willpower Ignited",
        "empowered_desc": "Within 12 blocks of a Green Lantern your ring recharges fast and you hit harder.",
        "gem": "minecraft:diamond_block", "glass": "minecraft:light_blue_stained_glass",
        "oath": ["In fearful day, in raging night,", "With strong hearts full, our souls ignite,",
                 "When all seems lost in the War of Light,", "Look to the stars... for hope burns bright!"],
    },
    "violet": {
        "name": "Star Sapphire", "emotion": "Love", "color": (215, 55, 220),
        "shapes": {"cage": "crystal"},
        "gem": "minecraft:amethyst_block", "glass": "minecraft:magenta_stained_glass",
        "oath": ["For hearts long lost and full of fright,", "For those alone in blackest night,",
                 "Accept our ring and join our fight,", "Love conquers all... with violet light!"],
    },
    "indigo": {
        "name": "Indigo Tribe", "emotion": "Compassion", "color": (105, 60, 230),
        "gem": "minecraft:lapis_block", "glass": "minecraft:blue_stained_glass",
        "oath": ["Tor lowar lan, Abin Sur,", "Ak wo tauva, Ihla wo nauva,",
                 "Natromo faan, Dur ak naja,", "Ono ot vauva, Abin Sur."],
    },
    "white": {
        "name": "White Lantern", "emotion": "Life", "color": (235, 242, 250),
        "gem": None,  # crafted from the seven spectrum rings, see main()
        "glass": "minecraft:white_stained_glass",
        "oath": ["From the light of creation,", "every color of the spectrum,", "all life, as one,",
                 "...shines White!"],
    },
    "black": {
        "name": "Black Lantern", "emotion": "Death", "color": (95, 98, 110),
        "feeds_on_death": 200, "regen": False,  # recharged by killing, not over time
        "gem": "minecraft:wither_skeleton_skull", "glass": "minecraft:black_stained_glass",
        "oath": ["The Blackest Night falls from the skies,", "The darkness grows as all light dies,",
                 "We crave your hearts and your demise,", "By my black hand, the dead shall rise!"],
    },
}
SPECTRUM = ["green", "yellow", "red", "orange", "blue", "violet", "indigo"]

# --- small helpers ----------------------------------------------------------------

OTHERS = "@e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..{r}]"
NEAREST = OTHERS[:-1] + ",limit=1,sort=nearest]"
ALLIES = "@a[distance=..{r}]"
UNIFORM = {"type": "palladium:ability_enabled", "ability": "uniform"}

# 3D hard-light shapes and the construct catalog live in constructs.py.
SHAPES = constructs.SHAPES


def construct_cmds(corps, shape, where):
    """Commands that spawn a display construct. `where` is an `execute ...` prefix that sets the position."""
    return constructs.construct_cmds(list(CORPS), corps, shape, where)


def hexcolor(rgb):
    return "#%02X%02X%02X" % tuple(rgb[:3])


def dust(rgb, size=1.0):
    return "%.2f %.2f %.2f %.1f" % (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, size)


def charge(amount):
    return {"type": "palladium:energy_bar", "energy_bar": BAR, "min": max(1, amount)}


def usage(amount):
    return {"energy_bar": BAR, "amount": amount}


def enabled(ability):
    return {"type": "palladium:ability_enabled", "ability": ability}


def unlocked(ability):
    return {"type": "palladium:ability_unlocked", "ability": ability}


def interval(every):
    return {"type": "palladium:interval", "active_ticks": 1, "disabled_ticks": every - 1}


def command(first=(), every=(), last=()):
    # All three lists are always written: Palladium's default for "commands"
    # is `say Hello World` every tick.
    return {"type": "palladium:command", "first_tick_commands": list(first),
            "commands": list(every), "last_tick_commands": list(last)}


def action(cooldown):
    return {"type": "palladium:action", "cooldown": cooldown}


def toggle():
    return {"type": "palladium:toggle"}


def held():
    return {"type": "palladium:held"}


def burst(rgb, size=2.0, spread="1 1 1", count=80, at="~ ~1 ~"):
    return f"particle minecraft:dust {dust(rgb, size)} {at} {spread} 0 {count} force"


def sound(snd, pitch=1.0):
    return f"playsound {snd} player @a[distance=..24] ~ ~ ~ 1 {pitch}"


def one(conds):
    return conds[0] if len(conds) == 1 else conds


class Kit:
    """Builds one corps' power: bar abilities, skill-tree nodes and hidden helpers."""

    SPECIAL_COLUMN = 9.5

    def __init__(self, corps, data):
        self.c = corps
        self.data = data
        self.rgb = data["color"]
        self.abilities = {}
        self.lang = {}
        self.specials = []
        self.attr_count = 0
        self.shapes = {**{s: s for s in SHAPES}, **data.get("shapes", {})}

    def tr(self, key, english, shared):
        lang_key = f"ability.{NS}.{key}" if shared else f"ability.{NS}.{self.c}.{key}"
        self.lang[lang_key] = english
        return {"translate": lang_key}

    def hidden(self, key, ability):
        self.abilities[key] = {**ability, "hidden": True, "hidden_in_bar": True}

    def node(self, key, name, desc, icon, pos, parents, xp, shared=True):
        """A skill-tree node bought with XP levels in the powers menu."""
        self.abilities[key] = {
            "type": "palladium:dummy",
            "title": self.tr(key, name, shared),
            "description": self.tr(key + ".description", desc + f" Costs {xp} XP levels.", shared),
            "icon": icon,
            "hidden_in_bar": True,
            "gui_position": list(pos),
            "conditions": {"unlocking": [*(unlocked(p) for p in parents),
                                         {"type": "palladium:experience_level_buyable", "xp_level": xp}]},
        }

    def bar(self, key, ability, name, icon, index, node=None, cost=0, suit=False, extra=(), shared=True):
        """An ability on the ability bar (hidden from the skill tree, which shows its node instead)."""
        conds = ability.get("conditions", {})
        unlocking = ([UNIFORM] if suit else []) + ([unlocked(node)] if node else []) + list(extra)
        if cost:
            unlocking.append(charge(cost))
            ability = {**ability, "energy_bar_usage": usage(cost)} if "energy_bar_usage" not in ability else ability
        if unlocking:
            conds = {"unlocking": one(unlocking), **conds}
        self.abilities[key] = {
            **ability, "conditions": conds, "title": self.tr(key, name, shared), "icon": icon,
            "bar_color": "white", "hidden": True, "hidden_in_bar": False, "list_index": index,
        }

    def attribute(self, key, attr, amount, unlocking, shared=False):
        """Shared modifiers use the same UUID in every corps, so wearing two rings never
        stacks them (Minecraft only applies one modifier per UUID)."""
        if shared:
            uuid = "6c7affff-1a2b-4c3d-8e4f-" + hashlib.md5(key.encode()).hexdigest()[:12]
        else:
            self.attr_count += 1
            n = list(CORPS).index(self.c)
            uuid = f"6c7a{n:04x}-1a2b-4c3d-8e4f-{self.attr_count:012x}"
        self.hidden(key, {
            "type": "palladium:attribute_modifier", "attribute": attr, "amount": amount, "operation": 0,
            "uuid": uuid, "conditions": {"unlocking": one(unlocking)},
        })

    def special(self, key, name, desc, icon, ability, cost=0, xp=8, index=None, extra=()):
        """A corps-specific ability: a tree node plus (if index is set) a bar ability."""
        n = len(self.specials)
        parents = ["skill_force_field"] if n == 0 else [self.specials[-1]]
        self.node(f"skill_{key}", name, desc, icon, (self.SPECIAL_COLUMN, 2 + n), parents, xp, shared=False)
        self.specials.append(f"skill_{key}")
        if index is None:  # passive: the effect is unlocked by the node alone
            ability["conditions"] = {"unlocking": one([unlocked(f"skill_{key}"), *extra])}
            self.hidden(key, ability)
        else:
            self.bar(key, ability, name, icon, index + 5, node=f"skill_{key}", cost=cost, extra=extra, shared=False)

    def pulse(self, key, source, every, commands):
        """Runs commands every N ticks while `source` is enabled."""
        self.hidden(key, {**command(first=commands), "conditions": {"enabling": [enabled(source), interval(every)]}})

    def ultimate(self, key, name, desc, icon, commands, cost=600, cooldown=1200):
        self.node(f"skill_{key}", name, "Ultimate: " + desc, icon, (self.SPECIAL_COLUMN, 2 + len(self.specials)),
                  [self.specials[-1]], 30, shared=False)
        self.bar(key, {**command(first=commands), "conditions": {"enabling": action(cooldown)}},
                 name, icon, 14, node=f"skill_{key}", cost=cost, shared=False)


# --- the kit every corps shares -----------------------------------------------------

def shared_kit(k):
    c, rgb, data = k.c, k.rgb, k.data
    # rings of corps listed before this one: with one of those also worn, this ring is on the left hand
    earlier = [{"type": "palladium:has_power", "power": f"{NS}:{o}_lantern"} for o in list(CORPS)[:list(CORPS).index(c)]]
    obj = f"glmax_{c}"

    # Suit Up: the root of the skill tree and the bottom slot of the first bar page.
    k.abilities["uniform"] = {
        "type": "palladium:dummy", "bar_color": "white", "list_index": 4,
        "title": k.tr("uniform", "Suit Up", True),
        "description": k.tr("uniform.description",
                            "Toggle your corps' suit on or off. Pick the suit and mask in the accessories menu.", True),
        "icon": f"{NS}:{c}_lantern_ring", "gui_position": [0, 0],
        # with two rings worn, only one suit at a time: stay off while another ring's suit is up
        "conditions": {"enabling": [toggle(), {"type": "palladium:not", "conditions": [
            {"type": "palladium:ability_enabled", "power": f"{NS}:{o}_lantern", "ability": "uniform"}
            for o in CORPS if o != c]}]},
    }
    k.hidden("suit_up_burst", {**command(first=[
        burst(rgb, 2.0, "0.4 1.0 0.4", 120), "particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force",
        sound("minecraft:block.beacon.activate", 1.4)]), "conditions": {"enabling": UNIFORM}})
    # The suit design comes from the corps' slot in the accessories menu. The player's own
    # jacket/sleeve/trouser layers are hidden under it; the head (face, hair, hat) stays visible.
    designs = art.DESIGNS[c]
    k.hidden("uniform_suit", {
        "type": "palladium:render_layer_by_accessory_slot", "accessory_slot": f"{NS}:{c}_suit",
        "default_layer": f"{NS}:{c}_suit_{designs[0][0]}", "conditions": {"enabling": UNIFORM},
    })
    k.hidden("uniform_mask", {
        "type": "palladium:render_layer_by_accessory_slot", "accessory_slot": f"{NS}:{c}_mask",
        "default_layer": f"{NS}:{c}_mask_{art.DEFAULT_MASK[c]}", "conditions": {"enabling": UNIFORM},
    })
    k.hidden("uniform_hide_layers", {
        "type": "palladium:hide_body_part", "affects_first_person": True,
        "body_parts": ["chest_overlay", "right_arm_overlay", "left_arm_overlay", "right_leg_overlay", "left_leg_overlay"],
        "conditions": {"enabling": UNIFORM},
    })
    # The ring is always visible on your hand while you wear it: the first ring (in CORPS order) on
    # the right hand, a second ring on the left.
    for part in ("band", "gem"):
        right = {"type": "palladium:render_layer", "render_layer": f"{NS}:{c}_ring_{part}"}
        if earlier:
            right["conditions"] = {"enabling": {"type": "palladium:not", "conditions": earlier}}
            k.hidden(f"ring_{part}_left", {"type": "palladium:render_layer", "render_layer": f"{NS}:{c}_ring_{part}_left",
                                           "conditions": {"enabling": {"type": "palladium:or", "conditions": earlier}}})
        k.hidden(f"ring_{part}", right)
    for side, cond in (("", {"type": "palladium:not", "conditions": earlier} if earlier else None),
                       ("_left", {"type": "palladium:or", "conditions": earlier} if earlier else False)):
        if cond is False:
            continue  # the first corps' ring is always on the right hand
        k.hidden(f"ring_aura{side}", {
            "type": "palladium:particles", "emitter": [f"{NS}:ring_hand{side}"], "particle_type": "minecraft:dust",
            "options": dust(rgb, 0.8), "conditions": {"enabling": [interval(4), *([cond] if cond else [])]},
        })

    # A charged ring alone makes you far tougher: 40 hearts and netherite-level armor.
    # Hearts, armor, protection and the shared skill bonuses live in the hidden lantern_base power
    # (see base_power), which every ring grants, so two rings never stack them. Only corps-specific
    # modifiers stay here, with UUIDs unique to this corps.
    charged = [charge(1)]
    if data.get("health_penalty"):
        k.attribute("ring_health_penalty", "minecraft:generic.max_health", -data["health_penalty"], charged)
    if data.get("bonus_damage"):
        k.attribute("ring_rage_fists", "palladium:punch_damage", data["bonus_damage"], charged)
        k.attribute("ring_strength", "minecraft:generic.attack_damage", data["bonus_damage"], charged)

    # Palladium resets a ring's charge to 0 whenever the ring is re-equipped or the player relogs, so
    # the charge is mirrored to a scoreboard every second and put back when the ring comes back.
    k.hidden("charge_restore", {**command(first=[f"function {NS}:charge/restore_{c}"],
                                          last=[f"tag @s remove gl_cr_{c}"])})

    # --- skill tree ---
    k.node("skill_health_1", "Vitality I", "+10 hearts while your ring is charged.",
           "minecraft:golden_apple", (-5, 1), ["uniform"], 5)
    k.node("skill_health_2", "Vitality II", "Another +10 hearts while your ring is charged.",
           "minecraft:enchanted_golden_apple", (-5, 2), ["skill_health_1"], 15)

    k.node("skill_combat_1", "Combat I", "+4 attack and punch damage while your ring is charged.",
           "minecraft:iron_sword", (-3, 1), ["uniform"], 5)
    k.node("skill_combat_2", "Combat II", "Another +4 attack and punch damage.",
           "minecraft:netherite_sword", (-3, 2), ["skill_combat_1"], 15)

    k.node("skill_charge_1", "Capacity I", "Your ring holds 1500 charge instead of 1000.",
           "minecraft:glowstone", (-1, 1), ["uniform"], 5)
    k.node("skill_charge_2", "Capacity II", "Your ring holds 2000 charge.",
           "minecraft:beacon", (-1, 2), ["skill_charge_1"], 15)
    # The bar's max reads a per-corps scoreboard score (falls back to 1000).
    setup = f"scoreboard objectives add {obj} dummy"
    k.hidden("charge_1_apply", {**command(first=[setup, f"scoreboard players set @s {obj} 1500"]),
                                "conditions": {"unlocking": [unlocked("skill_charge_1"),
                                                             {"type": "palladium:not", "conditions": [unlocked("skill_charge_2")]}]}})
    k.hidden("charge_2_apply", {**command(first=[setup, f"scoreboard players set @s {obj} 2000"]),
                                "conditions": {"unlocking": unlocked("skill_charge_2")}})

    k.node("skill_flight", "Flight", "Fly on the power of your ring, leaving a trail of light. Flying slowly drains charge.",
           "minecraft:feather", (1, 1), ["uniform"], 5)
    flying = [unlocked("skill_flight"), {"type": "palladium:is_flying"}]
    k.hidden("flight_trail", {"type": "palladium:trail", "trail": f"{NS}:{c}_trail", "conditions": {"enabling": flying}})
    k.hidden("flight_aura", {"type": "palladium:particles", "emitter": [f"{NS}:flight_aura"],
                             "particle_type": "minecraft:dust", "options": dust(rgb, 1.2),
                             "conditions": {"enabling": flying}})
    k.hidden("flight_drain", {"type": "palladium:dummy", "energy_bar_usage": usage(1),
                              "conditions": {"enabling": [*flying, interval(5)]}})

    # --- bar page 1: beam, constructs, force field, ring light, suit up ---
    k.bar("beam", {
        "type": "palladium:energy_beam", "energy_beam": f"{NS}:{c}_beam", "damage": 2.0, "max_distance": 40.0,
        "speed": 0.6, "energy_bar_usage": usage(3), "conditions": {"enabling": held()},
    }, f"{data['emotion']} Beam", "minecraft:blaze_rod", 0, cost=3, shared=False)
    # Point the ring hand at the target while beaming. The beam's origin follows the arm's pose
    # (BodyPart offset is applied after the arm's rotation), so it visibly leaves the hand.
    k.hidden("beam_aim", {"type": "palladium:aim", "arm": "right_arm", "time": 4,
                          "conditions": {"enabling": enabled("beam")}})
    k.hidden("beam_sound", {"type": "palladium:play_sound", "sound": "minecraft:block.beacon.ambient", "pitch": 1.6,
                            "looping": True, "conditions": {"enabling": enabled("beam")}})

    construct_abilities(k)
    benefit_abilities(k)

    k.node("skill_force_field", "Force Field", "Unlocks a bubble that blocks projectiles, explosions and fire.",
           "minecraft:shield", (Kit.SPECIAL_COLUMN, 1), ["uniform"], 5)
    k.bar("force_field", {
        "type": "palladium:damage_immunity",
        "damage_sources": ["minecraft:is_projectile", "minecraft:is_explosion", "minecraft:is_fire"],
        "energy_bar_usage": usage(2), "conditions": {"enabling": toggle()},
    }, "Force Field", "minecraft:shield", 2, node="skill_force_field", cost=2)
    k.hidden("force_field_glow", {"type": "palladium:entity_glow", "mode": "self", "color": hexcolor(rgb),
                                  "conditions": {"enabling": enabled("force_field")}})

    # Recharging: right-click while holding your battery, or right-click a placed one.
    # These only unlock while that's possible, so they never steal ordinary right-clicks.
    battery = f"{NS}:{c}_power_battery"
    right_click = {"type": "palladium:action", "key_type": "right_click", "cooldown": 20}
    # gl_look_<corps> is set by the datapack while you look at a placed battery of this corps
    looking_at = {"type": "palladium:has_tag", "tag": f"gl_look_{c}"}
    k.hidden("recharge", {
        "type": "palladium:dummy", "energy_bar_usage": usage(-1_000_000),
        "conditions": {"unlocking": {"type": "palladium:item_in_slot", "item": {"item": battery}, "slot": "mainhand"},
                       "enabling": right_click},
    })
    k.hidden("recharge_at_lantern", {
        "type": "palladium:dummy", "energy_bar_usage": usage(-1_000_000),
        "conditions": {"unlocking": [
            {"type": "palladium:not", "conditions": [{"type": "palladium:item_in_slot", "item": {"item": battery},
                                                      "slot": "mainhand"}]},
            looking_at],
            "enabling": right_click},
    })
    oath = []
    for i, line in enumerate(data["oath"], 1):
        k.lang[f"oath.{NS}.{c}.{i}"] = line
        prefix = [{"selector": "@s", "color": hexcolor(rgb)}, {"text": ": ", "color": "gray"}] if i == 1 else [{"text": "   "}]
        oath.append("tellraw @a[distance=..24] " + json.dumps(
            prefix + [{"translate": f"oath.{NS}.{c}.{i}", "color": hexcolor(rgb), "italic": True}], separators=(",", ":")))
    k.hidden("oath", {**command(first=oath + [
        burst(rgb, 1.5, "0.6 1 0.6", 80), sound("minecraft:block.beacon.power_select", 1.2)]),
        "conditions": {"enabling": {"type": "palladium:or", "conditions": [
            enabled("recharge"), enabled("recharge_at_lantern")]}}})

    # Corps leaders (appointed by an admin) can revoke the ring of the nearest member.
    k.bar("revoke_ring", {**command(first=[f"function {NS}:leader/revoke_{c}"]),
                          "conditions": {"enabling": action(40)}},
          "Revoke Ring", "minecraft:barrier", 17, extra=[{"type": "palladium:has_tag", "tag": f"gl_leader_{c}"}])
    k.lang[f"ability.{NS}.revoke_ring.description"] = "Leaders only: take the ring from the nearest member of your corps."
    k.bar("ring_light", {**command(first=["effect give @s minecraft:night_vision 30 0 true"],
                                   last=["effect clear @s minecraft:night_vision"]),
                         "conditions": {"enabling": toggle()}}, "Ring Light", "minecraft:glowstone_dust", 3)
    k.pulse("ring_light_pulse", "ring_light", 200, ["effect give @s minecraft:night_vision 30 0 true"])

    # Corps tags let rings react to each other (e.g. Blue Lanterns empower Green ones).
    k.hidden("corps_tag", {**command(first=[f"tag @s add gl_{c}"],
                                     every=[f"tag @s add gl_{c}", f"scoreboard players set @s gl_t_{c} 5"],
                                     last=[f"tag @s remove gl_{c}"])})
    if data.get("feeds_on_death"):
        kills = {"type": "palladium:objective_score", "objective": "gl_bkills", "min_score": 1,
                 "max_score": 2147483647}
        k.hidden("death_feed", {
            **command(first=["scoreboard players set @s gl_bkills 0",
                             "particle minecraft:soul ~ ~1 ~ 0.4 0.6 0.4 0.03 25 force",
                             sound("minecraft:particle.soul_escape", 0.8)]),
            "energy_bar_usage": usage(-data["feeds_on_death"]),
            "conditions": {"unlocking": kills},
        })
    ally = data.get("empowered_by")
    if ally:
        near = {"type": "palladium:has_tag", "tag": f"gl_near_{ally}"}  # set by the datapack
        k.node("skill_empowered", data["empowered_name"], data["empowered_desc"], f"{NS}:{ally}_lantern_ring",
               (1, 2), ["skill_flight"], 8)
        k.hidden("empowered_charge", {"type": "palladium:dummy", "energy_bar_usage": usage(-2),
                                      "conditions": {"unlocking": [unlocked("skill_empowered"), near]}})
        k.attribute("empowered_damage", "minecraft:generic.attack_damage", 4, [unlocked("skill_empowered"), near])
        k.attribute("empowered_armor", "minecraft:generic.armor_toughness", 4, [unlocked("skill_empowered"), near])


# --- constructs (catalog and datapack in constructs.py) ------------------------------

NODE_ICONS = {"constructs": "minecraft:emerald", "melee_1": f"{NS}:construct_sword", "melee_2": f"{NS}:construct_fist",
              "ranged_1": f"{NS}:construct_gatling", "ranged_2": f"{NS}:construct_ball",
              "defense_1": f"{NS}:construct_wall", "defense_2": "minecraft:glass",
              "utility_1": "minecraft:turtle_helmet", "utility_2": "minecraft:scaffolding"}


def construct_abilities(k):
    """The construct branch of the skill tree, the five construct slots (bar page 2), the construct
    wheel, Configure Constructs and the helpers held constructs need."""
    c = k.c
    sig = constructs.SIGNATURES[c]
    for node, (name, desc, pos, parents, xp) in constructs.NODES.items():
        icon = NODE_ICONS.get(node, sig.icon)
        if node == "signature":
            name, desc = f"Signature Construct: {sig.name}", sig.desc + " Needs all four construct branches."
        k.node(f"skill_{node}", name, desc, icon, pos, [p if p == "uniform" else f"skill_{p}" for p in parents], xp,
               shared=node != "signature")
        # the datapack checks these tags before running a construct
        k.hidden(f"unlocked_{node}", {**command(first=[f"tag @s add gl_u_{c}_{node}"],
                                                last=[f"tag @s remove gl_u_{c}_{node}"]),
                                      "conditions": {"unlocking": unlocked(f"skill_{node}")}})
    catalog = constructs.all_constructs(c)
    for con in catalog:
        shared = con.key != "signature"
        k.bar(f"cx_{con.key}", {**command(first=[f"function {NS}:construct/{c}/{con.key}"]),
                                "conditions": {"enabling": {"type": "palladium:ability_wheel", "cooldown": 5}}},
              con.name, con.icon, None, node=f"skill_{con.node}", shared=shared)
        k.abilities[f"cx_{con.key}"]["hidden_in_bar"] = True
        del k.abilities[f"cx_{con.key}"]["list_index"]
        k.abilities[f"cx_{con.key}"]["description"] = k.tr(
            f"cx_{con.key}.description", f"{con.desc} Costs {con.cost} charge.", shared)
    k.bar("constructs", {"type": "palladium:ability_wheel", "abilities": [f"cx_{con.key}" for con in catalog],
                         "conditions": {"enabling": held()}},
          "Construct Wheel", "minecraft:emerald", 1, node="skill_constructs")
    for n in range(1, 6):
        k.bar(f"construct_{n}", {**command(first=[f"function {NS}:construct/press/{c}_{n}"]),
                                 "conditions": {"enabling": action(5)}},
              f"Construct {n}", f"{NS}:textures/gui/construct_slot/{c}_{n}.png", 4 + n, node="skill_constructs")
        k.lang[f"ability.{NS}.construct_{n}.description"] = (
            f"Forms the construct in slot {n}. Choose it with Configure Constructs.")
    k.bar("configure_constructs", {**command(first=[f"function {NS}:construct/menu"]),
                                   "conditions": {"enabling": action(10)}},
          "Configure Constructs", "minecraft:writable_book", 15, node="skill_constructs")

    # Upkeep and dissolving run in the datapack (constructs.py), per ring, after the charge is restored.
    # The gatling fires while right-click is held (the datapack paces the shots and picks the ring).
    k.hidden("gatling_fire", {**command(every=[f"function {NS}:construct/gatling_tick"]),
                              "conditions": {"unlocking": {"type": "palladium:item_in_slot",
                                                           "item": {"item": f"{NS}:construct_gatling"},
                                                           "slot": "mainhand"},
                                             "enabling": {"type": "palladium:held", "key_type": "right_click"}}})
    # Scuba Gear: a diving helmet and air tank while the tag is set
    scuba = {"type": "palladium:has_tag", "tag": f"gl_scuba_{c}"}
    k.hidden("scuba_layer", {"type": "palladium:render_layer", "render_layer": f"{NS}:{c}_scuba",
                             "conditions": {"enabling": scuba}})
    # short effects, refreshed: nothing lingers if you log out wearing it
    effects = ["minecraft:water_breathing", "minecraft:conduit_power", "minecraft:dolphins_grace"]
    k.hidden("scuba_effects", {**command(first=[f"effect give @s {e} 15 0 true" for e in effects]),
                               "conditions": {"enabling": [scuba, interval(100)]}})
    if c == "indigo":  # the staff reaches further, and soothes everyone around its bearer
        k.attribute("staff_reach", "forge:entity_reach", 2, [{"type": "palladium:item_in_slot",
                                                             "item": {"item": f"{NS}:construct_staff"},
                                                             "slot": "mainhand"}])
        k.hidden("staff_aura", {**command(first=["effect give @a[distance=..6] minecraft:regeneration 3 0 true",
                                                 burst(k.rgb, 1.0, "2 0.5 2", 20)]),
                                "conditions": {"unlocking": {"type": "palladium:item_in_slot",
                                                             "item": {"item": f"{NS}:construct_staff"},
                                                             "slot": "mainhand"},
                                               "enabling": interval(40)}})


# --- ring benefits ------------------------------------------------------------------
# Passive gifts from canon: every ring keeps you alive anywhere and translates every language;
# each corps adds a gift of its own emotion. They work with or without the suit.

BENEFITS = {
    "green": ("Fearless Will", "Willpower overcomes fear: you can't be blinded, darkened or made dizzy."),
    "yellow": ("Terror Aura", "Hostile mobs within 8 blocks of you are weakened by fear."),
    "red": ("Burning Blood", "Your blood is napalm: fire and lava can't burn you, and poison can't touch you."),
    "orange": ("Avarice", "Experience orbs within 8 blocks fly to you, and your luck is higher (better loot)."),
    "blue": ("Hope Springs Eternal", "Below 10 hearts you keep regenerating."),
    "violet": ("Love's Bond", "You, the players and the pets around you (8 blocks) slowly regenerate."),
    "indigo": ("Empathic Link", "Whatever hurts you feels it too: hostile mobs within 5 blocks are weakened."),
    "white": ("Font of Life", "You regenerate constantly and never go hungry."),
    "black": ("Undead Body", "The dead don't hunger, wither or sicken: no hunger, wither or poison."),
}
RING_BENEFITS = ("Ring Benefits", "While charged: 40 hearts and netherite-level armor; no drowning, falling or "
                 "freezing damage; and the ring translates every language, so villagers trade with you as a Hero of "
                 "the Village.")


def benefit_abilities(k):
    c = k.c
    name, desc = BENEFITS[c]
    # info nodes beside Suit Up (always unlocked)
    for key, (title, text), pos, shared in (("ring_benefits", RING_BENEFITS, (-3, 0), True),
                                            ("corps_gift", (f"{k.data['emotion']}: {name}", desc), (3, 0), False)):
        k.abilities[key] = {"type": "palladium:dummy", "title": k.tr(key, title, shared),
                            "description": k.tr(key + ".description", text, shared),
                            "icon": f"{NS}:{c}_lantern_ring" if key == "corps_gift" else "minecraft:nether_star",
                            "hidden_in_bar": True, "gui_position": list(pos)}
    pulse = lambda key, every, cmds, *conds: k.hidden(key, {  # noqa: E731
        **command(first=cmds), "conditions": {"enabling": [*conds, interval(every)]}})
    if c == "red":
        pulse("burning_blood", 100, ["effect give @s minecraft:fire_resistance 15 0 true"])
    if c == "orange":
        k.attribute("avarice_luck", "minecraft:generic.luck", 3, [charge(1)])
        pulse("avarice_xp", 10, ["tp @e[type=minecraft:experience_orb,distance=..8] @s"])
    if c == "blue":
        pulse("hope_regen", 40, ["effect give @s minecraft:regeneration 3 0 true"],
              {"type": "palladium:health", "min_health": 0, "max_health": 20})
    if c == "violet":
        pets = ("@e[type=#" + NS + ":pets,distance=..8]")
        pulse("loves_bond", 60, ["effect give @a[distance=..8] minecraft:regeneration 4 0 true",
                                 f"effect give {pets} minecraft:regeneration 4 0 true",
                                 "particle minecraft:heart ~ ~2 ~ 1 0.3 1 0 2 force"])
    if c == "white":
        pulse("font_of_life", 50, ["effect give @s minecraft:regeneration 3 0 true"])
    if c in ("white", "black"):
        pulse("no_hunger", 200, ["effect give @s minecraft:saturation 1 0 true"])


def benefit_ticks():
    """Datapack lines for the gifts that clear effects or react to damage (cheap tag selectors)."""
    tick = [*[f"effect clear @a[tag=gl_green] minecraft:{e}" for e in ("darkness", "blindness", "nausea")],
            "effect clear @a[tag=gl_red] minecraft:poison",
            "effect clear @a[tag=gl_black] minecraft:wither",
            "effect clear @a[tag=gl_black] minecraft:poison",
            f"execute as @a[tag=gl_indigo,scores={{gl_hurt=1..}}] at @s run effect give "
            f"@e[type=#{NS}:greed_prey,distance=..5] minecraft:weakness 5 1 true",
            "scoreboard players set @a[scores={gl_hurt=1..}] gl_hurt 0"]
    second = [f"execute at @a[tag=gl_yellow] run effect give @e[type=#{NS}:greed_prey,distance=..8] "
              f"minecraft:weakness 2 0 true"]
    load = ["scoreboard objectives add gl_hurt minecraft.custom:minecraft.damage_taken"]
    return load, tick, second


# --- what makes each corps different ------------------------------------------------

def roar(k, extra=(), index=6, xp=8):
    around = OTHERS.format(r=7)
    k.special("roar", "Roar", "Let out a roar that knocks back and weakens everything within 7 blocks.",
              "minecraft:goat_horn", {**command(first=[
                  burst(k.rgb, 2.0, "2 1 2", 150),
                  f"effect give {around} minecraft:levitation 1 2 true",
                  f"effect give {around} minecraft:weakness 4 1 true", *extra,
                  sound("minecraft:entity.ender_dragon.growl", 1.5)]),
                  "conditions": {"enabling": action(200)}}, cost=120, xp=xp, index=index)


def specials_green(k):
    roar(k)
    around = OTHERS.format(r=8)
    k.ultimate("emerald_nova", "Emerald Nova", "a blast of pure will that hurts and launches everything within 8 blocks.",
               "minecraft:emerald_block", [
                   burst(k.rgb, 3.0, "4 2 4", 400), "particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force",
                   f"execute as {around} run damage @s 20 minecraft:player_attack",
                   f"effect give {around} minecraft:levitation 2 4 true",
                   sound("minecraft:entity.generic.explode", 0.7)])


def specials_red(k):
    k.special("napalm", "Napalm", "Spew burning blood plasma that sets targets on fire.", "minecraft:fire_charge", {
        "type": "palladium:energy_beam", "energy_beam": f"{NS}:red_napalm", "damage": 3.0, "max_distance": 16.0,
        "speed": 0.8, "set_on_fire_seconds": 5, "energy_bar_usage": usage(4), "conditions": {"enabling": held()},
    }, cost=4, xp=8, index=6)
    k.special("rage", "Rage", "Toggle: give in to your rage for Strength II and Speed. Drains charge.", "minecraft:redstone", {
        **command(first=["effect give @s minecraft:strength infinite 1 true", "effect give @s minecraft:speed infinite 0 true",
                         sound("minecraft:entity.ravager.roar", 0.8)],
                  last=["effect clear @s minecraft:strength", "effect clear @s minecraft:speed"]),
        "energy_bar_usage": usage(2), "conditions": {"enabling": toggle()},
    }, cost=2, xp=12, index=7)
    k.hidden("rage_overlay", {
        "type": "palladium:gui_overlay", "texture": f"{NS}:textures/gui/rage_overlay.png",
        "texture_width": 256, "texture_height": 256, "alignment": "stretch",
        "conditions": {"enabling": enabled("rage")},
    })
    roar(k, [f"effect give {OTHERS.format(r=7)} minecraft:slowness 4 1 true"], index=8, xp=16)
    around = OTHERS.format(r=8)
    k.ultimate("blood_rage", "Blood Rage", "a storm of rage that hurts, withers and burns everything within 8 blocks.",
               "minecraft:nether_wart", [
                   burst(k.rgb, 3.0, "4 2 4", 400),
                   f"execute as {around} run damage @s 16 minecraft:player_attack",
                   f"effect give {around} minecraft:wither 6 1 true",
                   f"execute at {around} run particle minecraft:flame ~ ~1 ~ 0.3 0.6 0.3 0.02 30 force",
                   sound("minecraft:entity.blaze.shoot", 0.6)])


def specials_orange(k):
    k.special("avarice", "Avarice", "Passive: you mine much faster while suited up.", "minecraft:golden_pickaxe", {
        "type": "palladium:attribute_modifier", "attribute": "palladium:destroy_speed", "amount": 1.0, "operation": 0,
        "uuid": "6c7a0003-1a2b-4c3d-8e4f-0000000000aa"}, xp=5)
    k.special("hoard", "Hoard", "MINE! Pull every item and experience orb within 16 blocks to you.", "minecraft:chest",
              {**command(first=["tp @e[type=minecraft:item,distance=..16] @s",
                                "tp @e[type=minecraft:experience_orb,distance=..16] @s",
                                burst(k.rgb, 1.5, "2 1 2", 80), sound("minecraft:entity.item.pickup", 0.6)]),
               "conditions": {"enabling": action(40)}}, cost=50, xp=8, index=6)
    target = NEAREST.format(r=10)
    k.special("life_drain", "Life Drain", "Steal the life of the nearest creature within 10 blocks to heal yourself.",
              "minecraft:ghast_tear", {**command(first=[
                  f"execute as {target} at @s run {burst(k.rgb, 1.5, '0.4 0.8 0.4', 60, '~ ~1 ~')}",
                  f"execute as {target} run damage @s 10 minecraft:magic",
                  "effect give @s minecraft:instant_health 1 1 true",
                  "effect give @s minecraft:regeneration 5 1 true",
                  sound("minecraft:entity.evoker.prepare_attack", 1.2)]),
                  "conditions": {"enabling": action(100)}}, cost=120, xp=12, index=7)
    k.special("greed_arrival", "Greed Construct Arrival",
              f"Every mob you defeat while wearing the ring joins your hoard (up to {GREED_LIMIT}). "
              f"Summon the whole hoard as orange constructs that fight for you for {GREED_SECONDS} seconds.",
              "minecraft:gold_block", {**command(first=[
                  f"function {NS}:greed/arrival", sound("minecraft:entity.evoker.prepare_summon", 1.2)]),
                  "conditions": {"enabling": action(1200)}}, cost=300, xp=16, index=8)
    around = OTHERS.format(r=8)
    k.ultimate("consume", "Consume", "devour the life of everything within 8 blocks and keep it as extra hearts.",
               "minecraft:enchanted_golden_apple", [
                   burst(k.rgb, 3.0, "4 2 4", 400),
                   f"execute as {around} run damage @s 12 minecraft:magic",
                   f"effect give {around} minecraft:wither 5 1 true",
                   "effect give @s minecraft:absorption 30 4 true",
                   sound("minecraft:entity.wither.ambient", 1.4)])


WHISPER = json.dumps({"text": "Don't you hear him?", "color": "yellow", "italic": True})


# Orange Lantern greed constructs: mobs you kill join your hoard (up to GREED_LIMIT) and
# can be summoned back as orange hard-light constructs that fight for you.
GREED_LIMIT = 10
GREED_SECONDS = 30
GREED_MOBS = {  # capturable mob -> what it holds when summoned
    "zombie": None, "husk": None, "drowned": "minecraft:trident", "skeleton": "minecraft:bow",
    "stray": "minecraft:bow", "wither_skeleton": "minecraft:stone_sword", "spider": None, "cave_spider": None,
    "enderman": None, "pillager": "minecraft:crossbow", "vindicator": "minecraft:iron_axe", "blaze": None,
    "zombified_piglin": "minecraft:golden_sword", "piglin_brute": "minecraft:golden_axe",
}
GREED_PREY = list(GREED_MOBS) + ["creeper", "witch", "slime", "magma_cube", "phantom", "silverfish", "endermite",
                                 "ghast", "hoglin", "zoglin", "piglin", "evoker", "ravager", "guardian", "vex",
                                 "shulker", "warden"]


# Summonable armies of captured mobs. Kills of GREED_MOBS by a ring wearer are claimed
# (up to GREED_LIMIT per player) and summoned back by the army's arrival function.
ARMIES = {
    "greed": {
        "corps": "orange", "store": "gl_s_", "count": "gl_hoard", "team": "gl_greed", "color": "gold",
        "team_name": "Greed Constructs", "minion": "Greed Construct", "invisible": True,
        "claim": "Your hoard claims the {name}!", "empty": "Your hoard is empty. Defeat mobs while wearing the ring to claim them.",
        "particle": "minecraft:dust 1 0.55 0.1 {size} ~ ~1 ~ 0.3 0.6 0.3 0 {count}",
    },
    "dead": {
        "corps": "black", "store": "gl_d_", "count": "gl_dead", "team": "gl_dead", "color": "dark_gray",
        "team_name": "Black Lantern Revenants", "minion": "Black Lantern Revenant", "invisible": False,
        "claim": "The {name} will rise again at your command.", "empty": "No dead answer you yet. Slay mobs while wearing the ring.",
        "particle": "minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.02 {count}",
    },
}


def army_functions():
    """Datapack lines for every army: (load, tick, {function path: lines})."""
    load = ["scoreboard objectives add gl_bkills totalKillCount"]
    tick = []
    functions = {}
    for mob in GREED_MOBS:
        load.append(f"scoreboard objectives add gl_k_{mob} minecraft.killed:minecraft.{mob}")
    for army, cfg in ARMIES.items():
        tag, count, team, minion = f"gl_{cfg['corps']}", cfg["count"], cfg["team"], f"gl_{army}_minion"
        fx = lambda size, n, cfg=cfg: "particle " + cfg["particle"].format(size=size, count=n)  # noqa: E731
        load += [f"scoreboard objectives add {count} dummy", f"team add {team}",
                 f"team modify {team} displayName " + json.dumps({"text": cfg["team_name"], "color": cfg["color"]}),
                 f"team modify {team} color {cfg['color']}", f"team modify {team} friendlyFire false"]
        tick.append(f"scoreboard players add @a[tag={tag}] {count} 0")
        summons = []
        # given with /effect after summoning (no numeric effect ids in NBT)
        effects = ["minecraft:fire_resistance infinite 0", "minecraft:strength infinite 1",
                   "minecraft:glowing infinite 0"]  # glowing shows the team-colored outline
        if cfg["invisible"]:
            effects.append("minecraft:invisibility infinite 0")  # only the outline shows
        name_json = json.dumps({"text": cfg["minion"], "color": cfg["color"]}, separators=(",", ":"))
        for mob, held in GREED_MOBS.items():
            k_obj, s_obj = f"gl_k_{mob}", f"{cfg['store']}{mob}"
            load.append(f"scoreboard objectives add {s_obj} dummy")
            new_kill = f"@a[tag={tag},scores={{{k_obj}=1..,{count}=..{GREED_LIMIT - 1}}}]"
            name = mob.replace("_", " ").title()
            tick += [
                f"scoreboard players add @a[tag={tag}] {s_obj} 0",
                f"execute as {new_kill} run title @s actionbar " + json.dumps(
                    {"text": cfg["claim"].format(name=name), "color": cfg["color"]}),
                f"scoreboard players add {new_kill} {s_obj} 1",
                f"scoreboard players add {new_kill} {count} 1",
            ]
            hand = f'HandItems:[{{id:"{held}",Count:1b}},{{}}],HandDropChances:[0f,0f],' if held else ""
            nbt = (f'{{Tags:["{minion}","gl_{army}_new"],Team:"{team}",PersistenceRequired:1b,'
                   f'DeathLootTable:"minecraft:empty",{hand}CustomName:\'{name_json}\'}}')
            for n in range(1, GREED_LIMIT + 1):
                summons.append(f"execute if score @s {s_obj} matches {n}.. run summon minecraft:{mob} ~ ~ ~ {nbt}")
        functions[f"{army}/arrival"] = [
            f"team join {team} @s",
            f"execute if score @s {count} matches ..0 run tellraw @s " + json.dumps({"text": cfg["empty"], "color": cfg["color"]}),
            *summons,
            *[f"effect give @e[tag=gl_{army}_new] {e} true" for e in effects],
            f"spreadplayers ~ ~ 1 3 false @e[tag=gl_{army}_new,distance=..4]",
            f"scoreboard players set @e[tag=gl_{army}_new] gl_life {GREED_SECONDS * 20}",
            f"execute at @e[tag=gl_{army}_new] run {fx(2, 40)}",
            f"tag @e[tag=gl_{army}_new] remove gl_{army}_new",
        ]
        prey = f"@e[type=#{NS}:greed_prey,tag=!{minion},distance=..16,limit=1,sort=nearest]"
        tick += [
            # every second, send each minion after the nearest hostile mob
            f"execute if score #timer gl_life matches 0 as @e[tag={minion}] at @s run damage @s 0.01 "
            f"minecraft:mob_attack by {prey}",
            f"execute if score #timer gl_life matches 0 at @e[tag={minion}] run {fx(1.2, 6)}",
            f"scoreboard players remove @e[tag={minion}] gl_life 1",
            f"execute at @e[tag={minion},scores={{gl_life=..0}}] run {fx(2, 30)}",
            f"kill @e[tag={minion},scores={{gl_life=..0}}]",
        ]
    tick = ["scoreboard players add #timer gl_life 1",
            "execute if score #timer gl_life matches 20.. run scoreboard players set #timer gl_life 0"] + tick
    # each kill is claimed by whichever army's ring the killer wears, then cleared
    tick += [f"scoreboard players set @a[scores={{gl_k_{mob}=1..}}] gl_k_{mob} 0" for mob in GREED_MOBS]
    # Black Lantern kills only count while wearing the black ring
    tick.append("scoreboard players set @a[tag=!gl_black] gl_bkills 0")
    return load, tick, functions


def specials_yellow(k):
    around = OTHERS.format(r=10)
    k.special("inflict_fear", "Inflict Fear", "Fill everything within 10 blocks with terror: darkness, slowness and weakness.",
              "minecraft:wither_skeleton_skull", {**command(first=[
                  burst(k.rgb, 2.0, "3 1 3", 150),
                  f"execute at {around} run particle minecraft:squid_ink ~ ~1 ~ 0.3 0.5 0.3 0.02 20 force",
                  f"effect give {around} minecraft:darkness 6 0 true",
                  f"effect give {around} minecraft:slowness 6 1 true",
                  f"effect give {around} minecraft:weakness 6 1 true",
                  f"title @a[distance=0.5..10] times 5 50 15",
                  f"title @a[distance=0.5..10] title {WHISPER}",
                  sound("minecraft:ambient.cave", 0.8)]),
                  "conditions": {"enabling": action(200)}}, cost=120, xp=8, index=6)
    target = NEAREST.format(r=12)
    k.special("nightmare", "Nightmare", "Show the nearest creature within 12 blocks its worst fear: blinded, dizzy and sluggish.",
              "minecraft:phantom_membrane", {**command(first=[
                  f"execute as {target} at @s run particle minecraft:sculk_soul ~ ~1 ~ 0.3 0.6 0.3 0.02 30 force",
                  f"effect give {target} minecraft:nausea 10 0 true",
                  f"effect give {target} minecraft:blindness 6 0 true",
                  f"effect give {target} minecraft:mining_fatigue 10 2 true",
                  f"execute as {target} if entity @s[type=minecraft:player] run title @s title {WHISPER}",
                  sound("minecraft:entity.warden.heartbeat", 1.0)]),
                  "conditions": {"enabling": action(120)}}, cost=100, xp=12, index=7)
    around = OTHERS.format(r=12)
    k.ultimate("fear_incarnate", "Fear Incarnate", "become terror itself, crippling everything within 12 blocks for 15 seconds.",
               "minecraft:sculk_shrieker", [
                   burst(k.rgb, 3.0, "5 2 5", 400),
                   f"effect give {around} minecraft:darkness 15 0 true",
                   f"effect give {around} minecraft:slowness 15 3 true",
                   f"effect give {around} minecraft:weakness 15 2 true",
                   f"effect give {around} minecraft:nausea 15 0 true",
                   sound("minecraft:entity.warden.roar", 1.0)])


def specials_blue(k):
    k.special("hope_aura", "Aura of Hope", "Toggle: you and every player within 8 blocks regenerate health. Drains charge.",
              "minecraft:light_blue_dye", {"type": "palladium:dummy", "energy_bar_usage": usage(1),
                                           "conditions": {"enabling": toggle()}}, cost=1, xp=8, index=6)
    k.pulse("hope_aura_pulse", "hope_aura", 40, [f"effect give {ALLIES.format(r=8)} minecraft:regeneration 3 0 true",
                                                 burst(k.rgb, 1.2, "3 1 3", 30)])
    k.special("rekindle", "Rekindle", "Restore hope to every player within 12 blocks: instant healing and extra hearts.",
              "minecraft:golden_apple", {**command(first=[
                  burst(k.rgb, 2.0, "3 1 3", 150),
                  f"effect give {ALLIES.format(r=12)} minecraft:instant_health 1 1 true",
                  f"effect give {ALLIES.format(r=12)} minecraft:absorption 60 1 true",
                  sound("minecraft:block.beacon.power_select", 1.6)]),
                  "conditions": {"enabling": action(600)}}, cost=300, xp=12, index=7)
    r = ALLIES.format(r=16)
    k.ultimate("hope_burns_bright", "Hope Burns Bright",
               "every player within 16 blocks is healed and gains Regeneration and Resistance for 20 seconds.",
               "minecraft:beacon", [
                   burst(k.rgb, 3.0, "5 2 5", 400),
                   f"effect give {r} minecraft:instant_health 1 2 true",
                   f"effect give {r} minecraft:regeneration 20 2 true",
                   f"effect give {r} minecraft:resistance 20 1 true",
                   sound("minecraft:ui.toast.challenge_complete", 1.2)])


def specials_indigo(k):
    k.special("phase", "Phase", "Throw a bolt of indigo light and teleport to wherever it lands.", "minecraft:ender_pearl", {
        "type": "palladium:projectile", "entity_type": "minecraft:ender_pearl", "velocity": 2.5, "inaccuracy": 0.0,
        "conditions": {"enabling": action(40)},
    }, cost=80, xp=8, index=6)
    target = NEAREST.format(r=12)
    k.special("compassion", "Compassion", "The nearest creature within 12 blocks feels the pain it causes and can barely fight for 10 seconds.",
              "minecraft:blue_orchid", {**command(first=[
                  f"execute as {target} at @s run {burst(k.rgb, 1.5, '0.4 0.8 0.4', 60, '~ ~1 ~')}",
                  f"effect give {target} minecraft:weakness 10 254 true",
                  f"effect give {target} minecraft:slowness 10 1 true",
                  sound("minecraft:block.amethyst_block.chime", 0.7)]),
                  "conditions": {"enabling": action(200)}}, cost=150, xp=12, index=7)
    k.special("healing_touch", "Healing Touch", "Heal every player within 6 blocks.", "minecraft:glistering_melon_slice",
              {**command(first=[f"effect give {ALLIES.format(r=6)} minecraft:instant_health 1 1 true",
                                burst(k.rgb, 1.2, "2 1 2", 60), sound("minecraft:block.amethyst_block.chime", 1.4)]),
               "conditions": {"enabling": action(100)}}, cost=100, xp=16, index=8)
    around = OTHERS.format(r=12)
    k.ultimate("staff_of_compassion", "Staff of Compassion",
               "everything within 12 blocks is overwhelmed by empathy and can barely fight for 15 seconds.",
               "minecraft:end_rod", [
                   burst(k.rgb, 3.0, "5 2 5", 400),
                   f"effect give {around} minecraft:weakness 15 254 true",
                   f"effect give {around} minecraft:slowness 15 2 true",
                   f"effect give {around} minecraft:nausea 10 0 true",
                   sound("minecraft:block.beacon.deactivate", 0.8)])


def specials_violet(k):
    target = NEAREST.format(r=12)
    k.special("crystal_prison", "Crystal Prison", "Seal the nearest creature within 12 blocks in violet crystal for 8 seconds.",
              "minecraft:amethyst_cluster", {**command(first=[
                  *construct_cmds("violet", "crystal", f"execute at {target} positioned ~ ~1 ~"),
                  f"execute as {target} at @s run particle minecraft:end_rod ~ ~1 ~ 0.4 0.8 0.4 0.01 60 force",
                  f"execute as {target} at @s run {burst(k.rgb, 2.0, '0.4 1 0.4', 100, '~ ~1 ~')}",
                  f"effect give {target} minecraft:slowness 8 255 true",
                  f"effect give {target} minecraft:jump_boost 8 250 true",
                  f"effect give {target} minecraft:mining_fatigue 8 4 true",
                  f"effect give {target} minecraft:glowing 8 0 true",
                  sound("minecraft:block.amethyst_cluster.place", 0.8)]),
                  "conditions": {"enabling": action(200)}}, cost=200, xp=8, index=6)
    k.special("loves_embrace", "Love's Embrace", "Heal every player within 8 blocks and give them Regeneration.",
              "minecraft:pink_tulip", {**command(first=[
                  f"effect give {ALLIES.format(r=8)} minecraft:instant_health 1 1 true",
                  f"effect give {ALLIES.format(r=8)} minecraft:regeneration 10 0 true",
                  "particle minecraft:heart ~ ~1.5 ~ 2 1 2 0 30 force",
                  sound("minecraft:entity.allay.ambient_with_item", 1.0)]),
                  "conditions": {"enabling": action(200)}}, cost=150, xp=12, index=7)
    around = OTHERS.format(r=10)
    k.special("charm", "Charm", "Enchant everything within 10 blocks with love so it can barely hurt anyone.",
              "minecraft:poppy", {**command(first=[
                  f"execute at {around} run particle minecraft:heart ~ ~2 ~ 0.3 0.3 0.3 0 3 force",
                  f"effect give {around} minecraft:weakness 10 3 true",
                  f"effect give {around} minecraft:slowness 10 0 true",
                  sound("minecraft:entity.allay.item_given", 1.2)]),
                  "conditions": {"enabling": action(200)}}, cost=120, xp=16, index=8)
    k.ultimate("love_conquers_all", "Love Conquers All",
               "fully heal every player within 16 blocks and pacify everything else around you.",
               "minecraft:amethyst_block", [
                   burst(k.rgb, 3.0, "5 2 5", 400), "particle minecraft:heart ~ ~1.5 ~ 5 2 5 0 80 force",
                   f"effect give {ALLIES.format(r=16)} minecraft:instant_health 1 4 true",
                   f"effect give {OTHERS.format(r=16)} minecraft:weakness 15 254 true",
                   sound("minecraft:ui.toast.challenge_complete", 1.4)])


def specials_white(k):
    k.special("life_growth", "Life Growth",
              "While crouching: bring the ground around you to life, turning dirt to grass and cobblestone to moss.",
              "minecraft:bone_meal", {**command(first=[
                  "fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 minecraft:grass_block replace minecraft:dirt",
                  "fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 minecraft:grass_block replace minecraft:coarse_dirt",
                  "fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 minecraft:moss_block replace minecraft:cobblestone",
                  "particle minecraft:happy_villager ~ ~0.5 ~ 4 0.5 4 0 150 force",
                  sound("minecraft:item.bone_meal.use", 1.0)]),
                  "conditions": {"enabling": action(40)}}, cost=60, xp=8, index=6,
              extra=[{"type": "palladium:crouching"}])
    k.special("life_aura", "Aura of Life", "Toggle: you and every player within 10 blocks regenerate health. Drains charge.",
              "minecraft:totem_of_undying", {"type": "palladium:dummy", "energy_bar_usage": usage(1),
                                             "conditions": {"enabling": toggle()}}, cost=1, xp=12, index=7)
    k.pulse("life_aura_pulse", "life_aura", 40, [f"effect give {ALLIES.format(r=10)} minecraft:regeneration 3 1 true",
                                                 "particle minecraft:end_rod ~ ~1 ~ 3 1 3 0.01 20 force"])
    k.ultimate("entitys_light", "Light of the Entity",
               "a wave of pure life that heals every living thing within 12 blocks and burns the undead.",
               "minecraft:nether_star", [
                   "particle minecraft:end_rod ~ ~1 ~ 5 2 5 0.05 400 force", "particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force",
                   "effect give @e[distance=..12,type=!minecraft:item,type=!minecraft:experience_orb] minecraft:instant_health 1 2 true",
                   f"effect give {ALLIES.format(r=12)} minecraft:regeneration 20 1 true",
                   sound("minecraft:block.beacon.activate", 0.6)])


def specials_black(k):
    target = NEAREST.format(r=8)
    k.special("heart_rip", "Heart Rip", "Tear at the heart of the nearest creature within 8 blocks, healing yourself.",
              "minecraft:wither_rose", {**command(first=[
                  f"execute as {target} at @s run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.02 40 force",
                  f"execute as {target} run damage @s 14 minecraft:magic",
                  f"effect give {target} minecraft:wither 6 1 true",
                  "effect give @s minecraft:instant_health 1 1 true",
                  sound("minecraft:entity.wither.hurt", 0.6)]),
                  "conditions": {"enabling": action(120)}}, cost=150, xp=8, index=6)
    k.special("death_aura", "Death Aura", "Toggle: everything within 6 blocks slowly withers. Drains charge.",
              "minecraft:wither_skeleton_skull", {"type": "palladium:dummy", "energy_bar_usage": usage(1),
                                                  "conditions": {"enabling": toggle()}}, cost=1, xp=12, index=7)
    k.pulse("death_aura_pulse", "death_aura", 40, [f"effect give {OTHERS.format(r=6)} minecraft:wither 3 0 true",
                                                   "particle minecraft:soul ~ ~1 ~ 3 1 3 0.01 20 force"])
    k.special("raise_dead", "Raise the Dead",
              f"Every mob you slay while wearing the ring can rise again (up to {GREED_LIMIT}). Raise them all as "
              f"Black Lantern revenants that fight for you for {GREED_SECONDS} seconds.",
              "minecraft:zombie_head", {**command(first=[
                  f"function {NS}:dead/arrival", sound("minecraft:entity.zombie_villager.cure", 0.6)]),
                  "conditions": {"enabling": action(1200)}}, cost=300, xp=16, index=8)
    k.special("undying", "Undying",
              "Passive: while your ring holds at least 500 charge, a killing blow leaves you standing instead. "
              "The ring spends all its charge to bring you back.",
              "minecraft:totem_of_undying", {"type": "palladium:immortality"}, xp=20, extra=[charge(500)])
    k.hidden("undying_revival", {
        **command(first=[
            "effect give @s minecraft:instant_health 1 2 true",
            "effect give @s minecraft:regeneration 10 2 true",
            "effect give @s minecraft:absorption 20 2 true",
            "particle minecraft:soul ~ ~1 ~ 0.6 1 0.6 0.05 120 force",
            "particle minecraft:totem_of_undying ~ ~1 ~ 0.6 1 0.6 0.4 80 force",
            "title @s actionbar " + json.dumps({"text": "The black ring will not let you die.", "color": "gray"}),
            sound("minecraft:item.totem.use", 0.6)]),
        "energy_bar_usage": usage(1_000_000),
        "conditions": {"unlocking": [unlocked("skill_undying"), charge(500),
                                     {"type": "palladium:health", "max_health": 1.5}]},
    })
    # Emotional Sight sits on the free slot at the start of the third bar page.
    k.node("skill_emotional_sight", "Emotional Sight",
           "Toggle: see every living thing within 32 blocks glowing through walls.", "minecraft:ender_eye",
           (1, 3), ["skill_flight"], 8, shared=False)
    k.bar("emotional_sight", {"type": "palladium:entity_glow", "mode": "others", "distance": 32.0,
                              "conditions": {"enabling": toggle()}},
          "Emotional Sight", "minecraft:ender_eye", 10, node="skill_emotional_sight", shared=False)
    around = OTHERS.format(r=12)
    k.ultimate("blackest_night", "Blackest Night", "plunge everything within 12 blocks into death: darkness, withering and pain.",
               "minecraft:sculk_catalyst", [
                   "particle minecraft:soul ~ ~1 ~ 5 2 5 0.05 400 force",
                   f"execute as {around} run damage @s 12 minecraft:magic",
                   f"effect give {around} minecraft:wither 10 2 true",
                   f"effect give {around} minecraft:darkness 10 0 true",
                   sound("minecraft:entity.wither.spawn", 0.8)])


# --- dual rings: Spectrum Fusion ------------------------------------------------------
# Wearing two rings at once gives a fusion ability that mixes both corps' signature effects.
# The corps listed first in CORPS owns the ability, so a pair never gets it twice.

FOE = OTHERS.format(r=10)
FRIENDS = ALLIES.format(r=10)
SIGNATURE = {
    "green": [f"execute as {FOE} run damage @s 10 minecraft:player_attack", f"effect give {FOE} minecraft:levitation 1 3 true"],
    "yellow": [f"effect give {FOE} minecraft:darkness 8 0 true", f"effect give {FOE} minecraft:slowness 8 2 true"],
    "red": [f"execute as {FOE} run damage @s 6 minecraft:magic", f"effect give {FOE} minecraft:wither 6 1 true",
            f"execute at {FOE} run particle minecraft:flame ~ ~1 ~ 0.3 0.6 0.3 0.02 20 force"],
    "orange": [f"execute as {FOE} run damage @s 6 minecraft:magic", "effect give @s minecraft:instant_health 1 1 true",
               "effect give @s minecraft:absorption 30 2 true"],
    "blue": [f"effect give {FRIENDS} minecraft:regeneration 10 2 true", f"effect give {FRIENDS} minecraft:absorption 30 1 true"],
    "violet": [f"effect give {FOE} minecraft:slowness 4 255 true", f"effect give {FOE} minecraft:jump_boost 4 250 true",
               f"effect give {FOE} minecraft:glowing 6 0 true"],
    "indigo": [f"effect give {FOE} minecraft:weakness 8 254 true", f"effect give {FRIENDS} minecraft:instant_health 1 0 true"],
    "white": [f"effect give {FRIENDS} minecraft:instant_health 1 2 true",
              "effect give @e[distance=..10,type=!minecraft:item,type=!minecraft:experience_orb] minecraft:instant_health 1 1 true"],
    "black": [f"effect give {FOE} minecraft:wither 8 2 true", f"effect give {FOE} minecraft:darkness 6 0 true"],
}
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
FUSION_COST = 250


def fusion_pairs():
    order = list(CORPS)
    return [(a, b) for i, a in enumerate(order) for b in order[i + 1:]]


def fusion_function(a, b):
    """Commands for the a+b fusion, run as the ring bearer."""
    name = FUSION_NAMES[(a, b)]
    ca, cb = CORPS[a]["color"], CORPS[b]["color"]
    return [
        "title @s times 5 40 10",
        "title @s subtitle " + json.dumps({"text": f"{CORPS[a]['emotion']} + {CORPS[b]['emotion']}", "color": "gray"}),
        "title @s title " + json.dumps([{"text": name.split(" ")[0] + " ", "color": hexcolor(ca)},
                                        {"text": " ".join(name.split(" ")[1:]), "color": hexcolor(cb)}]),
        burst(ca, 2.5, "4 1.5 4", 220), burst(cb, 2.5, "4 1.5 4", 220),
        "particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force",
        *SIGNATURE[a], *SIGNATURE[b],
        sound("minecraft:block.beacon.power_select", 0.8), sound("minecraft:entity.illusioner.cast_spell", 1.2),
    ]


def fusion_ability(k):
    """Adds Spectrum Fusion to corps k.c if it is the lower-ranked partner of any pair."""
    partners = [b for a, b in fusion_pairs() if a == k.c]
    if not partners:
        return
    k.bar("spectrum_fusion", {
        **command(first=[f"execute if entity @s[tag=gl_{b}] run function {NS}:fusion/{k.c}_{b}" for b in partners]),
        "energy_bar_usage": usage(FUSION_COST),
        "conditions": {"enabling": action(600)},
    }, "Spectrum Fusion", "minecraft:nether_star", 16, cost=FUSION_COST,
        extra=[{"type": "palladium:or", "conditions": [
            {"type": "palladium:has_power", "power": f"{NS}:{b}_lantern"} for b in partners]}])
    k.lang[f"ability.{NS}.spectrum_fusion.description"] = (
        "Wear two rings at once to fuse their powers. Each pair of corps has its own fusion.")


def base_power():
    """The hidden power every ring also grants. It holds the bonuses that must not stack when two
    rings are worn: Palladium keeps one holder per power, however many rings grant it. It keeps no
    saved state (no energy bars, no buyables), reading each corps' charge and skills instead."""
    def any_ring(*per_corps):
        return {"type": "palladium:or", "conditions": [
            {"type": "palladium:and", "conditions": [f(c) for f in per_corps]} if len(per_corps) > 1 else per_corps[0](c)
            for c in CORPS]}

    def charged(c):
        return {"type": "palladium:energy_bar", "power": f"{NS}:{c}_lantern", "energy_bar": BAR, "min": 1}

    def skill(name):
        return lambda c: {"type": "palladium:ability_unlocked", "power": f"{NS}:{c}_lantern", "ability": name}

    abilities = {}

    def attr(key, attribute, amount, cond):
        abilities[key] = {
            "type": "palladium:attribute_modifier", "attribute": attribute, "amount": amount, "operation": 0,
            "uuid": "6c7affff-1a2b-4c3d-8e4f-" + hashlib.md5(key.encode()).hexdigest()[:12],
            "hidden": True, "hidden_in_bar": True, "conditions": {"unlocking": cond}}

    attr("ring_health", "minecraft:generic.max_health", 60, any_ring(charged))       # 40 hearts
    attr("ring_armor", "minecraft:generic.armor", 20, any_ring(charged))             # netherite-level
    attr("ring_toughness", "minecraft:generic.armor_toughness", 12, any_ring(charged))
    attr("ring_knockback", "minecraft:generic.knockback_resistance", 0.4, any_ring(charged))
    attr("ring_fists", "palladium:punch_damage", 4, any_ring(charged))
    for i in (1, 2):
        attr(f"health_{i}", "minecraft:generic.max_health", 20, any_ring(skill(f"skill_health_{i}"), charged))
        attr(f"combat_{i}", "minecraft:generic.attack_damage", 4, any_ring(skill(f"skill_combat_{i}"), charged))
        attr(f"combat_{i}_fists", "palladium:punch_damage", 4, any_ring(skill(f"skill_combat_{i}"), charged))
    flight = any_ring(skill("skill_flight"), charged)
    attr("flight", "palladium:flight_speed", 1.0, flight)
    attr("flight_flexibility", "palladium:flight_flexibility", 5, flight)
    attr("heroic_flight", "palladium:heroic_flight_type", 1, flight)
    abilities["universal_translator"] = {  # villagers understand you: Hero of the Village prices
        **command(first=["effect give @s minecraft:hero_of_the_village 15 0 true"]),
        "hidden": True, "hidden_in_bar": True,
        "conditions": {"unlocking": any_ring(charged), "enabling": interval(100)}}
    abilities["ring_protection"] = {
        "type": "palladium:damage_immunity", "hidden": True, "hidden_in_bar": True,
        "damage_sources": ["minecraft:is_drowning", "minecraft:is_fall", "minecraft:is_freezing"],
        "conditions": {"unlocking": any_ring(charged)}}
    return {"name": {"translate": f"power.{NS}.lantern_base"}, "icon": f"{NS}:green_lantern_ring",
            "hidden": True, "abilities": abilities}


def charge_functions():
    """Save every worn ring's charge each second; restore it when the ring is equipped again."""
    fns, load, second = {}, [], []
    for c in CORPS:
        power = f"{NS}:{c}_lantern"
        load.append(f"scoreboard objectives add gl_ch_{c} dummy")
        restore = [f"scoreboard players add @s gl_ch_{c} 0",
                   f"scoreboard players operation @s gl_tmp = @s gl_ch_{c}",
                   f"energybar value set @s {power} {BAR} 0"]
        for bit in (2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1):  # no macros in 1.20.1: add it bit by bit
            restore += [f"execute if score @s gl_tmp matches {bit}.. run energybar value add @s {power} {BAR} {bit}",
                        f"execute if score @s gl_tmp matches {bit}.. run scoreboard players remove @s gl_tmp {bit}"]
        restore.append(f"tag @s add gl_cr_{c}")
        fns[f"charge/restore_{c}"] = restore
        second += [f"execute as @a[tag=gl_cr_{c}] store success score @s gl_ok store result score @s gl_tmp run "
                   f"energybar value get @s {power} {BAR}",
                   f"execute as @a[tag=gl_cr_{c},scores={{gl_ok=1}}] run scoreboard players operation @s gl_ch_{c} = @s gl_tmp"]
    load.append("scoreboard objectives add gl_ok dummy")
    fns["charge/save"] = second
    return fns, load


def sense_tags():
    """Tick lines that set cheap tags used by ability conditions (instead of per-tick commands)."""
    tick = []
    for c in CORPS:
        battery = f"{NS}:{c}_power_battery"
        tick.append(f"tag @a[tag=gl_look_{c}] remove gl_look_{c}")
        for d in range(1, 10):  # looking at your corps' placed battery, up to 4.5 blocks away
            tick.append(f"execute as @a[tag=gl_{c},tag=!gl_look_{c}] at @s anchored eyes positioned ^ ^ ^{d / 2} "
                        f"if block ~ ~ ~ {battery} run tag @s add gl_look_{c}")
    for c, data in CORPS.items():
        ally = data.get("empowered_by")
        if ally:
            tick += [f"tag @a[tag=gl_near_{ally}] remove gl_near_{ally}",
                     f"execute as @a[tag=gl_{c}] at @s if entity @a[tag=gl_{ally},distance=0.1..12] "
                     f"run tag @s add gl_near_{ally}"]
    return tick


SPECIALS = {
    "green": specials_green, "yellow": specials_yellow, "red": specials_red, "orange": specials_orange,
    "blue": specials_blue, "violet": specials_violet, "indigo": specials_indigo, "white": specials_white,
    "black": specials_black,
}

# --- output -----------------------------------------------------------------------

def write(rel, data):
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(rel, text):
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def save(img, rel):
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


GENERATED_DIRS = [
    f"addon/{NS}", f"data/{NS}/palladium", f"data/{NS}/recipes", f"data/{NS}/loot_tables", f"data/{NS}/curios",
    f"data/{NS}/functions", f"data/{NS}/tags", "data/minecraft/tags/functions",
    f"data/{NS}/predicates", f"data/{NS}/item_modifiers", f"data/{NS}/kubejs_scripts",
    f"assets/{NS}/models", f"assets/{NS}/blockstates", f"assets/{NS}/textures", f"assets/{NS}/palladium",
]


def main():
    for d in GENERATED_DIRS:
        shutil.rmtree(SRC / d, ignore_errors=True)

    lang = {
        f"itemGroup.{NS}.lantern_corps": "Lantern Corps",
        f"tooltip.{NS}.ring.hold": "Hold in either hand, or wear it in a Curios ring slot.",
        f"tooltip.{NS}.ring.tree": "Open the powers menu to upgrade it with XP.",
        f"tooltip.{NS}.battery.1": "Hold it in your main hand (ring in your other hand",
        f"tooltip.{NS}.battery.2": "or a ring slot) and press Recharge to fully charge it.",
    }
    items, tab = [], []

    for c, data in CORPS.items():
        rgb = data["color"]
        ring, battery = f"{c}_lantern_ring", f"{c}_power_battery"
        items.append(ring)
        tab += [f"{NS}:{ring}", f"{NS}:{battery}"]

        # ring item
        write(f"addon/{NS}/items/{ring}.json", {
            "max_stack_size": 1, "rarity": "epic", "is_fire_resistant": True, "creative_mode_tab": f"{NS}:lantern_corps",
            "tooltip": [{"translate": f"item.{NS}.{ring}.tooltip", "color": hexcolor(rgb), "italic": True},
                        {"translate": f"tooltip.{NS}.ring.hold", "color": "gray"},
                        {"translate": f"tooltip.{NS}.ring.tree", "color": "gray"}],
        })
        lang[f"item.{NS}.{ring}"] = f"{data['name']} Ring"
        lang[f"item.{NS}.{ring}.tooltip"] = f"Powered by {data['emotion']}"
        write(f"assets/{NS}/models/item/{ring}.json",
              {"parent": "minecraft:item/generated", "textures": {"layer0": f"{NS}:item/{ring}"}})
        save(art.ring_item(c, rgb), f"assets/{NS}/textures/item/{ring}.png")

        # power battery: a placeable lantern block with its own item
        write(f"addon/{NS}/blocks/{battery}.json", {
            "sound_type": "minecraft:lantern", "map_color": MAP_COLOR[c], "destroy_time": 2.0, "explosion_resistance": 6.0,
            "no_occlusion": True, "render_type": "translucent", "register_item": False,
        })
        write(f"addon/{NS}/items/{battery}.json", {
            "type": "palladium:block_item", "block": f"{NS}:{battery}", "max_stack_size": 1, "rarity": "rare",
            "creative_mode_tab": f"{NS}:lantern_corps",
            "tooltip": [{"translate": f"tooltip.{NS}.battery.1", "color": "gray"},
                        {"translate": f"tooltip.{NS}.battery.2", "color": "gray"}],
        })
        items.append(battery)
        lang[f"block.{NS}.{battery}"] = lang[f"item.{NS}.{battery}"] = f"{data['name']} Power Battery"
        write(f"assets/{NS}/blockstates/{battery}.json", {"variants": {"": {"model": f"{NS}:block/{battery}"}}})
        write(f"assets/{NS}/models/block/{battery}.json", art.battery_model(c))
        write(f"assets/{NS}/models/item/{battery}.json", {"parent": f"{NS}:block/{battery}"})
        for name, img in art.battery_textures(c, rgb).items():
            save(img, f"assets/{NS}/textures/block/{c}_battery_{name}.png")
        write(f"data/{NS}/loot_tables/blocks/{battery}.json", {
            "type": "minecraft:block",
            "pools": [{"rolls": 1, "entries": [{"type": "minecraft:item", "name": f"{NS}:{battery}"}],
                       "conditions": [{"condition": "minecraft:survives_explosion"}]}],
        })

        # power
        k = Kit(c, data)
        shared_kit(k)
        SPECIALS[c](k)
        fusion_ability(k)
        write(f"data/{NS}/palladium/powers/{c}_lantern.json", {
            "name": {"translate": f"power.{NS}.{c}_lantern"},
            "icon": f"{NS}:{ring}",
            "background": f"{NS}:textures/gui/menu/{c}.png",
            "gui_display_type": "tree",
            "primary_color": hexcolor(rgb),
            "secondary_color": hexcolor(art.shade(rgb, 0.4)),
            "persistent_data": True,
            "energy_bars": {BAR: {
                "max": {"type": "score", "objective": f"glmax_{c}", "fallback": BASE_CHARGE},
                "auto_increase_per_tick": 1 if data.get("regen", True) else 0, "auto_increase_interval": 10,
                "color": hexcolor(rgb)}},
            "abilities": k.abilities,
        })
        lang[f"power.{NS}.{c}_lantern"] = data["name"]
        save(art.menu_background(c, rgb), f"assets/{NS}/textures/gui/menu/{c}.png")
        save(art.construct_texture(c, rgb), f"assets/{NS}/textures/item/construct/{c}.png")
        lang.update(k.lang)
        for slot in ("mainhand", "offhand", "curios:ring"):
            write(f"data/{NS}/palladium/item_powers/{ring}_{slot.replace(':', '_')}.json",
                  {"slot": slot, "item": f"{NS}:{ring}", "power": [f"{NS}:{c}_lantern", f"{NS}:lantern_base"]})

        # Suits and masks: one accessory slot each in the accessories menu, shown while you
        # wear this corps' ring. Both render on the two-layer suit model.
        def layered(name, folder, both_skins=True):
            def tex(part):
                base = f"{NS}:textures/models/{folder}/{name}{part}"
                return {"normal": base + ".png", "slim": base + "_slim.png"} if both_skins else base + ".png"
            model = {"normal": f"{NS}:player#suit", "slim": f"{NS}:player#suit_slim"}
            return {"type": "palladium:compound", "layers": [
                {"model_layer": model, "texture": tex(""), "render_type": "solid"},
                {"model_layer": model, "texture": tex("_glow"), "render_type": "glow"},
            ]}

        for kind, label in (("suit", "Suit"), ("mask", "Mask")):
            write(f"addon/{NS}/accessory_slots/{c}_{kind}.json", {
                "icon": f"{NS}:textures/gui/accessory_slots/{c}_{kind}.png",
                "menu_visibility": {"type": "palladium:has_power", "power": f"{NS}:{c}_lantern"},
            })
            save(art.slot_icon(c, rgb, kind), f"assets/{NS}/textures/gui/accessory_slots/{c}_{kind}.png")
            lang[f"accessory_slot.{NS}.{c}_{kind}"] = f"{data['name']} {label}"
        for design, design_name in art.DESIGNS[c]:
            name = f"{c}_suit_{design}"
            for slim in (False, True):
                suit, glow = art.suit(c, rgb, design, slim)
                sfx = "_slim" if slim else ""
                save(suit, f"assets/{NS}/textures/models/suit/{name}{sfx}.png")
                save(glow, f"assets/{NS}/textures/models/suit/{name}_glow{sfx}.png")
            write(f"assets/{NS}/palladium/render_layers/{name}.json", layered(name, "suit"))
            write(f"addon/{NS}/accessories/{name}.json", {"type": "palladium:render_layer", "slot": f"{NS}:{c}_suit",
                                                          "render_layer": f"{NS}:{name}", "disable_rendering": True})
            lang[f"accessory.{NS}.{name}"] = design_name
        for mask_id, mask_name in art.MASKS + art.MASK_EXTRAS.get(c, []):
            name = f"{c}_mask_{mask_id}"
            if mask_id == "none":
                write(f"assets/{NS}/palladium/render_layers/{name}.json", {"type": "palladium:compound", "layers": []})
            else:
                mask, glow = art.mask(c, rgb, mask_id)
                save(mask, f"assets/{NS}/textures/models/mask/{name}.png")
                save(glow, f"assets/{NS}/textures/models/mask/{name}_glow.png")
                write(f"assets/{NS}/palladium/render_layers/{name}.json", layered(name, "mask", both_skins=False))
            write(f"addon/{NS}/accessories/{name}.json", {"type": "palladium:render_layer", "slot": f"{NS}:{c}_mask",
                                                          "render_layer": f"{NS}:{name}", "disable_rendering": True})
            lang[f"accessory.{NS}.{name}"] = mask_name
        band, gem = art.ring_textures(c, rgb)
        save(band, f"assets/{NS}/textures/models/ring/{c}_band.png")
        save(gem, f"assets/{NS}/textures/models/ring/{c}_gem.png")
        for part, render_type in (("band", "solid"), ("gem", "glow")):
            for side in ("", "_left"):
                write(f"assets/{NS}/palladium/render_layers/{c}_ring_{part}{side}.json", {
                    "model_layer": {"normal": f"{NS}:player#lantern_ring{side}",
                                    "slim": f"{NS}:player#lantern_ring{side}_slim"},
                    "texture": f"{NS}:textures/models/ring/{c}_{part}.png", "render_type": render_type})
        # Scuba Gear construct
        save(art.scuba_texture(c, rgb), f"assets/{NS}/textures/models/scuba/{c}.png")
        write(f"assets/{NS}/palladium/render_layers/{c}_scuba.json", {
            "model_layer": f"{NS}:player#scuba", "texture": f"{NS}:textures/models/scuba/{c}.png",
            "render_type": "solid"})
        for n in range(1, 6):
            save(art.construct_slot_icon(c, rgb, n), f"assets/{NS}/textures/gui/construct_slot/{c}_{n}.png")
        # placeable construct blocks (Construct Blocks) and temporary hard light (walls, domes, bridges)
        for block, hardlight in ((f"{c}_construct_block", False), (f"{c}_hardlight", True)):
            write(f"addon/{NS}/blocks/{block}.json", {
                "sound_type": "minecraft:amethyst", "map_color": MAP_COLOR[c], "destroy_time": 4.0 if hardlight else 0.3,
                "explosion_resistance": 1200.0 if hardlight else 1.0, "no_occlusion": True,
                "render_type": "translucent", "register_item": not hardlight,
                **({} if hardlight else {"creative_mode_tab": f"{NS}:lantern_corps"})})
            save(art.construct_block_texture(c, rgb, hardlight), f"assets/{NS}/textures/block/{block}.png")
            write(f"assets/{NS}/blockstates/{block}.json", {"variants": {"": {"model": f"{NS}:block/{block}"}}})
            write(f"assets/{NS}/models/block/{block}.json", art.construct_block_model(f"{NS}:block/{block}"))
            write(f"data/{NS}/loot_tables/blocks/{block}.json", {"type": "minecraft:block", "pools": []})  # no drops
            name = f"{data['name']} {'Hard Light' if hardlight else 'Construct Block'}"
            lang[f"block.{NS}.{block}"] = name
            if not hardlight:
                write(f"assets/{NS}/models/item/{block}.json", {"parent": f"{NS}:block/{block}"})
                lang[f"item.{NS}.{block}"] = name
        fx = rgb if c != "black" else (150, 155, 170)
        write(f"assets/{NS}/palladium/energy_beams/{c}_beam.json", {
            "type": "palladium:laser", "body_part": "right_arm", "offset": [-1, -11, 0],  # just past the knuckles
            "glow_color": hexcolor(fx), "core_color": "#FFFFFF" if c != "black" else "#101014",
            "glow_opacity": 0.9, "bloom": 3, "size": 1.4, "rotation_speed": 3,
            "particles": [{"particle_type": "minecraft:dust", "options": dust(fx), "amount": 2,
                           "offset_random": [0.2, 0.2, 0.2]}]})
        write(f"assets/{NS}/palladium/trails/{c}_trail.json",
              {"type": "palladium:gradient", "spacing": 2, "lifetime": 14, "color": hexcolor(fx)})

        # recipes
        if data["gem"]:
            write(f"data/{NS}/recipes/{ring}.json", {
                "type": "minecraft:crafting_shaped", "category": "equipment", "pattern": [" X ", "GEG", " G "],
                "key": {"X": {"item": data["gem"]}, "E": {"item": "minecraft:ender_eye"},
                        "G": {"item": "minecraft:gold_ingot"}},
                "result": {"item": f"{NS}:{ring}"}})
        write(f"data/{NS}/recipes/{battery}.json", {
            "type": "minecraft:crafting_shaped", "category": "equipment", "pattern": ["GXG", "SLS", "SSS"],
            "key": {"G": {"item": data["glass"]}, "X": {"item": data["gem"] or "minecraft:nether_star"},
                    "L": {"item": "minecraft:lantern"}, "S": {"item": "minecraft:polished_deepslate"}},
            "result": {"item": f"{NS}:{battery}"}})

    red = CORPS["red"]["color"]
    write(f"assets/{NS}/palladium/energy_beams/red_napalm.json", {
        "type": "palladium:laser", "body_part": "head", "offset": [0, 2, 0], "glow_color": hexcolor(red),
        "core_color": "#FF6A00", "glow_opacity": 0.95, "bloom": 2, "size": 2.2,
        "particles": [{"particle_type": "minecraft:flame", "amount": 3, "offset_random": [0.3, 0.3, 0.3]}]})

    # The White Lantern is earned by uniting the seven colors of the spectrum.
    write(f"data/{NS}/recipes/white_lantern_ring.json", {
        "type": "minecraft:crafting_shapeless", "category": "equipment",
        "ingredients": [{"item": f"{NS}:{c}_lantern_ring"} for c in SPECTRUM]
                       + [{"item": "minecraft:nether_star"}, {"item": "minecraft:totem_of_undying"}],
        "result": {"item": f"{NS}:white_lantern_ring"}})

    write(f"addon/{NS}/items/_loading_order.json", items)
    write(f"addon/{NS}/creative_mode_tabs/lantern_corps.json", {"icon": f"{NS}:green_lantern_ring", "items": tab})
    write(f"assets/{NS}/palladium/model_layers/lantern_ring/player.json", art.ring_model(False))
    write(f"assets/{NS}/palladium/model_layers/suit/player.json", art.suit_model(False))
    write(f"assets/{NS}/palladium/model_layers/suit_slim/player.json", art.suit_model(True))
    write(f"assets/{NS}/palladium/model_layers/lantern_ring_slim/player.json", art.ring_model(True))
    write(f"assets/{NS}/palladium/model_layers/lantern_ring_left/player.json", art.ring_model(False, left=True))
    write(f"assets/{NS}/palladium/model_layers/lantern_ring_left_slim/player.json", art.ring_model(True, left=True))
    write(f"assets/{NS}/palladium/model_layers/scuba/player.json", art.scuba_model())
    write(f"assets/{NS}/palladium/particle_emitters/ring_hand.json", {
        "body_part": "right_arm", "amount": 1, "offset": [-1, -10, 0], "offset_random": [1, 1, 1],
        "motion": [0, 0.5, 0], "motion_random": [0.3, 0.3, 0.3], "visible_in_first_person": False})
    write(f"assets/{NS}/palladium/particle_emitters/ring_hand_left.json", {
        "body_part": "left_arm", "amount": 1, "offset": [1, -10, 0], "offset_random": [1, 1, 1],
        "motion": [0, 0.5, 0], "motion_random": [0.3, 0.3, 0.3], "visible_in_first_person": False})
    write(f"assets/{NS}/palladium/particle_emitters/flight_aura.json", {
        "body_part": "chest", "amount": 2, "offset": [0, -6, 0], "offset_random": [6, 12, 6],
        "motion_random": [0.2, 0.2, 0.2], "visible_in_first_person": False})
    write("data/curios/tags/items/ring.json", {"replace": False, "values": [f"{NS}:{c}_lantern_ring" for c in CORPS]})
    write(f"data/{NS}/curios/entities/lantern_ring.json", {"entities": ["player"], "slots": ["ring"]})
    # Two ring slots so you can wear two rings (Curios merges sizes with max(), so this never shrinks it)
    write(f"data/{NS}/curios/slots/ring.json", {"size": 2})
    # Constructs: one hidden item per shape; CustomModelData picks the corps color.
    for shape, elements in art.construct_shapes().items():
        item = f"construct_{shape}"
        write(f"addon/{NS}/items/{item}.json", {"max_stack_size": 1})
        lang[f"item.{NS}.{item}"] = f"{SHAPES[shape]['name']} Construct"
        write(f"assets/{NS}/models/item/{item}_base.json", {
            "render_type": "minecraft:translucent",
            "textures": {"0": f"{NS}:item/construct/green", "particle": f"{NS}:item/construct/green"},
            "elements": elements,
            **({"display": art.SHAPE_DISPLAY[shape]} if shape in art.SHAPE_DISPLAY else {}),
        })
        write(f"assets/{NS}/models/item/{item}.json", {
            "parent": f"{NS}:item/{item}_base",
            "overrides": [{"predicate": {"custom_model_data": i + 1}, "model": f"{NS}:item/{item}_{c}"}
                          for i, c in enumerate(CORPS)],
        })
        for c in CORPS:
            write(f"assets/{NS}/models/item/{item}_{c}.json", {
                "parent": f"{NS}:item/{item}_base",
                "textures": {"0": f"{NS}:item/construct/{c}", "particle": f"{NS}:item/construct/{c}"}})
    items += [f"construct_{shape}" for shape in SHAPES]

    # Held constructs: real weapons and tools, colored per corps by CustomModelData.
    def colored(item, display, base_name):
        write(f"assets/{NS}/models/item/{base_name}.json", {
            "render_type": "minecraft:translucent", "gui_light": "front",
            "textures": {"0": f"{NS}:item/construct/green", "particle": f"{NS}:item/construct/green"},
            "elements": elements, "display": display})
        for c in CORPS:
            write(f"assets/{NS}/models/item/{base_name}_{c}.json", {
                "parent": f"{NS}:item/{base_name}",
                "textures": {"0": f"{NS}:item/construct/{c}", "particle": f"{NS}:item/construct/{c}"}})

    for item, (elements, display) in art.held_construct_models().items():
        spec, name = constructs.HELD_ITEMS[item]
        write(f"addon/{NS}/items/{item}.json", {**spec, "max_stack_size": 1, "is_fire_resistant": True,
                                               "tooltip": [{"translate": f"tooltip.{NS}.construct", "color": "gray"}]})
        lang[f"item.{NS}.{item}"] = name
        colored(item, display, f"{item}_base")
        overrides = []
        if item == "construct_shield":
            colored(item, art.SHIELD_BLOCKING_DISPLAY, f"{item}_blocking")
            overrides.append({"predicate": {"blocking": 1}, "model": f"{NS}:item/{item}_blocking"})
        for i, c in enumerate(CORPS):
            overrides.append({"predicate": {"custom_model_data": i + 1}, "model": f"{NS}:item/{item}_base_{c}"})
            if item == "construct_shield":
                overrides.append({"predicate": {"custom_model_data": i + 1, "blocking": 1},
                                  "model": f"{NS}:item/{item}_blocking_{c}"})
        write(f"assets/{NS}/models/item/{item}.json", {"parent": f"{NS}:item/{item}_base", "overrides": overrides})
        items.append(item)
    lang[f"tooltip.{NS}.construct"] = "Hard light: dissolves without its ring"
    held = [f"{NS}:{item}" for item in constructs.HELD_ITEMS]
    write(f"data/{NS}/tags/items/held_constructs.json", {"replace": False, "values": held})
    write(f"data/{NS}/tags/items/constructs.json", {"replace": False, "values": held + [
        f"{NS}:{c}_construct_block" for c in CORPS]})
    write(f"data/{NS}/tags/blocks/hardlight.json", {"replace": False, "values": [f"{NS}:{c}_hardlight" for c in CORPS]})
    write(f"data/{NS}/tags/blocks/empty.json", {"replace": False, "values": ["minecraft:air", "minecraft:cave_air"]})
    write(f"data/{NS}/tags/entity_types/not_creatures.json", {"replace": False, "values": [
        t if t.startswith("minecraft:") else {"id": t, "required": False} for t in constructs.NOT_CREATURES]})

    # Datapack: grows new constructs in and removes them when their time is up.
    tick = ["# Generated by tools/gen_corps.py"]
    for shape in constructs.GROWING:
        cfg = SHAPES[shape]
        sel = f"@e[type=minecraft:item_display,tag=gl_new,tag=gl_{shape}]"
        sc = f"{cfg['scale']}f"
        tick += [
            f"scoreboard players set {sel} gl_life {cfg['life']}",
            f"execute as {sel} run data merge entity @s {{start_interpolation:0,interpolation_duration:5,"
            f"transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],"
            f"scale:[{sc},{sc},{sc}]}}}}",
        ]
    tick += [
        "tag @e[type=minecraft:item_display,tag=gl_new] remove gl_new",
        # (a new train gets its life later in this tick, from constructs.py)
        "scoreboard players remove @e[type=minecraft:item_display,tag=gl_construct,tag=!gl_train_new] gl_life 1",
        "kill @e[type=minecraft:item_display,tag=gl_construct,tag=!gl_train_new,scores={gl_life=..0}]",
    ]
    (SRC / f"data/{NS}/functions").mkdir(parents=True, exist_ok=True)
    write(f"data/{NS}/palladium/powers/lantern_base.json", base_power())
    lang[f"power.{NS}.lantern_base"] = "Lantern Ring"
    g_load, g_tick, g_functions = army_functions()
    c_fns, c_load = charge_functions()
    g_functions.update(c_fns)
    g_load += c_load
    g_tick += sense_tags()
    for c in CORPS:  # a corps tag lasts while that ring's power keeps refreshing it
        g_load.append(f"scoreboard objectives add gl_t_{c} dummy")
        g_tick += [f"scoreboard players add @a[tag=gl_{c}] gl_t_{c} 0",
                   f"scoreboard players remove @a[scores={{gl_t_{c}=1..}}] gl_t_{c} 1",
                   f"tag @a[tag=gl_{c},scores={{gl_t_{c}=..0}}] remove gl_{c}"]
    # gl_ring: wearing any ring
    g_tick += ["tag @a[tag=gl_ring] remove gl_ring"] + [f"tag @a[tag=gl_{c}] add gl_ring" for c in CORPS]
    for a, b in fusion_pairs():
        g_functions[f"fusion/{a}_{b}"] = fusion_function(a, b)
    s_load, s_tick, s_functions = systems.generate(CORPS, write, write_text)
    g_load += s_load
    g_tick += s_tick
    g_functions.update(s_functions)
    g_functions["second"].append(f"function {NS}:charge/save")
    b_load, b_tick, b_second = benefit_ticks()
    g_load += b_load
    g_tick += b_tick
    g_functions["second"] += b_second
    write(f"data/{NS}/tags/entity_types/pets.json", {"replace": False, "values": [
        f"minecraft:{m}" for m in ("wolf", "cat", "parrot", "horse", "donkey", "mule", "llama", "allay", "fox", "axolotl")]})
    k_load, k_tick, k_second, k_functions, k_files = constructs.generate(CORPS)
    for path, data in k_files.items():
        write(f"data/{NS}/{path}", data)
    g_load += k_load
    g_tick += k_tick
    g_functions["second"] += k_second
    g_functions.update(k_functions)
    tick += g_tick
    for path, lines in g_functions.items():
        (SRC / f"data/{NS}/functions/{path}.mcfunction").parent.mkdir(parents=True, exist_ok=True)
        (SRC / f"data/{NS}/functions/{path}.mcfunction").write_text("\n".join(lines) + "\n")
    (SRC / f"data/{NS}/functions/tick.mcfunction").write_text("\n".join(tick) + "\n")
    (SRC / f"data/{NS}/functions/load.mcfunction").write_text(
        "\n".join(["scoreboard objectives add gl_life dummy"] + g_load) + "\n")
    write(f"data/{NS}/tags/entity_types/greed_prey.json",
          {"replace": False, "values": [f"minecraft:{m}" for m in GREED_PREY]})
    write("data/minecraft/tags/functions/tick.json", {"values": [f"{NS}:tick"]})
    write("data/minecraft/tags/functions/load.json", {"values": [f"{NS}:load"]})
    save(art.rage_overlay(), f"assets/{NS}/textures/gui/rage_overlay.png")

    write(f"assets/{NS}/lang/en_us.json", lang)
    save(art.logo_texture([CORPS[c]["color"] for c in SPECTRUM]), "pack.png")
    print(f"Generated {len(CORPS)} corps")


if __name__ == "__main__":
    main()
