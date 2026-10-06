"""Generates every Lantern Corps in the pack from the CORPS table below.

    python3 tools/gen_corps.py   # writes the generated files into src/
    python3 tools/build.py       # validates and packages the jar

Each corps gets: a ring, a power battery, a power (shared kit + its own
specials), a uniform (suit + glow textures), a beam, a flight trail,
recipes, translations and item/ring/battery textures.

To tweak a corps, edit its entry in CORPS (or its specials function) and
re-run this script. Hand-written files elsewhere in src/ are left alone.
"""
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
NS = "greenlantern"
BAR = "ring_charge"

# --- corps table ------------------------------------------------------------------

CORPS = {
    "green": {
        "name": "Green Lantern", "emotion": "Willpower", "color": (46, 200, 70),
        "ring_gem": "minecraft:emerald_block", "glass": "minecraft:lime_stained_glass",
        "emblem": ["BWWWWWWB", "BBWBBWBB", "BWBBBBWB", "BBWBBWBB", "BWWWWWWB"],
        "oath": [
            "In brightest day, in blackest night,",
            "No evil shall escape my sight.",
            "Let those who worship evil's might,",
            "Beware my power... Green Lantern's light!",
        ],
    },
    "yellow": {
        "name": "Sinestro Corps", "emotion": "Fear", "color": (245, 210, 40),
        "ring_gem": "minecraft:gold_block", "glass": "minecraft:yellow_stained_glass",
        "emblem": ["BBBWWBBB", "BBWBBWBB", "BWBWWBWB", "BBWBBWBB", "BBBWWBBB"],
        "oath": [
            "In blackest day, in brightest night,",
            "Beware your fears made into light.",
            "Let those who try to stop what's right,",
            "Burn like my power... Sinestro's might!",
        ],
    },
    "red": {
        "name": "Red Lantern", "emotion": "Rage", "color": (215, 30, 35),
        "ring_gem": "minecraft:redstone_block", "glass": "minecraft:red_stained_glass",
        "emblem": ["BWWWWWWB", "BWBBBBWB", "BWBBBBWB", "BWWWWWWB", "BWBWBBWB"],
        "oath": [
            "With blood and rage of crimson red,",
            "Ripped from a corpse so freshly dead,",
            "Together with our hellish hate,",
            "We'll burn you all... that is your fate!",
        ],
    },
    "orange": {
        "name": "Orange Lantern", "emotion": "Avarice", "color": (250, 135, 25),
        "ring_gem": "minecraft:raw_gold_block", "glass": "minecraft:orange_stained_glass",
        "emblem": ["WWBBBBWW", "BWWWWWWB", "BWBBBBWB", "BWWWWWWB", "WWBBBBWW"],
        "oath": [
            "What's mine is mine,",
            "and mine,",
            "and mine...",
            "and mine! And not yours!",
        ],
    },
    "blue": {
        "name": "Blue Lantern", "emotion": "Hope", "color": (60, 150, 255),
        "ring_gem": "minecraft:diamond_block", "glass": "minecraft:light_blue_stained_glass",
        "emblem": ["WBBWWBBW", "BWWBBWWB", "BBWBBWBB", "BWWBBWWB", "WBBWWBBW"],
        "oath": [
            "In fearful day, in raging night,",
            "With strong hearts full, our souls ignite,",
            "When all seems lost in the War of Light,",
            "Look to the stars... for hope burns bright!",
        ],
    },
    "indigo": {
        "name": "Indigo Tribe", "emotion": "Compassion", "color": (90, 40, 200),
        "ring_gem": "minecraft:lapis_block", "glass": "minecraft:blue_stained_glass",
        "emblem": ["BBBWWBBB", "BWWWWWWB", "BWBWWBWB", "BWWWWWWB", "BBBWWBBB"],
        "oath": [
            "Tor lowar lan, Abin Sur,",
            "Ak wo tauva, Ihla wo nauva,",
            "Natromo faan, Dur ak naja,",
            "Ono ot vauva, Abin Sur.",
        ],
    },
    "violet": {
        "name": "Star Sapphire", "emotion": "Love", "color": (200, 60, 210),
        "ring_gem": "minecraft:amethyst_block", "glass": "minecraft:magenta_stained_glass",
        "emblem": ["BBBWWBBB", "BBWWWWBB", "BWWBBWWB", "BBWWWWBB", "BBBWWBBB"],
        "oath": [
            "For hearts long lost and full of fright,",
            "For those alone in blackest night,",
            "Accept our ring and join our fight,",
            "Love conquers all... with violet light!",
        ],
    },
    "white": {
        "name": "White Lantern", "emotion": "Life", "color": (235, 240, 245),
        "ring_gem": None,  # crafted from all seven rings, see recipes()
        "glass": "minecraft:white_stained_glass",
        "emblem": ["WBWWWWBW", "BBWBBWBB", "WWBBBBWW", "BBWBBWBB", "WBWWWWBW"],
        "oath": [
            "From the light of creation,",
            "every color of the spectrum,",
            "all life, as one,",
            "...shines White!",
        ],
    },
}

# --- small helpers ----------------------------------------------------------------

OTHERS = "@e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..{r}]"
NEAREST = OTHERS[:-1] + ",limit=1,sort=nearest]"
ALLIES = "@a[distance=..{r}]"

UNIFORM = {"type": "palladium:ability_enabled", "ability": "uniform"}


def hexcolor(rgb):
    return "#%02X%02X%02X" % rgb


def dust(rgb, size=1.0):
    return "%.2f %.2f %.2f %.1f" % (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, size)


def charge(amount):
    return {"type": "palladium:energy_bar", "energy_bar": BAR, "min": amount}


def unlock(cost=0, *extra):
    conds = [UNIFORM, *extra]
    if cost:
        conds.append(charge(cost))
    return conds if len(conds) > 1 else conds[0]


def usage(amount):
    return {"energy_bar": BAR, "amount": amount}


def enabled(ability):
    return {"type": "palladium:ability_enabled", "ability": ability}


def text(key):
    return {"translate": key}


class Kit:
    """Collects a power's abilities and their translations."""

    def __init__(self, corps):
        self.corps = corps
        self.abilities = {}
        self.lang = {}

    def add(self, key, ability, name=None, desc=None, shared=True, icon=None, index=None):
        """Adds an ability. name/desc are English strings; shared keys are reused by every corps."""
        lang_key = f"ability.{NS}.{key}" if shared else f"ability.{NS}.{self.corps}.{key}"
        if name:
            ability = {"title": text(lang_key), **ability}
            self.lang[lang_key] = name
        if desc:
            ability = {**ability, "description": text(lang_key + ".description")}
            self.lang[lang_key + ".description"] = desc
        if icon:
            ability["icon"] = icon
        if index is not None:
            ability["list_index"] = index
        self.abilities[key] = ability
        return ability

    def hidden(self, key, ability):
        self.abilities[key] = {**ability, "hidden": True, "hidden_in_bar": True}


