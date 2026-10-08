"""Host powers for the emotional spectrum entities: final_lanterns:host_<entity> (see entities.py for how hosting works).

A host needs no ring. Their power is a copy of the entity's corps' A New Corps ring power (trees.clone_ring): the
same skill tree, bar texture and background, and every ability the ring has, working without a ring and stronger
(a bigger bar that refills on its own, faster than any ring's, and beams half again as strong). Beside the ring's tree
the entity adds two branches:

- its power (right): its own passive, three abilities and its ultimate;
- its light (left): Empower Ring fills the ring of the bearer you look at, Living Lantern makes you a lantern
  (bearers near you recharge, and sneaking beside you recites their oath for a full charge), Forge Ring forges a new
  ring of its color, and Hard Light is a second construct wheel with the entity's own weapons and shapes.

The suit node is the entity's: its key shows the entity's suit (A New Corps' suit of its best-known host) and aura.
"""
import copy
import json
import re
from pathlib import Path

import entities
import icons
import trees
from common import CORPS, HOSTILE, NS, TARGETS, burst, dust, hexcolor, sound, tellraw

BASE = Path(__file__).resolve().parent.parent / "base"
BAR = "entity_power"
HOST_MAX = 3000    # a ring's bar holds 2000
MAX_SCALE = 1.5    # the ring tree's charge nodes (3000 and 4000 for a ring) hold half again as much
BEAM_SCALE = 1.5   # the ring's beam, fed by the entity, is half again as strong
BASE_REGEN = 3     # per tick, always (A New Corps' rings: 2 at best, after Natural Regeneration)
EMPOWER_COST, EMPOWER_GIVE = 400, 1000      # Empower Ring: host power spent, ring charge given
LANTERN_TRICKLE, LANTERN_COST = 100, 1      # Living Lantern: charge a second to bearers within 8; cost a tick
OATH_GIVE, OATH_COST, OATH_COOLDOWN = 4000, 800, 30  # reciting the oath beside a Living Lantern host
FORGE_COST, FORGE_COOLDOWN = 3000, 6000     # Forge Ring (cooldown in ticks)

OTHERS = "@e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..{r}]"
ALLIES = "@a[distance=..{r}]"

HOST_ICON = {"ion": "minecraft:heart_of_the_sea", "parallax": "minecraft:spider_eye", "butcher": "minecraft:nether_wart",
             "ophidian": "minecraft:gold_block", "adara": "minecraft:feather", "predator": "minecraft:amethyst_cluster",
             "proselyte": "minecraft:ink_sac", "life": "minecraft:nether_star", "nekron": "minecraft:wither_skeleton_skull"}

# The host's suit: A New Corps' suit of the entity's best-known host. (folder under textures/models/skins, texture,
# glow texture or None, cape render layer or None)
HOST_SUITS = {
    "ion": ("greenlanterns", "iongalaxy", "iongalaxyglow", None),
    "parallax": ("yellowlanterns", "yellowparallax", None, "capes/yellowparallax"),
    "butcher": ("redlanterns", "atrocitus", None, None),
    "ophidian": ("orangelanterns", "larfleeze", None, None),
    "adara": ("bluelanterns", "saintwalker", None, None),
    "predator": ("pinklanterns", "carolferris", None, None),
    "proselyte": ("purplelanterns", "indigo1", None, None),
    "life": ("whitelanterns", "white1", None, None),
    "nekron": ("blacklanterns", "blacklantern", None, None),
}

# The construct wheel: A New Corps construct weapons (item, name, held in the offhand) of the entity's color, and
# the entity's world constructs (function under host_cx/, name, cost, icon).
WHEEL_ITEMS = {
    "ion": [("bat_willpower", "Baseball Bat"), ("battleaxe_willpower", "Battle Axe"), ("greenlongsword", "Longsword"),
            ("greatsword_willpower", "Greatsword"), ("hammer_willpower", "Hammer"), ("katana_willpower", "Katana"),
            ("scythe_willpower", "Scythe"), ("spear_willpower", "Spear"), ("axe_willpower", "Axe"),
            ("pickaxe_willpower", "Pickaxe"), ("shield", "Shield", True)],
    "parallax": [("scytheyellow", "Scythe"), ("clawsyellow", "Claws"), ("axeyellow", "Axe"),
                 ("pickaxeyellow", "Pickaxe"), ("yellowshield", "Fear Shield", True)],
    "butcher": [("greatswordred", "Crucible"), ("red_battleaxe", "Battle Axe"), ("red_claw", "Blood Claw"),
                ("red_hammer", "Hammer"), ("red_trident", "Trident")],
    "ophidian": [("bundle", "Dimensional Sack"), ("scytheorange", "Scythe"), ("axeorange", "Axe"),
                 ("pickaxeorange", "Pickaxe"), ("orangeshield", "Greed Shield", True)],
    "adara": [("bostaffblue", "Bo Staff"), ("spearblue", "Spear"), ("hammerblue", "Hammer"), ("axeblue", "Axe"),
              ("pickaxeblue", "Pickaxe"), ("blueshield", "Hope Shield", True)],
    "predator": [("bowpink", "Cupid Bow"), ("lovearrow", "Love Arrows"), ("spearpink", "Spear"), ("axepink", "Axe"),
                 ("pickaxepink", "Pickaxe"), ("pinkshield", "Love Shield", True)],
    # the Indigo Tribe borrows the light of others: so does its entity
    "proselyte": [("bostaffblue", "Bo Staff"), ("spearblue", "Spear"), ("bowpink", "Bow"), ("lovearrow", "Arrows"),
                  ("hammerblue", "Hammer"), ("blueshield", "Shield", True)],
    "life": [("greatsword_willpower", "Greatsword of Will"), ("scytheyellow", "Scythe of Fear"),
             ("red_trident", "Trident of Rage"), ("axeorange", "Axe of Avarice"), ("hammerblue", "Hammer of Hope"),
             ("bowpink", "Bow of Love"), ("lovearrow", "Arrows of Love"), ("shield", "Shield", True)],
    "nekron": [("scythebalance", "Reaper's Scythe"), ("spearbalance", "Bone Spear"), ("axebalance", "Grave Axe"),
               ("pickaxebalance", "Grave Pick"), ("bostaffbalance", "Staff of the Dead")],
}
WHEEL_WORLD = {
    "ion": [("green/fist", "Giant Fist", 100, f"{NS}:construct_fist")],
    "parallax": [("yellow/spikes", "Fear Spikes", 150, "minecraft:pointed_dripstone")],
    "ophidian": [("orange/hand", "Grasping Hand", 100, "minecraft:lead")],
    "predator": [("violet/crystal", "Crystal Prison", 150, "minecraft:amethyst_cluster")],
    "proselyte": [("indigo/cage", "Compassion Cage", 150, "minecraft:iron_bars")],
    "nekron": [("black/cage", "Grave Cage", 150, "minecraft:iron_bars"), ("black/spikes", "Grave Spikes", 150,
                                                                          "minecraft:bone")],
}
ARROW_COUNT = 4
WHISPER = json.dumps({"text": "Don't you hear him?", "color": "yellow", "italic": True})

