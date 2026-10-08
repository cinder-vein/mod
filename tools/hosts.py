"""Host powers for the emotional spectrum entities: final_lanterns:host_<entity> (see entities.py for how hosting works).

A host needs no ring. Their power refills on its own, always, and faster than any ring's (BASE_REGEN a tick; A New
Corps' rings regenerate 2 at best, or 5 while empowered by hope). The power has its own skill tree:

- the body: Vitality, Might, Flight and the entity's own passive;
- its three abilities and its ultimate;
- its light, borrowed from that corps' A New Corps ring: the ring's beam, a construct wheel of that corps' construct
  weapons (plus the entity's world constructs) and Forge Ring, which forges a new ring of its color;
- its bond with the rings of its color: Empower Ring fills the ring of the bearer you look at, and Living Lantern
  makes you a lantern: bearers near you recharge, and sneaking beside you recites their oath for a full charge;
- its reserves: Deep Reserves and Wellspring.

The host wears the entity's own suit (A New Corps' suit of its best-known host) and its aura; Mortal Form hides it.
"""
import copy
import hashlib
import json
from pathlib import Path

import entities
import icons
from common import CORPS, HOSTILE, NS, TARGETS, burst, dust, hexcolor, sound, tellraw

BASE = Path(__file__).resolve().parent.parent / "base"
BAR = "entity_power"
BASE_MAX, RESERVES_MAX = 4000, 6000
BASE_REGEN, WELLSPRING_REGEN = 3, 3  # per tick; Wellspring adds its own on top
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

    def node(self, key, name, desc, icon, pos, parents, xp):
        """A skill-tree node bought with XP levels in the powers menu."""
        self.abilities[key] = {
            "type": "palladium:dummy", "title": self.tr(key, name),
            "description": self.tr(key + ".description", desc + f" Costs {xp} XP levels."),
            "icon": icon, "hidden_in_bar": True, "gui_position": list(pos),
            "conditions": {"unlocking": [*(unlocked(p) for p in parents),
                                         {"type": "palladium:experience_level_buyable", "xp_level": xp}]},
        }

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


def retarget(ability, corps, key):
    """An A New Corps ring ability made to run on the host's power: its energy bar becomes the host's, and the
    conditions that only make sense inside that ring's power (its other abilities, its effects) are dropped."""
    ring_bar = CORPS[corps]["bar"]
    ability.pop("gui_position", None)
    if "energy_bar_usage" in ability:
        ability["energy_bar_usage"] = {**ability["energy_bar_usage"], "energy_bar": BAR}

    def keep(cond):
        t = cond.get("type")
        if t in ("palladium:ability_unlocked", "palladium:ability_enabled", "palladium:has_effect",
                 "palladium:objective_score", "palladium:animation_timer_ability"):
            return None
        if t in ("palladium:not", "palladium:or", "palladium:and"):
            inner = [c for c in (keep(c) for c in cond.get("conditions", [])) if c]
            return {**cond, "conditions": inner} if inner else None
        if t == "palladium:energy_bar":
            return {"type": "palladium:energy_bar", "energy_bar": BAR, "min": cond.get("min", 1)}
        return cond

    conds = {}
    for kind, value in ability.get("conditions", {}).items():
        value = value if isinstance(value, list) else [value]
        kept = [c for c in (keep(c) for c in value) if c]
        if kept:
            conds[kind] = kept
    ability["conditions"] = conds
    for field in ("first_tick_commands", "commands", "last_tick_commands", "commands_on_block_hit",
                  "commands_on_entity_hit"):
        if field in ability:
            ability[field] = [c.replace(f"{NS}:{CORPS[corps]['power']} {ring_bar}", f"{NS}:host_{key} {BAR}")
                              for c in ability[field]]
    return ability