def command(first=(), last=(), every=()):
    a = {"type": "palladium:command"}
    if first:
        a["first_tick_commands"] = list(first)
    if every:
        a["commands"] = list(every)
    if last:
        a["last_tick_commands"] = list(last)
    return a


def action(cooldown):
    return {"type": "palladium:action", "cooldown": cooldown}


def toggle():
    return {"type": "palladium:toggle"}


def burst(rgb, size=2.0, spread="1 1 1", count=80, at="~ ~1 ~"):
    return f"particle minecraft:dust {dust(rgb, size)} {at} {spread} 0 {count} force"


def sound(snd, pitch=1.0):
    return f"playsound {snd} player @a[distance=..24] ~ ~ ~ 1 {pitch}"


def pulse(kit, key, source, every_ticks, commands):
    """A hidden ability that runs commands every N ticks while `source` is enabled."""
    kit.hidden(key, {
        **command(first=commands),
        "conditions": {"enabling": [
            enabled(source),
            {"type": "palladium:interval", "active_ticks": 1, "disabled_ticks": every_ticks - 1},
        ]},
    })


def ultimate(kit, key, name, desc, icon, commands, cost=600, cooldown=1200, index=9):
    kit.add(key, {
        **command(first=commands),
        "bar_color": "white",
        "energy_bar_usage": usage(cost),
        "conditions": {"unlocking": unlock(cost), "enabling": action(cooldown)},
    }, name, desc, shared=False, icon=icon, index=index)


# --- the kit every corps shares -----------------------------------------------------

