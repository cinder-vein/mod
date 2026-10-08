"""The emotional spectrum entities: nine beings of pure emotion loose in the world, one of each.

Each is free, hosted by a player, or sealed in a lantern (world state in objective gl_ent, fake players #state_<e>
0 dormant, 1 out in the world, 2 hosted, 3 sealed; #host_<e> = the host's gl_id).

How they come: every SEEK_SECONDS seconds, each free entity looks for players who can draw it (anywhere, in any
dimension, not hosting one, not cooling down) and comes to one of them at once.
- bond (Ion, Ophidian, Adara, the Proselyte, the Life Entity): it appears near a player whose emotion is full (100%; the
  Life Entity wants all seven spectrum emotions full) and offers to make them its host. Ophidian first wants an offering:
  a block of gold thrown to it.
- hunt (Parallax, the Predator): it appears behind a player strong in its emotion (85%), hunts them down and possesses
  them, wanted or not. A host of a hunting entity is sometimes overtaken by it.
- defeat (the Butcher, Nekron): a boss that comes to challenge a player with 90% of its emotion. Bring it down to 15% and it takes the
  nearest player as its host, if they're worthy (95% of its emotion); otherwise it vanishes.

A host needs no ring: hosting gives the final_lanterns:host_<e> power (built in hosts.py) with its own skill tree.
It ends when the host gives the entity up, or when another player draws it out: sneak while holding a corps' lantern and
look at the host for five seconds. The lantern becomes an Entity Lantern with the entity sealed inside. Right-click it to
release the entity into the world, or to become its host if you're worthy.

One entity per host, and after a host loses theirs (released, drawn out, or taken back) no entity chooses them for an
hour (gl_ehcd, in seconds). A free entity strengthens the rings of its own color: bearers within 24 blocks recharge.
"""
import json

from common import CORPS, NS, actionbar, burst, hexcolor, sound, tellraw
from systems import EMOTION_OF, SPECTRUM

RING_COLOR = {"green": (46, 200, 70), "yellow": (245, 205, 30), "red": (220, 30, 35), "orange": (250, 130, 20),
              "blue": (40, 130, 255), "violet": (215, 55, 220), "indigo": (105, 60, 230), "white": (235, 242, 250),
              "black": (150, 155, 170)}
BOSSBAR_COLOR = {"red": "red", "black": "white"}


class Entity:
    def __init__(self, key, name, emotion, corps, kind, home, title, flavor, lifetime):
        self.key, self.name, self.emotion, self.corps, self.kind, self.home = key, name, emotion, corps, kind, home
        self.title, self.flavor, self.lifetime = title, flavor, lifetime
        self.rgb = RING_COLOR[corps]
        self.color = hexcolor(self.rgb)


ENTITIES = [
    Entity("ion", "Ion", "will", "green", "bond", "sky", "the willpower entity",
           "A vast green leviathan swims through the sky toward you.", 600),
    Entity("parallax", "Parallax", "fear", "yellow", "hunt", "any", "the fear entity",
           "Something is hunting you. You can feel it feeding on your fear...", 1200),
    Entity("butcher", "The Butcher", "rage", "red", "defeat", "nether", "the rage entity",
           "The Butcher has come for blood!", 1200),
    Entity("ophidian", "Ophidian", "greed", "orange", "bond", "caves", "the avarice entity",
           "A great serpent coils in the dark, eyeing your treasure. Throw it a block of gold.", 600),
    Entity("adara", "Adara", "hope", "blue", "bond", "sky", "the hope entity",
           "A blue bird of light circles above you. Hope has found you.", 600),
    Entity("predator", "The Predator", "love", "violet", "hunt", "any", "the love entity",
           "Something is stalking you. It wants your heart...", 1200),
    Entity("proselyte", "The Proselyte", "compassion", "indigo", "bond", "sky", "the compassion entity",
           "A great indigo creature drifts toward you, its single eye full of compassion.", 600),
    Entity("life", "The Life Entity", "life", "white", "bond", "sky", "the entity of life itself",
           "The Life Entity descends: every color of the spectrum shines in you.", 600),
    Entity("nekron", "Nekron", "death", "black", "defeat", "deep", "the lord of the dead",
           "Nekron rises from the deep dark!", 1200),
]
BY_KEY = {e.key: e for e in ENTITIES}
INDEX = {e.key: i for i, e in enumerate(ENTITIES, 1)}
# % of the ring threshold. Everyone starts at 50-75% (emotions.START_MIN/START_MAX), so all are above that: no entity
# comes for a player the day they join.
REQUIRED = {"bond": 100, "hunt": 85, "defeat": 95}   # % of the threshold to become a host
APPEAR = {"bond": 100, "hunt": 85, "defeat": 90}     # % for it to come to you
PERCENTS = sorted(set(REQUIRED.values()) | set(APPEAR.values()))
BOSS_HEALTH = {"butcher": 400, "nekron": 320}
SEEK_SECONDS = 10  # how often a free entity looks for someone worthy (it comes to them at once)
EXORCISE_TICKS = 100
HOST_COOLDOWN = 3600    # seconds after losing an entity before any entity will choose you
DECLINE_COOLDOWN = 1800  # seconds before an entity you turned away offers itself again
NEAR_CHARGE = 40        # ring charge per second for a matching bearer within 24 blocks of a free entity


def free(k):
    """Selector arguments for a player entity k may choose: hosting nothing, not turned away, not cooling down."""
    return f"tag=!gl_host,scores={{gl_edc_{k}=..0,gl_ehcd=..0}}"


def wait_message():
    return tellraw("@s", ["", {"text": "No entity will join you yet: you lost one too recently. ", "color": "gray"},
                          {"text": "(see your Emotional Spectrum menu)", "color": "dark_gray"}])


def emotion_cond(e, pct):
    """`if score ...` conditions true when @s has `pct`% of e's emotion (all seven for the Life Entity)."""
    if e.emotion == "life":
        return " ".join(f"if score @s gl_e_{EMOTION_OF[c]} >= #req{pct} gl_ent" for c in SPECTRUM)
    return f"if score @s gl_e_{e.emotion} >= #req{pct} gl_ent"


def emotion_ok(e, pct):
    return "execute " + emotion_cond(e, pct)


