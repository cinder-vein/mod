"""Hard-light constructs, modeled on the construct system of the Green Lantern mod showcase:

- a catalog of constructs in four categories (melee, ranged, defense, utility), unlocked in the
  skill tree, plus one signature construct per corps;
- every construct is formed from the radial construct wheel (hold its key, pick one with the mouse).

Energy Blast and Scan aren't constructs: they sit on the ring's blast-mode bar (see gen_corps.py) and
use the ring functions generated here (ring/<corps>/blast, ring/<corps>/scan).

Held constructs are real items (sword, shield, mace, axe, drill, gatling...): they form in your hand,
drain charge while you hold them, and dissolve when you pick them on the wheel again, run out of
charge or take the ring off. Walls, domes and bridges are temporary hard-light blocks.

gen_corps.py adds the abilities to each corps' power (see construct_abilities there) and merges the
datapack lines returned by generate().
"""
import json

NS = "greenlantern"
STORAGE = f"{NS}:tmp"
BAR = "ring_charge"


# Skill-tree nodes of the construct branch: key -> (name, description, position, parents, xp)
NODES = {
    "constructs": ("Constructs", "Unlocks the construct wheel and the basics: Sword, Tower Shield and Construct Blocks.",
                   (6, 1), ["ring_root"], 5),
    "melee_1": ("Melee Constructs I", "Adds Sword & Shield, Mace and Battle Axe.", (4.5, 2), ["constructs"], 8),
    "melee_2": ("Melee Constructs II", "Adds Giant Fist and Hammer Slam.", (4.5, 3), ["melee_1"], 12),
    "ranged_1": ("Ranged Constructs I", "Adds the Gatling and the Missile Barrage.", (5.5, 2), ["constructs"], 8),
    "ranged_2": ("Ranged Constructs II", "Adds the Cannon.", (5.5, 3), ["ranged_1"], 12),
    "defense_1": ("Defense Constructs I", "Adds the Barrier Wall and the Cage.", (6.5, 2), ["constructs"], 8),
    "defense_2": ("Defense Constructs II", "Adds the Dome.", (6.5, 3), ["defense_1"], 12),
    "utility_1": ("Utility Constructs I", "Adds Scuba Gear and the Mining Drill.", (7.5, 2), ["constructs"], 8),
    "utility_2": ("Utility Constructs II", "Adds the Bridge.", (7.5, 3), ["utility_1"], 12),
    "signature": (None, None, (6, 4), ["melee_2", "ranged_2", "defense_2", "utility_2"], 20),
}


class Construct:
    def __init__(self, key, name, cat, node, cost, cooldown, kind, icon, desc):
        self.key, self.name, self.cat, self.node = key, name, cat, node
        self.cost, self.cooldown, self.kind, self.icon, self.desc = cost, cooldown, kind, icon, desc


# kind: "held" (an item in your hand; press again to dismiss), "toggle" (press again to end),
# "instant" (happens once; the cooldown is in ticks)
CATALOG = [
    Construct("sword", "Sword", "melee", "constructs", 30, 10, "held", f"{NS}:construct_sword",
              "A hard-light sword in your hand."),
    Construct("sword_shield", "Sword & Shield", "melee", "melee_1", 50, 10, "held", f"{NS}:construct_shield",
              "A sword in your main hand and a shield in your offhand."),
    Construct("mace", "Mace", "melee", "melee_1", 40, 10, "held", f"{NS}:construct_mace",
              "A heavy, slow mace that hits very hard."),
    Construct("axe", "Battle Axe", "melee", "melee_1", 40, 10, "held", f"{NS}:construct_axe",
              "A battle axe that also fells trees and breaks shields."),
    Construct("fist", "Giant Fist", "melee", "melee_2", 100, 60, "instant", f"{NS}:construct_fist",
              "A giant fist punches whatever is in front of you into the air."),
    Construct("slam", "Hammer Slam", "melee", "melee_2", 120, 80, "instant", f"{NS}:construct_hammer",
              "A giant hammer slams the ground, hurting and launching everything within 6 blocks."),
    Construct("gatling", "Gatling", "ranged", "ranged_1", 40, 10, "held", f"{NS}:construct_gatling",
              "A gatling gun: hold right-click to fire. Each shot costs 3 charge."),
    Construct("missiles", "Missile Barrage", "ranged", "ranged_1", 120, 80, "instant", "minecraft:firework_rocket",
              "Three missiles that explode on impact (they never break blocks)."),
    Construct("cannon", "Cannon", "ranged", "ranged_2", 150, 100, "instant", f"{NS}:construct_ball",
              "A huge cannonball with a big explosion (it never breaks blocks)."),
    Construct("shield", "Tower Shield", "defense", "constructs", 30, 10, "held", f"{NS}:construct_shield",
              "A shield in your offhand. Block with right-click."),
    Construct("barrier", "Barrier Wall", "defense", "defense_1", 100, 120, "instant", f"{NS}:construct_wall",
              "A 5-wide, 4-high wall of hard light in front of you for 15 seconds."),
    Construct("cage", "Cage", "defense", "defense_1", 150, 100, "instant", f"{NS}:construct_cage",
              "Trap the nearest creature within 12 blocks in a cage."),
    Construct("dome", "Dome", "defense", "defense_2", 200, 300, "instant", "minecraft:glass",
              "A dome of hard light around you for 15 seconds."),
    Construct("blocks", "Construct Blocks", "utility", "constructs", 60, 40, "instant", "minecraft:lime_stained_glass",
              "64 hard-light blocks you can place to build with."),
    Construct("scuba", "Scuba Gear", "utility", "utility_1", 20, 10, "toggle", "minecraft:turtle_helmet",
              "A diving helmet and air tank: breathe, see and swim fast underwater. Drains charge slowly."),
    Construct("drill", "Mining Drill", "utility", "utility_1", 30, 10, "held", f"{NS}:construct_drill",
              "A drill that mines like a netherite pickaxe."),
    Construct("bridge", "Bridge", "utility", "utility_2", 80, 60, "instant", "minecraft:scaffolding",
              "A 3-wide bridge of hard light 16 blocks ahead of you for 30 seconds."),
]