def shared_kit(kit, c, data):
    rgb = data["color"]
    emotion = data["emotion"]

    kit.add("uniform", {
        "type": "palladium:dummy", "bar_color": "white",
        "conditions": {"enabling": {**toggle(), "cooldown": 20}},
    }, "Suit Up", "Let the ring clothe you in your corps' uniform. The ring's other powers only work while suited up.",
        icon=f"{NS}:{c}_lantern_ring", index=0)
    kit.hidden("suit_up_burst", {
        **command(first=[
            burst(rgb, 2.0, "0.4 1.0 0.4", 120),
            "particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force",
            sound("minecraft:block.beacon.activate", 1.4),
        ]),
        "conditions": {"enabling": UNIFORM},
    })
    for layer in ("uniform", "uniform_glow"):
        kit.hidden(f"{layer}_layer", {
            "type": "palladium:render_layer", "render_layer": f"{NS}:{c}_{layer}",
            "conditions": {"enabling": UNIFORM},
        })
    kit.hidden("ring_aura", {
        "type": "palladium:particles", "emitter": [f"{NS}:ring_hand"],
        "particle_type": "minecraft:dust", "options": dust(rgb, 0.8),
        "conditions": {"enabling": [UNIFORM, {"type": "palladium:interval", "active_ticks": 1, "disabled_ticks": 3}]},
    })

    # passives while suited up
    kit.add("ring_protection", {
        "type": "palladium:damage_immunity", "hidden_in_bar": True,
        "damage_sources": ["minecraft:is_drowning", "minecraft:is_fall", "minecraft:is_freezing"],
        "conditions": {"unlocking": UNIFORM},
    }, "Ring Protection", "The ring's life support keeps you safe from drowning, freezing and falling.",
        icon="minecraft:turtle_helmet")
    for key, attr, amount, uuid_tail in (
        ("construct_armor", "minecraft:generic.armor", 8, "0a11"),
        ("construct_toughness", "minecraft:generic.armor_toughness", 4, "0a22"),
    ):
        kit.hidden(key, {
            "type": "palladium:attribute_modifier", "attribute": attr, "amount": amount, "operation": 0,
            "uuid": uuid(c, uuid_tail), "conditions": {"unlocking": UNIFORM},
        })
    kit.add("construct_fists", {
        "type": "palladium:attribute_modifier", "hidden_in_bar": True,
        "attribute": "palladium:punch_damage", "amount": 5, "operation": 0, "uuid": uuid(c, "0a33"),
        "conditions": {"unlocking": UNIFORM},
    }, "Construct Fists", "Hard-light armor protects you and your punches hit much harder.", icon="minecraft:iron_ingot")

    # flight
    kit.add("flight", {
        "type": "palladium:attribute_modifier", "hidden_in_bar": True,
        "attribute": "palladium:flight_speed", "amount": 1.0, "operation": 0, "uuid": uuid(c, "0b11"),
        "conditions": {"unlocking": unlock(1)},
    }, "Flight", "Fly on the power of the ring, leaving a trail of light. Flying slowly drains the ring.",
        icon="minecraft:feather")
    for key, attr, amount, tail in (
        ("flight_flexibility", "palladium:flight_flexibility", 5, "0b22"),
        ("heroic_flight", "palladium:heroic_flight_type", 1, "0b33"),
    ):
        kit.hidden(key, {
            "type": "palladium:attribute_modifier", "attribute": attr, "amount": amount, "operation": 0,
            "uuid": uuid(c, tail), "conditions": {"unlocking": {"type": "palladium:ability_unlocked", "ability": "flight"}},
        })
    flying = [{"type": "palladium:ability_unlocked", "ability": "flight"}, {"type": "palladium:is_flying"}]
    kit.hidden("flight_trail", {"type": "palladium:trail", "trail": f"{NS}:{c}_trail", "conditions": {"enabling": flying}})
    kit.hidden("flight_aura", {
        "type": "palladium:particles", "emitter": [f"{NS}:flight_aura"],
        "particle_type": "minecraft:dust", "options": dust(rgb, 1.2),
        "conditions": {"enabling": flying},
    })
    kit.hidden("flight_drain", {
        "type": "palladium:dummy", "energy_bar_usage": usage(1),
        "conditions": {"enabling": [
            {"type": "palladium:is_hovering_or_flying"},
            {"type": "palladium:interval", "active_ticks": 1, "disabled_ticks": 4},
        ]},
    })

    # beam
    kit.add("beam", {
        "type": "palladium:energy_beam", "bar_color": "white",
        "energy_beam": f"{NS}:{c}_beam", "damage": 2.0, "max_distance": 40.0, "speed": 0.6,
        "energy_bar_usage": usage(3),
        "conditions": {"unlocking": unlock(3), "enabling": {"type": "palladium:held"}},
    }, f"{emotion} Beam", "Hold to fire a continuous beam from your ring.", shared=False, icon="minecraft:blaze_rod", index=1)
    kit.hidden("beam_sound", {
        "type": "palladium:play_sound", "sound": "minecraft:block.beacon.ambient", "pitch": 1.6, "looping": True,
        "conditions": {"enabling": enabled("beam")},
    })

    # construct wheel
    constructs = ["construct_blast", "construct_fist", "construct_cage", "construct_slam"]
    kit.add("constructs", {
        "type": "palladium:ability_wheel", "bar_color": "white", "abilities": constructs,
        "conditions": {"unlocking": UNIFORM, "enabling": {"type": "palladium:held"}},
    }, "Constructs", "Hold to open the construct wheel, then pick a construct to create.",
        icon="minecraft:emerald", index=2)
    wheel = {"type": "palladium:ability_wheel"}
    kit.add("construct_blast", {
        "type": "palladium:projectile", "hidden_in_bar": True,
        "entity_type": "palladium:custom_projectile", "velocity": 2.5, "inaccuracy": 0.0,
        "entity_data": {
            "Damage": 8, "Gravity": 0.0, "Size": 0.4, "Lifetime": 100,
            "DieOnEntityHit": True, "DieOnBlockHit": True,
            "Appearances": [
                {"Type": "laser", "Thickness": 0.15, "Color": hexcolor(rgb)},
                {"Type": "particles", "ParticleType": "minecraft:end_rod", "Spread": 0.3},
            ],
        },
        "energy_bar_usage": usage(40),
        "conditions": {"unlocking": unlock(40), "enabling": {**wheel, "cooldown": 15}},
    }, "Construct: Blast", "Fire a fast bolt of hard light. Costs 40.", icon="minecraft:arrow")
    kit.hidden("construct_blast_sound", {
        "type": "palladium:play_sound", "sound": "minecraft:entity.firework_rocket.blast", "pitch": 1.5,
        "conditions": {"enabling": enabled("construct_blast")},
    })
    front = "execute anchored eyes positioned ^ ^ ^3"
    # everything near the point 3 blocks ahead (you stand ~3 blocks away, so you're never hit)
    hit = "@e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=..2.5]"
    kit.add("construct_fist", {
        **command(first=[
            f"{front} run {burst(rgb, 2.5, '0.8 0.8 0.8', 60, '~ ~ ~')}",
            f"{front} as {hit} run damage @s 10 minecraft:player_attack",
            f"{front} as {hit} run effect give @s minecraft:levitation 1 3 true",
            sound("minecraft:entity.iron_golem.attack", 0.6),
        ]),
        "hidden_in_bar": True, "energy_bar_usage": usage(100),
        "conditions": {"unlocking": unlock(100), "enabling": {**wheel, "cooldown": 60}},
    }, "Construct: Giant Fist", "Slam everything in front of you with a giant fist, launching it. Costs 100.",
        icon="minecraft:iron_block")
    target = NEAREST.format(r=12)
    kit.add("construct_cage", {
        **command(first=[
            f"execute as {target} at @s run {burst(rgb, 2.0, '0.6 1.0 0.6', 120, '~ ~1 ~')}",
            f"effect give {target} minecraft:slowness 6 6 true",
            f"effect give {target} minecraft:weakness 6 2 true",
            f"effect give {target} minecraft:glowing 6 0 true",
            sound("minecraft:block.amethyst_block.resonate", 0.8),
        ]),
        "hidden_in_bar": True, "energy_bar_usage": usage(150),
        "conditions": {"unlocking": unlock(150), "enabling": {**wheel, "cooldown": 100}},
    }, "Construct: Cage", "Trap the nearest creature within 12 blocks, slowing and weakening it. Costs 150.",
        icon="minecraft:iron_bars")
    around = OTHERS.format(r=6)
    kit.add("construct_slam", {
        **command(first=[
            burst(rgb, 2.5, "3 0.2 3", 200, "~ ~0.2 ~"),
            f"execute as {around} run damage @s 6 minecraft:player_attack",
            f"effect give {around} minecraft:levitation 1 5 true",
            sound("minecraft:entity.generic.explode", 1.2),
        ]),
        "hidden_in_bar": True, "energy_bar_usage": usage(120),
        "conditions": {"unlocking": unlock(120), "enabling": {**wheel, "cooldown": 80}},
    }, "Construct: Hammer Slam", "Smash the ground with a giant hammer, hurting and launching everything within 6 blocks. Costs 120.",
        icon="minecraft:anvil")

    # defence + utility
    kit.add("force_field", {
        "type": "palladium:damage_immunity", "bar_color": "white",
        "damage_sources": ["minecraft:is_projectile", "minecraft:is_explosion", "minecraft:is_fire"],
        "energy_bar_usage": usage(2),
        "conditions": {"unlocking": unlock(2), "enabling": toggle()},
    }, "Force Field", "Toggle a bubble that blocks projectiles, explosions and fire. Drains the ring while active.",
        icon="minecraft:shield", index=3)
    kit.hidden("force_field_glow", {
        "type": "palladium:entity_glow", "mode": "self", "color": hexcolor(rgb),
        "conditions": {"enabling": enabled("force_field")},
    })
    kit.add("ring_light", {
        **command(first=["effect give @s minecraft:night_vision infinite 0 true"],
                  last=["effect clear @s minecraft:night_vision"]),
        "bar_color": "white",
        "conditions": {"unlocking": UNIFORM, "enabling": toggle()},
    }, "Ring Light", "Toggle the ring's glow to see in the dark.", icon="minecraft:glowstone_dust", index=4)

    # recharging at your battery
    battery = f"{NS}:{c}_power_battery"
    kit.add("recharge", {
        "type": "palladium:dummy", "bar_color": "white", "energy_bar_usage": usage(-10),
        "conditions": {
            "unlocking": {"type": "palladium:item_in_slot", "item": {"item": battery}, "slot": "mainhand"},
            "enabling": {"type": "palladium:held"},
        },
    }, "Recharge", "Hold your corps' Power Battery in your main hand, then hold this to recite the oath and recharge.",
        icon=battery, index=5)
    oath = [f"tellraw @a[distance=..24] " + json.dumps(
        [{"selector": "@s", "color": hexcolor(rgb)}, {"text": ": ", "color": "gray"},
         {"translate": f"oath.{NS}.{c}.1", "color": hexcolor(rgb), "italic": True}], separators=(",", ":"))]
    for i in (2, 3, 4):
        oath.append("tellraw @a[distance=..24] " + json.dumps(
            [{"text": "   "}, {"translate": f"oath.{NS}.{c}.{i}", "color": hexcolor(rgb), "italic": True}],
            separators=(",", ":")))
    for i, line in enumerate(data["oath"], 1):
        kit.lang[f"oath.{NS}.{c}.{i}"] = line
    kit.hidden("oath", {**command(first=oath + [sound("minecraft:block.beacon.power_select", 1.2)]),
                        "conditions": {"enabling": enabled("recharge")}})
    kit.hidden("recharge_sound", {
        "type": "palladium:play_sound", "sound": "minecraft:block.conduit.ambient", "pitch": 1.2, "looping": True,
        "conditions": {"enabling": enabled("recharge")},
    })