def host_power(e):
    k = Power(e)
    key, rgb, name, corps = e.key, e.rgb, e.name, e.corps
    ring_name = CORPS[corps]["name"]
    hunt = f" Beware: {name} hunts its hosts down and sometimes takes control of you." if e.kind == "hunt" else ""
    k.abilities["host_root"] = {
        "type": "palladium:dummy", "title": k.tr("host_root", name),
        "description": k.tr("host_root.description",
                            f"You host {name}, {e.title}. Its power is yours, no ring needed, and it refills on its "
                            f"own, always. Grow it here with XP levels. Give it up with Release or by saying \"I "
                            f"release you\". Another player can draw it out of you by sneaking with a corps' lantern "
                            f"and staring at you for five seconds. After you lose it, no entity will choose you for "
                            f"an hour." + hunt),
        "icon": HOST_ICON[key], "hidden_in_bar": True, "gui_position": [0, 0]}

    def attr(akey, attribute, amount, conds=None):
        k.hidden(akey, {"type": "palladium:attribute_modifier", "attribute": attribute, "amount": amount, "operation": 0,
                        "uuid": "6c7afe00-1a2b-4c3d-8e4f-" + hashlib.md5(f"{key}.{akey}".encode()).hexdigest()[:12],
                        **({"conditions": {"unlocking": one(conds)}} if conds else {})})

    # --- the body, always: hearts, armor, the entity's aura and its suit
    attr("host_health", "minecraft:generic.max_health", 20)
    attr("host_armor", "minecraft:generic.armor", 6)
    attr("host_toughness", "minecraft:generic.armor_toughness", 4)
    light = hexcolor(rgb if corps != "black" else (150, 155, 170))
    k.hidden("host_aura", {"type": "gravecore:particle_aura", "count": 3, "start_hex": light,
                           "end_hex": hexcolor(tuple(min(255, int(v * 1.3)) for v in rgb)), "aura_type": "aura",
                           "particle_type": "smoke", "particle_size": 0.8, "visibility": 0.25})
    k.hidden("host_glow", {"type": "palladium:entity_glow", "mode": "self", "color": light,
                           "conditions": {"enabling": [unlocked("skill_flight"), {"type": "palladium:is_flying"}]}})
    form = NOT(enabled("mortal_form"))
    k.hidden("host_suit", {"type": "palladium:render_layer", "render_layer": f"{NS}:hosts/{key}",
                           "conditions": {"enabling": form}})
    k.hidden("host_suit_skin", {"type": "palladium:hide_body_part", "body_parts": [
        "right_arm_overlay", "left_arm_overlay", "right_leg_overlay", "left_leg_overlay", "chest_overlay",
        "head_overlay"], "affects_first_person": True, "conditions": {"enabling": form}})
    # the entity is an endless source: its power is full whenever it comes to you (or you log back in)
    k.hidden("host_fill", {**command(first=[f"energybar value add @s {NS}:host_{key} {BAR} 100000"])})

    # --- skill tree: the body (left), the abilities (middle), the light, the bond and the reserves (right)
    k.node("skill_vitality_1", "Vitality I", "+10 hearts.", "minecraft:golden_apple", (-3, 1), ["host_root"], 8)
    k.node("skill_vitality_2", "Vitality II", "Another +10 hearts.", "minecraft:enchanted_golden_apple", (-3, 2),
           ["skill_vitality_1"], 16)
    attr("vitality_1", "minecraft:generic.max_health", 20, [unlocked("skill_vitality_1")])
    attr("vitality_2", "minecraft:generic.max_health", 20, [unlocked("skill_vitality_2")])
    k.node("skill_might_1", "Might I", "+4 attack and punch damage.", "minecraft:iron_sword", (-2, 1), ["host_root"], 8)
    k.node("skill_might_2", "Might II", "Another +4 attack and punch damage.", "minecraft:netherite_sword", (-2, 2),
           ["skill_might_1"], 16)
    for n in (1, 2):
        attr(f"might_{n}", "minecraft:generic.attack_damage", 4, [unlocked(f"skill_might_{n}")])
        attr(f"might_{n}_fists", "palladium:punch_damage", 4, [unlocked(f"skill_might_{n}")])
    k.node("skill_flight", "Flight", f"Fly on {name}'s power.", "minecraft:feather", (-1, 1), ["host_root"], 5)
    attr("flight", "palladium:flight_speed", 1.0, [unlocked("skill_flight")])
    attr("flight_flexibility", "palladium:flight_flexibility", 5, [unlocked("skill_flight")])
    attr("heroic_flight", "palladium:heroic_flight_type", 1, [unlocked("skill_flight")])

    passive, abilities = host_kits(e)
    pname, pdesc, picon, pabilities = passive
    k.node("skill_passive", pname, pdesc, picon, (-1, 2), ["skill_flight"], 10)
    for pkey, pjson in pabilities.items():  # every part of the passive needs its node
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

    # the entity's own abilities: a chain down the middle; slots 3-5 and the ultimate on 6
    parent = "host_root"
    for n, (akey, aname, adesc, glyph, item, cost, cooldown, payload) in enumerate(abilities):
        ultimate = n == 3
        xp = (5, 10, 15, 30)[n]
        k.node(f"skill_{akey}", aname, adesc, item, (0, 1 + n), [parent], xp)
        parent = f"skill_{akey}"
        if isinstance(payload, list):
            payload = {**command(first=payload), "conditions": {"enabling": action(cooldown)}}
        elif cooldown and "conditions" not in payload:
            payload = {**payload, "conditions": {"enabling": action(cooldown)}}
        k.bar(akey, payload, aname, k.glyph(glyph, item), (2, 3, 4, 5)[n], node=f"skill_{akey}", cost=cost,
              desc=("Ultimate: " if ultimate and not adesc.startswith("Ultimate") else "") + adesc
              + f" Costs {cost} power" + ("" if cooldown else " a tick") + ".")

    # --- the light of its corps: beam, construct wheel, Forge Ring
    beam = retarget(anc_ability(corps, CORPS[corps]["beam"]), corps, key)
    beam_icon = beam.get("icon", HOST_ICON[key])
    k.node("skill_beam", f"{ring_name} Beam", f"Hold to fire the {ring_name} ring's beam, fed by {name}.", beam_icon,
           (1, 1), ["host_root"], 5)
    beam.pop("title", None)
    beam.pop("description", None)
    enabling = beam["conditions"].setdefault("enabling", [])
    if not any(c.get("type") == "palladium:held" for c in enabling):
        enabling.insert(0, held())
    k.bar("beam", beam, f"{name}'s Beam", beam_icon, 0, node="skill_beam",
          desc=f"Hold: the {ring_name} beam, {beam.get('damage', 0)} damage.")
    k.hidden("beam_aim", {"type": "palladium:aim", "time": 1, "arm": "main_arm",
                          "conditions": {"enabling": enabled("beam")}})
    wheel_icon = f"{NS}:textures/icons/slots/{CORPS[corps]['power']}3.png"
    if not (BASE / f"assets/{NS}/textures/icons/slots/{CORPS[corps]['power']}3.png").exists():
        wheel_icon = f"{NS}:{WHEEL_ITEMS[key][0][0]}"
    k.node("skill_constructs", "Constructs", f"Hold the construct key and pick a construct of {name}'s light: "
           + ", ".join(i[1] for i in WHEEL_ITEMS[key]) + "".join(f", {w[1]}" for w in WHEEL_WORLD.get(key, [])) + ".",
           wheel_icon, (1, 2), ["skill_beam"], 10)
    children = []
    for n, item in enumerate(WHEEL_ITEMS[key]):
        iid, iname, offhand = item[0], item[1], len(item) > 2
        nbt = f"{{CustomTag:{corps},fl_host:1b}}"
        give = (f"item replace entity @s weapon.offhand with {NS}:{iid}{nbt}" if offhand else
                f"give @s {NS}:{iid}{nbt} {ARROW_COUNT if iid == 'lovearrow' else 1}")
        enabling = [key_action(30, empty_hand=not offhand)]
        if offhand:
            enabling.append({"type": "palladium:empty_slot", "slot": "offhand"})
        ck = f"construct_{n}"
        children.append(ck)
        k.hidden(ck, {**command(first=[give, sound("minecraft:block.beacon.power_select", 1.8)]),
                      "title": k.tr(ck, iname), "icon": f"{NS}:{iid}", "list_index": 1,
                      "conditions": {"unlocking": unlocked("skill_constructs"), "enabling": enabling}})
    for n, (path, wname, cost, icon) in enumerate(WHEEL_WORLD.get(key, [])):
        ck = f"world_construct_{n}"
        children.append(ck)
        k.hidden(ck, {**command(first=["tag @s add gl_user", f"function {NS}:host_cx/{path}", "tag @s remove gl_user"]),
                      "title": k.tr(ck, wname), "icon": icon, "list_index": 1, "energy_bar_usage": usage(cost),
                      "conditions": {"unlocking": [unlocked("skill_constructs"), charge(cost)],
                                     "enabling": [key_action(60)]}})
    k.bar("constructs", {"type": "palladium:ability_wheel", "abilities": children, "texture": "null",
                         "disable_mouse_scrolling": False, "conditions": {"enabling": [held()]}},
          "Constructs", wheel_icon, 1, node="skill_constructs")
    ring = f"{NS}:{CORPS[corps]['ring']}"
    k.node("skill_forge", "Forge Ring", f"Forge a new {ring_name} ring from {name}'s light, for someone worthy. Costs "
           f"{FORGE_COST} power; once every {FORGE_COOLDOWN // 1200} minutes.", ring, (1, 3), ["skill_constructs"], 25)
    k.bar("forge_ring", {**command(first=[f"function {NS}:host/{key}/forge"]),
                         "conditions": {"enabling": action(FORGE_COOLDOWN)}},
          "Forge Ring", ring, 8, node="skill_forge", cost=FORGE_COST,
          desc=f"Forge a new {ring_name} ring. Costs {FORGE_COST} power.")

    # --- its bond with the rings of its color
    battery = CORPS[corps]["battery"]
    k.node("skill_empower", "Empower Ring", f"Pour {name}'s light into the {ring_name} ring of the bearer you look at "
           f"(within 24 blocks): +{EMPOWER_GIVE} charge for {EMPOWER_COST} power.", battery, (2, 1), ["host_root"], 8)
    k.bar("empower_ring", {**command(first=[f"function {NS}:host/{key}/empower"]),
                           "conditions": {"unlocking": charge(EMPOWER_COST), "enabling": action(60)}},
          "Empower Ring", battery, 6, node="skill_empower",
          desc=f"Look at a {ring_name} ring bearer: +{EMPOWER_GIVE} charge to their ring.")
    k.node("skill_lantern", "Living Lantern", f"Toggle: become a living {ring_name} lantern. {ring_name} rings within 8 "
           f"blocks recharge (+{LANTERN_TRICKLE} a second), and a bearer who sneaks beside you recites their oath for a "
           f"full charge ({OATH_COST} power, once every {OATH_COOLDOWN} seconds each).", ring, (2, 2), ["skill_empower"],
           15)
    k.bar("living_lantern", {**command(first=["tag @s add gl_living_lantern"], last=["tag @s remove gl_living_lantern"]),
                             "energy_bar_usage": usage(LANTERN_COST), "conditions": {"enabling": toggle()}},
          "Living Lantern", k.glyph("hope_aura", ring), 7, node="skill_lantern", cost=LANTERN_COST,
          desc=f"Toggle: {ring_name} rings near you recharge. Costs {LANTERN_COST * 20} power a second.")

    # --- its reserves
    k.node("skill_reserves", "Deep Reserves", f"Your power holds {RESERVES_MAX} instead of {BASE_MAX}.",
           "minecraft:glowstone", (3, 1), ["host_root"], 8)
    k.node("skill_wellspring", "Wellspring", "Your power refills twice as fast.", "minecraft:beacon", (3, 2),
           ["skill_reserves"], 16)
    k.hidden("reserves_apply", {**command(first=[f"scoreboard objectives add glhmax_{key} dummy",
                                                 f"scoreboard players set @s glhmax_{key} {RESERVES_MAX}"]),
                                "conditions": {"unlocking": unlocked("skill_reserves")}})
    k.hidden("wellspring_regen", {"type": "palladium:dummy", "energy_bar_usage": usage(-WELLSPRING_REGEN),
                                  "conditions": {"unlocking": unlocked("skill_wellspring")}})

    # --- always there: Release, the Emotional Spectrum menu, Mortal Form
    k.bar("release", {**command(first=[f"function {NS}:entity/release_ask"]), "conditions": {"enabling": action(40)}},
          f"Release {name}", k.glyph("revoke", "minecraft:barrier"), 9,
          desc=f"Give {name} up. No entity will choose you for an hour afterwards.")
    k.bar("emotions", {**command(first=[f"function {NS}:emotion/menu"]), "conditions": {"enabling": action(20)}},
          "Emotional Spectrum", k.glyph("emotional_sight", "minecraft:nether_star"), 10,
          desc="Your emotions, what raised them, and their quests.")
    k.bar("mortal_form", {**command(), "conditions": {"enabling": toggle()}}, "Mortal Form",
          k.glyph("suit_up", "minecraft:leather_chestplate"), 11, desc=f"Toggle: hide {name}'s form (its suit).")

    power = {
        "name": {"translate": f"power.{NS}.host_{key}"}, "icon": HOST_ICON[key],
        "background": "minecraft:textures/block/black_concrete.png", "gui_display_type": "tree",
        "primary_color": hexcolor(rgb), "secondary_color": hexcolor(tuple(int(v * 0.4) for v in rgb)),
        "persistent_data": True,
        "energy_bars": {BAR: {"max": {"type": "score", "objective": f"glhmax_{key}", "fallback": BASE_MAX},
                              "auto_increase_per_tick": BASE_REGEN, "color": hexcolor(rgb)}},
        "abilities": k.abilities,
    }
    return power, k.lang


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
            f"execute if score #hit gl_tmp matches 1 run energybar value subtract @s {NS}:host_{key} {BAR} {EMPOWER_COST}",
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
            f"energybar value subtract @a[tag=gl_lantern_host,limit=1] {NS}:host_{key} {BAR} {OATH_COST}",
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
    return sorted(items)