def generate(sizes):
    """sizes: {entity key: (display scale, lift in blocks)} from its model."""
    """Returns (load, tick, second, functions, files) for the datapack; files maps paths under data/final_lanterns/."""
    fn, files, load, tick, second = {}, {}, [], [], []
    load += ["scoreboard objectives add gl_ent dummy", "scoreboard objectives add gl_eser dummy",
             "scoreboard objectives add gl_exo dummy", "scoreboard objectives add gl_entity trigger",
             "scoreboard objectives add gl_eofft dummy", "scoreboard objectives add gl_lifecd dummy",
             "scoreboard objectives add gl_takeover dummy", "scoreboard objectives add gl_ehcd dummy",
             "execute unless score #entities gl_cfg matches 0.. run scoreboard players set #entities gl_cfg 1"]
    for e in ENTITIES:
        load += [f"scoreboard players add #state_{e.key} gl_ent 0", f"scoreboard players add #host_{e.key} gl_ent 0",
                 f"scoreboard players add #ser_{e.key} gl_ent 0", f"scoreboard players add #seal_{e.key} gl_ent 0",
                 f"scoreboard objectives add gl_edc_{e.key} dummy"]
        if e.kind == "defeat":
            load += [f"bossbar add {NS}:{e.key} " + json.dumps({"text": e.name, "color": e.color}),
                     f"bossbar set {NS}:{e.key} color {BOSSBAR_COLOR.get(e.corps, 'white')}",
                     f"bossbar set {NS}:{e.key} max {BOSS_HEALTH[e.key]}",
                     f"bossbar set {NS}:{e.key} style notched_10"]
    files["predicates/entity/sneaking.json"] = {"condition": "minecraft:entity_properties", "entity": "this",
                                                "predicate": {"flags": {"is_sneaking": True}}}
    files["predicates/entity/holding_battery.json"] = {
        "condition": "minecraft:entity_properties", "entity": "this",
        "predicate": {"equipment": {"mainhand": {"tag": f"{NS}:power_batteries"}}}}
    files["predicates/entity/chance_quarter.json"] = {"condition": "minecraft:random_chance", "chance": 0.25}
    for name, loc in (("overworld", {"dimension": "minecraft:overworld"}),
                      ("the_nether", {"dimension": "minecraft:the_nether"}),
                      ("sky", {"dimension": "minecraft:overworld", "position": {"y": {"min": 50}}}),
                      ("caves", {"dimension": "minecraft:overworld", "position": {"y": {"max": 30}}}),
                      ("deep", {"dimension": "minecraft:overworld", "position": {"y": {"max": 0}}})):
        files[f"predicates/entity/in_{name}.json"] = {"condition": "minecraft:location_check", "predicate": loc}
    for e in ENTITIES:
        files[f"predicates/entity/lantern_{e.key}.json"] = {
            "condition": "minecraft:entity_properties", "entity": "this",
            "predicate": {"equipment": {"mainhand": {"items": [f"{NS}:entity_lantern"],
                                                     "nbt": f"{{gl_entity:{INDEX[e.key]}}}"}}}}

    # --- thresholds, refreshed every second ------------------------------------------------------
    second += [f"scoreboard players operation #req{p} gl_ent = #threshold gl_cfg" for p in PERCENTS]
    second += ["scoreboard players set #pct gl_ent 100"]
    for p in [p for p in PERCENTS if p != 100]:
        second += [f"scoreboard players set #p{p} gl_ent {p}",
                   f"scoreboard players operation #req{p} gl_ent *= #p{p} gl_ent",
                   f"scoreboard players operation #req{p} gl_ent /= #pct gl_ent"]

    # --- appearing: every few seconds, each free entity comes to someone who can draw it -------------
    # (scores first: a selector only matches players who have the score)
    second += [f"scoreboard players add @a gl_edc_{e.key} 0" for e in ENTITIES]
    second += [f"scoreboard players remove @a[scores={{gl_edc_{e.key}=1..}}] gl_edc_{e.key} 1" for e in ENTITIES]
    second += ["scoreboard players add #seek gl_ent 1",
               f"execute if score #seek gl_ent matches {SEEK_SECONDS}.. if score #entities gl_cfg matches 1 run "
               f"function {NS}:entity/seek",
               f"execute if score #seek gl_ent matches {SEEK_SECONDS}.. run scoreboard players set #seek gl_ent 0",
               "scoreboard players add #minute gl_ent 1",
               f"execute if score #minute gl_ent matches 60.. run function {NS}:entity/minute",
               "execute if score #minute gl_ent matches 60.. run scoreboard players set #minute gl_ent 0"]
    seek = []
    for e in ENTITIES:
        cand = f"gl_ecand_{e.key}"
        seek += [
            f"tag @a remove {cand}",
            f"execute if score #state_{e.key} gl_ent matches 0 as @a[{free(e.key)},gamemode=!spectator] "
            f"{emotion_cond(e, APPEAR[e.kind])} run tag @s add {cand}",
            f"execute if score #state_{e.key} gl_ent matches 0 as @r[tag={cand}] at @s run "
            f"function {NS}:entity/{e.key}/manifest",
            f"tag @a remove {cand}",
        ]
    fn["entity/seek"] = seek
    fn["entity/minute"] = []
    second += ["scoreboard players add @a gl_ehcd 0", "scoreboard players remove @a[scores={gl_ehcd=1..}] gl_ehcd 1"]

    # --- shared helpers --------------------------------------------------------------------------
    fn["entity/remove_body"] = [  # as a body (the base mob): take it and its model away without a death
        "execute on passengers run kill @s",
        "tp @s ~ -400 ~",
        "kill @s",
    ]
    dash = ["scoreboard players set #d gl_tmp 0"]
    for d in range(1, 9):
        dash.append(f"execute if score #d gl_tmp matches {d - 1} anchored eyes positioned ^ ^ ^{d} if block ~ ~ ~ "
                    f"#minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp {d}")
    for d in range(1, 9):
        dash.append(f"execute if score #d gl_tmp matches {d} anchored eyes positioned ^ ^ ^{d} run tp @s ~ ~-1.62 ~")
    fn["entity/dash"] = dash + ["particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force",
                                "playsound minecraft:entity.ender_dragon.flap player @a[distance=..24] ~ ~ ~ 1 1.6"]

    # --- every entity ----------------------------------------------------------------------------
    for i, e in enumerate(ENTITIES, 1):
        k = e.key
        body = f"@e[tag=gl_ent_{k}]"
        state = f"#state_{k} gl_ent"
        col = e.color
        burst_e = lambda size=2.0, spread="1 1 1", count=80, at="~ ~1 ~", e=e: burst(e.rgb, size, spread, count, at)  # noqa: E731

        # manifesting near the player it came for (as and at them)
        if e.kind == "defeat":
            base = ("minecraft:ravager" if k == "butcher" else "minecraft:wither_skeleton")
            nbt = (f'{{Tags:["gl_ent","gl_ent_{k}","gl_ent_new"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",'
                   f'Silent:1b,HandItems:[{{}},{{}}],HandDropChances:[0f,0f],'
                   f'CustomName:\'{json.dumps({"text": e.name, "color": col})}\'}}')
            spots = [f"execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^ ^{d} if block ~ ~ ~ "
                     f"#minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable if block ~ ~2 ~ #minecraft:replaceable "
                     f"run function {NS}:entity/{k}/place" for d in (12, 10, 8, 6, 4)]
        else:  # a bat carries the model: no AI, can't be hurt, can't be traded with
            base = "minecraft:bat"
            nbt = (f'{{Tags:["gl_ent","gl_ent_{k}","gl_ent_new"],PersistenceRequired:1b,NoAI:1b,NoGravity:1b,'
                   f'Invulnerable:1b,Silent:1b,DeathLootTable:"minecraft:empty"}}')
            if e.kind == "hunt":   # behind them, a little way off
                spots = [f"execute if score #placed gl_tmp matches 0 rotated ~180 0 positioned ^ ^4 ^22 "
                         f"run function {NS}:entity/{k}/place"]
            elif e.home == "caves":
                spots = [f"execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^1 ^{d} if block ~ ~ ~ "
                         f"#minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable run function {NS}:entity/{k}/place"
                         for d in (10, 8, 6, 4)]
            else:                  # in the sky ahead of them, or nearer if that's in rock
                spots = [f"execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^{up} ^{d} if block ~ ~ ~ "
                         f"#minecraft:replaceable run function {NS}:entity/{k}/place" for up, d in ((9, 20), (4, 12), (1, 6))]
        spots.append(f"execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function {NS}:entity/{k}/place")
        display = (f'{{id:"minecraft:item_display",Tags:["gl_entm","gl_entm_{k}"],item_display:"none",view_range:6f,'
                   f'brightness:{{sky:15,block:15}},item:{{id:"{NS}:entity_body",Count:1b,tag:{{CustomModelData:{i}}}}},'
                   f'transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],'
                   f'scale:[0.1f,0.1f,0.1f]}}}}')
        fn[f"entity/{k}/manifest"] = ["scoreboard players set #placed gl_tmp 0", *spots, f"function {NS}:entity/{k}/arrive"]
        # an admin's summon: right in front of them
        fn[f"entity/{k}/summon_here"] = [
            "scoreboard players set #placed gl_tmp 0",
            f"execute rotated ~ 0 positioned ^ ^{1 if e.kind != 'defeat' else 0} ^6 run function {NS}:entity/{k}/place",
            f"execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function {NS}:entity/{k}/place",
            f"function {NS}:entity/{k}/arrive",
        ]
        fn[f"entity/{k}/arrive"] = [
            f"scoreboard players set {state} 1",
            f"scoreboard players add #ser_{k} gl_ent 1",
            f"scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_{k} gl_ent",
            f"scoreboard players set #life_{k} gl_ent {e.lifetime}",
            f"scoreboard players set #miss_{k} gl_ent 0",
            "tag @e[tag=gl_ent_new] remove gl_ent_new",
            *([f"tag @a remove gl_hunted_{k}", f"tag @s add gl_hunted_{k}"] if e.kind == "hunt" else []),
            "title @s times 10 60 20",
            "title @s subtitle " + json.dumps({"text": e.flavor, "color": "gray"}),
            "title @s title " + json.dumps({"text": e.name, "color": col, "bold": True}),
            sound("minecraft:block.beacon.activate", 0.5),
        ]
        place = [f"summon {base} ~ ~ ~ {nbt[:-1]},Passengers:[{display}]}}",
                 "effect give @e[tag=gl_ent_new] minecraft:invisibility infinite 0 true",
                 f"execute as @e[tag=gl_ent_new] at @s run {burst_e(3.0, '2 2 2', 200)}",
                 "scoreboard players set #placed gl_tmp 1"]
        if e.kind == "defeat":
            hp = BOSS_HEALTH[k]
            place += [f"attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.max_health base set {hp}",
                      f"data merge entity @e[tag=gl_ent_new,limit=1] {{Health:{hp}f}}",
                      "attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.knockback_resistance base set 1",
                      "attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.follow_range base set 48",
                      "effect give @e[tag=gl_ent_new] minecraft:fire_resistance infinite 0 true",
                      "effect give @e[tag=gl_ent_new] minecraft:resistance infinite 0 true",
                      *(["attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.attack_damage base set 18"]
                        if k == "butcher" else
                        ["attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.attack_damage base set 14",
                         "attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.movement_speed base set 0.32"])]
        fn[f"entity/{k}/place"] = place
        # the model grows in once it's riding
        tick.append(f"execute as @e[type=minecraft:item_display,tag=gl_entm_{k},tag=!gl_entm_grown] run function "
                    f"{NS}:entity/{k}/grow")

        # every tick while it's out: face and move, offer or possess
        move = [f"execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_{k},limit=1] Rotation"]
        if e.kind == "bond":
            near = f"@a[{free(k)},distance=..40]"
            move += [
                # drift toward the nearest player who could host it; otherwise turn slowly
                f"execute as {near} at @s {emotion_cond(e, REQUIRED['bond'])} run tag @s add gl_ent_worthy",
                f"execute if entity @a[tag=gl_ent_worthy,distance=6..40] facing entity @p[tag=gl_ent_worthy] eyes "
                f"run tp @s ^ ^ ^0.2 ~ ~",
                f"execute unless entity @a[tag=gl_ent_worthy,distance=..40] run tp @s ~ ~ ~ ~1 ~",
                f"execute if entity @a[tag=gl_ent_worthy,distance=..6] facing entity @p[tag=gl_ent_worthy] eyes run tp @s ~ ~ ~ ~ ~",
            ]
            if k == "ophidian":   # it wants an offering first
                move += [
                    f'execute unless entity @s[tag=gl_ent_fed] as @e[type=minecraft:item,distance=..4,limit=1,'
                    f'nbt={{Item:{{id:"minecraft:gold_block"}}}}] run function {NS}:entity/ophidian/fed',
                    f"execute unless entity @s[tag=gl_ent_fed] as @a[tag=gl_ent_worthy,distance=..8] run "
                    + actionbar([{"text": "Ophidian eyes your hoard. Throw it a block of gold.", "color": col}]),
                    f"execute if entity @s[tag=gl_ent_fed] as @a[tag=gl_ent_worthy,distance=..8,tag=!gl_eoffer_{k}] "
                    f"run function {NS}:entity/{k}/offer",
                ]
            else:
                move.append(f"execute as @a[tag=gl_ent_worthy,distance=..8,tag=!gl_eoffer_{k}] run function "
                            f"{NS}:entity/{k}/offer")
            move.append("tag @a[tag=gl_ent_worthy] remove gl_ent_worthy")
        elif e.kind == "hunt":
            prey = f"@a[tag=gl_hunted_{k},limit=1]"
            move += [
                f"execute if entity {prey} facing entity {prey} eyes run tp @s ^ ^ ^0.3 ~ ~",
                f"execute as @a[tag=gl_hunted_{k},tag=!gl_host,scores={{gl_ehcd=..0}},distance=..2] at @s run "
                f"function {NS}:entity/{k}/host",
                f"execute as @a[tag=gl_hunted_{k},distance=2..10] run "
                + actionbar([{"text": f"{e.name} is right behind you...", "color": col}]),
            ]
        else:  # a boss: its own AI fights; the bar follows it, and it yields when worn down
            move += [
                f"execute store result bossbar {NS}:{k} value run data get entity @s Health",
                f"bossbar set {NS}:{k} players @a[distance=..64]",
                f"execute store result score #hp gl_tmp run data get entity @s Health",
                f"execute if score #hp gl_tmp matches ..{BOSS_HEALTH[k] * 15 // 100} run function {NS}:entity/{k}/yield",
            ]
        fn[f"entity/{k}/tick"] = move
        tick.append(f"execute if score {state} matches 1 as {body} at @s run function {NS}:entity/{k}/tick")

        # every second: lifetime, missing bodies, stale bodies
        fn[f"entity/{k}/second"] = [
            f"execute as {body} unless score @s gl_eser = #ser_{k} gl_ent run function {NS}:entity/remove_body",
            f"execute unless score {state} matches 1 as {body} at @s run function {NS}:entity/remove_body",
            f"execute if score {state} matches 1 run scoreboard players remove #life_{k} gl_ent 1",
            f"execute if score {state} matches 1 if score #life_{k} gl_ent matches ..0 run function {NS}:entity/{k}/depart",
            f"execute if score {state} matches 1 unless entity {body} run scoreboard players add #miss_{k} gl_ent 1",
            f"execute if score {state} matches 1 if entity {body} run scoreboard players set #miss_{k} gl_ent 0",
            f"execute if score {state} matches 1 if score #miss_{k} gl_ent matches 20.. run scoreboard players set {state} 0",
            *([f"execute unless score {state} matches 1 run bossbar set {NS}:{k} players"] if e.kind == "defeat" else []),
            # keep hosts and the host power in step (the power persists with the player; the state is the truth)
            f"execute as @a[tag=gl_host_{k}] unless score {state} matches 2 run function {NS}:entity/{k}/strip",
            f"execute as @a[tag=gl_host_{k}] unless score @s gl_id = #host_{k} gl_ent run function {NS}:entity/{k}/strip",
            f"execute as @a[tag=gl_host_{k}] run superpower add {NS}:host_{k} @s",
            f"execute as @a[tag=!gl_host_{k}] run superpower remove {NS}:host_{k} @s",
            # a free entity strengthens the rings of its own color nearby
            f"execute if score {state} matches 1 at {body} as @a[tag=gl_{e.corps},distance=..24] at @s run "
            f"function {NS}:entity/{k}/near_ring",
            # a sealed entity breaks free if its lantern stays shut for two hours
            f"execute if score {state} matches 3 run scoreboard players remove #life_{k} gl_ent 1",
            f"execute if score {state} matches 3 if score #life_{k} gl_ent matches ..0 run function {NS}:entity/{k}/break_free",
        ]
        second.append(f"function {NS}:entity/{k}/second")

        scale, lift = sizes.get(k, (3.0, 0.0))
        fn[f"entity/{k}/grow"] = [
            "tag @s add gl_entm_grown",
            f"data merge entity @s {{start_interpolation:0,interpolation_duration:20,transformation:{{left_rotation:"
            f"[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,{lift}f,0f],scale:[{scale}f,{scale}f,{scale}f]}}}}",
        ]
        fn[f"entity/{k}/depart"] = [
            f"execute as {body} at @s run {burst_e(3.0, '2 2 2', 150)}",
            f"execute as {body} at @s run function {NS}:entity/remove_body",
            f"scoreboard players set {state} 0",
            f"tag @a remove gl_hunted_{k}",
            f"tag @a remove gl_eoffer_{k}",
            f"tellraw @a[distance=..64] " + json.dumps([{"text": f"{e.name} fades away.", "color": col, "italic": True}]),
        ]

        # becoming its host (as the new host, at them)
        fn[f"entity/{k}/host"] = [
            f"execute as {body} at @s run function {NS}:entity/remove_body",
            f"superpower add {NS}:host_{k} @s",
            "tag @s add gl_host", f"tag @s add gl_host_{k}",
            f"scoreboard players operation #host_{k} gl_ent = @s gl_id",
            f"scoreboard players set {state} 2",
            f"tag @a remove gl_hunted_{k}", f"tag @a remove gl_eoffer_{k}",
            *([f"bossbar set {NS}:{k} players"] if e.kind == "defeat" else []),
            burst_e(3.0, "1 2 1", 250), "particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force",
            sound("minecraft:block.end_portal.spawn", 0.7),
            "title @s times 10 70 20",
            "title @s subtitle " + json.dumps({"text": "Open the powers menu to grow its power", "color": "gray"}),
            "title @s title " + json.dumps({"text": f"You host {e.name}", "color": col, "bold": True}),
            "tellraw @a " + json.dumps([{"selector": "@s", "color": col}, {"text": f" is now the host of {e.name}, "
                                                                                    f"{e.title}.", "color": col}]),
        ]
        fn[f"entity/{k}/strip"] = [f"superpower remove {NS}:host_{k} @s", f"tag @s remove gl_host_{k}",
                                   "tag @s remove gl_host", f"scoreboard players set @s gl_ehcd {HOST_COOLDOWN}",
                                   f"clear @s #{NS}:host_constructs{{fl_host:1b}}", "tag @s remove gl_living_lantern"]
        corps = CORPS[e.corps]
        fn[f"entity/{k}/near_ring"] = [  # as a bearer of the entity's color near it
            f"energybar value add @s {NS}:{corps['power']} {corps['bar']} {NEAR_CHARGE}",
            f"particle minecraft:dust {e.rgb[0] / 255:.2f} {e.rgb[1] / 255:.2f} {e.rgb[2] / 255:.2f} 1 ~ ~1 ~ 0.4 0.6 0.4 0 "
            "4 force",
            actionbar([{"text": f"{e.name} is near: your ring drinks its light.", "color": col}]),
        ]

        # bond: the offer
        if e.kind == "bond":
            fn[f"entity/{k}/offer"] = [
                f"tag @s add gl_eoffer_{k}", "scoreboard players set @s gl_eofft 60",
                "scoreboard players enable @s gl_entity",
                tellraw("@s", ["", {"text": f"\n{e.name}", "color": col, "bold": True},
                               {"text": f", {e.title}, senses the strength of your "
                                        f"{'spirit' if e.emotion == 'life' else e.emotion} and offers to make you its "
                                        f"host. ", "color": "gray"},
                               {"text": "[ACCEPT]", "color": "green", "bold": True,
                                "clickEvent": {"action": "run_command", "value": f"/trigger gl_entity set {i}"}},
                               {"text": "  "},
                               {"text": "[DECLINE]", "color": "red", "bold": True,
                                "clickEvent": {"action": "run_command", "value": f"/trigger gl_entity set {10 + i}"}}]),
                sound("minecraft:block.amethyst_block.resonate", 0.7),
            ]
        if k == "ophidian":
            fn["entity/ophidian/fed"] = [  # as the gold block item, at Ophidian
                "kill @s",
                f"tag {body} add gl_ent_fed",
                f"execute at {body} run particle minecraft:wax_on ~ ~1 ~ 1 1 1 0 40 force",
                sound("minecraft:entity.player.burp", 0.5),
            ]
        fn[f"entity/{k}/accept"] = [  # trigger: accept its offer
            f"execute unless entity @s[tag=gl_eoffer_{k}] run "
            + tellraw("@s", ["", {"text": f"{e.name} hasn't offered itself to you.", "color": "gray"}]),
            f"execute if entity @s[tag=gl_eoffer_{k}] unless score {state} matches 1 run "
            + tellraw("@s", ["", {"text": f"{e.name} is gone.", "color": "gray"}]),
            f"execute if entity @s[tag=gl_eoffer_{k},tag=gl_host] run "
            + tellraw("@s", ["", {"text": "You already host an entity.", "color": "gray"}]),
            f"execute if entity @s[tag=gl_eoffer_{k},tag=!gl_host,scores={{gl_ehcd=1..}}] run {wait_message()}",
            f"execute if entity @s[tag=gl_eoffer_{k},tag=!gl_host,scores={{gl_ehcd=..0}}] if score {state} matches 1 at @s "
            f"run function {NS}:entity/{k}/host",
            f"tag @s remove gl_eoffer_{k}",
        ]
        fn[f"entity/{k}/decline"] = [
            f"execute if entity @s[tag=gl_eoffer_{k}] run "
            + tellraw("@s", ["", {"text": f"{e.name} turns away from you.", "color": col, "italic": True}]),
            f"tag @s remove gl_eoffer_{k}", f"scoreboard players set @s gl_edc_{k} {DECLINE_COOLDOWN}",
        ]

        # defeat: worn down, it takes the nearest worthy player
        if e.kind == "defeat":
            fn[f"entity/{k}/yield"] = [  # as and at the boss
                "tag @a remove gl_ent_victor",
                "tag @p[distance=..24,tag=!gl_host,scores={gl_ehcd=..0}] add gl_ent_victor",
                f"execute as @a[tag=gl_ent_victor] {emotion_cond(e, REQUIRED['defeat'])} run tag @s add gl_ent_worthy",
                f"execute as @a[tag=gl_ent_worthy,limit=1] at @s run function {NS}:entity/{k}/host",
                f"execute unless entity @a[tag=gl_ent_worthy] run function {NS}:entity/{k}/scorn",
                "tag @a remove gl_ent_worthy", "tag @a remove gl_ent_victor",
            ]
            fn[f"entity/{k}/scorn"] = [
                "tellraw @a[distance=..48] " + json.dumps([{"text": f"{e.name} finds no one worthy here and vanishes.",
                                                            "color": col, "italic": True}]),
                f"function {NS}:entity/{k}/depart",
            ]
            # special attacks every 8 seconds
            if k == "butcher":
                special = ["execute at @s run " + burst(e.rgb, 2.5, "3 1 3", 150),
                           f"execute at @s as @a[distance=..7] run damage @s 8 minecraft:mob_attack by {body.replace(']', ',limit=1]')}",
                           "execute at @s run effect give @a[distance=..7] minecraft:levitation 1 3 true",
                           "execute at @s run effect give @a[distance=..7] minecraft:wither 4 0 true",
                           "execute at @s run " + sound("minecraft:entity.ravager.roar", 0.6)]
            else:
                minion = '{Tags:["gl_boss_minion","gl_boss_new"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty"}'
                special = ["execute at @s as @p[distance=..16] at @s run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.03 30 force",
                           "execute at @s run tp @p[distance=3..16] ^ ^ ^2",
                           "execute at @s run effect give @a[distance=..16] minecraft:darkness 6 0 true",
                           "execute at @s run effect give @a[distance=..6] minecraft:wither 6 1 true",
                           f"execute at @s run summon minecraft:zombie ~1 ~ ~ {minion}",
                           f"execute at @s run summon minecraft:skeleton ~-1 ~ ~ {minion}",
                           "scoreboard players set @e[tag=gl_boss_new] gl_life 600",
                           "tag @e[tag=gl_boss_new] remove gl_boss_new",
                           "execute at @s run " + sound("minecraft:entity.wither.ambient", 0.6)]
            fn[f"entity/{k}/special"] = special
            second.append(f"execute if score {state} matches 1 as {body} at @s run function {NS}:entity/{k}/special_clock")
            fn[f"entity/{k}/special_clock"] = [
                "scoreboard players add @s gl_ent 1",
                f"execute if score @s gl_ent matches 8.. run function {NS}:entity/{k}/special",
                "execute if score @s gl_ent matches 8.. run scoreboard players set @s gl_ent 0",
            ]

        # hunting entities sometimes take over their host
        if e.kind == "hunt":
            if k == "parallax":
                takeover = ["effect give @s minecraft:darkness 6 0 true", "effect give @s minecraft:nausea 8 0 true",
                            "effect give @a[distance=0.1..8] minecraft:darkness 6 0 true",
                            "effect give @a[distance=0.1..8] minecraft:slowness 6 1 true",
                            "scoreboard players remove @s[scores={gl_e_will=150..}] gl_e_will 150"]
            else:
                takeover = ["effect give @s minecraft:slowness 6 2 true", "effect give @s minecraft:nausea 8 0 true",
                            "effect give @s minecraft:strength 6 1 true",
                            "particle minecraft:heart ~ ~2 ~ 0.5 0.5 0.5 0 10 force",
                            "scoreboard players remove @s[scores={gl_e_compassion=150..}] gl_e_compassion 150"]
            fn[f"entity/{k}/takeover"] = [
                *takeover, burst_e(2.0, "0.6 1 0.6", 80),
                "title @s times 5 40 10",
                "title @s title " + json.dumps({"text": f"{e.name} takes control", "color": col}),
                sound("minecraft:entity.warden.heartbeat", 0.8),
            ]

        # giving it up (as the host)
        fn[f"entity/{k}/release"] = [
            f"function {NS}:entity/{k}/strip",
            f"scoreboard players set {state} 0", f"scoreboard players set #host_{k} gl_ent 0",
            burst_e(3.0, "1 2 1", 200), sound("minecraft:block.beacon.deactivate", 0.6),
            tellraw("@s", ["", {"text": f"{e.name} leaves you and returns to the world.", "color": col}]),
        ]

        # sealed in a lantern by an exorcist (as the exorcist, at them; the host is tagged gl_exo_target)
        lantern = (f'{NS}:entity_lantern{{CustomModelData:{i},gl_entity:{i},gl_seal:0,Enchantments:[{{}}],'
                   f'display:{{Name:\'{json.dumps({"text": f"Lantern of {e.name}", "color": col, "italic": False})}\','
                   f'Lore:[\'{json.dumps({"text": "Right-click to release it, or to host it.", "color": "gray"})}\']}}}}')
        fn[f"entity/{k}/sealed"] = [
            f"execute as @a[tag=gl_exo_target] run function {NS}:entity/{k}/strip",
            f"scoreboard players set {state} 3", f"scoreboard players set #host_{k} gl_ent 0",
            f"scoreboard players add #seal_{k} gl_ent 1",
            f"scoreboard players set #life_{k} gl_ent 7200",
            f"item replace entity @s weapon.mainhand with {lantern}",
            f"item modify entity @s weapon.mainhand {NS}:entity/seal",
            burst_e(3.0, "0.6 1 0.6", 200), "particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force",
            sound("minecraft:block.end_portal_frame.fill", 0.6), sound("minecraft:entity.evoker.prepare_summon", 0.8),
            "tellraw @a " + json.dumps([{"selector": "@s", "color": col}, {"text": f" has drawn {e.name} out of ",
                                                                           "color": "gray"},
                                        {"selector": "@a[tag=gl_exo_target]", "color": col},
                                        {"text": " and sealed it in a lantern.", "color": "gray"}]),
        ]
        fn[f"entity/{k}/break_free"] = [
            f"scoreboard players set {state} 0",
            "tellraw @a " + json.dumps([{"text": f"{e.name} has broken free of its lantern.", "color": col,
                                         "italic": True}]),
        ]
        # the lantern: host it or let it go (as the holder)
        fresh = (f"execute store result score #s gl_tmp run data get entity @s SelectedItem.tag.gl_seal",
                 f"scoreboard players set #fresh gl_tmp 0",
                 f"execute if score {state} matches 3 if score #s gl_tmp = #seal_{k} gl_ent run scoreboard players set #fresh gl_tmp 1")
        empty_lantern = [f"execute if score #fresh gl_tmp matches 0 run item replace entity @s weapon.mainhand with "
                         f"{corps['battery']}",
                         "execute if score #fresh gl_tmp matches 0 run "
                         + tellraw("@s", ["", {"text": "The lantern is empty: the entity broke free long ago.",
                                               "color": "gray"}])]
        fn[f"entity/{k}/lantern_host"] = [
            f"execute unless predicate {NS}:entity/lantern_{k} run "
            + tellraw("@s", ["", {"text": f"Hold the Lantern of {e.name} in your main hand.", "color": "gray"}]),
            f"execute unless predicate {NS}:entity/lantern_{k} run scoreboard players set #fresh gl_tmp -1",
            *[f"execute if predicate {NS}:entity/lantern_{k} run {line}" for line in fresh],
            *[f"execute if predicate {NS}:entity/lantern_{k} run {line}" for line in empty_lantern],
            "scoreboard players set #worthy gl_tmp 0",
            emotion_ok(e, REQUIRED[e.kind]) + " run scoreboard players set #worthy gl_tmp 1",
            "execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 0 run "
            + tellraw("@s", ["", {"text": f"{e.name} doesn't answer you: you need ",
                                  "color": "gray"},
                             {"text": ("all seven spectrum emotions at 100%" if e.emotion == "life"
                                       else f"{REQUIRED[e.kind]}% {e.emotion}"), "color": col},
                             {"text": " (see your Emotional Spectrum menu).", "color": "gray"}]),
            "execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity @s[tag=gl_host] run "
            + tellraw("@s", ["", {"text": "You already host an entity.", "color": "gray"}]),
            "execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity "
            f"@s[tag=!gl_host,scores={{gl_ehcd=1..}}] run {wait_message()}",
            "execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity "
            f"@s[tag=!gl_host,scores={{gl_ehcd=..0}}] run item replace entity @s weapon.mainhand with {corps['battery']}",
            "execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity "
            f"@s[tag=!gl_host,scores={{gl_ehcd=..0}}] at @s run function {NS}:entity/{k}/host",
        ]
        fn[f"entity/{k}/lantern_release"] = [
            f"execute unless predicate {NS}:entity/lantern_{k} run "
            + tellraw("@s", ["", {"text": f"Hold the Lantern of {e.name} in your main hand.", "color": "gray"}]),
            f"execute unless predicate {NS}:entity/lantern_{k} run scoreboard players set #fresh gl_tmp -1",
            *[f"execute if predicate {NS}:entity/lantern_{k} run {line}" for line in fresh],
            *[f"execute if predicate {NS}:entity/lantern_{k} run {line}" for line in empty_lantern],
            f"execute if score #fresh gl_tmp matches 1 run item replace entity @s weapon.mainhand with "
            f"{corps['battery']}",
            f"execute if score #fresh gl_tmp matches 1 run scoreboard players set {state} 0",
            f"execute if score #fresh gl_tmp matches 1 run {burst_e(3.0, '1 2 1', 200)}",
            "execute if score #fresh gl_tmp matches 1 run "
            + tellraw("@a", ["", {"text": f"{e.name} bursts free of its lantern and vanishes into the world.",
                                  "color": col}]),
        ]

    # the lantern seal number (an item modifier: no macros in 1.20.1)
    files["item_modifiers/entity/seal.json"] = {
        "function": "minecraft:copy_nbt", "source": {"type": "minecraft:storage", "source": f"{NS}:entity"},
        "ops": [{"source": "seal", "target": "gl_seal", "op": "replace"}]}
    for e in ENTITIES:  # store the seal number before modifying
        fn[f"entity/{e.key}/sealed"].insert(
            fn[f"entity/{e.key}/sealed"].index(f"item modify entity @s weapon.mainhand {NS}:entity/seal"),
            f"execute store result storage {NS}:entity seal int 1 run scoreboard players get #seal_{e.key} gl_ent")

    # --- offers time out; the trigger ------------------------------------------------------------
    second += ["scoreboard players remove @a[scores={gl_eofft=1..}] gl_eofft 1",
               *[f"tag @a[tag=gl_eoffer_{e.key},scores={{gl_eofft=..0}}] remove gl_eoffer_{e.key}" for e in ENTITIES],
               "scoreboard players enable @a gl_entity"]
    trig = ["scoreboard players operation #v gl_tmp = @s gl_entity", "scoreboard players set @s gl_entity 0",
            "scoreboard players enable @s gl_entity"]
    for i, e in enumerate(ENTITIES, 1):
        trig += [f"execute if score #v gl_tmp matches {i} at @s run function {NS}:entity/{e.key}/accept",
                 f"execute if score #v gl_tmp matches {10 + i} run function {NS}:entity/{e.key}/decline",
                 f"execute if score #v gl_tmp matches {20 + i} at @s run function {NS}:entity/{e.key}/lantern_host",
                 f"execute if score #v gl_tmp matches {30 + i} at @s run function {NS}:entity/{e.key}/lantern_release",
                 f"execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_{e.key}] at @s run "
                 f"function {NS}:entity/{e.key}/release"]
    fn["entity/trigger"] = trig
    tick.append(f"execute as @a[scores={{gl_entity=1..}}] run function {NS}:entity/trigger")

    fn["entity/release_ask"] = [  # the host's Release ability, or saying "I release you"
        "execute unless entity @s[tag=gl_host] run "
        + tellraw("@s", ["", {"text": "You host no entity.", "color": "gray"}]),
        "scoreboard players enable @s gl_entity",
        "execute if entity @s[tag=gl_host] run "
        + tellraw("@s", ["", {"text": "Give up the entity you host? Its powers leave with it. ", "color": "gray"},
                         {"text": "[RELEASE IT]", "color": "red", "bold": True,
                          "clickEvent": {"action": "run_command", "value": "/trigger gl_entity set 40"}}]),
    ]
    use = ["scoreboard players enable @s gl_entity",
           "execute store result score #e gl_tmp run data get entity @s SelectedItem.tag.gl_entity"]
    for i, e in enumerate(ENTITIES, 1):
        use.append(f"execute if score #e gl_tmp matches {i} run " + tellraw("@s", [
            "", {"text": f"The Lantern of {e.name}: ", "color": e.color},
            {"text": "[HOST IT]", "color": "green", "bold": True,
             "clickEvent": {"action": "run_command", "value": f"/trigger gl_entity set {20 + i}"},
             "hoverEvent": {"action": "show_text", "contents": f"Become the host of {e.name} (needs "
                            + ("all seven spectrum emotions at 100%" if e.emotion == "life"
                               else f"{REQUIRED[e.kind]}% {e.emotion}") + ")"}},
            {"text": "  "},
            {"text": "[RELEASE IT]", "color": "yellow", "bold": True,
             "clickEvent": {"action": "run_command", "value": f"/trigger gl_entity set {30 + i}"},
             "hoverEvent": {"action": "show_text", "contents": f"Let {e.name} go back into the world"}}]))
    fn["entity/lantern_use"] = use

    # --- drawing an entity out with a lantern ------------------------------------------------------
    # Sneak while holding a corps' lantern and look at a host within 6 blocks for five seconds.
    tick += [
        f"execute as @a[predicate={NS}:entity/sneaking,predicate={NS}:entity/holding_battery] at @s if entity "
        f"@a[tag=gl_host,distance=0.1..6] run function {NS}:entity/exorcise",
        f"scoreboard players set @a[scores={{gl_exo=1..}},predicate=!{NS}:entity/sneaking] gl_exo 0",
        f"scoreboard players set @a[scores={{gl_exo=1..}},predicate=!{NS}:entity/holding_battery] gl_exo 0",
    ]
    ray = ["tag @s add gl_exorcist", "tag @a remove gl_exo_target", "scoreboard players set #hit gl_tmp 0"]
    for d in range(2, 13):  # every half block out to 6 blocks, checked around the body's middle
        ray.append(f"execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^{d / 2} positioned ~ ~-0.9 ~ "
                   f"as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function {NS}:entity/exorcise_hit")
    exo = ray + [
        "execute if score #hit gl_tmp matches 0 run scoreboard players set @s gl_exo 0",
        "execute if score #hit gl_tmp matches 1 run scoreboard players add @s gl_exo 1",
        "execute if score #hit gl_tmp matches 1 at @a[tag=gl_exo_target] run particle minecraft:end_rod ~ ~1 ~ 0.4 0.8 0.4 0.05 6 force",
        "execute if score #hit gl_tmp matches 1 run particle minecraft:enchant ~ ~1.2 ~ 0.3 0.3 0.3 1 12 force",
        "execute if score #hit gl_tmp matches 1 run "
        + actionbar([{"text": "Drawing the entity out... ", "color": "gold"},
                     {"score": {"name": "@s", "objective": "gl_exo"}, "color": "white"},
                     {"text": f"/{EXORCISE_TICKS}", "color": "gray"}]),
        "execute if score #hit gl_tmp matches 1 as @a[tag=gl_exo_target] run "
        + actionbar([{"text": "Someone is drawing your entity out with a lantern! Get away!", "color": "red"}]),
        f"execute if score @s gl_exo matches {EXORCISE_TICKS}.. run function {NS}:entity/exorcise_done",
        "tag @s remove gl_exorcist",
    ]
    fn["entity/exorcise"] = exo
    fn["entity/exorcise_hit"] = ["scoreboard players set #hit gl_tmp 1", "tag @s add gl_exo_target"]
    fn["entity/exorcise_done"] = ["scoreboard players set @s gl_exo 0"] + [
        f"execute if entity @a[tag=gl_exo_target,tag=gl_host_{e.key}] run function {NS}:entity/{e.key}/sealed"
        for e in ENTITIES] + ["tag @a remove gl_exo_target"]

    # A New Corps' road to Parallax: sacrifice ten rings to the yellow lantern and Parallax takes you, if it's free
    fn["entity/parallax/sacrifice"] = [  # as and at the player (from the patched ring_sacrifice function)
        "scoreboard players set #ok gl_tmp 0",
        "execute if score #state_parallax gl_ent matches 0..1 if entity @s[tag=!gl_host,scores={gl_ehcd=..0}] run "
        "scoreboard players set #ok gl_tmp 1",
        f"execute if score #ok gl_tmp matches 1 run function {NS}:entity/parallax/host",
        "execute if score #ok gl_tmp matches 1 run advancement grant @s only lanterncorps:parallax",
        "execute if score #ok gl_tmp matches 0 run " + tellraw("@s", [
            "", {"text": "Parallax does not answer your sacrifice: ", "color": "yellow"},
            {"text": "it is bound elsewhere, or you can't take an entity right now.", "color": "gray"}]),
    ]

    # Nekron's risen dead last 30 seconds
    tick += ["scoreboard players remove @e[tag=gl_boss_minion] gl_life 1",
             "execute at @e[tag=gl_boss_minion,scores={gl_life=..0}] run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.02 20 force",
             "kill @e[tag=gl_boss_minion,scores={gl_life=..0}]"]

    # --- hosts, every minute: the hunting entities sometimes overtake theirs -----------------------
    fn["entity/minute"] += [f"execute as @a[tag=gl_host_{e.key}] if predicate {NS}:entity/chance_quarter at @s run "
                            f"function {NS}:entity/{e.key}/takeover" for e in ENTITIES if e.kind == "hunt"]
    # Life Entity: Eternal Life comes back every ten minutes
    second += ["scoreboard players remove @a[scores={gl_lifecd=1..}] gl_lifecd 1",
               "tag @a[tag=gl_host_life,scores={gl_lifecd=..0}] add gl_life_ready",
               "scoreboard players add @a[tag=gl_host_life] gl_lifecd 0"]

    # --- admin ---------------------------------------------------------------------------------
    for e in ENTITIES:
        need = REQUIRED[e.kind]
        how = {"bond": "offers itself to", "hunt": "hunts down and possesses", "defeat": "can be defeated by"}[e.kind]
        emotion = "all seven spectrum emotions" if e.emotion == "life" else e.emotion
        fn[f"entity/admin/summon/{e.key}"] = [
            f"execute unless score #state_{e.key} gl_ent matches 0 run "
            + tellraw("@s", ["", {"text": f"{e.name} isn't free (it's out, hosted or sealed). ", "color": "gray"},
                             {"text": "[Free every entity]", "color": "aqua",
                              "clickEvent": {"action": "run_command", "value": f"/function {NS}:entity/admin/reset"}}]),
            f"execute if score #state_{e.key} gl_ent matches 0 run function {NS}:entity/{e.key}/summon_here",
            f"execute if score #state_{e.key} gl_ent matches 1 run " + tellraw("@s", [
                "", {"text": f"{e.name} ", "color": e.color, "bold": True},
                {"text": f"{how} players with {need}% {emotion}" + (" (it takes the nearest worthy player when worn "
                         "down to 15%)" if e.kind == "defeat" else "") + ". ", "color": "gray"},
                {"text": "[Make me its host now]", "color": "green",
                 "clickEvent": {"action": "run_command", "value": f"/function {NS}:entity/admin/host/{e.key}"},
                 "hoverEvent": {"action": "show_text", "contents": "Skips its emotion check and the one-hour wait"}}]),
        ]
        fn[f"entity/admin/host/{e.key}"] = [  # as the player: host it now, whatever their emotions or cooldown
            f"execute if entity @s[tag=gl_host] run " + tellraw("@s", ["", {"text": "You already host an entity: "
                                                                               "release it first.", "color": "gray"}]),
            f"execute if score #state_{e.key} gl_ent matches 2 run " + tellraw("@s", [
                "", {"text": f"{e.name} already has a host.", "color": "gray"}]),
            f"execute if score #state_{e.key} gl_ent matches 3 run " + tellraw("@s", [
                "", {"text": f"{e.name} is sealed in a lantern.", "color": "gray"}]),
            f"execute if entity @s[tag=!gl_host] if score #state_{e.key} gl_ent matches 0..1 at @s run "
            f"function {NS}:entity/{e.key}/host",
        ]
    fn["entity/admin/reset"] = [
        *[line for e in ENTITIES for line in (f"scoreboard players set #state_{e.key} gl_ent 0",
                                              f"scoreboard players set #host_{e.key} gl_ent 0")],
        f"execute as @e[tag=gl_ent] at @s run function {NS}:entity/remove_body",
        tellraw("@s", ["", {"text": "Every entity is free again (hosts lose them within a second).", "color": "green"}]),
    ]
    status = [tellraw("@s", ["", {"text": "Emotional spectrum entities:", "color": "white", "bold": True}])]
    for e in ENTITIES:
        name = {"text": f" {e.name}: ", "color": e.color}
        status += [
            f"execute if score #state_{e.key} gl_ent matches 0 run " + tellraw("@s", ["", name, {"text": "free (dormant)", "color": "gray"}]),
            f"execute if score #state_{e.key} gl_ent matches 1 run " + tellraw("@s", ["", name, {"text": "out in the world", "color": "gray"}]),
            f"execute if score #state_{e.key} gl_ent matches 2 run " + tellraw("@s", ["", name, {"text": "hosted by ", "color": "gray"},
                                                                                       {"selector": f"@a[tag=gl_host_{e.key}]"},
                                                                                       {"text": " (id ", "color": "gray"},
                                                                                       {"score": {"name": f"#host_{e.key}", "objective": "gl_ent"}},
                                                                                       {"text": ")", "color": "gray"}]),
            f"execute if score #state_{e.key} gl_ent matches 3 run " + tellraw("@s", ["", name, {"text": "sealed in a lantern", "color": "gray"}]),
        ]
    fn["entity/admin/status"] = status
    for state, value in (("on", 1), ("off", 0)):
        fn[f"entity/admin/{state}"] = [f"scoreboard players set #entities gl_cfg {value}",
                                       tellraw("@s", ["", {"text": f"Entities appearing on their own: {state.upper()}.",
                                                           "color": "green" if value else "red"}])]
    return load, tick, second, fn, files


def body_sizes(models):
    """{entity key: (display scale, lift)} from the models in tools/entity_models (defaults while one is missing)."""
    return {e.key: (float(models.get(e.key, {}).get("scale", 3.0)), float(models.get(e.key, {}).get("lift", 0.0)))
            for e in ENTITIES}