ICONS = {}  # texture file under assets/final_lanterns/textures/gui/ability/ -> (glyph, rgb)


def glyph_icon(glyph, key, rgb, fallback):
    """The ability icon for `glyph` in these colors, or `fallback` (an item id) while that glyph isn't drawn yet."""
    if glyph not in icons.GLYPHS:
        return fallback
    ICONS[f"{glyph}_{key}.png"] = (glyph, rgb)
    return f"{NS}:textures/gui/ability/{glyph}_{key}.png"


def NOT(*conds):
    return {"type": "palladium:not", "conditions": list(conds)}


def has_tag(tag):
    return {"type": "palladium:has_tag", "tag": tag}


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
    # All three lists are always written: Palladium's default for "commands" is `say Hello World` every tick.
    return {"type": "palladium:command", "first_tick_commands": list(first),
            "commands": list(every), "last_tick_commands": list(last)}


def action(cooldown):
    return {"type": "palladium:action", "cooldown": cooldown}


def key_action(cooldown, empty_hand=False):
    return {"type": "palladium:action", "cooldown": cooldown, "key_type": "key_bind", "needs_empty_hand": empty_hand,
            "allow_scrolling_when_crouching": True}


def toggle():
    return {"type": "palladium:toggle"}


def held():
    return {"type": "palladium:held"}


def one(conds):
    return conds[0] if len(conds) == 1 else conds


def anc_ability(corps, key):
    """A copy of one ability of that corps' A New Corps ring power (from base/)."""
    path = BASE / f"data/{NS}/palladium/powers/{CORPS[corps]['power']}.json"
    return copy.deepcopy(json.loads(path.read_text(encoding="utf-8"))["abilities"][key])


class Power:
    """Builds one host power: bar abilities, skill-tree nodes and hidden helpers."""

    def __init__(self, e):
        self.e = e
        self.key = e.key
        self.rgb = e.rgb
        self.abilities = {}
        self.lang = {}

    def glyph(self, glyph, fallback):
        return glyph_icon(glyph, self.key, self.rgb, fallback)

    def tr(self, key, english):
        lang_key = f"ability.{NS}.host_{self.key}.{key}"
        self.lang[lang_key] = english
        return {"translate": lang_key}

    def hidden(self, key, ability):
        self.abilities[key] = {**ability, "hidden": True, "hidden_in_bar": True}

    def bar(self, key, ability, name, icon, index, node=None, cost=0, desc=None):
        """An ability on the ability bar (hidden from the skill tree, which shows its node instead)."""
        conds = dict(ability.get("conditions", {}))
        unlocking = [unlocked(node)] if node else []
        if cost:
            unlocking.append(charge(cost))
            if "energy_bar_usage" not in ability:
                ability = {**ability, "energy_bar_usage": usage(cost)}
        if unlocking:
            own = conds.get("unlocking", [])
            own = own if isinstance(own, list) else [own]
            conds["unlocking"] = one(unlocking + own)
        self.abilities[key] = {**ability, "conditions": conds, "title": self.tr(key, name), "icon": icon,
                               "bar_color": "white", "hidden": True, "hidden_in_bar": False, "list_index": index}
        if desc:
            self.abilities[key]["description"] = self.tr(key + ".description", desc)

    def pulse(self, key, source, every, commands):
        """Runs commands every N ticks while `source` is enabled."""
        self.hidden(key, {**command(first=commands), "conditions": {"enabling": [enabled(source), interval(every)]}})