# One signature construct per corps, fitting its emotion. Unlocked by mastering all four branches.
SIGNATURES = {
    "green": Construct("signature", "Construct Train", "melee", "signature", 200, 200, "instant", "minecraft:minecart",
                       "A speeding train of will smashes through everything in a line 14 blocks ahead."),
    "yellow": Construct("signature", "Fear Spikes", "defense", "signature", 200, 200, "instant",
                        "minecraft:pointed_dripstone",
                        "A ring of yellow spikes bursts from the ground: everything within 5 blocks is hurt and terrified."),
    "red": Construct("signature", "Blood Claws", "melee", "signature", 60, 10, "held", f"{NS}:construct_claws",
                     "Fast, burning claws of rage (Fire Aspect II)."),
    "orange": Construct("signature", "Grasping Hands", "utility", "signature", 200, 200, "instant", "minecraft:lead",
                        "Greedy hands drag every hostile mob within 14 blocks to your feet and weaken them."),
    "blue": Construct("signature", "Sanctuary", "defense", "signature", 250, 400, "instant", "minecraft:beacon",
                      "A dome of hope: you and every player within 5 blocks regenerate and resist damage for 15 seconds."),
    "violet": Construct("signature", "Crystal Spear", "ranged", "signature", 120, 60, "instant",
                        "minecraft:amethyst_shard",
                        "A violet crystal spear that seals whatever it hits in crystal for 5 seconds."),
    "indigo": Construct("signature", "Indigo Staff", "melee", "signature", 60, 10, "held", f"{NS}:construct_staff",
                        "The Indigo Tribe's staff: long reach, and while you hold it every player within 6 blocks "
                        "regenerates."),
    "white": Construct("signature", "Radiant Aegis", "defense", "signature", 250, 400, "instant",
                       "minecraft:totem_of_undying",
                       "A shell of pure life: you and every player within 8 blocks gain 12 extra hearts for 30 s."),
    "black": Construct("signature", "Black Hand", "melee", "signature", 150, 120, "instant",
                       "minecraft:wither_skeleton_skull",
                       "A black hand drags the nearest creature within 12 blocks to you and withers it."),
}

# Held construct items: item -> (Palladium item json, display name)
HELD_ITEMS = {
    "construct_sword": ({"type": "palladium:sword", "tier": "minecraft:netherite", "base_damage": 4,
                         "attack_speed": -2.4}, "Construct Sword"),
    "construct_shield": ({"type": "palladium:shield"}, "Construct Shield"),
    "construct_mace": ({"type": "palladium:sword", "tier": "minecraft:netherite", "base_damage": 8,
                        "attack_speed": -3.2}, "Construct Mace"),
    "construct_axe": ({"type": "palladium:axe", "tier": "minecraft:netherite", "base_damage": 6,
                       "attack_speed": -3.0}, "Construct Battle Axe"),
    "construct_drill": ({"type": "palladium:pickaxe", "tier": "minecraft:netherite", "base_damage": 1,
                         "attack_speed": -2.8}, "Construct Mining Drill"),
    "construct_gatling": ({}, "Construct Gatling"),
    "construct_claws": ({"type": "palladium:sword", "tier": "minecraft:netherite", "base_damage": 3,
                         "attack_speed": -1.6}, "Blood Claws"),
    # its +2 reach comes from the Indigo power (forge:entity_reach isn't registered yet when items are built)
    "construct_staff": ({"type": "palladium:sword", "tier": "minecraft:netherite", "base_damage": 5,
                         "attack_speed": -2.6}, "Indigo Staff"),
}
HELD_OF = {"sword": ["construct_sword"], "sword_shield": ["construct_sword", "construct_shield"],
           "mace": ["construct_mace"], "axe": ["construct_axe"], "gatling": ["construct_gatling"],
           "shield": ["construct_shield"], "drill": ["construct_drill"]}
SIGNATURE_HELD = {"red": "construct_claws", "indigo": "construct_staff"}

# 3D hard-light shapes shown by item_display entities (or as projectile models). They grow in,
# then the datapack removes them after `life` ticks.
SHAPES = {
    "fist": {"name": "Fist", "scale": 2.6, "life": 24},
    "hammer": {"name": "Hammer", "scale": 3.2, "life": 24},
    "cage": {"name": "Cage", "scale": 2.4, "life": 120},
    "wall": {"name": "Wall", "scale": 3.2, "life": 100},
    "claw": {"name": "Claw", "scale": 2.8, "life": 24},
    "crystal": {"name": "Crystal", "scale": 2.6, "life": 160},
    "spike": {"name": "Spike", "scale": 2.2, "life": 40},
    "hand": {"name": "Hand", "scale": 2.8, "life": 30},
    "train": {"name": "Train", "scale": 2.4, "life": 14},
    "ball": {"name": "Cannonball", "scale": 1.0, "life": 1},
}
GROWING = [s for s in SHAPES if s not in ("train", "ball")]  # the train slides instead; the ball is a projectile

# your own Greed Constructs and Black Lantern revenants are never targets
OWN_ARMY = "tag=!gl_greed_minion,tag=!gl_dead_minion"
HOSTILE = f"@e[type=#{NS}:greed_prey,{OWN_ARMY},distance=..{{r}}]"
# creatures near a point (not items, frames, paintings, boats, minecarts or projectiles: see NOT_CREATURES),
# never the construct's user (tagged gl_user while it runs) or their own army
TARGETS = f"@e[type=!#{NS}:not_creatures,tag=!gl_user,{OWN_ARMY},distance=..{{r}}"
NOT_CREATURES = [f"minecraft:{t}" for t in (
    "area_effect_cloud", "armor_stand", "arrow", "block_display", "boat", "chest_boat", "chest_minecart",
    "command_block_minecart", "dragon_fireball", "egg", "end_crystal", "ender_pearl", "evoker_fangs",
    "experience_bottle", "experience_orb", "eye_of_ender", "falling_block", "fireball", "firework_rocket",
    "fishing_bobber", "furnace_minecart", "glow_item_frame", "hopper_minecart", "interaction", "item", "item_display",
    "item_frame", "leash_knot", "lightning_bolt", "llama_spit", "marker", "minecart", "painting", "potion",
    "shulker_bullet", "small_fireball", "snowball", "spawner_minecart", "spectral_arrow", "text_display", "tnt",
    "tnt_minecart", "trident", "wither_skull")] + ["palladium:custom_projectile"]


def hexcolor(rgb):
    return "#%02X%02X%02X" % tuple(rgb[:3])


def dust(rgb, size=1.0):
    return "%.2f %.2f %.2f %.1f" % (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, size)