def uuid(corps, tail):
    """Stable, unique attribute modifier UUIDs per corps."""
    n = list(CORPS).index(corps)
    return f"6c7a{n:04x}-1a2b-4c3d-8e4f-5a6b7c8d{tail}"


# --- what makes each corps different ------------------------------------------------

def roar(kit, rgb, extra=()):
    around = OTHERS.format(r=7)
    kit.add("roar", {
        **command(first=[
            burst(rgb, 2.0, "2 1 2", 150),
            f"effect give {around} minecraft:levitation 1 2 true",
            f"effect give {around} minecraft:weakness 4 1 true",
            *extra,
            sound("minecraft:entity.ender_dragon.growl", 1.5),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(120),
        "conditions": {"unlocking": unlock(120), "enabling": action(200)},
    }, "Roar", "Let out a roar of raw emotion, knocking back and weakening everything within 7 blocks. Costs 120.",
        icon="minecraft:goat_horn", index=6)


def specials_green(kit, rgb):
    roar(kit, rgb)
    around = OTHERS.format(r=8)
    ultimate(kit, "emerald_nova", "Emerald Nova",
             "Ultimate: unleash all of your willpower in a blast that hurts and launches everything within 8 blocks. Costs 600.",
             "minecraft:emerald_block", [
                 burst(rgb, 3.0, "4 2 4", 400),
                 "particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force",
                 f"execute as {around} run damage @s 16 minecraft:player_attack",
                 f"effect give {around} minecraft:levitation 2 4 true",
                 sound("minecraft:entity.generic.explode", 0.7),
             ])


def specials_red(kit, rgb):
    kit.add("napalm", {
        "type": "palladium:energy_beam", "bar_color": "white", "energy_beam": f"{NS}:red_napalm",
        "damage": 3.0, "max_distance": 16.0, "speed": 0.8, "set_on_fire_seconds": 5,
        "energy_bar_usage": usage(4),
        "conditions": {"unlocking": unlock(4), "enabling": {"type": "palladium:held"}},
    }, "Napalm", "Hold to spew burning blood plasma that sets your targets on fire.", shared=False,
        icon="minecraft:fire_charge", index=7)
    kit.add("rage", {
        **command(first=["effect give @s minecraft:strength infinite 1 true", "effect give @s minecraft:speed infinite 0 true",
                         sound("minecraft:entity.ravager.roar", 0.8)],
                  last=["effect clear @s minecraft:strength", "effect clear @s minecraft:speed"]),
        "bar_color": "white", "energy_bar_usage": usage(2),
        "conditions": {"unlocking": unlock(2), "enabling": toggle()},
    }, "Rage", "Toggle: give in to your rage for Strength II and Speed. Drains the ring while active.", shared=False,
        icon="minecraft:redstone", index=8)
    roar(kit, rgb, [f"effect give {OTHERS.format(r=7)} minecraft:slowness 4 1 true"])
    around = OTHERS.format(r=8)
    ultimate(kit, "blood_rage", "Blood Rage",
             "Ultimate: a storm of burning rage that hurts, withers and ignites everything within 8 blocks. Costs 600.",
             "minecraft:nether_wart", [
                 burst(rgb, 3.0, "4 2 4", 400),
                 f"execute as {around} run damage @s 14 minecraft:player_attack",
                 f"effect give {around} minecraft:wither 6 1 true",
                 f"execute at {around} run particle minecraft:flame ~ ~1 ~ 0.3 0.6 0.3 0.02 30 force",
                 f"execute as {around} run data merge entity @s {{Fire:120s}}",
                 sound("minecraft:entity.blaze.shoot", 0.6),
             ])


def specials_orange(kit, rgb):
    kit.add("avarice", {
        "type": "palladium:attribute_modifier", "hidden_in_bar": True,
        "attribute": "palladium:destroy_speed", "amount": 1.0, "operation": 0, "uuid": uuid("orange", "0c11"),
        "conditions": {"unlocking": UNIFORM},
    }, "Avarice", "Your greed drives you: you mine much faster while suited up.", shared=False,
        icon="minecraft:golden_pickaxe")
    kit.add("hoard", {
        **command(first=[
            "tp @e[type=minecraft:item,distance=..16] @s",
            "tp @e[type=minecraft:experience_orb,distance=..16] @s",
            burst(rgb, 1.5, "2 1 2", 80),
            sound("minecraft:entity.item.pickup", 0.6),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(50),
        "conditions": {"unlocking": unlock(50), "enabling": action(40)},
    }, "Hoard", "MINE! Pull every item and experience orb within 16 blocks to you. Costs 50.", shared=False,
        icon="minecraft:chest", index=6)
    target = NEAREST.format(r=10)
    kit.add("life_drain", {
        **command(first=[
            f"execute as {target} at @s run {burst(rgb, 1.5, '0.4 0.8 0.4', 60, '~ ~1 ~')}",
            f"execute as {target} run damage @s 8 minecraft:magic",
            "effect give @s minecraft:instant_health 1 0 true",
            "effect give @s minecraft:regeneration 5 1 true",
            sound("minecraft:entity.evoker.prepare_attack", 1.2),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(120),
        "conditions": {"unlocking": unlock(120), "enabling": action(100)},
    }, "Life Drain", "Steal the life of the nearest creature within 10 blocks to heal yourself. Costs 120.", shared=False,
        icon="minecraft:ghast_tear", index=7)
    around = OTHERS.format(r=8)
    ultimate(kit, "consume", "Consume",
             "Ultimate: devour the life of everything within 8 blocks and keep it as extra hearts. Costs 600.",
             "minecraft:enchanted_golden_apple", [
                 burst(rgb, 3.0, "4 2 4", 400),
                 f"execute as {around} run damage @s 10 minecraft:magic",
                 f"effect give {around} minecraft:wither 5 1 true",
                 "effect give @s minecraft:absorption 30 3 true",
                 sound("minecraft:entity.wither.ambient", 1.4),
             ])


def specials_yellow(kit, rgb):
    around = OTHERS.format(r=10)
    kit.add("inflict_fear", {
        **command(first=[
            burst(rgb, 2.0, "3 1 3", 150),
            f"execute at {around} run particle minecraft:squid_ink ~ ~1 ~ 0.3 0.5 0.3 0.02 20 force",
            f"effect give {around} minecraft:darkness 6 0 true",
            f"effect give {around} minecraft:slowness 6 1 true",
            f"effect give {around} minecraft:weakness 6 1 true",
            sound("minecraft:ambient.cave", 0.8),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(120),
        "conditions": {"unlocking": unlock(120), "enabling": action(200)},
    }, "Inflict Fear", "Fill everything within 10 blocks with terror: darkness, slowness and weakness. Costs 120.",
        shared=False, icon="minecraft:wither_skeleton_skull", index=6)
    target = NEAREST.format(r=12)
    kit.add("nightmare", {
        **command(first=[
            f"execute as {target} at @s run particle minecraft:sculk_soul ~ ~1 ~ 0.3 0.6 0.3 0.02 30 force",
            f"effect give {target} minecraft:nausea 10 0 true",
            f"effect give {target} minecraft:blindness 6 0 true",
            f"effect give {target} minecraft:mining_fatigue 10 2 true",
            sound("minecraft:entity.warden.heartbeat", 1.0),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(100),
        "conditions": {"unlocking": unlock(100), "enabling": action(120)},
    }, "Nightmare", "Show the nearest creature within 12 blocks its worst fear: blinded, dizzy and sluggish. Costs 100.",
        shared=False, icon="minecraft:phantom_membrane", index=7)
    around = OTHERS.format(r=12)
    ultimate(kit, "fear_incarnate", "Fear Incarnate",
             "Ultimate: become terror itself, crippling everything within 12 blocks for 15 seconds. Costs 600.",
             "minecraft:sculk_shrieker", [
                 burst(rgb, 3.0, "5 2 5", 400),
                 f"effect give {around} minecraft:darkness 15 0 true",
                 f"effect give {around} minecraft:slowness 15 3 true",
                 f"effect give {around} minecraft:weakness 15 2 true",
                 f"effect give {around} minecraft:nausea 15 0 true",
                 sound("minecraft:entity.warden.roar", 1.0),
             ])


def specials_blue(kit, rgb):
    kit.add("hope_aura", {
        "type": "palladium:dummy", "bar_color": "white", "energy_bar_usage": usage(1),
        "conditions": {"unlocking": unlock(1), "enabling": toggle()},
    }, "Aura of Hope", "Toggle: you and every player within 8 blocks slowly regenerate health. Drains the ring.",
        shared=False, icon="minecraft:light_blue_dye", index=6)
    pulse(kit, "hope_aura_pulse", "hope_aura", 40, [
        f"effect give {ALLIES.format(r=8)} minecraft:regeneration 3 0 true",
        burst(rgb, 1.2, "3 1 3", 30),
    ])
    kit.add("rekindle", {
        **command(first=[
            burst(rgb, 2.0, "3 1 3", 150),
            f"effect give {ALLIES.format(r=12)} minecraft:instant_health 1 1 true",
            f"effect give {ALLIES.format(r=12)} minecraft:absorption 60 1 true",
            sound("minecraft:block.beacon.power_select", 1.6),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(300),
        "conditions": {"unlocking": unlock(300), "enabling": action(600)},
    }, "Rekindle", "Restore hope to every player within 12 blocks: instant healing and extra hearts. Costs 300.",
        shared=False, icon="minecraft:golden_apple", index=7)
    ultimate(kit, "hope_burns_bright", "Hope Burns Bright",
             "Ultimate: every player within 16 blocks is healed and gains Regeneration and Resistance for 20 seconds. Costs 600.",
             "minecraft:beacon", [
                 burst(rgb, 3.0, "5 2 5", 400),
                 f"effect give {ALLIES.format(r=16)} minecraft:instant_health 1 2 true",
                 f"effect give {ALLIES.format(r=16)} minecraft:regeneration 20 2 true",
                 f"effect give {ALLIES.format(r=16)} minecraft:resistance 20 1 true",
                 sound("minecraft:ui.toast.challenge_complete", 1.2),
             ])


def specials_indigo(kit, rgb):
    kit.add("phase", {
        "type": "palladium:projectile", "bar_color": "white",
        "entity_type": "minecraft:ender_pearl", "velocity": 2.5, "inaccuracy": 0.0,
        "energy_bar_usage": usage(80),
        "conditions": {"unlocking": unlock(80), "enabling": action(40)},
    }, "Phase", "Throw a bolt of indigo light and teleport to wherever it lands. Costs 80.", shared=False,
        icon="minecraft:ender_pearl", index=6)
    target = NEAREST.format(r=12)
    kit.add("compassion", {
        **command(first=[
            f"execute as {target} at @s run {burst(rgb, 1.5, '0.4 0.8 0.4', 60, '~ ~1 ~')}",
            f"effect give {target} minecraft:weakness 10 254 true",
            f"effect give {target} minecraft:slowness 10 1 true",
            sound("minecraft:block.amethyst_block.chime", 0.7),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(150),
        "conditions": {"unlocking": unlock(150), "enabling": action(200)},
    }, "Compassion", "Make the nearest creature within 12 blocks feel the pain it causes. It can barely fight for 10 seconds. Costs 150.",
        shared=False, icon="minecraft:blue_orchid", index=7)
    kit.add("healing_touch", {
        **command(first=[
            f"effect give {ALLIES.format(r=6)} minecraft:instant_health 1 0 true",
            burst(rgb, 1.2, "2 1 2", 60),
            sound("minecraft:block.amethyst_block.chime", 1.4),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(100),
        "conditions": {"unlocking": unlock(100), "enabling": action(100)},
    }, "Healing Touch", "Heal every player within 6 blocks. Costs 100.", shared=False, icon="minecraft:glistering_melon_slice",
        index=8)
    around = OTHERS.format(r=12)
    ultimate(kit, "staff_of_compassion", "Staff of Compassion",
             "Ultimate: everything within 12 blocks is overwhelmed by empathy and can barely fight for 15 seconds. Costs 600.",
             "minecraft:end_rod", [
                 burst(rgb, 3.0, "5 2 5", 400),
                 f"effect give {around} minecraft:weakness 15 254 true",
                 f"effect give {around} minecraft:slowness 15 2 true",
                 f"effect give {around} minecraft:nausea 10 0 true",
                 sound("minecraft:block.beacon.deactivate", 0.8),
             ])


def specials_violet(kit, rgb):
    target = NEAREST.format(r=12)
    kit.add("crystal_prison", {
        **command(first=[
            f"execute as {target} at @s run particle minecraft:end_rod ~ ~1 ~ 0.4 0.8 0.4 0.01 60 force",
            f"execute as {target} at @s run {burst(rgb, 2.0, '0.4 1 0.4', 100, '~ ~1 ~')}",
            f"effect give {target} minecraft:slowness 8 255 true",
            f"effect give {target} minecraft:jump_boost 8 250 true",
            f"effect give {target} minecraft:mining_fatigue 8 4 true",
            f"effect give {target} minecraft:glowing 8 0 true",
            sound("minecraft:block.amethyst_cluster.place", 0.8),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(200),
        "conditions": {"unlocking": unlock(200), "enabling": action(200)},
    }, "Crystal Prison", "Seal the nearest creature within 12 blocks in violet crystal so it cannot move for 8 seconds. Costs 200.",
        shared=False, icon="minecraft:amethyst_cluster", index=6)
    kit.add("loves_embrace", {
        **command(first=[
            f"effect give {ALLIES.format(r=8)} minecraft:instant_health 1 0 true",
            f"effect give {ALLIES.format(r=8)} minecraft:regeneration 10 0 true",
            "particle minecraft:heart ~ ~1.5 ~ 2 1 2 0 30 force",
            sound("minecraft:entity.allay.ambient_with_item", 1.0),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(150),
        "conditions": {"unlocking": unlock(150), "enabling": action(200)},
    }, "Love's Embrace", "Heal every player within 8 blocks and give them Regeneration. Costs 150.", shared=False,
        icon="minecraft:pink_tulip", index=7)
    around = OTHERS.format(r=10)
    kit.add("charm", {
        **command(first=[
            f"execute at {around} run particle minecraft:heart ~ ~2 ~ 0.3 0.3 0.3 0 3 force",
            f"effect give {around} minecraft:weakness 10 3 true",
            f"effect give {around} minecraft:slowness 10 0 true",
            sound("minecraft:entity.allay.item_given", 1.2),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(120),
        "conditions": {"unlocking": unlock(120), "enabling": action(200)},
    }, "Charm", "Enchant everything within 10 blocks with love so it can barely hurt anyone. Costs 120.", shared=False,
        icon="minecraft:poppy", index=8)
    ultimate(kit, "love_conquers_all", "Love Conquers All",
             "Ultimate: fully heal every player within 16 blocks and pacify everything else around you. Costs 600.",
             "minecraft:amethyst_block", [
                 burst(rgb, 3.0, "5 2 5", 400),
                 "particle minecraft:heart ~ ~1.5 ~ 5 2 5 0 80 force",
                 f"effect give {ALLIES.format(r=16)} minecraft:instant_health 1 3 true",
                 f"effect give {OTHERS.format(r=16)} minecraft:weakness 15 254 true",
                 sound("minecraft:ui.toast.challenge_complete", 1.4),
             ])


def specials_white(kit, rgb):
    kit.add("life_growth", {
        **command(first=[
            "fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 minecraft:grass_block replace minecraft:dirt",
            "fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 minecraft:grass_block replace minecraft:coarse_dirt",
            "fill ~-4 ~-1 ~-4 ~4 ~-1 ~4 minecraft:moss_block replace minecraft:cobblestone",
            "particle minecraft:happy_villager ~ ~0.5 ~ 4 0.5 4 0 150 force",
            sound("minecraft:item.bone_meal.use", 1.0),
        ]),
        "bar_color": "white", "energy_bar_usage": usage(60),
        "conditions": {"unlocking": unlock(60, {"type": "palladium:crouching"}), "enabling": action(40)},
    }, "Life Growth", "While crouching: bring the ground around you to life, turning dirt to grass and cobblestone to moss. Costs 60.",
        shared=False, icon="minecraft:bone_meal", index=6)
    kit.add("life_aura", {
        "type": "palladium:dummy", "bar_color": "white", "energy_bar_usage": usage(1),
        "conditions": {"unlocking": unlock(1), "enabling": toggle()},
    }, "Aura of Life", "Toggle: you and every player within 10 blocks regenerate health. Drains the ring.", shared=False,
        icon="minecraft:totem_of_undying", index=7)
    pulse(kit, "life_aura_pulse", "life_aura", 40, [
        f"effect give {ALLIES.format(r=10)} minecraft:regeneration 3 1 true",
        "particle minecraft:end_rod ~ ~1 ~ 3 1 3 0.01 20 force",
    ])
    ultimate(kit, "entitys_light", "Light of the Entity",
             "Ultimate: a wave of pure life that heals every living thing within 12 blocks and burns the undead. Costs 600.",
             "minecraft:nether_star", [
                 "particle minecraft:end_rod ~ ~1 ~ 5 2 5 0.05 400 force",
                 "particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force",
                 "effect give @e[distance=..12,type=!minecraft:item,type=!minecraft:experience_orb] minecraft:instant_health 1 2 true",
                 f"effect give {ALLIES.format(r=12)} minecraft:regeneration 20 1 true",
                 sound("minecraft:block.beacon.activate", 0.6),
             ])


SPECIALS = {
    "green": specials_green, "yellow": specials_yellow, "red": specials_red, "orange": specials_orange,
    "blue": specials_blue, "indigo": specials_indigo, "violet": specials_violet, "white": specials_white,
}

# --- textures ---------------------------------------------------------------------

CLEAR = (0, 0, 0, 0)
BLACK = (24, 26, 28, 255)
BLACK_LIGHT = (44, 48, 52, 255)
WHITE = (240, 248, 240, 255)


def shade(rgb, f):
    if f >= 1:
        return tuple(int(v + (255 - v) * (f - 1)) for v in rgb) + (255,)
    return tuple(int(v * f) for v in rgb) + (255,)


def palette(rgb):
    p = {"main": shade(rgb, 1.0), "light": shade(rgb, 1.35), "dark": shade(rgb, 0.6), "deep": shade(rgb, 0.35),
         "black": BLACK, "black2": BLACK_LIGHT, "symbol": WHITE, "glow": shade(rgb, 1.45)}
    if min(rgb) > 200:  # White Lantern: white suit, dark trim, glowing symbol
        p.update(dark=(170, 175, 185, 255), deep=(120, 125, 135, 255), black=(205, 210, 220, 255),
                 black2=(190, 195, 205, 255), symbol=(30, 32, 36, 255), glow=(255, 255, 255, 255))
    return p


def box_faces(u, v, w, h, d):
    return {
        "top": (u + d, v, w, d), "bottom": (u + d + w, v, w, d), "right": (u, v + d, d, h),
        "front": (u + d, v + d, w, h), "left": (u + d + w, v + d, d, h), "back": (u + d + w + d, v + d, w, h),
    }


def paint_box(img, u, v, w, h, d, painter):
    for face, (fx, fy, fw, fh) in box_faces(u, v, w, h, d).items():
        for y in range(fh):
            for x in range(fw):
                col = painter(face, x, y, fw, fh)
                if col is not None:
                    img.putpixel((fx + x, fy + y), col)


def uniform_textures(p, emblem, slim):
    suit = Image.new("RGBA", (64, 64), CLEAR)
    glow = Image.new("RGBA", (64, 64), CLEAR)

    def head(face, x, y, w, h):  # domino mask
        if y not in (3, 4):
            return None
        if face == "front":
            return p["dark"] if y == 3 or x in (0, 3, 4, 7) else None
        if (face == "right" and x >= 5) or (face == "left" and x <= 2):
            return p["dark"]
        return None

    def body(face, x, y, w, h):
        if face == "top":
            return p["main"]
        if face == "bottom":
            return p["black"]
        if face in ("right", "left"):
            return p["black"] if y >= 2 else p["main"]
        if face == "front":
            if 1 <= y <= 5:
                return p["symbol"] if emblem[y - 1][x] == "W" else p["black"]
            if y == 0:
                return p["light"]
        if y >= 10:
            return p["black"]  # belt
        return p["main"] if 1 < x < 6 else p["black"]

    def arm(face, x, y, w, h):
        if face == "top":
            return p["main"]
        if face == "bottom":
            return p["dark"]
        if y >= h - 4:  # gloves
            return p["dark"] if y == h - 4 else p["main"]
        if y < 3:  # shoulders
            return p["main"]
        return p["black"] if (x + y) % 7 else p["black2"]

    def leg(face, x, y, w, h):
        if face == "top":
            return p["main"]
        if face == "bottom":
            return p["deep"]
        if y >= h - 4:  # boots
            return p["dark"] if y == h - 4 else p["main"]
        if face in ("right", "left"):
            return p["black"]
        return p["main"] if 0 < x < w - 1 else p["black"]

    def eyes(face, x, y, w, h):
        return WHITE if face == "front" and y == 4 and x in (1, 2, 5, 6) else None

    def emblem_glow(face, x, y, w, h):
        return p["glow"] if face == "front" and 1 <= y <= 5 and emblem[y - 1][x] == "W" else None

    def ring(face, x, y, w, h):
        return p["glow"] if face in ("front", "right", "left", "back") and y == h - 2 else None

    aw = 3 if slim else 4
    paint_box(suit, 0, 0, 8, 8, 8, head)
    paint_box(suit, 16, 16, 8, 12, 4, body)
    paint_box(suit, 40, 16, aw, 12, 4, arm)
    paint_box(suit, 32, 48, aw, 12, 4, arm)
    paint_box(suit, 0, 16, 4, 12, 4, leg)
    paint_box(suit, 16, 48, 4, 12, 4, leg)
    paint_box(glow, 0, 0, 8, 8, 8, eyes)
    paint_box(glow, 16, 16, 8, 12, 4, emblem_glow)
    paint_box(glow, 40, 16, aw, 12, 4, ring)
    return suit, glow


RING = [
    "................", "................", ".....GGGGGG.....", "....GLLLLLLG....",
    "....GLWWWWLG....", "....GWLLLLWG....", "....GWLLLLWG....", "....GLWWWWLG....",
    "....GGLLLLGG....", ".....DGGGGD.....", "....D......D....", "...D........D...",
    "...D........D...", "....D......D....", ".....DDDDDD.....", "................",
]
BATTERY = [
    "......YYYY......", ".....Y....Y.....", "....DDDDDDDD....", "...DGGGGGGGGD...",
    "...DGLLLLLLGD...", "...DGLWWWWLGD...", "...DGWLLLLWGD...", "...DGWLLLLWGD...",
    "...DGLWWWWLGD...", "...DGLLLLLLGD...", "...DGGGGGGGGD...", "....DDDDDDDD....",
    "...SSSSSSSSSS...", "..SBBBBBBBBBBS..", "..SSSSSSSSSSSS..", "................",
]


def item_texture(rows, p):
    pal = {"G": p["main"], "L": p["light"], "D": p["dark"], "W": WHITE if p["symbol"] == WHITE else p["dark"],
           "Y": (210, 170, 60, 255), "S": BLACK_LIGHT, "B": BLACK}
    img = Image.new("RGBA", (16, 16), CLEAR)
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in pal:
                img.putpixel((x, y), pal[ch])
    return img


def logo():
    size = 128
    img = Image.new("RGBA", (size, size), (10, 14, 12, 255))
    draw = ImageDraw.Draw(img)
    colors = [d["color"] for d in CORPS.values() if d["color"] != CORPS["white"]["color"]]
    for i, rgb in enumerate(colors):  # a ring of the emotional spectrum
        a = 360 / len(colors)
        draw.pieslice((8, 8, 120, 120), i * a - 90, (i + 1) * a - 90, fill=rgb + (255,))
    draw.ellipse((22, 22, 106, 106), fill=(10, 14, 12, 255))
    glow = (240, 255, 240, 255)
    draw.rectangle((30, 34, 98, 44), fill=glow)
    draw.rectangle((30, 84, 98, 94), fill=glow)
    draw.ellipse((42, 42, 86, 86), outline=glow, width=8)
    return img


# --- output -----------------------------------------------------------------------

def write(rel, data):
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def save(img, rel):
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


GENERATED_DIRS = [
    f"addon/{NS}/items", f"addon/{NS}/creative_mode_tabs", f"data/{NS}/palladium/powers",
    f"data/{NS}/palladium/item_powers", f"data/{NS}/recipes", f"assets/{NS}/models/item",
    f"assets/{NS}/textures", f"assets/{NS}/palladium/render_layers", f"assets/{NS}/palladium/energy_beams",
    f"assets/{NS}/palladium/trails", f"assets/{NS}/palladium/particle_emitters",
]


def main():
    for d in GENERATED_DIRS:
        shutil.rmtree(SRC / d, ignore_errors=True)

    lang = {
        f"itemGroup.{NS}.lantern_corps": "Lantern Corps",
        f"power.{NS}.tooltip.hold": "Hold in either hand, or wear it in a Curios ring slot.",
        f"power.{NS}.tooltip.suit": "Use Suit Up to unlock the ring's powers.",
        f"item.{NS}.battery.tooltip.1": "Hold in your main hand while wearing a ring of the same corps,",
        f"item.{NS}.battery.tooltip.2": "then hold the Recharge key to recite the oath.",
    }
    order, tab = [], []

    for c, data in CORPS.items():
        rgb, p = data["color"], palette(data["color"])
        ring, battery = f"{c}_lantern_ring", f"{c}_power_battery"
        order += [ring, battery]
        tab += [f"{NS}:{ring}", f"{NS}:{battery}"]

        # items
        write(f"addon/{NS}/items/{ring}.json", {
            "max_stack_size": 1, "rarity": "epic", "is_fire_resistant": True,
            "creative_mode_tab": f"{NS}:lantern_corps",
            "tooltip": [
                {"translate": f"item.{NS}.{ring}.tooltip", "color": hexcolor(rgb), "italic": True},
                {"translate": f"power.{NS}.tooltip.hold", "color": "gray"},
                {"translate": f"power.{NS}.tooltip.suit", "color": "gray"},
            ],
        })
        write(f"addon/{NS}/items/{battery}.json", {
            "max_stack_size": 1, "rarity": "rare", "is_fire_resistant": True,
            "creative_mode_tab": f"{NS}:lantern_corps",
            "tooltip": [{"translate": f"item.{NS}.battery.tooltip.1", "color": "gray"},
                        {"translate": f"item.{NS}.battery.tooltip.2", "color": "gray"}],
        })
        lang[f"item.{NS}.{ring}"] = f"{data['name']} Ring"
        lang[f"item.{NS}.{ring}.tooltip"] = f"Powered by {data['emotion']}"
        lang[f"item.{NS}.{battery}"] = f"{data['name']} Power Battery"
        for item, rows in ((ring, RING), (battery, BATTERY)):
            write(f"assets/{NS}/models/item/{item}.json",
                  {"parent": "minecraft:item/generated", "textures": {"layer0": f"{NS}:item/{item}"}})
            save(item_texture(rows, p), f"assets/{NS}/textures/item/{item}.png")

        # power
        kit = Kit(c)
        shared_kit(kit, c, data)
        SPECIALS[c](kit, rgb)
        write(f"data/{NS}/palladium/powers/{c}_lantern.json", {
            "name": text(f"power.{NS}.{c}_lantern"),
            "icon": f"{NS}:{ring}",
            "background": "minecraft:textures/block/black_concrete.png",
            "energy_bars": {BAR: {"max": 1000, "auto_increase_per_tick": 1, "auto_increase_interval": 10,
                                  "color": hexcolor(rgb)}},
            "abilities": kit.abilities,
        })
        lang[f"power.{NS}.{c}_lantern"] = data["name"]
        lang.update(kit.lang)
        for slot in ("mainhand", "offhand", "curios:ring"):
            write(f"data/{NS}/palladium/item_powers/{ring}_{slot.replace(':', '_')}.json",
                  {"slot": slot, "item": f"{NS}:{ring}", "power": f"{NS}:{c}_lantern"})

        # visuals
        for slim in (False, True):
            suit, glow = uniform_textures(p, data["emblem"], slim)
            suffix = "_slim" if slim else ""
            save(suit, f"assets/{NS}/textures/models/{c}_uniform{suffix}.png")
            save(glow, f"assets/{NS}/textures/models/{c}_uniform_glow{suffix}.png")
        for layer in ("uniform", "uniform_glow"):
            rl = {"type": "palladium:skin_overlay", "texture": {
                "normal": f"{NS}:textures/models/{c}_{layer}.png",
                "slim": f"{NS}:textures/models/{c}_{layer}_slim.png"}}
            if layer == "uniform_glow":
                rl["render_type"] = "glow"
            write(f"assets/{NS}/palladium/render_layers/{c}_{layer}.json", rl)
        write(f"assets/{NS}/palladium/energy_beams/{c}_beam.json", {
            "type": "palladium:laser", "body_part": "right_arm", "offset": [0, -11, 0],
            "glow_color": hexcolor(rgb), "core_color": "#FFFFFF", "glow_opacity": 0.9, "bloom": 3,
            "size": 1.4, "rotation_speed": 3,
            "particles": [{"particle_type": "minecraft:dust", "options": dust(rgb), "amount": 2,
                           "offset_random": [0.2, 0.2, 0.2]}],
        })
        if c == "red":
            write(f"assets/{NS}/palladium/energy_beams/red_napalm.json", {
                "type": "palladium:laser", "body_part": "head", "offset": [0, 2, 0],
                "glow_color": "#B0000A", "core_color": "#FF6A00", "glow_opacity": 0.95, "bloom": 2, "size": 2.2,
                "particles": [{"particle_type": "minecraft:flame", "amount": 3, "offset_random": [0.3, 0.3, 0.3]}],
            })
        write(f"assets/{NS}/palladium/trails/{c}_trail.json",
              {"type": "palladium:gradient", "spacing": 2, "lifetime": 14, "color": hexcolor(rgb)})

        # recipes
        if data["ring_gem"]:
            write(f"data/{NS}/recipes/{ring}.json", {
                "type": "minecraft:crafting_shaped", "category": "equipment",
                "pattern": [" X ", "GEG", " G "],
                "key": {"X": {"item": data["ring_gem"]}, "E": {"item": "minecraft:ender_eye"},
                        "G": {"item": "minecraft:gold_ingot"}},
                "result": {"item": f"{NS}:{ring}"},
            })
        write(f"data/{NS}/recipes/{battery}.json", {
            "type": "minecraft:crafting_shaped", "category": "equipment",
            "pattern": ["GRG", "XLX", "III"],
            "key": {"G": {"item": "minecraft:gold_ingot"}, "R": {"item": data["ring_gem"] or "minecraft:nether_star"},
                    "X": {"item": data["glass"]}, "L": {"item": "minecraft:lantern"},
                    "I": {"item": "minecraft:iron_ingot"}},
            "result": {"item": f"{NS}:{battery}"},
        })

    # The White Lantern is earned by uniting the whole spectrum.
    write(f"data/{NS}/recipes/white_lantern_ring.json", {
        "type": "minecraft:crafting_shapeless", "category": "equipment",
        "ingredients": [{"item": f"{NS}:{c}_lantern_ring"} for c in CORPS if c != "white"]
                       + [{"item": "minecraft:nether_star"}, {"item": "minecraft:totem_of_undying"}],
        "result": {"item": f"{NS}:white_lantern_ring"},
    })

    write(f"addon/{NS}/items/_loading_order.json", order)
    write(f"addon/{NS}/creative_mode_tabs/lantern_corps.json", {"icon": f"{NS}:green_lantern_ring", "items": tab})
    write(f"assets/{NS}/palladium/particle_emitters/ring_hand.json", {
        "body_part": "right_arm", "amount": 1, "offset": [0, -10, 0], "offset_random": [1, 1, 1],
        "motion": [0, 0.5, 0], "motion_random": [0.3, 0.3, 0.3], "visible_in_first_person": False,
    })
    write(f"assets/{NS}/palladium/particle_emitters/flight_aura.json", {
        "body_part": "body", "amount": 2, "offset": [0, -6, 0], "offset_random": [6, 12, 6],
        "motion_random": [0.2, 0.2, 0.2], "visible_in_first_person": False,
    })
    write(f"data/curios/tags/items/ring.json",
          {"replace": False, "values": [f"{NS}:{c}_lantern_ring" for c in CORPS]})
    write(f"assets/{NS}/lang/en_us.json", lang)
    save(logo(), "pack.png")
    print(f"Generated {len(CORPS)} corps")


if __name__ == "__main__":
    main()