def host_kits(e):
    """(passive, [ability, ability, ability, ultimate]) for entity e. A passive is (name, description, item, abilities
    {key: json}); an ability is (key, name, description, glyph, fallback item, cost, cooldown or None for a held/toggle
    ability, ability json or command lines)."""
    rgb = e.rgb
    T = lambda r: TARGETS.format(r=r) + "]"  # noqa: E731  creatures, never the host (tagged gl_user)
    T1 = lambda r: TARGETS.format(r=r) + ",limit=1,sort=nearest]"  # noqa: E731
    pulse = lambda every, cmds: {**command(first=cmds), "conditions": {"enabling": interval(every)}}  # noqa: E731
    user = lambda lines: ["tag @s add gl_user", *lines, "tag @s remove gl_user"]  # noqa: E731
    big = lambda: [burst(rgb, 3.0, "4 2 4", 300), "particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force"]  # noqa: E731
    k = e.key
    if k == "ion":
        return (("Indomitable", "Nothing moves you: no knockback, no slowness, weakness, blindness or darkness.",
                 "minecraft:anvil", {
                     "indomitable_clear": pulse(10, [f"effect clear @s minecraft:{x}" for x in
                                                     ("slowness", "weakness", "blindness", "darkness")])}),
                [("will_surge", "Will Surge", "Surge forward up to 8 blocks and knock everything around you away.",
                  "blast", "minecraft:feather", 60, 60, user([
                      f"function {NS}:entity/dash", burst(rgb, 2.0, "1.5 1 1.5", 80),
                      f"execute as {T(4)} run damage @s 6 minecraft:player_attack by @p[tag=gl_user]",
                      f"effect give {T(4)} minecraft:levitation 1 2 true"])),
                 ("giant_fist", "Giant Fist", "A giant fist of will punches whatever is in front of you into the air.",
                  "rage", "minecraft:iron_block", 100, 60, user([f"function {NS}:host_cx/green/fist"])),
                 ("unbreakable", "Unbreakable Will", "Toggle: Resistance III while your power lasts.",
                  "force_field", "minecraft:shield", 1, None, {
                      **command(first=["effect give @s minecraft:resistance infinite 2 true"],
                                last=["effect clear @s minecraft:resistance"]),
                      "energy_bar_usage": usage(1), "conditions": {"enabling": toggle()}}),
                 ("will_unbound", "Willpower Unbound", "Ultimate: a nova of pure will hurts and hurls everything within "
                  "12 blocks, and a construct train smashes through what's ahead.", "overload", "minecraft:emerald_block",
                  600, 1200, user([*big(), f"execute as {T(12)} run damage @s 24 minecraft:player_attack by @p[tag=gl_user]",
                                   f"effect give {T(12)} minecraft:levitation 2 4 true",
                                   f"function {NS}:host_cx/green/train",
                                   sound("minecraft:entity.generic.explode", 0.6)]))])
    if k == "parallax":
        return (("Feeds on Fear", "Hostile mobs around you feed you: you regenerate while one is within 10 blocks.",
                 "minecraft:spider_eye", {
                     "feeds_on_fear": pulse(40, [f"execute if entity {HOSTILE.format(r=10)} run "
                                                 "effect give @s minecraft:regeneration 3 1 true"])}),
                [("fear_gaze", "Fear Gaze", "Everything in front of you is struck with darkness, slowness and weakness.",
                  "inflict_fear", "minecraft:ender_eye", 80, 100, user([
                      *[f"execute anchored eyes positioned ^ ^ ^5 run effect give {T(6)} minecraft:{x} 8 1 true"
                        for x in ("darkness", "slowness", "weakness")],
                      f"execute anchored eyes positioned ^ ^ ^5 as {T(6)} at @s run particle minecraft:squid_ink ~ ~1 ~ "
                      f"0.3 0.5 0.3 0.02 15 force",
                      f"execute anchored eyes positioned ^ ^ ^5 as @a[tag=!gl_user,distance=..6] run title @s title {WHISPER}",
                      sound("minecraft:ambient.cave", 0.6)])),
                 ("fear_spikes", "Spikes of Terror", "A ring of fear spikes bursts from the ground around you.",
                  "nightmare", "minecraft:pointed_dripstone", 150, 160, user([f"function {NS}:host_cx/yellow/spikes"])),
                 ("terror", "Terror", "The nearest creature within 12 blocks is lifted, withered and maddened by fear.",
                  "inflict_fear", "minecraft:wither_rose", 100, 120, user([
                      f"effect give {T1(12)} minecraft:levitation 2 2 true", f"effect give {T1(12)} minecraft:wither 5 1 true",
                      f"effect give {T1(12)} minecraft:nausea 8 0 true",
                      f"execute as {T1(12)} if entity @s[type=minecraft:player] run title @s title {WHISPER}",
                      sound("minecraft:entity.warden.heartbeat", 1.2)])),
                 ("fear_incarnate", "Fear Incarnate", "Ultimate: everything within 16 blocks is crippled by terror for "
                  "15 seconds.", "overload", "minecraft:sculk_shrieker", 600, 1200, user([
                      *big(), *[f"effect give {T(16)} minecraft:{x} 15 {a} true" for x, a in
                                (("darkness", 0), ("slowness", 3), ("weakness", 2), ("nausea", 0))],
                      sound("minecraft:entity.warden.roar", 1.0)]))])
    if k == "butcher":
        return (("Bloodlust", "+4 attack damage, and fire can't burn you.", "minecraft:iron_axe", {
                    "bloodlust_fire": pulse(100, ["effect give @s minecraft:fire_resistance 15 0 true"])}),
                [("rage_roar", "Roar of Rage", "A roar of pure rage hurls everything within 8 blocks away and sets it "
                  "ablaze.", "roar", "minecraft:fire_charge", 120, 160, user([
                      f"execute as {T(8)} at @s facing entity @p[tag=gl_user] feet rotated ~180 0 run tp @s ^ ^0.5 ^3",
                      f"execute as {T(8)} run damage @s 8 minecraft:player_attack by @p[tag=gl_user]",
                      f"execute as {T(8)} run data merge entity @s {{Fire:120s}}",
                      burst(rgb, 2.5, "4 1 4", 200), "particle minecraft:flame ~ ~1 ~ 3 1 3 0.05 120 force",
                      sound("minecraft:entity.ravager.roar", 0.6)])),
                 ("rampage", "Rampage", "Strength III, Speed II and Resistance for 12 seconds.", "rage",
                  "minecraft:blaze_powder", 150, 400, [
                      "effect give @s minecraft:strength 12 2 true", "effect give @s minecraft:speed 12 1 true",
                      "effect give @s minecraft:resistance 12 0 true", burst(rgb, 2.0, "0.6 1 0.6", 120),
                      sound("minecraft:entity.ravager.roar", 0.8)]),
                 ("gore_charge", "Gore Charge", "Charge forward and gore everything where you land.", "blast",
                  "minecraft:goat_horn", 100, 80, user([
                      f"function {NS}:entity/dash", f"execute as {T(3)} run damage @s 12 minecraft:player_attack by @p[tag=gl_user]",
                      f"effect give {T(3)} minecraft:levitation 1 3 true", burst(rgb, 2.0, "1 1 1", 100)])),
                 ("slaughter", "Slaughter", "Ultimate: a storm of rage hurts, withers and burns everything within 10 "
                  "blocks.", "overload", "minecraft:nether_wart_block", 600, 1200, user([
                      *big(), f"execute as {T(10)} run damage @s 24 minecraft:player_attack by @p[tag=gl_user]",
                      f"effect give {T(10)} minecraft:wither 6 2 true",
                      f"execute at {T(10)} run particle minecraft:flame ~ ~1 ~ 0.3 0.6 0.3 0.02 30 force",
                      sound("minecraft:entity.blaze.shoot", 0.5)]))])
    if k == "ophidian":
        return (("Endless Avarice", "+5 luck: better loot from everything.", "minecraft:gold_ingot", {}),
                [("coil", "Coil", "A grasping hand of avarice drags the nearest creature within 12 blocks to you and "
                  "holds it.", "greed_arrival", "minecraft:lead", 100, 120, user([
                      f"function {NS}:host_cx/orange/hand", sound("minecraft:item.armor.equip_chain", 0.6)])),
                 ("hoard", "Hoard", "Everything within 20 blocks that glitters is yours: items and experience fly to you.",
                  "hoard", "minecraft:chest", 50, 40, [
                      "tp @e[type=minecraft:item,distance=..20] @s", "tp @e[type=minecraft:experience_orb,distance=..20] @s",
                      burst(rgb, 1.5, "2 1 2", 80), sound("minecraft:entity.item.pickup", 0.6)]),
                 ("devour", "Devour", "Bite the nearest creature within 8 blocks and keep its life as extra hearts.",
                  "life_drain", "minecraft:ghast_tear", 120, 120, user([
                      f"execute as {T1(8)} run damage @s 12 minecraft:magic by @p[tag=gl_user]",
                      "effect give @s minecraft:absorption 30 2 true", "effect give @s minecraft:instant_health 1 0 true",
                      sound("minecraft:entity.generic.eat", 0.5)])),
                 ("serpents_hoard", "Serpent's Hoard", "Ultimate: devour the life of everything within 10 blocks and keep it.",
                  "overload", "minecraft:enchanted_golden_apple", 600, 1200, user([
                      *big(), f"execute as {T(10)} run damage @s 16 minecraft:magic by @p[tag=gl_user]",
                      f"effect give {T(10)} minecraft:wither 5 1 true", "effect give @s minecraft:absorption 60 4 true",
                      sound("minecraft:entity.wither.ambient", 1.4)]))])
    if k == "adara":
        return (("Undying Hope", "Below 10 hearts you keep regenerating.", "minecraft:golden_apple", {
                    "undying_hope": {**command(first=["effect give @s minecraft:regeneration 3 1 true"]),
                                     "conditions": {"unlocking": {"type": "palladium:health", "min_health": 0,
                                                                  "max_health": 20},
                                                    "enabling": interval(40)}}}),
                [("wings_of_hope", "Wings of Hope", "Soar upward and glide down; players around you regenerate.",
                  "hope_aura", "minecraft:elytra", 80, 160, [
                      "effect give @s minecraft:levitation 1 12 true", "effect give @s minecraft:slow_falling 10 0 true",
                      f"effect give {ALLIES.format(r=8)} minecraft:regeneration 5 1 true", burst(rgb, 2.0, "1 1 1", 100),
                      sound("minecraft:entity.ender_dragon.flap", 1.4)]),
                 ("beacon_of_hope", "Beacon of Hope", "Every player within 12 blocks regenerates and resists damage for "
                  "12 seconds.", "rekindle", "minecraft:beacon", 150, 300, [
                      f"effect give {ALLIES.format(r=12)} minecraft:regeneration 12 1 true",
                      f"effect give {ALLIES.format(r=12)} minecraft:resistance 12 0 true", burst(rgb, 2.0, "3 1 3", 150),
                      sound("minecraft:block.beacon.power_select", 1.6)]),
                 ("rekindle", "Rekindle", "Heal every player within 12 blocks and give them extra hearts.",
                  "healing_touch", "minecraft:golden_apple", 200, 600, [
                      f"effect give {ALLIES.format(r=12)} minecraft:instant_health 1 1 true",
                      f"effect give {ALLIES.format(r=12)} minecraft:absorption 60 1 true", burst(rgb, 2.0, "3 1 3", 150),
                      sound("minecraft:block.beacon.power_select", 1.8)]),
                 ("hope_eternal", "Hope Eternal", "Ultimate: every player within 24 blocks is healed and gains "
                  "Regeneration and Resistance for 20 seconds.", "overload", "minecraft:beacon", 600, 1200, [
                      *big(), *[f"effect give {ALLIES.format(r=24)} minecraft:{x} {t} {a} true" for x, t, a in
                                (("instant_health", 1, 2), ("regeneration", 20, 2), ("resistance", 20, 1))],
                      sound("minecraft:ui.toast.challenge_complete", 1.2)])])
    if k == "predator":
        return (("Devotion", "You regenerate while another player is within 8 blocks.", "minecraft:pink_tulip", {
                    "devotion": pulse(40, ["execute if entity @a[distance=0.1..8] run "
                                           "effect give @s minecraft:regeneration 3 0 true"])}),
                [("crystal_embrace", "Crystal Embrace", "Seal the nearest creature within 12 blocks in violet crystal.",
                  "crystal_prison", "minecraft:amethyst_cluster", 150, 200, user([f"function {NS}:host_cx/violet/crystal"])),
                 ("hearts_desire", "Heart's Desire", "Everything within 10 blocks is charmed and can barely hurt anyone.",
                  "charm", "minecraft:poppy", 120, 200, user([
                      f"execute at {T(10)} run particle minecraft:heart ~ ~2 ~ 0.3 0.3 0.3 0 3 force",
                      f"effect give {T(10)} minecraft:weakness 10 3 true", f"effect give {T(10)} minecraft:slowness 10 0 true",
                      sound("minecraft:entity.allay.item_given", 1.2)])),
                 ("obsession", "Obsession", "Mark the nearest creature within 16 blocks: it glows and weakens, and you "
                  "gain Strength II and Speed for 15 seconds.", "loves_embrace", "minecraft:spyglass", 100, 300, user([
                      f"effect give {T1(16)} minecraft:glowing 15 0 true", f"effect give {T1(16)} minecraft:weakness 15 1 true",
                      "effect give @s minecraft:strength 15 1 true", "effect give @s minecraft:speed 15 0 true",
                      sound("minecraft:entity.warden.heartbeat", 1.4)])),
                 ("love_unending", "Love Unending", "Ultimate: fully heal every player within 16 blocks and pacify "
                  "everything else.", "overload", "minecraft:amethyst_block", 600, 1200, user([
                      *big(), "particle minecraft:heart ~ ~1.5 ~ 5 2 5 0 80 force",
                      f"effect give {ALLIES.format(r=16)} minecraft:instant_health 1 4 true",
                      f"effect give {T(16)} minecraft:weakness 15 254 true",
                      sound("minecraft:ui.toast.challenge_complete", 1.4)]))])
    if k == "proselyte":
        return (("Empathic Link", "Players within 8 blocks of you slowly regenerate.", "minecraft:blue_orchid", {
                    "empathic_link": pulse(60, [f"effect give {ALLIES.format(r=8)} minecraft:regeneration 4 0 true"])}),
                [("empathy", "Empathy", "The nearest creature within 12 blocks feels every hurt it causes and can barely "
                  "fight for 10 seconds.", "compassion", "minecraft:blue_orchid", 150, 200, user([
                      f"effect give {T1(12)} minecraft:weakness 10 254 true", f"effect give {T1(12)} minecraft:slowness 10 1 true",
                      f"execute at {T1(12)} run {burst(rgb, 1.5, '0.4 0.8 0.4', 60, '~ ~1 ~')}",
                      sound("minecraft:block.amethyst_block.chime", 0.7)])),
                 ("tendrils", "Tendrils", "Tentacles drag everything within 8 blocks in front of you and slow it.",
                  "greed_arrival", "minecraft:ink_sac", 120, 160, user([
                      f"execute rotated ~ 0 positioned ^ ^ ^2.5 run tp {T(8)} ~ ~ ~",
                      f"effect give {T(4)} minecraft:slowness 5 2 true", burst(rgb, 1.5, "2 1 2", 100),
                      sound("minecraft:entity.squid.squirt", 0.6)])),
                 ("phase", "Indigo Phase", "Throw a bolt of indigo light and teleport to where it lands.", "phase",
                  "minecraft:ender_pearl", 80, 40, {
                      "type": "palladium:projectile", "entity_type": "minecraft:ender_pearl", "velocity": 2.5,
                      "inaccuracy": 0.0}),
                 ("compassion_for_all", "Compassion for All", "Ultimate: everything within 16 blocks is overwhelmed by "
                  "empathy and can barely fight for 15 seconds.", "overload", "minecraft:end_rod", 600, 1200, user([
                      *big(), f"effect give {T(16)} minecraft:weakness 15 254 true",
                      f"effect give {T(16)} minecraft:slowness 15 2 true", f"effect give {T(16)} minecraft:nausea 10 0 true",
                      sound("minecraft:block.beacon.deactivate", 0.8)]))])
    if k == "life":
        return (("Eternal Life", "Once every ten minutes a killing blow leaves you standing instead.",
                 "minecraft:totem_of_undying", {
                     "eternal_life": {"type": "palladium:immortality",
                                      "conditions": {"unlocking": [unlocked("skill_passive"), has_tag("gl_life_ready")]}},
                     "eternal_life_revival": {
                         **command(first=["effect give @s minecraft:instant_health 1 3 true",
                                          "effect give @s minecraft:regeneration 10 2 true",
                                          "effect give @s minecraft:absorption 20 3 true",
                                          "particle minecraft:totem_of_undying ~ ~1 ~ 0.6 1 0.6 0.4 120 force",
                                          "tag @s remove gl_life_ready", "scoreboard players set @s gl_lifecd 600",
                                          "title @s actionbar " + json.dumps({"text": "Life will not let you go.",
                                                                              "color": "white"}),
                                          sound("minecraft:item.totem.use", 1.2)]),
                         "conditions": {"unlocking": [unlocked("skill_passive"), has_tag("gl_life_ready"),
                                                      {"type": "palladium:health", "max_health": 1.5}]}}}),
                [("life_wave", "Life Wave", "A wave of life heals every living thing within 10 blocks and burns the undead.",
                  "life_aura", "minecraft:glistering_melon_slice", 150, 160, [
                      "effect give @e[distance=..10,type=!minecraft:item,type=!minecraft:experience_orb] "
                      "minecraft:instant_health 1 1 true", "particle minecraft:end_rod ~ ~1 ~ 4 1 4 0.05 150 force",
                      sound("minecraft:block.beacon.activate", 1.4)]),
                 ("regrowth", "Regrowth", "The ground around you comes to life: dirt turns to grass, cobblestone to moss.",
                  "life_growth", "minecraft:bone_meal", 60, 40, [
                      "fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:grass_block replace minecraft:dirt",
                      "fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:grass_block replace minecraft:coarse_dirt",
                      "fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:moss_block replace minecraft:cobblestone",
                      "particle minecraft:happy_villager ~ ~0.5 ~ 5 0.5 5 0 200 force",
                      sound("minecraft:item.bone_meal.use", 1.0)]),
                 ("breath_of_life", "Breath of Life", "Every player within 12 blocks gains 8 extra hearts and regenerates.",
                  "healing_touch", "minecraft:totem_of_undying", 200, 600, [
                      f"effect give {ALLIES.format(r=12)} minecraft:absorption 60 3 true",
                      f"effect give {ALLIES.format(r=12)} minecraft:regeneration 10 1 true",
                      "particle minecraft:end_rod ~ ~1 ~ 3 1 3 0.02 100 force", sound("minecraft:item.totem.use", 1.6)]),
                 ("light_of_creation", "Light of Creation", "Ultimate: a blaze of pure life heals everything within 20 "
                  "blocks and scorches the undead.", "overload", "minecraft:nether_star", 600, 1200, [
                      "particle minecraft:end_rod ~ ~1 ~ 8 3 8 0.05 500 force", "particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force",
                      "effect give @e[distance=..20,type=!minecraft:item,type=!minecraft:experience_orb] "
                      "minecraft:instant_health 1 3 true",
                      f"effect give {ALLIES.format(r=20)} minecraft:regeneration 20 1 true",
                      sound("minecraft:block.beacon.activate", 0.6)])])
    # nekron
    minion = ('{Tags:["gl_dead_minion","gl_dead_new"],Team:"gl_dead",PersistenceRequired:1b,'
              'DeathLootTable:"minecraft:empty",CustomName:\'{"text":"Risen Dead","color":"dark_gray"}\'}')
    raise_dead = ["team join gl_dead @s", *[f"summon minecraft:{m} ~ ~ ~ {minion}" for m in ("zombie", "zombie",
                                                                                          "skeleton", "skeleton")],
                  "effect give @e[tag=gl_dead_new] minecraft:strength infinite 1 true",
                  "effect give @e[tag=gl_dead_new] minecraft:fire_resistance infinite 0 true",
                  "spreadplayers ~ ~ 1 3 false @e[tag=gl_dead_new,distance=..4]",
                  f"scoreboard players set @e[tag=gl_dead_new] gl_life 600",
                  "execute at @e[tag=gl_dead_new] run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.02 30 force",
                  "tag @e[tag=gl_dead_new] remove gl_dead_new"]
    return (("Deathless", "The dead don't hunger, wither or sicken: no hunger, wither or poison.",
             "minecraft:rotten_flesh", {
                 "deathless": pulse(100, ["effect give @s minecraft:saturation 1 0 true",
                                          *[f"effect clear @s minecraft:{x}" for x in ("wither", "poison", "hunger")]])}),
            [("black_hand", "Black Hand", "A black hand drags the nearest creature within 12 blocks to you and withers it.",
              "heart_rip", "minecraft:wither_skeleton_skull", 150, 120, user([f"function {NS}:host_cx/black/hand"])),
             ("raise_dead", "Raise the Dead", "Four of the dead rise to fight for you for 30 seconds.", "raise_dead",
              "minecraft:zombie_head", 300, 1200, raise_dead + [sound("minecraft:entity.zombie_villager.cure", 0.6)]),
             ("deaths_touch", "Death's Touch", "Toggle: everything within 6 blocks slowly withers while your power lasts.",
              "death_aura", "minecraft:wither_rose", 1, None, {
                  **command(), "energy_bar_usage": usage(1), "conditions": {"enabling": toggle()}}),
             ("blackest_night", "Blackest Night", "Ultimate: plunge everything within 16 blocks into death, and raise "
              "the dead.", "overload", "minecraft:sculk_catalyst", 600, 1200, user([
                  "particle minecraft:soul ~ ~1 ~ 6 2 6 0.05 400 force",
                  f"execute as {T(16)} run damage @s 16 minecraft:magic by @p[tag=gl_user]",
                  f"effect give {T(16)} minecraft:wither 10 2 true", f"effect give {T(16)} minecraft:darkness 10 0 true",
                  *raise_dead, sound("minecraft:entity.wither.spawn", 0.8)]))])