def burst(rgb, size=2.0, spread="1 1 1", count=80, at="~ ~1 ~"):
    return f"particle minecraft:dust {dust(rgb, size)} {at} {spread} 0 {count} force"


def sound(snd, pitch=1.0):
    return f"playsound {snd} player @a[distance=..24] ~ ~ ~ 1 {pitch}"


def tellraw(target, parts):
    return f"tellraw {target} " + json.dumps(parts, separators=(",", ":"))


def actionbar(parts):
    return "title @s actionbar " + json.dumps(parts, separators=(",", ":"))


def construct_cmds(corps_list, corps, shape, where, extra_tags=()):
    """Commands that spawn a display construct. `where` is an `execute ...` prefix that sets the position."""
    n = corps_list.index(corps) + 1
    tags = ",".join(f'"{t}"' for t in ["gl_construct", "gl_new", f"gl_{shape}", *extra_tags])
    nbt = ('{Tags:[%s],item:{id:"%s:construct_%s",Count:1b,tag:{CustomModelData:%d}},'
           'item_display:"none",brightness:{sky:15,block:15},view_range:2f,'
           'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],'
           'scale:[0.2f,0.2f,0.2f]}}') % (tags, NS, shape, n)
    newest = "@e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest]"
    return [f"{where} run summon minecraft:item_display ~ ~ ~ {nbt}",
            f"{where} run tp {newest} ~ ~ ~ ~ 0"]


def all_constructs(corps):
    return CATALOG + [SIGNATURES[corps]]