def host_power(e):
    """The host's power: a copy of its corps' A New Corps ring power (the same tree, bar texture and background, every
    ring ability, all working without a ring), made stronger, with the entity's own branches beside it."""
    k = Power(e)
    key, rgb, name, corps = e.key, e.rgb, e.name, e.corps
    pid, bar, ring_name = f"{NS}:host_{key}", CORPS[corps]["bar"], CORPS[corps]["name"]
    power, root = trees.clone_ring(corps, pid)
    trees.raise_caps(power)
    ab = k.abilities = power["abilities"]
    hunt = f" Beware: {name} hunts its hosts down and sometimes takes control of you." if e.kind == "hunt" else ""

    # --- the suit node is the entity: its key shows its suit, like a ring's
    ab[root].update({
        "title": k.tr("host_root", name),
        "description": k.tr("host_root.description",
                            f"You host {name}, {e.title}. Everything the {ring_name} ring does is yours, stronger, "
                            f"no ring needed, and its light refills on its own. Toggle this to wear {name}'s form. "
                            f"Give it up with Release or by saying \"I release you\". Another player can draw it out "
                            f"of you by sneaking with a corps' lantern and staring at you for five seconds. After you "
                            f"lose it, no entity will choose you for an hour." + hunt)})

    # --- stronger than the ring: a bigger bar that refills on its own, and beams half again as strong
    bars = power["energy_bars"]
    bars[bar] = {**bars[bar], "max": HOST_MAX, "auto_increase_per_tick": BASE_REGEN}
    max_set = re.compile(rf"^(energybar max set @s {re.escape(pid)} {bar} )(\d+)$")
    for a in ab.values():
        for field in ("first_tick_commands", "commands", "last_tick_commands"):
            if field in a:
                a[field] = [max_set.sub(lambda m: m[1] + str(int(int(m[2]) * MAX_SCALE)), c) for c in a[field] or []]
        if a.get("type") == "palladium:energy_beam" and isinstance(a.get("damage"), (int, float)):
            a["damage"] = round(a["damage"] * BEAM_SCALE)
            if isinstance(a.get("description"), str):
                a["description"] = re.sub(r"Damage: (\d+)", lambda m: f"Damage: {round(int(m[1]) * BEAM_SCALE)}",
                                          a["description"])

    # --- the host's body, form and aura (its form shows while the entity node is on)
    def attr(akey, attribute, amount, conds=None):
        k.hidden(akey, {"type": "palladium:attribute_modifier", "attribute": attribute, "amount": amount, "operation": 0,
                        "uuid": trees.uuid_for(f"{pid}.{akey}"),
                        **({"conditions": {"unlocking": one(conds)}} if conds else {})})

    attr("host_health", "minecraft:generic.max_health", 20)
    attr("host_armor", "minecraft:generic.armor", 6)
    attr("host_toughness", "minecraft:generic.armor_toughness", 4)
    light = hexcolor(rgb if corps != "black" else (150, 155, 170))
    form = trees.enabled(root)
    k.hidden("host_aura", {"type": "gravecore:particle_aura", "count": 3, "start_hex": light,
                           "end_hex": hexcolor(tuple(min(255, int(v * 1.3)) for v in rgb)), "aura_type": "aura",
                           "particle_type": "smoke", "particle_size": 0.8, "visibility": 0.25,
                           "conditions": {"enabling": form}})
    k.hidden("host_glow", {"type": "palladium:entity_glow", "mode": "self", "color": light,
                           "conditions": {"enabling": [form, {"type": "palladium:is_flying"}]}})
    k.hidden("host_suit", {"type": "palladium:render_layer", "render_layer": f"{NS}:hosts/{key}",
                           "conditions": {"enabling": form}})
    k.hidden("host_suit_skin", {"type": "palladium:hide_body_part", "body_parts": [
        "right_arm_overlay", "left_arm_overlay", "right_leg_overlay", "left_leg_overlay", "chest_overlay",
        "head_overlay"], "affects_first_person": True, "conditions": {"enabling": form}})
    # the entity is an endless source: its power is full whenever it comes to you (or you log back in)
    k.hidden("host_fill", {**command(first=[f"energybar value add @s {pid} {bar} 100000"])})

    lo, hi = trees.occupied(power)
    right, left = hi + trees.STEP, lo - trees.STEP
    index = iter(range(trees.free_index(power), 100))

    # --- the entity's branch (right of the ring's tree): its passive, three abilities and its ultimate
    passive, abilities = host_kits(e)
    pname, pdesc, picon, pabilities = passive
    ab["entity_tree"] = trees.node(k.tr("entity_tree", f"{name}'s Power"),
                                   k.tr("entity_tree.description", f"What {name} adds to the {ring_name} ring's "
                                        "light: its own nature and abilities."),
                                   HOST_ICON[key], (right, -0.5), ["skilltree"])
    ab["skill_passive"] = trees.node(k.tr("skill_passive", pname), k.tr("skill_passive.description", pdesc),
                                     picon, (right, 0), ["entity_tree"], 10)
    for pkey, pjson in pabilities.items():  # every part of the passive comes with its node
        conds = dict(pjson.get("conditions", {}))
        own = conds.get("unlocking")
        own = [] if own is None else (own if isinstance(own, list) else [own])
        if unlocked("skill_passive") not in own:
            own = [unlocked("skill_passive")] + own
        conds["unlocking"] = one(own)
        k.hidden(pkey, {**pjson, "conditions": conds})
    if key == "ophidian":
        attr("avarice_luck", "minecraft:generic.luck", 5, [unlocked("skill_passive")])
    if key == "ion":
        attr("indomitable", "minecraft:generic.knockback_resistance", 1, [unlocked("skill_passive")])
    if key == "butcher":
        attr("bloodlust", "minecraft:generic.attack_damage", 4, [unlocked("skill_passive")])
    if key == "nekron":
        k.pulse("deaths_touch_pulse", "deaths_touch", 40, [
            f"effect give {OTHERS.format(r=6)} minecraft:wither 3 0 true",
            "particle minecraft:soul ~ ~1 ~ 3 1 3 0.01 20 force"])
    parent = "skill_passive"
    for n, (akey, aname, adesc, glyph, item, cost, cooldown, payload) in enumerate(abilities):
        ultimate = n == 3
        if isinstance(payload, list):
            payload = {**command(first=payload), "conditions": {"enabling": action(cooldown)}}
        elif cooldown and "conditions" not in payload:
            payload = {**payload, "conditions": {"enabling": action(cooldown)}}
        payload = spend(payload, cost)
        desc = (("Ultimate: " if ultimate and not adesc.startswith("Ultimate") else "") + adesc
                + f" Costs {cost} {CORPS[corps]['emotion'].lower()}" + ("" if cooldown else " a tick") + ".")
        ab[akey] = trees.node(k.tr(akey, aname), k.tr(akey + ".description", desc), k.glyph(glyph, item),
                              (right, 0.5 * (n + 1)), [parent], (15, 20, 25, 35)[n], payload, next(index))
        parent = akey

    # --- its light (left of the ring's tree): Empower Ring, Living Lantern, Forge Ring and its hard-light shapes
    battery, ring = CORPS[corps]["battery"], f"{NS}:{CORPS[corps]['ring']}"
    ab["light_tree"] = trees.node(k.tr("light_tree", f"{name}'s Light"),
                                  k.tr("light_tree.description", f"{name} is a source of {ring_name} light: it fills "
                                       "the rings of its color, forges new ones, and shapes more than any ring can."),
                                  battery, (left, -0.5), ["skilltree"])
    ab["empower_ring"] = trees.node(
        k.tr("empower_ring", "Empower Ring"),
        k.tr("empower_ring.description", f"Look at a {ring_name} ring bearer within 24 blocks: +{EMPOWER_GIVE} charge "
             f"to their ring for {EMPOWER_COST} of yours."), battery, (left, 0), ["light_tree"], 10,
        {**command(first=[f"function {NS}:host/{key}/empower"]),
         "conditions": {"enabling": [action(60), charge(EMPOWER_COST)]}}, next(index))
    ab["living_lantern"] = trees.node(
        k.tr("living_lantern", "Living Lantern"),
        k.tr("living_lantern.description", f"Toggle: become a living {ring_name} lantern. {ring_name} rings within 8 "
             f"blocks recharge (+{LANTERN_TRICKLE} a second), and a bearer who sneaks beside you recites their oath for "
             f"a full charge ({OATH_COST} of yours, once every {OATH_COOLDOWN} seconds each). Costs "
             f"{LANTERN_COST * 20} a second."), k.glyph("hope_aura", ring), (left, 0.5), ["empower_ring"], 15,
        {**command(first=["tag @s add gl_living_lantern"], last=["tag @s remove gl_living_lantern"]),
         "energy_bar_usage": usage(LANTERN_COST), "conditions": {"enabling": [toggle(), charge(LANTERN_COST)]}},
        next(index))
    ab["forge_ring"] = trees.node(
        k.tr("forge_ring", "Forge Ring"),
        k.tr("forge_ring.description", f"Forge a new {ring_name} ring from {name}'s light, for someone worthy, no "
             f"lantern needed. Costs {FORGE_COST}; once every {FORGE_COOLDOWN // 1200} minutes."), ring, (left, 1),
        ["living_lantern"], 25,
        spend({**command(first=[f"function {NS}:host/{key}/forge"]),
               "conditions": {"enabling": action(FORGE_COOLDOWN)}}, FORGE_COST), next(index))
    children = []
    for n, item in enumerate(WHEEL_ITEMS[key]):
        iid, iname, offhand = item[0], item[1], len(item) > 2
        nbt = f"{{CustomTag:{corps},fl_host:1b}}"
        give = (f"item replace entity @s weapon.offhand with {NS}:{iid}{nbt}" if offhand else
                f"give @s {NS}:{iid}{nbt} {ARROW_COUNT if iid == 'lovearrow' else 1}")
        enabling = [key_action(30, empty_hand=not offhand)]
        if offhand:
            enabling.append({"type": "palladium:empty_slot", "slot": "offhand"})
        ck = f"hard_light_{n}"
        children.append(ck)
        k.hidden(ck, {**command(first=[give, sound("minecraft:block.beacon.power_select", 1.8)]),
                      "title": k.tr(ck, iname), "icon": f"{NS}:{iid}",
                      "conditions": {"unlocking": unlocked("hard_light"), "enabling": enabling}})
    for n, (path, wname, cost, icon) in enumerate(WHEEL_WORLD.get(key, [])):
        ck = f"hard_shape_{n}"
        children.append(ck)
        k.hidden(ck, {**command(first=["tag @s add gl_user", f"function {NS}:host_cx/{path}", "tag @s remove gl_user"]),
                      "title": k.tr(ck, wname), "icon": icon, "energy_bar_usage": usage(cost),
                      "conditions": {"unlocking": unlocked("hard_light"),
                                     "enabling": [key_action(60), charge(cost)]}})
    shapes = "".join(f", {w[1]}" for w in WHEEL_WORLD.get(key, []))
    ab["hard_light"] = trees.node(
        k.tr("hard_light", "Hard Light"),
        k.tr("hard_light.description", f"Hold: a second construct wheel, shaped by {name}: "
             + ", ".join(i[1] for i in WHEEL_ITEMS[key]) + shapes + "."),
        k.glyph("constructs", f"{NS}:{WHEEL_ITEMS[key][0][0]}"), (left, 1.5), ["forge_ring"], 20,
        {"type": "palladium:ability_wheel", "abilities": children, "texture": "null", "disable_mouse_scrolling": False,
         "conditions": {"enabling": [held()]}}, next(index))

    # --- always on the bar: Release and the Emotional Spectrum menu
    k.bar("release", {**command(first=[f"function {NS}:entity/release_ask"]), "conditions": {"enabling": action(40)}},
          f"Release {name}", k.glyph("revoke", "minecraft:barrier"), next(index),
          desc=f"Give {name} up. No entity will choose you for an hour afterwards.")
    k.bar("emotions", {**command(first=[f"function {NS}:emotion/menu"]), "conditions": {"enabling": action(20)}},
          "Emotional Spectrum", k.glyph("emotional_sight", "minecraft:nether_star"), next(index),
          desc="Your emotions, what raised them, and their quests.")

    power.update({"name": {"translate": f"power.{NS}.host_{key}"}, "icon": HOST_ICON[key], "persistent_data": True})
    # everything we added spends the ring's bar (the kits were written against BAR)
    power = json.loads(json.dumps(power).replace(f'"energy_bar": "{BAR}"', f'"energy_bar": "{bar}"'))
    return power, k.lang


def spend(payload, cost):
    """An ability that spends `cost` of the host's bar: needs that much to start, and pays it (once for an action,
    every tick for a held or toggled one)."""
    if not cost:
        return payload
    payload = copy.deepcopy(payload)
    conds = payload.setdefault("conditions", {})
    enabling = conds.get("enabling", [])
    enabling = enabling if isinstance(enabling, list) else [enabling]
    conds["enabling"] = enabling + [charge(cost)]
    payload.setdefault("energy_bar_usage", usage(cost))
    return payload


def suit_layer(key):
    folder, texture, glow, cape = HOST_SUITS[key]
    slim = {"SLIM": {"type": "palladium:small_arms", "true_value": "slim", "false_value": "steve"}}
    layers = [{"model_layer": {"normal": f"{NS}:humanoid", "slim": f"{NS}:humanoid_slim"},
               "texture": {"base": f"{NS}:textures/models/skins/{folder}/#SLIM/{texture}.png", "variables": slim}}]
    if glow:
        layers.append({"model_layer": "palladium:humanoid#tight_suit", "render_type": "glow",
                       "texture": {"base": f"{NS}:textures/models/skins/{folder}/#SLIM/{glow}.png", "variables": slim}})
    if cape:
        cape_json = json.loads((BASE / f"assets/{NS}/palladium/render_layers/{cape}.json").read_text(encoding="utf-8"))
        layers += cape_json["layers"]
    return {"type": "palladium:compound", "layers": layers}