class Gen:
    """Collects datapack functions while generating."""

    def __init__(self, corps_table):
        self.corps_table = corps_table
        self.corps = list(corps_table)
        self.fn = {}
        self.files = {}  # extra data files: path under data/greenlantern/ -> json
        self.load = []
        self.tick = []
        self.second = []

    # --- helpers ------------------------------------------------------------------------------

    def item(self, corps, item, extra=""):
        n = self.corps.index(corps) + 1
        return f"{NS}:{item}{{CustomModelData:{n},gl_construct:1b{extra}}}"  # they wear out like netherite gear

    def projectile(self, nbt, speed, where="execute anchored eyes positioned ^ ^ ^1.2"):
        """Summon a Palladium custom projectile in front of the player and send it where they look.
        `nbt` is the projectile's data without braces; it is tagged gl_proj_new until launched."""
        return [f'{where} run summon palladium:custom_projectile ~ ~ ~ {{Tags:["gl_proj_new"],'
                f"PreventShooterInteraction:1b,{nbt}}}",
                f"function {NS}:construct/aim/{self.speed_fn(speed)}"]

    def speed_fn(self, speed):
        key = str(speed).replace(".", "_")
        if f"construct/aim/{key}" not in self.fn:
            # direction = (point 1 block ahead of the eyes) - (eyes), in thousandths of a block
            aim = ["tag @s add gl_shooter",
                   'execute anchored eyes positioned ^ ^ ^ run summon minecraft:marker ~ ~ ~ {Tags:["gl_v0"]}',
                   'execute anchored eyes positioned ^ ^ ^1 run summon minecraft:marker ~ ~ ~ {Tags:["gl_v1"]}']
            for i, axis in enumerate("xyz"):
                aim += [f"execute store result score #{axis}0 gl_tmp run data get entity "
                        f"@e[type=minecraft:marker,tag=gl_v0,limit=1] Pos[{i}] 1000",
                        f"execute store result score #{axis}1 gl_tmp run data get entity "
                        f"@e[type=minecraft:marker,tag=gl_v1,limit=1] Pos[{i}] 1000",
                        f"scoreboard players operation #{axis}1 gl_tmp -= #{axis}0 gl_tmp"]
            aim += [f"execute as @e[type=palladium:custom_projectile,tag=gl_proj_new] run function {NS}:construct/launch/{key}",
                    "kill @e[type=minecraft:marker,tag=gl_v0]",
                    "kill @e[type=minecraft:marker,tag=gl_v1]",
                    "tag @s remove gl_shooter"]
            self.fn[f"construct/aim/{key}"] = aim
            scale = speed / 1000
            self.fn[f"construct/launch/{key}"] = [
                *[f"execute store result entity @s Motion[{i}] double {scale:.6f} run scoreboard players get #{a}1 gl_tmp"
                  for i, a in enumerate("xyz")],
                "data modify entity @s Owner set from entity @a[tag=gl_shooter,limit=1] UUID",
                "tag @s remove gl_proj_new",
            ]
        return key

    def laser(self, rgb, thickness, damage, size=0.4, life=100, particles="minecraft:end_rod", extra=""):
        app = f'{{Type:"laser",Thickness:{thickness}f,Color:"{hexcolor(rgb)}"}}'
        if particles:
            app += f',{{Type:"particles",ParticleType:"{particles}",Spread:0.2f}}'
        return (f"Damage:{damage}f,Gravity:0.0f,Size:{size}f,Lifetime:{life},DieOnEntityHit:1b,DieOnBlockHit:1b,"
                f"Appearances:[{app}]{extra}")

    # --- held items ---------------------------------------------------------------------------

    def equip(self, corps, item, hand, extra=""):
        """Form the item in the main hand or offhand: the hand's current item moves to a free inventory slot
        (room_check made sure there is one; if not, the construct goes to the inventory)."""
        full = self.item(corps, item, extra)
        slot = "weapon.mainhand" if hand == "main" else "weapon.offhand"
        return [
            f"function {NS}:construct/free_{hand}",
            f"execute if score #free gl_tmp matches 1 run item replace entity @s {slot} with {full}",
            f"execute if score #free gl_tmp matches 0 run give @s {full}",
        ]

    def hand_functions(self):
        for hand, slot, path in (("main", "weapon.mainhand", "SelectedItem"),
                                 ("off", "weapon.offhand", "Inventory[{Slot:-106b}]")):
            self.fn[f"construct/free_{hand}"] = [
                "scoreboard players set #free gl_tmp 1",
                f"execute if data entity @s {path} run scoreboard players set #free gl_tmp 0",
                f"execute if score #free gl_tmp matches 0 run function {NS}:construct/stash_{hand}",
            ]
            stash = [f"data modify storage {STORAGE} inv set from entity @s Inventory"]
            for i in list(range(9, 36)) + list(range(0, 9)):
                stash.append(f"execute if score #free gl_tmp matches 0 unless data storage {STORAGE} inv[{{Slot:{i}b}}] "
                             f"run function {NS}:construct/stash/{hand}_{i}")
                self.fn[f"construct/stash/{hand}_{i}"] = [
                    f"item replace entity @s container.{i} from entity @s {slot}",
                    f"item replace entity @s {slot} with minecraft:air",
                    "scoreboard players set #free gl_tmp 1",
                ]
            self.fn[f"construct/stash_{hand}"] = stash

    # --- hard light -----------------------------------------------------------------------------

    def hardlight(self, corps, shape, fill_cmds, life):
        """Place temporary hard-light blocks (only into air) and a marker that removes them later."""
        return [*fill_cmds,
                f'summon minecraft:marker ~ ~ ~ {{Tags:["gl_hl","gl_hl_new","gl_hl_{shape}"]}}',
                f"scoreboard players set @e[type=minecraft:marker,tag=gl_hl_new] gl_life {life}",
                "tag @e[type=minecraft:marker,tag=gl_hl_new] remove gl_hl_new",
                # structures it may overlap last as long as it does, so an expiring one never clears it early
                f"scoreboard players set @e[type=minecraft:marker,tag=gl_hl,distance=..34,scores={{gl_life=..{life}}}] "
                f"gl_life {life}"]

    # --- the effect of each construct ----------------------------------------------------------

    def effect(self, corps, con):
        rgb = self.corps_table[corps]["color"]
        fx = rgb if corps != "black" else (150, 155, 170)
        hl = f"{NS}:{corps}_hardlight"
        empty = f"#{NS}:empty"
        front = "execute anchored eyes positioned ^ ^ ^3"
        k = con.key
        if k in HELD_OF:
            items = HELD_OF[k]
            out = []
            for it in items:
                hand = "off" if it == "construct_shield" else "main"
                out += self.equip(corps, it, hand)
            return out + [burst(fx, 1.0, "0.3 0.3 0.3", 30, "~ ~1.2 ~"),
                          sound("minecraft:block.beacon.power_select", 1.8)]
        if k == "signature" and corps in SIGNATURE_HELD:
            extra = ",Enchantments:[{id:\"minecraft:fire_aspect\",lvl:2s}]" if corps == "red" else ""
            return self.equip(corps, SIGNATURE_HELD[corps], "main", extra) + [
                burst(fx, 1.0, "0.3 0.3 0.3", 30, "~ ~1.2 ~"), sound("minecraft:block.beacon.power_select", 1.4)]
        hit = TARGETS.format(r=2.5) + "]"
        if k == "fist":
            return [*construct_cmds(self.corps, corps, self.shape(corps, "fist"), "execute anchored eyes positioned ^ ^-0.4 ^2.6"),
                    f"{front} run {burst(fx, 2.5, '0.8 0.8 0.8', 60, '~ ~ ~')}",
                    f"{front} as {hit} run damage @s 12 minecraft:player_attack by @p[tag=gl_user]",
                    f"{front} run effect give {hit} minecraft:levitation 1 3 true",
                    sound("minecraft:entity.iron_golem.attack", 0.6)]
        if k == "slam":
            around = TARGETS.format(r=6) + "]"
            return [*construct_cmds(self.corps, corps, "hammer", "execute positioned ~ ~3.4 ~"),
                    burst(fx, 2.5, "3 0.2 3", 200, "~ ~0.2 ~"),
                    f"execute as {around} run damage @s 8 minecraft:player_attack by @p[tag=gl_user]",
                    f"effect give {around} minecraft:levitation 1 5 true",
                    sound("minecraft:entity.generic.explode", 1.2)]
        if k == "missiles":
            nbt = self.laser(fx, 0.25, 6, life=80, particles="minecraft:smoke",
                             extra=',ExplosionRadius:1.5f,ExplosionCausesFire:0b,ExplosionBlockInteraction:"keep"')
            out = []
            for x, y in ((-0.7, 0), (0, 0.5), (0.7, 0)):
                out += self.projectile(nbt, 1.6, f"execute anchored eyes positioned ^{x} ^{y} ^1.2")
            return out + [sound("minecraft:entity.firework_rocket.launch", 0.9),
                          sound("minecraft:entity.firework_rocket.launch", 1.2)]
        if k == "cannon":
            n = self.corps.index(corps) + 1
            nbt = (f"Damage:16f,Gravity:0.01f,Size:1.0f,Lifetime:120,DieOnEntityHit:1b,DieOnBlockHit:1b,"
                   f'ExplosionRadius:3.0f,ExplosionCausesFire:0b,ExplosionBlockInteraction:"keep",'
                   f'Appearances:[{{Type:"item",Item:{{id:"{NS}:construct_ball",Count:1b,tag:{{CustomModelData:{n}}}}}}},'
                   f'{{Type:"particles",ParticleType:"minecraft:end_rod",Spread:0.5f}}]')
            return [*self.projectile(nbt, 1.4, "execute anchored eyes positioned ^ ^ ^1.6"),
                    sound("minecraft:entity.generic.explode", 1.6), sound("minecraft:entity.firework_rocket.blast", 0.6)]
        if k == "barrier":
            return [f"execute if entity @s[y_rotation=-45..45] rotated ~ 0 positioned ^ ^ ^3 align xyz run "
                    f"function {NS}:construct/{corps}/wall_x",
                    f"execute if entity @s[y_rotation=135..-135] rotated ~ 0 positioned ^ ^ ^3 align xyz run "
                    f"function {NS}:construct/{corps}/wall_x",
                    f"execute if entity @s[y_rotation=45..135] rotated ~ 0 positioned ^ ^ ^3 align xyz run "
                    f"function {NS}:construct/{corps}/wall_z",
                    f"execute if entity @s[y_rotation=-135..-45] rotated ~ 0 positioned ^ ^ ^3 align xyz run "
                    f"function {NS}:construct/{corps}/wall_z",
                    sound("minecraft:block.beacon.power_select", 0.7)]
        if k == "cage":
            target = TARGETS.format(r=12) + ",limit=1,sort=nearest]"
            return [*construct_cmds(self.corps, corps, self.shape(corps, "cage"), f"execute at {target} positioned ~ ~1 ~"),
                    f"execute as {target} at @s run {burst(fx, 2.0, '0.6 1.0 0.6', 120, '~ ~1 ~')}",
                    f"effect give {target} minecraft:slowness 6 6 true",
                    f"effect give {target} minecraft:weakness 6 2 true",
                    f"effect give {target} minecraft:glowing 6 0 true",
                    sound("minecraft:block.amethyst_block.resonate", 0.8)]
        if k == "dome":
            return [f"execute align xyz run function {NS}:construct/{corps}/dome",
                    burst(fx, 2.0, "3 2 3", 150), sound("minecraft:block.beacon.activate", 1.2)]
        if k == "blocks":
            return [f"give @s {NS}:{corps}_construct_block 64", burst(fx, 1.0, "0.3 0.3 0.3", 30, "~ ~1.2 ~"),
                    sound("minecraft:block.amethyst_block.chime", 1.4)]
        if k == "scuba":
            return [f"tag @s add gl_scuba_{corps}", burst(fx, 1.0, "0.4 0.4 0.4", 40, "~ ~1.7 ~"),
                    sound("minecraft:item.armor.equip_turtle", 1.2)]
        if k == "bridge":
            lines = []
            for rot, d in (("-45..45", "s"), ("135..-135", "n"), ("45..135", "w"), ("-135..-45", "e")):
                lines.append(f"execute if entity @s[y_rotation={rot}] align xyz run function {NS}:construct/{corps}/bridge_{d}")
            return lines + [sound("minecraft:block.beacon.power_select", 1.0)]
        # signature constructs
        if k == "signature" and corps == "green":
            lines = [*construct_cmds(self.corps, corps, "train", "execute rotated ~ 0 positioned ^ ^0.3 ^1.5",
                                     extra_tags=["gl_train_new"]),
                     sound("minecraft:entity.minecart.riding", 0.6), sound("minecraft:block.bell.use", 0.5)]
            for d in range(2, 16, 2):
                at = f"execute rotated ~ 0 positioned ^ ^0.5 ^{d}"
                tgt = TARGETS.format(r=2) + "]"
                lines += [f"{at} as {tgt} run damage @s 14 minecraft:player_attack by @p[tag=gl_user]",
                          f"{at} run effect give {tgt} minecraft:levitation 1 4 true",
                          f"{at} run {burst(fx, 2.0, '0.6 0.6 0.6', 20, '~ ~ ~')}"]
            return lines
        if k == "signature" and corps == "yellow":
            lines = []
            for a in range(0, 360, 45):
                lines += construct_cmds(self.corps, corps, "spike", f"execute rotated {a} 0 positioned ^ ^ ^3")
            around = TARGETS.format(r=5) + "]"
            return lines + [f"execute as {around} run damage @s 10 minecraft:player_attack by @p[tag=gl_user]",
                            f"effect give {around} minecraft:slowness 6 2 true",
                            f"effect give {around} minecraft:darkness 6 0 true",
                            f"effect give {around} minecraft:weakness 6 1 true",
                            burst(fx, 2.0, "3 0.5 3", 150, "~ ~0.5 ~"), sound("minecraft:block.pointed_dripstone.land", 0.6),
                            sound("minecraft:entity.warden.sonic_charge", 1.4)]
        if k == "signature" and corps == "orange":
            prey = HOSTILE.format(r=14)
            return [*construct_cmds(self.corps, corps, "hand", "execute anchored eyes positioned ^ ^-0.4 ^2"),
                    f"execute at {prey} run {burst(fx, 1.5, '0.3 0.6 0.3', 20, '~ ~1 ~')}",
                    f"execute rotated ~ 0 positioned ^ ^ ^2 run tp {prey} ~ ~ ~",
                    f"effect give {HOSTILE.format(r=4)} minecraft:weakness 8 1 true",
                    f"effect give {HOSTILE.format(r=4)} minecraft:slowness 8 1 true",
                    sound("minecraft:entity.evoker.cast_spell", 0.7), sound("minecraft:item.armor.equip_chain", 0.6)]
        if k == "signature" and corps == "blue":
            friends = "@a[distance=..5]"
            return [f"execute align xyz run function {NS}:construct/{corps}/dome",
                    f"effect give {friends} minecraft:regeneration 15 1 true",
                    f"effect give {friends} minecraft:resistance 15 1 true",
                    f"effect give {friends} minecraft:instant_health 1 0 true",
                    burst(fx, 2.0, "3 2 3", 200), sound("minecraft:block.beacon.activate", 1.4),
                    sound("minecraft:block.amethyst_block.resonate", 1.6)]
        if k == "signature" and corps == "violet":
            seal = "effect give @e[distance=..2.5,type=!minecraft:item,type=!minecraft:marker] minecraft:slowness 5 255 true"
            nbt = self.laser(fx, 0.2, 10, life=80, particles="minecraft:end_rod",
                             extra=f',CommandOnEntityHit:"{seal}"')
            return [*self.projectile(nbt, 2.2), sound("minecraft:block.amethyst_cluster.break", 0.8),
                    sound("minecraft:entity.arrow.shoot", 0.6)]
        if k == "signature" and corps == "white":
            friends = "@a[distance=..8]"
            return [f"effect give {friends} minecraft:absorption 30 5 true",
                    f"effect give {friends} minecraft:regeneration 10 0 true",
                    "particle minecraft:end_rod ~ ~1 ~ 3 1.5 3 0.02 200 force",
                    "particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force",
                    sound("minecraft:block.beacon.activate", 1.6), sound("minecraft:item.totem.use", 1.4)]
        if k == "signature" and corps == "black":
            target = TARGETS.format(r=12) + ",limit=1,sort=nearest]"
            return [*construct_cmds(self.corps, corps, "hand", f"execute at {target} positioned ~ ~1 ~"),
                    f"execute as {target} at @s run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.03 40 force",
                    f"execute rotated ~ 0 positioned ^ ^ ^1.5 run tp {target} ~ ~ ~",
                    f"execute as {target} run damage @s 8 minecraft:magic by @p[tag=gl_user]",
                    f"effect give {target} minecraft:wither 6 2 true",
                    "effect give @s minecraft:instant_health 1 0 true",
                    sound("minecraft:entity.wither.shoot", 0.6)]
        raise ValueError(f"no effect for {corps}/{k}")

    # --- Energy Blast and Scan (the ring's blast-mode bar) -------------------------------------

    BLAST_COST, SCAN_COST = 40, 10

    def blast_lines(self, corps, where="execute anchored eyes positioned ^ ^ ^1.2"):
        rgb = self.corps_table[corps]["color"]
        fx = rgb if corps != "black" else (150, 155, 170)
        return [*self.projectile(self.laser(fx, 0.15, 8), 2.5, where),
                sound("minecraft:entity.firework_rocket.blast", 1.5)]

    def scan_lines(self, corps):
        """Scan what you're looking at, up to 24 blocks (run as and at the player, tagged gl_user)."""
        ray = ["scoreboard players set #found gl_tmp 0", "tag @e[tag=gl_scanned] remove gl_scanned"]
        for i in range(1, 49):  # every half block, up to 24 blocks; a 1-block box around the ray point
            d = i / 2           # must touch the creature's hitbox, and solid blocks stop the ray
            at = f"execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^{d}"
            ray.append(f"{at} positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#{NS}:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,"
                       f"limit=1,sort=nearest] run function {NS}:construct/scan_hit")
            ray.append(f"{at} unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2")
        ray.append("execute unless score #found gl_tmp matches 1 run "
                   + actionbar([{"text": "Scan found nothing in your line of sight.", "color": "gray"}]))
        ray.append(f"execute if score #found gl_tmp matches 1 run function {NS}:construct/{corps}/scan_report")
        return ray + [sound("minecraft:block.beacon.ambient", 2.0)]

    def ring_functions(self, corps):
        """ring/<corps>/blast and ring/<corps>/scan: check and spend the charge, then fire. The bar abilities
        only add a cooldown, so a ring that's too low says so instead of greying the slot out.
        blast_fire_right/left fire one bolt from that hand (two rings: one bolt from each)."""
        power = f"{NS}:{corps}_lantern"
        for key, cost, body in (("blast", self.BLAST_COST, self.blast_lines(corps)),
                                ("scan", self.SCAN_COST, self.scan_lines(corps))):
            self.fn[f"ring/{corps}/{key}"] = [
                f"execute store result score #charge gl_tmp run energybar value get @s {power} {BAR}",
                f"execute if score #charge gl_tmp matches ..{cost - 1} run function {NS}:construct/low_charge",
                f"execute if score #charge gl_tmp matches {cost}.. run function {NS}:ring/{corps}/{key}_go",
            ]
            self.fn[f"ring/{corps}/{key}_go"] = [f"energybar value subtract @s {power} {BAR} {cost}",
                                                  "tag @s add gl_user", *body, "tag @s remove gl_user"]
        self.fn[f"ring/{corps}/scan_fire"] = ["tag @s add gl_user", *self.scan_lines(corps), "tag @s remove gl_user"]
        for side, x in (("right", -0.35), ("left", 0.35)):
            self.fn[f"ring/{corps}/blast_fire_{side}"] = self.blast_lines(
                corps, f"execute anchored eyes positioned ^{x} ^-0.3 ^1.2")

    def held_items(self, corps, con):
        if con.key in HELD_OF:
            return HELD_OF[con.key]
        if con.key == "signature" and corps in SIGNATURE_HELD:
            return [SIGNATURE_HELD[corps]]
        return []

    def room_check(self, corps, con):
        """Held constructs and Construct Blocks need somewhere to go: each item needs its hand empty or a
        free inventory slot (an item in the hand moves to a free slot). Otherwise nothing is spent."""
        items = self.held_items(corps, con)
        if not items and con.key != "blocks":
            return []
        need = ["scoreboard players set #need gl_tmp 0"]
        if con.key == "blocks":
            need.append("scoreboard players set #need gl_tmp 1")
        for it in items:
            path = "Inventory[{Slot:-106b}]" if it == "construct_shield" else "SelectedItem"
            need.append(f"execute if data entity @s {path} run scoreboard players add #need gl_tmp 1")
        return [*[f"execute if score #ok gl_tmp matches 1 run {line}" for line in need],
                f"execute if score #ok gl_tmp matches 1 run function {NS}:construct/count_free",
                f"execute if score #ok gl_tmp matches 1 if score #fs gl_tmp < #need gl_tmp run function {NS}:construct/no_room"]

    def target_check(self, corps, con):
        """Constructs aimed at the nearest creature cost nothing when there's none in range."""
        if con.key == "cage" or (con.key == "signature" and corps == "black"):
            return ["tag @s add gl_user",
                    f"execute if score #ok gl_tmp matches 1 unless entity {TARGETS.format(r=12)}] run "
                    f"function {NS}:construct/no_target",
                    "tag @s remove gl_user"]
        return []

    def shape(self, corps, shape):
        return self.corps_table[corps].get("shapes", {}).get(shape, shape)

    # --- per corps ------------------------------------------------------------------------------

    def corps_functions(self, corps):
        self.ring_functions(corps)
        rgb = self.corps_table[corps]["color"]
        col = hexcolor(rgb if corps != "black" else (170, 175, 190))
        power = f"{NS}:{corps}_lantern"
        hl = f"{NS}:{corps}_hardlight"
        empty = f"#{NS}:empty"
        for con in all_constructs(corps):
            base = f"construct/{corps}/{con.key}"
            node_title = NODES[con.node][0] or con.name
            self.fn[base] = [  # run as and at the player, from the construct wheel
                f"execute unless entity @s[tag=gl_u_{corps}_{con.node}] run "
                + actionbar([{"text": f"{con.name} isn't unlocked yet. Buy ", "color": "gray"},
                             {"text": node_title, "color": col}, {"text": " in the powers menu.", "color": "gray"}]),
                f"execute if entity @s[tag=gl_u_{corps}_{con.node}] run function {NS}:{base}_try",
            ]
            held = HELD_OF.get(con.key) or ([SIGNATURE_HELD[corps]] if con.key == "signature" and corps in SIGNATURE_HELD
                                            else None)
            if held:  # press again to dismiss
                self.fn[f"{base}_try"] = [
                    "scoreboard players set #have gl_tmp 0",
                    *[line for it in held for line in (
                        f"execute store result score #h gl_tmp run clear @s {NS}:{it} 0",
                        "scoreboard players operation #have gl_tmp += #h gl_tmp")],
                    f"execute if score #have gl_tmp matches 1.. run function {NS}:{base}_dismiss",
                    f"execute if score #have gl_tmp matches 0 run function {NS}:{base}_check",
                ]
                self.fn[f"{base}_dismiss"] = [*[f"clear @s {NS}:{it}" for it in held],
                                              burst(rgb, 1.0, "0.3 0.3 0.3", 20, "~ ~1.2 ~"),
                                              sound("minecraft:block.beacon.deactivate", 1.8),
                                              actionbar([{"text": f"{con.name} dismissed.", "color": "gray"}])]
            elif con.kind == "toggle":
                tag = f"gl_scuba_{corps}"
                self.fn[f"{base}_try"] = [  # decide first: dismissing must not fall through into forming it
                    f"execute store success score #on gl_tmp if entity @s[tag={tag}]",
                    f"execute if score #on gl_tmp matches 1 run function {NS}:{base}_dismiss",
                    f"execute if score #on gl_tmp matches 0 run function {NS}:{base}_check",
                ]
                self.fn[f"{base}_dismiss"] = [f"tag @s remove {tag}",
                                              *[f"effect clear @s minecraft:{e}" for e in
                                                ("water_breathing", "conduit_power", "dolphins_grace")],
                                              sound("minecraft:block.beacon.deactivate", 1.8),
                                              actionbar([{"text": f"{con.name} dismissed.", "color": "gray"}])]
            else:
                self.fn[f"{base}_try"] = [f"function {NS}:{base}_check"]
            self.fn[f"{base}_check"] = [
                "scoreboard players set #ok gl_tmp 1",
                f"execute if score @s gl_cc_{con.key} matches 1.. run scoreboard players set #ok gl_tmp 0",
                f"execute if score #ok gl_tmp matches 0 run "
                + actionbar([{"text": f"{con.name} is recharging...", "color": "gray"}]),
                f"execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s {power} {BAR}",
                f"execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..{con.cost - 1} run "
                f"function {NS}:construct/low_charge",
                *self.target_check(corps, con),
                *self.room_check(corps, con),
                f"execute if score #ok gl_tmp matches 1 run function {NS}:{base}_go",
            ]
            self.fn[f"{base}_go"] = [
                f"energybar value subtract @s {power} {BAR} {con.cost}",
                f"scoreboard players set @s gl_cc_{con.key} {con.cooldown}",
                actionbar([{"text": "Construct: ", "color": "gray"}, {"text": con.name, "color": col}]),
                "tag @s add gl_user",
                *self.effect(corps, con),
                "tag @s remove gl_user",
            ]
        # hard-light structures, placed at an aligned block position
        self.fn[f"construct/{corps}/wall_x"] = self.hardlight(
            corps, "wx", [f"fill ~-2 ~ ~ ~2 ~3 ~ {hl} replace {empty}"], 300)
        self.fn[f"construct/{corps}/wall_z"] = self.hardlight(
            corps, "wz", [f"fill ~ ~ ~-2 ~ ~3 ~2 {hl} replace {empty}"], 300)
        shell = []
        for x in range(-4, 5):
            for y in range(0, 5):
                for z in range(-4, 5):
                    if 3.5 <= (x * x + y * y + z * z) ** 0.5 < 4.5:
                        shell.append(f"setblock ~{x} ~{y} ~{z} {hl} keep")
        self.fn[f"construct/{corps}/dome"] = self.hardlight(corps, "dome", shell, 300)
        for d, box in BRIDGE_BOXES.items():
            self.fn[f"construct/{corps}/bridge_{d}"] = self.hardlight(
                corps, f"b{d}", [f"fill {box} {hl} replace {empty}"], 600)
        # scan results
        self.fn[f"construct/{corps}/scan_report"] = [
            tellraw("@s", [{"text": "Scan: ", "color": col, "bold": True}, {"selector": "@e[tag=gl_scanned]"},
                           {"text": "  Health ", "color": "gray"}, {"score": {"name": "#hp", "objective": "gl_tmp"}},
                           {"text": "/", "color": "gray"}, {"score": {"name": "#maxhp", "objective": "gl_tmp"}},
                           {"text": "  Armor ", "color": "gray"}, {"score": {"name": "#armor", "objective": "gl_tmp"}}]),
            f"execute as @e[tag=gl_scanned] at @s run {burst(rgb, 1.0, '0.3 0.6 0.3', 30, '~ ~1 ~')}",
            "tag @e[tag=gl_scanned] remove gl_scanned",
        ]
        self.fn[f"construct/{corps}/gatling_shot"] = [
            f"execute store result score #charge gl_tmp run energybar value get @s {power} {BAR}",
            f"execute if score #charge gl_tmp matches ..2 run function {NS}:construct/low_charge",
            f"execute if score #charge gl_tmp matches 3.. run function {NS}:construct/{corps}/gatling_fire",
        ]
        self.fn[f"construct/{corps}/gatling_fire"] = [
            f"energybar value subtract @s {power} {BAR} 3",
            *self.projectile(self.laser(rgb if corps != "black" else (150, 155, 170), 0.08, 3, size=0.25, life=40,
                                        particles=None), 3.0, "execute anchored eyes positioned ^-0.3 ^-0.2 ^1.2"),
            "playsound minecraft:block.note_block.snare player @a[distance=..16] ~ ~ ~ 0.6 1.8",
        ]

    # --- shared ----------------------------------------------------------------------------------

    def shared(self):
        corps = self.corps
        keys = [c.key for c in CATALOG] + ["signature"]
        self.load += ["scoreboard objectives add gl_gat dummy",
                      *[f"scoreboard objectives add gl_cc_{k} dummy" for k in keys]]
        self.tick += [f"scoreboard players remove @a[scores={{gl_cc_{k}=1..}}] gl_cc_{k} 1" for k in keys]
        self.fn["construct/low_charge"] = [
            "scoreboard players set #ok gl_tmp 0",
            actionbar([{"text": "Not enough charge. Recharge your ring at its Power Battery.", "color": "red"}]),
            "playsound minecraft:block.beacon.deactivate player @s ~ ~ ~ 0.6 2",
        ]
        # gatling: while right-click is held this runs every tick and fires every third tick, from the
        # ring whose gatling it is (with two rings, either ring's ability may be the one pressed)
        self.fn["construct/gatling_tick"] = [
            "scoreboard players add @s gl_gat 1",
            *[f"execute if score @s gl_gat matches 3.. if predicate {NS}:construct_held/{c}_mainhand run "
              f"function {NS}:construct/{c}/gatling_shot" for c in corps],
            "execute if score @s gl_gat matches 3.. run scoreboard players set @s gl_gat 0",
        ]
        # Upkeep: each held construct (and Scuba Gear) costs its own ring 3 charge a second, a little more
        # than the ring regains, and dissolves when that ring runs dry. Only once the ring's charge has been
        # restored after it was put on (gl_cr_<corps>), so re-equipping never dissolves anything.
        for c in corps:
            n = corps.index(c) + 1
            power = f"{NS}:{c}_lantern"
            name = self.corps_table[c]["name"]
            ready = f"@a[tag=gl_{c},tag=gl_cr_{c}]"
            self.second += [
                f"execute as {ready} if predicate {NS}:construct_held/{c}_mainhand run function {NS}:construct/{c}/upkeep",
                f"execute as {ready} if predicate {NS}:construct_held/{c}_offhand run function {NS}:construct/{c}/upkeep",
                f"execute as @a[tag=gl_{c},tag=gl_cr_{c},tag=gl_scuba_{c}] run function {NS}:construct/{c}/upkeep",
            ]
            self.fn[f"construct/{c}/upkeep"] = [
                f"execute store result score #charge gl_tmp run energybar value get @s {power} {BAR}",
                f"execute if score #charge gl_tmp matches ..2 run function {NS}:construct/{c}/dissolve",
                f"execute if score #charge gl_tmp matches 3.. run energybar value subtract @s {power} {BAR} 3",
            ]
            self.fn[f"construct/{c}/dissolve"] = [
                *[f"clear @s {NS}:{item}{{CustomModelData:{n}}}" for item in HELD_ITEMS],
                f"tag @s remove gl_scuba_{c}",
                *[f"effect clear @s minecraft:{e}" for e in ("water_breathing", "conduit_power", "dolphins_grace")],
                actionbar([{"text": f"Your {name} ring is out of charge: its constructs dissolve.", "color": "gray"}]),
            ]
            for hand in ("mainhand", "offhand"):
                self.files[f"predicates/construct_held/{c}_{hand}.json"] = {
                    "condition": "minecraft:entity_properties", "entity": "this",
                    "predicate": {"equipment": {hand: {"tag": f"{NS}:held_constructs", "nbt": f"{{CustomModelData:{n}}}"}}}}
        self.fn["construct/count_free"] = [  # #fs = free main-inventory slots (0-35)
            "scoreboard players set #fs gl_tmp 0",
            f"data modify storage {STORAGE} inv set from entity @s Inventory",
            *[f"execute unless data storage {STORAGE} inv[{{Slot:{i}b}}] run scoreboard players add #fs gl_tmp 1"
              for i in range(36)],
        ]
        self.fn["construct/no_room"] = [
            "scoreboard players set #ok gl_tmp 0",
            actionbar([{"text": "No room for the construct: free a slot in your inventory.", "color": "gray"}]),
        ]
        self.fn["construct/no_target"] = [
            "scoreboard players set #ok gl_tmp 0",
            actionbar([{"text": "Nothing within 12 blocks to use that on.", "color": "gray"}]),
        ]
        self.fn["construct/scan_hit"] = [  # as the scanned entity
            "scoreboard players set #found gl_tmp 1",
            "tag @s add gl_scanned",
            "effect give @s minecraft:glowing 10 0 true",
            "execute store result score #hp gl_tmp run data get entity @s Health",
            "execute store result score #maxhp gl_tmp run attribute @s minecraft:generic.max_health get",
            "execute store result score #armor gl_tmp run attribute @s minecraft:generic.armor get",
        ]
        self.hand_functions()
        # hard light: count down, then clear the blocks (only hard light is removed)
        hl = f"#{NS}:hardlight"
        end = []
        boxes = {"wx": "~-2 ~ ~ ~2 ~3 ~", "wz": "~ ~ ~-2 ~ ~3 ~2", "dome": "~-5 ~-1 ~-5 ~5 ~5 ~5",
                 **{f"b{d}": box for d, box in BRIDGE_BOXES.items()}}
        for shape, box in boxes.items():
            end.append(f"execute if entity @s[tag=gl_hl_{shape}] run fill {box} minecraft:air replace {hl}")
        self.fn["construct/hardlight_end"] = end + [
            "particle minecraft:end_rod ~ ~1 ~ 1.5 1.5 1.5 0.02 30 force",
            "playsound minecraft:block.amethyst_block.break block @a[distance=..24] ~ ~ ~ 1 1.2",
            "kill @s"]
        self.tick += [
            "scoreboard players remove @e[type=minecraft:marker,tag=gl_hl] gl_life 1",
            f"execute as @e[type=minecraft:marker,tag=gl_hl,scores={{gl_life=..0}}] at @s run function {NS}:construct/hardlight_end",
            # the train slides forward (in its own facing direction) as it fades
            "scoreboard players set @e[type=minecraft:item_display,tag=gl_train_new] gl_life 14",
            "execute as @e[type=minecraft:item_display,tag=gl_train_new] run data merge entity @s {start_interpolation:0,"
            "interpolation_duration:12,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],"
            "translation:[0f,0f,13f],scale:[2.4f,2.4f,2.4f]}}",
            "tag @e[type=minecraft:item_display,tag=gl_train_new] remove gl_new",
            "tag @e[type=minecraft:item_display,tag=gl_train_new] remove gl_train_new",
        ]
        self.second += [
            # constructs only exist through a ring: they dissolve when you wear none
            f"clear @a[tag=!gl_ring] #{NS}:constructs",
            f"kill @e[type=minecraft:item,nbt={{Item:{{tag:{{gl_construct:1b}}}}}}]",
            *[f"tag @a[tag=gl_scuba_{c},tag=!gl_{c}] remove gl_scuba_{c}" for c in corps],
        ]

# bridge boxes at y-1, from the block in front of you: south (+z), north, west (-x), east
BRIDGE_BOXES = {"s": "~-1 ~-1 ~1 ~1 ~-1 ~16", "n": "~-1 ~-1 ~-16 ~1 ~-1 ~-1",
                "w": "~-16 ~-1 ~-1 ~-1 ~-1 ~1", "e": "~1 ~-1 ~-1 ~16 ~-1 ~1"}


def generate(corps_table):
    """Returns (load, tick, second, functions, files) for the construct system; files maps paths
    under data/greenlantern/ to JSON."""
    g = Gen(corps_table)
    g.shared()
    for c in corps_table:
        g.corps_functions(c)
    return g.load, g.tick, g.second, g.fn, g.files