TAGS = {}  # item tags the functions use: path under tags/items -> items


def write_tag(path, items):
    TAGS[path] = items


def functions():
    """{function path: lines} and the tick and second lines for the hosts' ring abilities."""
    fn, second = {}, []
    for e in entities.ENTITIES:
        key, corps = e.key, e.corps
        data = CORPS[corps]
        power, bar = f"{NS}:{data['power']}", data["bar"]
        bearer = f"gl_{corps}"
        col = hexcolor(e.rgb if corps != "black" else (170, 175, 190))
        fx = e.rgb if corps != "black" else (150, 155, 170)
        ray = ["tag @s add gl_user", "scoreboard players set #hit gl_tmp 0"]
        for d in range(1, 25):
            ray.append(f"execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^{d} positioned ~ ~-0.9 ~ "
                       f"as @a[tag={bearer},tag=!gl_user,distance=..1.4,limit=1,sort=nearest] at @s run "
                       f"function {NS}:host/{key}/empower_hit")
        fn[f"host/{key}/empower"] = ray + [
            "execute if score #hit gl_tmp matches 0 run title @s actionbar " + json.dumps(
                {"text": f"Look at a {data['name']} ring bearer to empower their ring.", "color": "gray"}),
            f"execute if score #hit gl_tmp matches 1 run energybar value subtract @s {NS}:host_{key} {bar} {EMPOWER_COST}",
            f"execute if score #hit gl_tmp matches 1 anchored eyes run particle minecraft:dust {dust(fx, 1.5)} "
            "^ ^ ^1 0.2 0.2 0.2 0 30 force",
            "tag @s remove gl_user"]
        fn[f"host/{key}/empower_hit"] = [  # as and at the bearer
            "scoreboard players set #hit gl_tmp 1",
            f"energybar value add @s {power} {bar} {EMPOWER_GIVE}",
            burst(fx, 1.5, "0.4 0.8 0.4", 60), sound("minecraft:block.beacon.power_select", 1.6),
            "title @s actionbar " + json.dumps([{"text": f"{e.name}'s light fills your ring.", "color": col}]),
        ]
        oath_lines = [tellraw("@a[distance=..16]", ([{"selector": "@s", "color": col}, {"text": ": ", "color": "gray"}]
                                                    if i == 0 else [{"text": "   "}])
                              + [{"text": line, "color": col, "italic": True}])
                      for i, line in enumerate(data["oath"])]
        fn[f"host/{key}/lantern_pulse"] = [  # as and at a host whose Living Lantern is lit, every second
            "tag @s add gl_lantern_host",
            f"execute as @a[tag={bearer},distance=..8] run energybar value add @s {power} {bar} {LANTERN_TRICKLE}",
            f"execute as @a[tag={bearer},distance=..8] at @s run particle minecraft:dust {dust(fx, 1.0)} ~ ~1 ~ 0.3 0.6 "
            "0.3 0 6 force",
            f"execute as @a[tag={bearer},distance=..3,predicate={NS}:entity/sneaking,scores={{gl_lcd=..0}}] at @s run "
            f"function {NS}:host/{key}/oath",
            burst(fx, 1.0, "1.5 1 1.5", 12),
            "tag @s remove gl_lantern_host",
        ]
        fn[f"host/{key}/oath"] = oath_lines + [  # as a bearer beside the living lantern
            f"energybar value add @s {power} {bar} {OATH_GIVE}",
            f"scoreboard players set @s gl_lcd {OATH_COOLDOWN}",
            f"energybar value subtract @a[tag=gl_lantern_host,limit=1] {NS}:host_{key} {bar} {OATH_COST}",
            burst(fx, 2.0, "0.6 1 0.6", 120), sound("minecraft:block.beacon.activate", 1.4),
        ]
        second.append(f"execute as @a[tag=gl_living_lantern,tag=gl_host_{key}] at @s run "
                      f"function {NS}:host/{key}/lantern_pulse")
        fn[f"host/{key}/forge"] = [
            f"execute anchored eyes positioned ^ ^ ^3 run function {NS}:{data['forge']}",
            "tellraw @a[distance=..32] " + json.dumps([{"selector": "@s", "color": col},
                                                        {"text": f" forges a new {data['name']} ring from {e.name}'s "
                                                                 "light!", "color": "white"}]),
        ]
        # on release, the ring constructs the host made go too (unless they also wear a ring of that color)
        clear = []
        for tag, items in sorted(trees.ring_constructs(corps).items()):
            write_tag(f"host_constructs/{key}_{tag}", sorted(items))
            clear.append(f"execute unless entity @s[tag=gl_{trees.COLOR_CORPS[tag]}] run "
                         f"clear @s #{NS}:host_constructs/{key}_{tag}{{CustomTag:\"{tag}\"}}")
        fn[f"host/{key}/release_clear"] = clear or ["# nothing to clear"]
    second += ["scoreboard players add @a gl_lcd 0", "scoreboard players remove @a[scores={gl_lcd=1..}] gl_lcd 1",
               "tag @a[tag=gl_living_lantern,tag=!gl_host] remove gl_living_lantern"]
    return fn, ["scoreboard objectives add gl_lcd dummy"], second


def assets(write, lang):
    """The host powers, their suits and the construct tag; returns the items the hosts' constructs use."""
    items = set()
    for e in entities.ENTITIES:
        power, power_lang = host_power(e)
        write(f"data/{NS}/palladium/powers/host_{e.key}.json", power)
        lang.update(power_lang)
        lang[f"power.{NS}.host_{e.key}"] = f"{e.name} (host)"
        write(f"assets/{NS}/palladium/render_layers/hosts/{e.key}.json", suit_layer(e.key))
        items.update(f"{NS}:{i[0]}" for i in WHEEL_ITEMS[e.key])
    write(f"data/{NS}/tags/items/host_constructs.json", {"replace": False, "values": sorted(items)})
    for path, values in TAGS.items():
        write(f"data/{NS}/tags/items/{path}.json", {"replace": False, "values": values})
    return sorted(items)
