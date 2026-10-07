"""Survival systems for the Lantern Corps, generated as a datapack (plus an optional KubeJS
script for /lantern commands and chat replies).

- Ring binding: a ring is bound to the first player who holds it (lore "Bound to <name>").
  A bound ring held by anyone else is thrown out of their hand and flies back to its bearer.
- Emotions: every player has a score for each emotion, fed by vanilla statistics.
- Ring offers: when an emotion passes the threshold (default 20 000), that corps' ring flies to
  the player and asks them to join. They accept or decline in chat (click or type yes/no).
  Declining (or waiting 60 s) sends the ring away; it won't return for an hour.
- Corps leaders: an admin appoints them. Leaders can revoke rings from their corps' members.
- Admin tools: functions under greenlantern:admin/..., wrapped by /lantern when KubeJS is installed.

gen_corps.py calls generate() and merges the returned load/tick lines and functions.
"""
import json

NS = "greenlantern"
STORAGE = f"{NS}:binding"
SPECTRUM = ["green", "yellow", "red", "orange", "blue", "violet", "indigo"]

# Emotion objective per corps. White has none: it chooses those strong in all seven.
EMOTION_OF = {"green": "will", "yellow": "fear", "red": "rage", "orange": "greed", "blue": "hope",
              "violet": "love", "indigo": "compassion", "black": "death"}
EMOTION_NAME = {"will": "willpower", "fear": "fear", "rage": "rage", "greed": "avarice", "hope": "hope",
                "love": "love", "compassion": "compassion", "death": "a closeness to death"}
CORPS_TITLE = {"green": "Green Lantern Corps", "yellow": "Sinestro Corps", "red": "Red Lantern Corps",
               "orange": "Orange Lanterns", "blue": "Blue Lantern Corps", "violet": "Star Sapphires",
               "indigo": "Indigo Tribe", "white": "White Lantern Corps", "black": "Black Lantern Corps"}

# Where emotions come from: (vanilla criterion, points per unit). Damage stats count tenths of a heart.
SOURCES = {
    "will": [("minecraft.custom:minecraft.damage_taken", 1), ("minecraft.custom:minecraft.damage_blocked_by_shield", 2),
             ("minecraft.custom:minecraft.damage_absorbed", 1)],
    "fear": [("minecraft.custom:minecraft.deaths", 600), ("minecraft.custom:minecraft.sneak_time", 1)],
    "rage": [("minecraft.custom:minecraft.damage_dealt", 1), ("playerKillCount", 500)],
    "greed": [("minecraft.custom:minecraft.traded_with_villager", 100), ("minecraft.custom:minecraft.open_chest", 20),
              ("minecraft.custom:minecraft.open_barrel", 20), ("minecraft.mined:minecraft.diamond_ore", 300),
              ("minecraft.mined:minecraft.deepslate_diamond_ore", 300), ("minecraft.mined:minecraft.emerald_ore", 300),
              ("minecraft.mined:minecraft.deepslate_emerald_ore", 300), ("minecraft.mined:minecraft.gold_ore", 50),
              ("minecraft.mined:minecraft.deepslate_gold_ore", 50), ("minecraft.mined:minecraft.ancient_debris", 500)],
    "hope": [("minecraft.custom:minecraft.raid_win", 5000), ("minecraft.custom:minecraft.sleep_in_bed", 200),
             ("minecraft.custom:minecraft.bell_ring", 50), ("minecraft.custom:minecraft.play_time", -20)],  # -N: divide
    "love": [("minecraft.custom:minecraft.animals_bred", 200), ("minecraft.custom:minecraft.eat_cake_slice", 50)],
    "compassion": [("minecraft.custom:minecraft.talked_to_villager", 25), ("minecraft.custom:minecraft.pot_flower", 100),
                   ("minecraft.custom:minecraft.fill_cauldron", 20)],
    "death": [("totalKillCount", 100), ("minecraft.custom:minecraft.deaths", 300)],
}
EMOTIONS = list(SOURCES)

OFFER_SECONDS = 60
ID_BITS = 16  # player ids up to 65 535
CURIOS_SLOTS = 32  # ring slots handled (Curios merges slot counts from every pack)
DECLINE_COOLDOWN = 3600  # seconds before a declined corps asks again
FORGE_COST = 500  # charge spent forging a new ring
FORGE_COOLDOWN = 300  # seconds between forgings (/lantern forgecooldown)
DEFAULT_THRESHOLD = 20000

# Main-inventory slot numbers -> /item slot names (for leader revokes and admin removal we use /clear).
DISPLAY_TRANSFORM = ("transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],"
                     "translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}")


# Chat phrases answered without KubeJS, through Palladium's chat conditions (an exact message, any capitals; see
# the emotional_spectrum power in gen_corps.py). With KubeJS, its script also understands looser wordings.
RECALL_PHRASES = ["ring, come to me", "ring come to me", "come to me, ring", "come to me ring", "ring, return to me",
                  "ring return to me", "return to me, ring", "ring, come back", "ring come back", "i summon my ring",
                  "i call my ring", "ring, to me"]
RECALL_CORPS_PHRASES = ["{n} ring, come to me", "{n} ring come to me", "come to me, {n} ring", "return to me, {n} ring"]
RING_NAMES = {"yellow": ["yellow", "sinestro"], "violet": ["violet", "star sapphire"]}
OFFER_ANSWERS = {"yes": "chat_yes", "y": "chat_yes", "accept": "chat_yes", "i accept": "chat_yes",
                 "no": "chat_no", "n": "chat_no", "decline": "chat_no", "i decline": "chat_no"}
MENU_PHRASES = ["emotions", "my emotions", "emotional spectrum", "show my emotions"]


def chat_phrases(corps_table):
    """{phrase: function (without namespace)} for every chat phrase the mod answers."""
    out = {}
    for p in RECALL_PHRASES:
        for end in ("", "!"):
            out[p + end] = "recall/request"
    for c in corps_table:
        for n in RING_NAMES.get(c, [c]):
            for p in RECALL_CORPS_PHRASES:
                for end in ("", "!"):
                    out[p.format(n=n) + end] = f"recall/request_{c}"
    for c, data in corps_table.items():  # the oath as shown when recharging, or without punctuation
        oath = " ".join(data["oath"]).lower()
        for keep in ("", "'"):  # with or without apostrophes
            bare = "".join(ch if ch.isalpha() or ch == " " or ch in keep else ("" if ch == "'" else " ") for ch in oath)
            out[" ".join(bare.split())] = f"forge/request_{c}"
        out[oath] = f"forge/request_{c}"
    for word, fn in OFFER_ANSWERS.items():
        out[word] = f"offer/{fn}"
    for p in MENU_PHRASES:
        out[p] = "emotion/menu"
    return out


def tellraw(target, parts):
    return f"tellraw {target} " + json.dumps(parts, separators=(",", ":"))


def color(rgb):
    return "#%02X%02X%02X" % tuple(rgb[:3])


def generate(corps_table, write, write_text):
    """Returns (load, tick, functions). Writes predicates, loot tables, item modifiers and tags
    with write(path, json_data) and the KubeJS script with write_text(path, text)."""
    corps = list(corps_table)
    idx = {c: i + 1 for i, c in enumerate(corps)}  # trigger values
    load, tick, fn = [], [], {}
    ring = lambda c: f"{NS}:{c}_lantern_ring"  # noqa: E731

    # ---------------------------------------------------------------- shared objectives & config
    load += [
        "scoreboard objectives add gl_id dummy",
        "scoreboard objectives add gl_tmp dummy",
        "scoreboard objectives add gl_cfg dummy",
        "scoreboard objectives add gl_offer dummy",
        "scoreboard objectives add gl_accept trigger",
        "scoreboard objectives add gl_decline trigger",
        "scoreboard objectives add gl_revoke trigger",
        "scoreboard objectives add gl_roster trigger",
        "scoreboard objectives add gl_emotions trigger",
        f"execute unless score #threshold gl_cfg matches 1.. run scoreboard players set #threshold gl_cfg {DEFAULT_THRESHOLD}",
        "execute unless score #enabled gl_cfg matches 0.. run scoreboard players set #enabled gl_cfg 1",
        "execute unless score #second gl_cfg matches 0.. run scoreboard players set #second gl_cfg 0",
    ]
    for c in corps:
        load.append(f"scoreboard objectives add gl_cd_{c} dummy")
    for e in EMOTIONS:
        load.append(f"scoreboard objectives add gl_e_{e} dummy")
        for i, (crit, w) in enumerate(SOURCES[e]):
            load.append(f"scoreboard objectives add gl_s_{e}{i} {crit}")
            if abs(w) > 1:
                load.append(f"scoreboard players set #w{abs(w)} gl_cfg {abs(w)}")

    # ---------------------------------------------------------------- ids
    # gl_id is a scoreboard score, and scores are keyed by player name. Every player also carries
    # their id as tags (gl_b0..gl_b15; tags live on the UUID-keyed entity), so a renamed player
    # gets the same id back, and a bound ring can be checked against them with cheap item predicates
    # instead of reading the player's NBT every tick.
    load.append("scoreboard players set #2 gl_cfg 2")
    fn["id/assign"] = [  # run when a player has no gl_id score: a new player, or a renamed one
        f"execute if entity @s[tag=gl_hasid] run function {NS}:id/from_tags",
        f"execute unless entity @s[tag=gl_hasid] run function {NS}:id/new",
    ]
    fn["id/new"] = ["scoreboard players add #next gl_id 1", "scoreboard players operation @s gl_id = #next gl_id",
                    f"function {NS}:id/to_tags"]
    fn["id/from_tags"] = ["scoreboard players set @s gl_id 0"] + [
        f"execute if entity @s[tag=gl_b{i}] run scoreboard players add @s gl_id {2 ** i}" for i in range(ID_BITS)] + [
        # their ring serials were keyed by the old name: for a minute, the rings they wear set them again
        *[f"scoreboard players reset @s gl_ser_{c}" for c in corps], f"function {NS}:ring/load_serials",
        "tag @s add gl_reser", "scoreboard players set @s gl_reser 60"]
    to_tags = ["scoreboard players operation #v gl_tmp = @s gl_id"]
    for i in range(ID_BITS):
        to_tags += [f"tag @s remove gl_b{i}",
                    "scoreboard players operation #bit gl_tmp = #v gl_tmp",
                    "scoreboard players operation #bit gl_tmp %= #2 gl_cfg",
                    f"execute if score #bit gl_tmp matches 1 run tag @s add gl_b{i}",
                    "scoreboard players operation #v gl_tmp /= #2 gl_cfg"]
    fn["id/to_tags"] = to_tags + ["tag @s add gl_hasid"]
    fn["id/migrate"] = [
        "scoreboard players set #old gl_tmp 0",
        *[f"execute if entity @s[tag=gl_member_{c}] run scoreboard players set #old gl_tmp 1" for c in corps],
        f"execute if score #old gl_tmp matches 1 run function {NS}:id/to_tags",
        f"execute if score #old gl_tmp matches 0 run function {NS}:id/fresh",
    ]
    fn["id/fresh"] = [f"function {NS}:id/new", *[f"scoreboard players reset @s gl_ser_{c}" for c in corps]]
    # the tags win over a name-keyed score left by someone else under this name
    fn["id/verify"] = [
        "scoreboard players set #t gl_tmp 0",
        *[f"execute if entity @s[tag=gl_b{i}] run scoreboard players add #t gl_tmp {2 ** i}" for i in range(ID_BITS)],
        f"execute unless score @s gl_id = #t gl_tmp run function {NS}:id/from_tags",
    ]
    tick += [
        f"execute as @a unless score @s gl_id matches 1.. run function {NS}:id/assign",
        # players from before 9.0 have an id but no tags yet: bearers (8.0 tagged them gl_member_*)
        # keep it; anyone else gets a fresh id (a reused old name must not inherit its rings)
        f"execute as @a[tag=!gl_hasid] run function {NS}:id/migrate",
    ]

    # ---------------------------------------------------------------- binding
    # A bound ring stores its bearer three ways: gl_owner (their id), gl_ob (the id's bits, checked
    # against the bearer's gl_b tags by predicates) and gl_owner_uuid (so a ring thrown out of a
    # thief's hand can only be picked up by its bearer). An unbound ring may carry gl_gv/gl_giver:
    # the player who handed it on (a leader after a revoke, or an admin unbind) doesn't bind it.
    write(f"data/{NS}/tags/items/lantern_rings.json", {"replace": False, "values": [ring(c) for c in corps]})

    def held_pred(hand, nbt=None):
        item = {"tag": f"{NS}:lantern_rings"}
        if nbt:
            item["nbt"] = nbt
        return {"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"equipment": {hand: item}}}

    def inverted(term):
        return {"condition": "minecraft:inverted", "term": term}

    for hand in ("mainhand", "offhand"):
        bound = held_pred(hand, "{gl_bound:1b}")
        write(f"data/{NS}/predicates/unbound_ring_{hand}.json", [held_pred(hand), inverted(bound)])
        write(f"data/{NS}/predicates/bound_ring_{hand}.json", bound)
        write(f"data/{NS}/predicates/ring_{hand}.json", held_pred(hand))
        for c in corps:
            write(f"data/{NS}/predicates/held/{c}_{hand}.json", {
                "condition": "minecraft:entity_properties", "entity": "this",
                "predicate": {"equipment": {hand: {"items": [ring(c)]}}}})
        write(f"data/{NS}/predicates/giver_ring_{hand}.json", [held_pred(hand, "{gl_gv:1b}"), inverted(bound)])
        # bound before 9.0: no owner bits yet
        write(f"data/{NS}/predicates/legacy_ring_{hand}.json", [
            bound, inverted(held_pred(hand, "{gl_ob:{b0:0b}}")), inverted(held_pred(hand, "{gl_ob:{b0:1b}}"))])
        for i in range(ID_BITS):
            for v in (0, 1):
                write(f"data/{NS}/predicates/ob/{hand}_{i}_{v}.json", held_pred(hand, f"{{gl_ob:{{b{i}:{v}b}}}}"))
    bind_functions = [
        {"function": "minecraft:set_nbt", "tag": "{gl_bound:1b,gl_gv:0b,gl_giver:0}"},
        {"function": "minecraft:copy_nbt", "source": {"type": "minecraft:storage", "source": STORAGE},
         "ops": [{"source": "owner", "target": "gl_owner", "op": "replace"},
                 {"source": "bits", "target": "gl_ob", "op": "replace"},
                 {"source": "serial", "target": "gl_serial", "op": "replace"}]},
        {"function": "minecraft:copy_nbt", "source": "this",
         "ops": [{"source": "UUID", "target": "gl_owner_uuid", "op": "replace"}]},
        {"function": "minecraft:set_lore", "entity": "this", "replace": True, "lore": [
            {"text": "Bound to ", "color": "gray", "italic": False, "extra": [{"selector": "@s", "color": "white"}]}]},
    ]
    giver_functions = [  # unbound, but the giver (in storage) can carry it without binding it
        {"function": "minecraft:set_nbt", "tag": "{gl_bound:0b,gl_gv:1b}"},
        {"function": "minecraft:copy_nbt", "source": {"type": "minecraft:storage", "source": STORAGE},
         "ops": [{"source": "giver", "target": "gl_giver", "op": "replace"}]},
        {"function": "minecraft:set_lore", "replace": True, "lore": [
            {"text": "Unbound: it will choose the next bearer", "color": "gray", "italic": True}]},
    ]
    write(f"data/{NS}/item_modifiers/bind.json", bind_functions)
    write(f"data/{NS}/item_modifiers/unbind.json", giver_functions)
    for c in corps:
        for name, functions in ((c, bind_functions), (f"giver_{c}", giver_functions)):
            write(f"data/{NS}/loot_tables/rings/{name}.json", {
                "type": "minecraft:chest",  # `loot give ... loot` rolls tables with the chest context
                "pools": [{"rolls": 1, "entries": [{"type": "minecraft:item", "name": ring(c), "functions": functions}]}],
            })

    fn["ring/secure_drop"] = [  # as and at the bearer, right after a bound ring was dropped at their feet
        "tag @s add gl_giving",
        f"execute as @e[type=minecraft:item,distance=..1.5,nbt={{Item:{{tag:{{gl_bound:1b}}}}}},limit=1,sort=nearest] run "
        f"function {NS}:ring/secure_item",
        "tag @s remove gl_giving",
        tellraw("@s", [{"text": "Your inventory is full: your ring waits at your feet.", "color": "gray"}]),
    ]
    fn["ring/secure_item"] = ["data merge entity @s {Age:-32768s,PickupDelay:0s}",
                              "data modify entity @s Owner set from entity @a[tag=gl_giving,limit=1] UUID"]
    # owner id and id bits of @s, for the bind modifier
    fn["ring/store_owner"] = [
        f"execute store result storage {STORAGE} owner int 1 run scoreboard players get @s gl_id",
        f"data modify storage {STORAGE} bits set value {{{','.join(f'b{i}:0b' for i in range(ID_BITS))}}}",
        *[f"execute if entity @s[tag=gl_b{i}] run data modify storage {STORAGE} bits.b{i} set value 1b"
          for i in range(ID_BITS)],
    ]
    fn["ring/store_giver"] = [f"execute store result storage {STORAGE} giver int 1 run scoreboard players get @s gl_id"]
    # Every binding gets a new serial number, and each player remembers the serial of their one
    # valid ring per corps (gl_ser_<corps>; 0 = bound before 9.0, -1 = revoked). A ring whose serial
    # isn't its bearer's current one has gone dark: it was replaced by a recall (see below).
    load += ["execute unless score #serial gl_cfg matches 1.. run scoreboard players set #serial gl_cfg 0",
             *[f"scoreboard objectives add gl_ser_{c} dummy" for c in corps]]
    fn["ring/new_serial"] = ["scoreboard players add #serial gl_cfg 1",
                             f"execute store result storage {STORAGE} serial int 1 run scoreboard players get #serial gl_cfg"]
    set_serial = lambda c: f"scoreboard players operation @s gl_ser_{c} = #serial gl_cfg"  # noqa: E731
    # Scores are keyed by name, so every change to a player's serials is also saved under their id
    # (storage sers: [{id, green, yellow, ...}]) and restored when a renamed player comes back.
    fn["ring/save_serials"] = [
        "tag @s add gl_sersaved",
        f"data modify storage {STORAGE} me set value {{}}",
        f"execute store result storage {STORAGE} me.id int 1 run scoreboard players get @s gl_id",
        *[f"scoreboard players add @s gl_ser_{c} 0" for c in corps],
        *[f"execute store result storage {STORAGE} me.{c} int 1 run scoreboard players get @s gl_ser_{c}" for c in corps],
        f"data modify storage {STORAGE} rest set value []",
        f"execute if data storage {STORAGE} sers[0] run function {NS}:ring/save_next",
        f"data modify storage {STORAGE} sers set from storage {STORAGE} rest",
        f"data modify storage {STORAGE} sers append from storage {STORAGE} me",
    ]
    fn["ring/save_next"] = [  # keep every entry but this player's
        f"execute store result score #eid gl_tmp run data get storage {STORAGE} sers[0].id",
        f"execute unless score #eid gl_tmp = @s gl_id run data modify storage {STORAGE} rest append from storage {STORAGE} sers[0]",
        f"data remove storage {STORAGE} sers[0]",
        f"execute if data storage {STORAGE} sers[0] run function {NS}:ring/save_next",
    ]
    fn["ring/load_serials"] = [
        f"data modify storage {STORAGE} look set from storage {STORAGE} sers",
        f"execute if data storage {STORAGE} look[0] run function {NS}:ring/load_next",
    ]
    fn["ring/load_next"] = [
        f"execute store result score #eid gl_tmp run data get storage {STORAGE} look[0].id",
        *[f"execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_{c} run "
          f"data get storage {STORAGE} look[0].{c}" for c in corps],
        f"data remove storage {STORAGE} look[0]",
        f"execute if data storage {STORAGE} look[0] run function {NS}:ring/load_next",
    ]
    load += ["scoreboard objectives add gl_reser dummy"]

    def bearer(c, run):
        """Lines running `run` when @s bears a ring of corps c: a valid serial, or a pre-update ring
        they've been seen wearing since the update (gl_legacy_<c>)."""
        return [f"execute if score @s gl_ser_{c} matches 1.. run {run}",
                f"execute if score @s gl_ser_{c} matches 0 if entity @s[tag=gl_legacy_{c}] run {run}"]

    def give_ring(table):
        """Gives a ring from a loot table; drops it at your feet when your inventory is full. A bound
        ring dropped that way never despawns and only its bearer can pick it up."""
        lines = [f"execute store result score #given gl_tmp run loot give @s loot {NS}:rings/{table}",
                 f"execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot {NS}:rings/{table}"]
        if table.startswith("giver_"):
            lines.append(f"execute if score #given gl_tmp matches 0 at @s run data merge entity @e[type=minecraft:item,"
                         f"distance=..1.5,nbt={{Item:{{tag:{{gl_gv:1b}}}}}},limit=1,sort=nearest] {{Age:-32768s}}")
        else:
            lines.append(f"execute if score #given gl_tmp matches 0 at @s run function {NS}:ring/secure_drop")
        return lines

    newest_eject = "@e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest]"
    eject_summon = ('summon minecraft:item ~ ~1 ~ {Tags:["gl_eject"],PickupDelay:20s,Age:-32768s,'
                    'Motion:[0.0d,0.3d,0.0d],Item:{id:"minecraft:stone",Count:1b}}')
    eject_message = [
        "particle minecraft:end_rod ~ ~1 ~ 0.2 0.2 0.2 0.05 20 force",
        tellraw("@s", [{"text": "This ring has already chosen its bearer. It returns to them.", "color": "gray",
                        "italic": True}]),
        "playsound minecraft:entity.enderman.teleport player @a[distance=..16] ~ ~ ~ 1 1.4",
    ]
    # an ejected ring flies to its bearer if they're online (any dimension); otherwise it waits where
    # it fell. It never despawns, and only its bearer can pick it up.
    fn["ring/return_to_owner"] = [  # run as the bearer, at the bearer
        "tp @e[type=minecraft:item,tag=gl_eject] ~ ~0.5 ~",
        "data merge entity @e[type=minecraft:item,tag=gl_eject,limit=1] {PickupDelay:0s}",
        "particle minecraft:end_rod ~ ~1 ~ 0.3 0.5 0.3 0.05 20 force",
        tellraw("@s", [{"text": "Your ring returns to you.", "color": "gray", "italic": True}]),
    ]
    for hand, slot, path in (("mainhand", "weapon.mainhand", "SelectedItem"),
                             ("offhand", "weapon.offhand", "Inventory[{Slot:-106b}]")):
        held_ring = (lambda c: f'SelectedItem{{id:"{ring(c)}"}}') if hand == "mainhand" else (
            lambda c: f'Inventory[{{Slot:-106b,id:"{ring(c)}"}}]')
        fn[f"ring/claim_{hand}"] = [
            "scoreboard players set #giver gl_tmp 0",
            f"execute if predicate {NS}:giver_ring_{hand} store result score #giver gl_tmp run "
            f"data get entity @s {path}.tag.gl_giver",
            f"execute if score #giver gl_tmp = @s gl_id run function {NS}:ring/giver_held_{hand}",
            f"execute unless score #giver gl_tmp = @s gl_id run function {NS}:ring/claim_new_{hand}",
        ]
        # A ring of a corps you already bear waits for another bearer: binding it would make it your one
        # valid ring and darken the one you wear. (A lost ring is replaced with recall.)
        claim_new = ["scoreboard players set #keep gl_tmp 0", *[f"scoreboard players add @s gl_ser_{c} 0" for c in corps]]
        for c in corps:
            claim_new += [line.replace("execute if score", f"execute if predicate {NS}:held/{c}_{hand} if score", 1)
                          for line in bearer(c, "scoreboard players set #keep gl_tmp 1")]
        fn[f"ring/claim_new_{hand}"] = claim_new + [
            f"execute if score #keep gl_tmp matches 1 run function {NS}:ring/second_ring_{hand}",
            f"execute if score #keep gl_tmp matches 0 run function {NS}:ring/bind_{hand}",
        ]
        # A ring being handed on (forged, revoked or unbound) doesn't bind to the one handing it on. A
        # valid bearer of that corps (a leader, a forger) may carry it; anyone else (revoked, or unbound
        # by an admin) can't wield it, or it would be a power source a revoke can't reach: it drops at
        # their feet for its new bearer.
        keep = ["scoreboard players set #keep gl_tmp 0", *[f"scoreboard players add @s gl_ser_{c} 0" for c in corps]]
        for c in corps:
            keep += [line.replace("execute if score", f"execute if predicate {NS}:held/{c}_{hand} if score", 1)
                     for line in bearer(c, "scoreboard players set #keep gl_tmp 1")]
        fn[f"ring/giver_held_{hand}"] = keep + [
            f"execute if score #keep gl_tmp matches 0 run function {NS}:ring/giver_drop_{hand}"]
        fn[f"ring/second_ring_{hand}"] = [
            f"function {NS}:ring/drop_{hand}",
            "title @s actionbar " + json.dumps({"text": "You already bear a ring of this corps: this one waits for "
                                                        "another bearer.", "color": "gray"}),
        ]
        fn[f"ring/drop_{hand}"] = [
            'summon minecraft:item ~ ~0.5 ~ {Tags:["gl_drop"],PickupDelay:40s,Age:-32768s,'
            'Item:{id:"minecraft:stone",Count:1b}}',
            f"data modify entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Item set from entity @s {path}",
            f"item replace entity @s {slot} with minecraft:air",
            "tag @e[type=minecraft:item,tag=gl_drop] remove gl_drop",
        ]
        fn[f"ring/giver_drop_{hand}"] = [
            'summon minecraft:item ~ ~0.5 ~ {Tags:["gl_drop"],PickupDelay:40s,Age:-32768s,'
            'Item:{id:"minecraft:stone",Count:1b}}',
            f"data modify entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Item set from entity @s {path}",
            f"item replace entity @s {slot} with minecraft:air",
            "tag @e[type=minecraft:item,tag=gl_drop] remove gl_drop",
            "title @s actionbar " + json.dumps({"text": "This ring won't serve you: drop it for the one it should choose. "
                                                        "It binds to the next player who holds it.", "color": "gray"}),
        ]
        fn[f"ring/bind_{hand}"] = [
            f"function {NS}:ring/rebind_{hand}",
            *[f"execute if predicate {NS}:held/{c}_{hand} run tag @s add gl_member_{c}" for c in corps],
            tellraw("@s", [{"text": "The ring is now bound to you.", "color": "gray", "italic": True}]),
            "playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6",
        ]
        fn[f"ring/rebind_{hand}"] = [
            f"function {NS}:ring/store_owner", f"function {NS}:ring/new_serial",
            f"item modify entity @s {slot} {NS}:bind",
            *[f"execute if predicate {NS}:held/{c}_{hand} run {set_serial(c)}" for c in corps],
            *[f"execute if predicate {NS}:held/{c}_{hand} run tag @s remove gl_legacy_{c}" for c in corps],
            f"function {NS}:ring/save_serials",
        ]
        check = [f"execute if predicate {NS}:legacy_ring_{hand} run function {NS}:ring/legacy_{hand}"]
        for i in range(ID_BITS):
            check += [f"execute if entity @s[tag=gl_b{i}] if predicate {NS}:ob/{hand}_{i}_0 run function {NS}:ring/eject_{hand}",
                      f"execute if entity @s[tag=!gl_b{i}] if predicate {NS}:ob/{hand}_{i}_1 run function {NS}:ring/eject_{hand}"]
        fn[f"ring/check_{hand}"] = check
        legacy_ok = ["scoreboard players set #keep gl_tmp 0", *[f"scoreboard players add @s gl_ser_{c} 0" for c in corps],
                     *[f"execute if predicate {NS}:held/{c}_{hand} if score @s gl_ser_{c} matches 0 if entity "
                       f"@s[tag=gl_member_{c}] run scoreboard players set #keep gl_tmp 1" for c in corps]]
        fn[f"ring/legacy_{hand}"] = [  # a pre-9.0 ring: its bearer's ring is upgraded; a revoked or replaced one goes dark
            f"execute store result score #owner gl_tmp run data get entity @s {path}.tag.gl_owner",
            f"execute unless score #owner gl_tmp = @s gl_id run function {NS}:ring/eject_{hand}",
            f"execute if score #owner gl_tmp = @s gl_id run function {NS}:ring/legacy_own_{hand}",
        ]
        fn[f"ring/legacy_own_{hand}"] = legacy_ok + [  # decided before rebind changes the serial
            f"execute if score #keep gl_tmp matches 1 run function {NS}:ring/rebind_{hand}",
            f"execute if score #keep gl_tmp matches 0 run function {NS}:ring/dark_{hand}",
        ]
        fn[f"ring/eject_{hand}"] = [  # run as the holder, at the holder
            f"execute store result score #owner gl_tmp run data get entity @s {path}.tag.gl_owner",
            eject_summon,
            f"data modify entity {newest_eject} Item set from entity @s {path}",
            f"data modify entity {newest_eject} Owner set from entity @s {path}.tag.gl_owner_uuid",
            f"item replace entity @s {slot} with minecraft:air",
            *eject_message,
            f"execute as @a if score @s gl_id = #owner gl_tmp at @s run function {NS}:ring/return_to_owner",
            "tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject",
        ]
    fn["ring/bind_check"] = [  # every tick, as and at every player
        f"execute if predicate {NS}:unbound_ring_mainhand run function {NS}:ring/claim_mainhand",
        f"execute if predicate {NS}:unbound_ring_offhand run function {NS}:ring/claim_offhand",
        f"execute if predicate {NS}:bound_ring_mainhand run function {NS}:ring/check_mainhand",
        f"execute if predicate {NS}:bound_ring_offhand run function {NS}:ring/check_offhand",
    ]

    # Rings worn in Curios ring slots. Curios items can't be read with predicates, so twice a second
    # each player wearing a ring power gets one snapshot of their ring slots into storage, and every
    # check runs against that. Curios' own commands (/curios replace) live in a function reached
    # through a function tag whose entry is optional, so the pack still loads without Curios.
    curios_items = 'ForgeCaps."curios:inventory".Curios[{Identifier:"ring"}].StacksHandler.Stacks.Items'
    is_lantern = [f'execute if data storage {STORAGE} cur{{id:"{ring(c)}"}} run scoreboard players set #lantern gl_tmp 1'
                  for c in corps]
    fn["ring/curios_check"] = [  # as and at a player
        f"data remove storage {STORAGE} rings",
        f"data modify storage {STORAGE} rings set from entity @s {curios_items}",
        f"execute if data storage {STORAGE} rings[0] run function {NS}:ring/curios_next",
    ]
    fn["ring/curios_next"] = [
        f"data modify storage {STORAGE} cur set from storage {STORAGE} rings[0]",
        f"data remove storage {STORAGE} rings[0]",
        "scoreboard players set #lantern gl_tmp 0",
        *is_lantern,
        f"execute if score #lantern gl_tmp matches 1 run function {NS}:ring/curios_item",
        f"execute if data storage {STORAGE} rings[0] run function {NS}:ring/curios_next",
    ]
    fn["ring/curios_item"] = [
        f"execute store result score #slot gl_tmp run data get storage {STORAGE} cur.Slot",
        f"execute if data storage {STORAGE} cur.tag{{gl_bound:1b}} run function {NS}:ring/curios_bound",
        f"execute unless data storage {STORAGE} cur.tag{{gl_bound:1b}} run function {NS}:ring/curios_unbound",
    ]
    fn["ring/curios_bound"] = [
        f"execute store result score #owner gl_tmp run data get storage {STORAGE} cur.tag.gl_owner",
        f"execute unless score #owner gl_tmp = @s gl_id run function {NS}:ring/curios_eject",
        f"execute if score #owner gl_tmp = @s gl_id run function {NS}:ring/curios_serial",
    ]
    fn["ring/curios_serial"] = [  # an owned ring in a Curios slot
        f"execute store result score #s gl_tmp run data get storage {STORAGE} cur.tag.gl_serial",
        *[f"scoreboard players add @s gl_ser_{c} 0" for c in corps],
        *[f'execute if entity @s[tag=gl_reser] if score @s gl_ser_{c} matches 0 if score #s gl_tmp matches 1.. if data '
          f'storage {STORAGE} cur{{id:"{ring(c)}"}} run scoreboard players operation @s gl_ser_{c} = #s gl_tmp' for c in corps],
        *[f'execute if score #s gl_tmp matches 0 if score @s gl_ser_{c} matches 0 if data storage {STORAGE} '
          f'cur{{id:"{ring(c)}"}} run tag @s add gl_legacy_{c}' for c in corps],
        *[f'execute if data storage {STORAGE} cur{{id:"{ring(c)}"}} unless score #s gl_tmp = @s gl_ser_{c} run '
          f"function {NS}:ring/curios_dark" for c in corps],
        f"execute if entity @s[tag=gl_reser] run function {NS}:ring/save_serials",
    ]
    fn["ring/curios_dark"] = [f"function #{NS}:curios_clear_slot", f"function {NS}:ring/dark_message"]
    fn["ring/dark_message"] = [
        "particle minecraft:smoke ~ ~1.2 ~ 0.2 0.3 0.2 0.02 30 force",
        "playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 0.6",
        tellraw("@s", [{"text": "This ring has gone dark: its power answers another ring now. It crumbles to dust.",
                        "color": "gray", "italic": True}]),
    ]
    # rings in your hands: checked twice a second (the owner check above runs every tick)
    for hand, slot, path in (("mainhand", "weapon.mainhand", "SelectedItem"),
                             ("offhand", "weapon.offhand", "Inventory[{Slot:-106b}]")):
        fn[f"ring/serial_{hand}"] = [
            f"data modify storage {STORAGE} held set from entity @s {path}.tag",
            f"execute store result score #owner gl_tmp run data get storage {STORAGE} held.gl_owner",
            f"execute store result score #s gl_tmp run data get storage {STORAGE} held.gl_serial",
            *[f"scoreboard players add @s gl_ser_{c} 0" for c in corps],
            *[f"execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_{c} matches 0 if score "
              f"#s gl_tmp matches 1.. if predicate {NS}:held/{c}_{hand} run scoreboard players operation @s gl_ser_{c} = #s gl_tmp"
              for c in corps],
            *[f"execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_{c} matches 0 "
              f"if predicate {NS}:held/{c}_{hand} run tag @s add gl_legacy_{c}" for c in corps],
            *[f"execute if score #owner gl_tmp = @s gl_id if predicate {NS}:held/{c}_{hand} unless score #s gl_tmp = "
              f"@s gl_ser_{c} run function {NS}:ring/dark_{hand}" for c in corps],
            f"execute if entity @s[tag=gl_reser] run function {NS}:ring/save_serials",
        ]
        fn[f"ring/dark_{hand}"] = [f"item replace entity @s {slot} with minecraft:air", f"function {NS}:ring/dark_message"]
    fn["ring/serial_check"] = [
        f"execute if predicate {NS}:bound_ring_mainhand run function {NS}:ring/serial_mainhand",
        f"execute if predicate {NS}:bound_ring_offhand run function {NS}:ring/serial_offhand",
        f"function {NS}:ring/curios_check",
    ]
    fn["ring/curios_pop"] = [  # throw the ring in storage `cur` out of its Curios slot (#slot)
        f"execute if score #slot gl_tmp matches 0..{CURIOS_SLOTS - 1} run function {NS}:ring/curios_pop_slot",
        f"execute if score #slot gl_tmp matches {CURIOS_SLOTS}.. run "
        + tellraw("@s", [{"text": f"Lantern rings only work in the first {CURIOS_SLOTS} ring slots.", "color": "gray"}]),
    ]
    fn["ring/curios_pop_slot"] = [
        eject_summon,
        f"data modify entity {newest_eject} Item set from storage {STORAGE} cur",
        f"data remove entity {newest_eject} Item.Slot",
        # only a bound ring is kept for its bearer; an unbound one is anyone's
        f"execute if data storage {STORAGE} cur.tag{{gl_bound:1b}} run "
        f"data modify entity {newest_eject} Owner set from storage {STORAGE} cur.tag.gl_owner_uuid",
        f"function #{NS}:curios_clear_slot",
    ]
    fn["ring/curios_eject"] = [
        f"function {NS}:ring/curios_pop",
        *eject_message,
        f"execute as @a if score @s gl_id = #owner gl_tmp at @s run function {NS}:ring/return_to_owner",
        "tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject",
    ]
    fn["ring/curios_unbound"] = [
        f"function {NS}:ring/curios_pop",
        "tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject",
        tellraw("@s", [{"text": "A ring has to bind to you before you can wear it. It binds when you carry it, unless you "
                                "already bear a ring of its corps or you're handing it on.", "color": "gray",
                        "italic": True}]),
    ]
    # A ring binds to the first player who carries it: an unbound ring in your inventory binds to you, unless you're
    # handing it on (a forged or revoked ring, marked with you as its giver) or you already bear a ring of its corps
    # (a spare, waiting for another bearer). Rings held in a hand bind the same way, every tick (bind_check).
    fn["ring/carry_check"] = [  # as a player, twice a second
        f"execute store result score #all gl_tmp run clear @s #{NS}:lantern_rings 0",
        f"execute store result score #bound gl_tmp run clear @s #{NS}:lantern_rings{{gl_bound:1b}} 0",
        f"execute if score #all gl_tmp > #bound gl_tmp run function {NS}:ring/carry_scan",
    ]
    fn["ring/carry_scan"] = [
        f"data remove storage {STORAGE} carry",
        f"data modify storage {STORAGE} carry set from entity @s Inventory",
        f"execute if data storage {STORAGE} carry[0] run function {NS}:ring/carry_next",
    ]
    fn["ring/carry_next"] = [
        f"data modify storage {STORAGE} cur set from storage {STORAGE} carry[0]",
        f"data remove storage {STORAGE} carry[0]",
        "scoreboard players set #corps gl_tmp 0",
        *[f'execute if data storage {STORAGE} cur{{id:"{ring(c)}"}} run scoreboard players set #corps gl_tmp {idx[c]}'
          for c in corps],
        f"execute if score #corps gl_tmp matches 1.. unless data storage {STORAGE} cur.tag{{gl_bound:1b}} run "
        f"function {NS}:ring/carry_item",
        f"execute if data storage {STORAGE} carry[0] run function {NS}:ring/carry_next",
    ]
    carry_item = [
        f"execute store result score #slot gl_tmp run data get storage {STORAGE} cur.Slot",
        "execute unless score #slot gl_tmp matches 0..35 run scoreboard players set #corps gl_tmp 0",
        "scoreboard players set #giver gl_tmp 0",
        f"execute if data storage {STORAGE} cur.tag{{gl_gv:1b}} store result score #giver gl_tmp run "
        f"data get storage {STORAGE} cur.tag.gl_giver",
        "execute if score #giver gl_tmp = @s gl_id run scoreboard players set #corps gl_tmp 0",
        *[f"scoreboard players add @s gl_ser_{c} 0" for c in corps],
    ]
    for c in corps:
        carry_item += [line.replace("execute if score", f"execute if score #corps gl_tmp matches {idx[c]} if score", 1)
                       for line in bearer(c, "scoreboard players set #corps gl_tmp 0")]
    fn["ring/carry_item"] = carry_item + [f"execute if score #corps gl_tmp matches 1.. run function {NS}:ring/carry_bind"]
    fn["ring/carry_bind"] = [
        f"function {NS}:ring/store_owner", f"function {NS}:ring/new_serial",
        *[f"execute if score #slot gl_tmp matches {i} run item modify entity @s container.{i} {NS}:bind" for i in range(36)],
        *[line for c in corps for line in (
            f"execute if score #corps gl_tmp matches {idx[c]} run {set_serial(c)}",
            f"execute if score #corps gl_tmp matches {idx[c]} run tag @s remove gl_legacy_{c}",
            f"execute if score #corps gl_tmp matches {idx[c]} run tag @s add gl_member_{c}")],
        f"function {NS}:ring/save_serials",
        tellraw("@s", [{"text": "The ring binds itself to you. Wear it in a ring slot to use its power.", "color": "gray",
                        "italic": True}]),
        "playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6",
    ]
    fn["ring/curios_clear_slot"] = [f"execute if score #slot gl_tmp matches {i} run curios replace ring {i} @s with minecraft:air"
                                    for i in range(CURIOS_SLOTS)]
    write(f"data/{NS}/tags/functions/curios_clear_slot.json",
          {"values": [{"id": f"{NS}:ring/curios_clear_slot", "required": False}]})
    # remove every ring of corps #strip (an index) from the Curios ring slots, counting them in #stripped
    fn["ring/curios_strip"] = [
        f"data remove storage {STORAGE} rings",
        f"data modify storage {STORAGE} rings set from entity @s {curios_items}",
        f"execute if data storage {STORAGE} rings[0] run function {NS}:ring/curios_strip_next",
    ]
    fn["ring/curios_strip_next"] = [
        f"data modify storage {STORAGE} cur set from storage {STORAGE} rings[0]",
        f"data remove storage {STORAGE} rings[0]",
        "scoreboard players set #lantern gl_tmp 0",
        *[f'execute if score #strip gl_tmp matches {idx[c]} if data storage {STORAGE} cur{{id:"{ring(c)}"}} '
          f"run scoreboard players set #lantern gl_tmp 1" for c in corps],
        f"execute if score #lantern gl_tmp matches 1 store result score #slot gl_tmp run data get storage {STORAGE} cur.Slot",
        f"execute if score #lantern gl_tmp matches 1 unless score #slot gl_tmp matches 0..{CURIOS_SLOTS - 1} run "
        "scoreboard players set #lantern gl_tmp 0",
        f"execute if score #lantern gl_tmp matches 1 run function #{NS}:curios_clear_slot",
        "execute if score #lantern gl_tmp matches 1 run scoreboard players add #stripped gl_tmp 1",
        f"execute if data storage {STORAGE} rings[0] run function {NS}:ring/curios_strip_next",
    ]

    # ---------------------------------------------------------------- recall
    # Anyone can call their own rings back: /trigger gl_recall (every ring that chose you), and with
    # KubeJS "/ring recall [corps]" or a chat phrase like "ring, come to me".
    # - Already on you (hands, inventory or Curios slots): nothing to do.
    # - Lying in a loaded chunk, in any dimension: it flies back to you.
    # - Anywhere else (a chest, an unloaded chunk, lost): commands can't reach into chests, so a new
    #   ring forms in your inventory and the one left behind goes dark for good (new serial, see
    #   above). A dark ring crumbles when worn and comes back as a dead ring, so rings never duplicate.
    # A revoked or removed ring (gl_ser -1) can't be recalled.
    load += ["scoreboard objectives add gl_recall trigger", "scoreboard objectives add gl_rcd dummy"]
    init_serials = [f"scoreboard players add @s gl_ser_{c} 0" for c in corps]

    eligible = bearer

    cooldown_msg = tellraw("@s", [{"text": "Your ring is still answering your last call. Try again in ", "color": "gray"},
                                  {"score": {"name": "@s", "objective": "gl_rcd"}, "color": "white"},
                                  {"text": " s.", "color": "gray"}])
    fn["recall/request"] = [  # every ring that chose you
        f"execute if score @s gl_rcd matches 1.. run {cooldown_msg}",
        f"execute unless score @s gl_rcd matches 1.. run function {NS}:recall/all",
    ]
    fn["recall/all"] = [
        "scoreboard players set #called gl_tmp 0", *init_serials,
        *[line for c in corps for line in eligible(c, f"function {NS}:recall/{c}")],
        "execute if score #called gl_tmp matches 0 run "
        + tellraw("@s", [{"text": "No ring has chosen you yet.", "color": "gray"}]),
    ]
    fn["recall/trigger"] = [
        "scoreboard players operation #v gl_tmp = @s gl_recall",
        "scoreboard players set @s gl_recall 0",
        "scoreboard players enable @s gl_recall",
        f"execute if score #v gl_tmp matches 1 run function {NS}:recall/request",
        *[f"execute if score #v gl_tmp matches {10 + idx[c]} run function {NS}:recall/request_{c}" for c in corps],
        "execute unless score #v gl_tmp matches 1 unless score #v gl_tmp matches 11..19 run "
        + tellraw("@s", [{"text": "/trigger gl_recall calls all your rings. One ring: /trigger gl_recall set "
                                  + ", ".join(f"{10 + idx[c]} ({c})" for c in corps), "color": "gray"}]),
    ]
    rc = f"{STORAGE} rc"
    clear_inv = [f"execute if score #slot gl_tmp matches {i} run item replace entity @s container.{i} with minecraft:air"
                 for i in range(36)]
    clear_inv.append("execute if score #slot gl_tmp matches -106 run item replace entity @s weapon.offhand with minecraft:air")
    fn["recall/clear_inv_slot"] = clear_inv
    fn["recall/dark_inv"] = [f"execute store result score #slot gl_tmp run data get storage {rc}.Slot",
                             f"function {NS}:recall/clear_inv_slot", f"function {NS}:ring/dark_message"]
    fn["recall/dark_curios"] = [f"execute store result score #slot gl_tmp run data get storage {rc}.Slot",
                                f"function #{NS}:curios_clear_slot", f"function {NS}:ring/dark_message"]
    fn["recall/dark_ender"] = [f"execute store result score #slot gl_tmp run data get storage {rc}.Slot",
                                f"function {NS}:recall/clear_ender_slot", f"function {NS}:ring/dark_message"]
    fn["recall/clear_ender_slot"] = [
        f"execute if score #slot gl_tmp matches {i} run item replace entity @s enderchest.{i} with minecraft:air"
        for i in range(27)]
    fn["recall/from_ender"] = [  # a valid ring in your ender chest comes out at your feet, yours to pick up
        "scoreboard players set #found gl_tmp 2",
        f"execute store result score #slot gl_tmp run data get storage {rc}.Slot",
        'summon minecraft:item ~ ~0.5 ~ {Tags:["gl_drop"],PickupDelay:0s,Age:-32768s,Item:{id:"minecraft:stone",Count:1b}}',
        f"data modify entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Item set from storage {rc}",
        "data remove entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Item.Slot",
        "data modify entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Owner set from entity @s UUID",
        "tag @e[type=minecraft:item,tag=gl_drop] remove gl_drop",
        f"function {NS}:recall/clear_ender_slot",
    ]
    fn["recall/fly"] = [  # as the ring's item entity
        "scoreboard players set #found gl_tmp 2",
        "data merge entity @s {PickupDelay:0s,Age:-32768s}",
        "execute at @s run particle minecraft:end_rod ~ ~0.5 ~ 0.2 0.2 0.2 0.05 20 force",
        "execute at @a[tag=gl_caller,limit=1] run tp @s ~ ~0.5 ~",
    ]
    for c in corps:
        rgb = corps_table[c]["color"]
        col = color(rgb if c != "black" else (170, 175, 190))
        name = corps_table[c]["name"]
        fn[f"recall/request_{c}"] = [
            f"execute if score @s gl_rcd matches 1.. run {cooldown_msg}",
            f"execute unless score @s gl_rcd matches 1.. run function {NS}:recall/one_{c}",
        ]
        fn[f"recall/one_{c}"] = [
            "scoreboard players set #called gl_tmp 0", *init_serials,
            *eligible(c, f"function {NS}:recall/{c}"),
            "execute if score #called gl_tmp matches 0 run "
            + tellraw("@s", [{"text": f"No {name} ring has chosen you.", "color": "gray"}]),
        ]
        fn[f"recall/{c}"] = [  # as and at the caller, who may call it
            "scoreboard players add #called gl_tmp 1",
            "scoreboard players set @s gl_rcd 10",
            "scoreboard players set #found gl_tmp 0",
            "tag @a remove gl_caller",
            "tag @s add gl_caller",
            f"function {NS}:recall/self_{c}",
            f"execute if score #found gl_tmp matches 0 as @e[type=minecraft:item,nbt={{Item:{{id:\"{ring(c)}\","
            f"tag:{{gl_bound:1b}}}}}}] run function {NS}:recall/item_{c}",
            f"execute if score #found gl_tmp matches 0 run function {NS}:recall/reforge_{c}",
            "execute if score #found gl_tmp matches 1 run "
            + tellraw("@s", [{"text": f"Your {name} ring is already with you.", "color": col}]),
            "execute if score #found gl_tmp matches 2 run "
            + tellraw("@s", [{"text": f"Your {name} ring flies back to you.", "color": col}]),
            "execute if score #found gl_tmp matches 2 run playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6",
            "tag @s remove gl_caller",
        ]
        # 1. on you: your inventory (hands included) and your Curios ring slots
        fn[f"recall/self_{c}"] = [
            f"data remove storage {STORAGE} scan",
            f"data modify storage {STORAGE} scan set from entity @s Inventory",
            f"execute if data storage {STORAGE} scan[0] run function {NS}:recall/self_next_{c}",
            f"data remove storage {STORAGE} scan",
            f"data modify storage {STORAGE} scan set from entity @s {curios_items}",
            f"execute if data storage {STORAGE} scan[0] run function {NS}:recall/curios_next_{c}",
            # your ender chest: a valid ring there comes out to you
            f"data remove storage {STORAGE} scan",
            f"execute if score #found gl_tmp matches 0 run data modify storage {STORAGE} scan set from entity @s EnderItems",
            f"execute if data storage {STORAGE} scan[0] run function {NS}:recall/ender_next_{c}",
        ]
        for kind, dark in (("self", "dark_inv"), ("curios", "dark_curios"), ("ender", "dark_ender")):
            fn[f"recall/{kind}_next_{c}"] = [
                f"data modify storage {rc} set from storage {STORAGE} scan[0]",
                f"data remove storage {STORAGE} scan[0]",
                f'execute if data storage {rc}{{id:"{ring(c)}",tag:{{gl_bound:1b}}}} run function {NS}:recall/{kind}_item_{c}',
                f"execute if data storage {STORAGE} scan[0] run function {NS}:recall/{kind}_next_{c}",
            ]
            found = f"function {NS}:recall/from_ender" if kind == "ender" else "scoreboard players set #found gl_tmp 1"
            fn[f"recall/{kind}_item_{c}"] = [
                f"execute store result score #owner gl_tmp run data get storage {rc}.tag.gl_owner",
                f"execute store result score #s gl_tmp run data get storage {rc}.tag.gl_serial",
                f"execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp = @s gl_ser_{c} run {found}",
                f"execute if score #owner gl_tmp = @s gl_id unless score #s gl_tmp = @s gl_ser_{c} run "
                f"function {NS}:recall/{dark}",
            ]
        # 2. lying in a loaded chunk anywhere (run as each such item); dark copies crumble
        caller = "@a[tag=gl_caller,limit=1]"
        fn[f"recall/item_{c}"] = [
            "execute store result score #owner gl_tmp run data get entity @s Item.tag.gl_owner",
            "execute store result score #s gl_tmp run data get entity @s Item.tag.gl_serial",
            f"execute if score #owner gl_tmp = {caller} gl_id unless score #s gl_tmp = {caller} gl_ser_{c} run "
            "execute at @s run particle minecraft:smoke ~ ~0.3 ~ 0.1 0.1 0.1 0.02 15 force",
            f"execute if score #owner gl_tmp = {caller} gl_id unless score #s gl_tmp = {caller} gl_ser_{c} run kill @s",
            f"execute if score #owner gl_tmp = {caller} gl_id if score #s gl_tmp = {caller} gl_ser_{c} run "
            f"function {NS}:recall/fly",
        ]
        # 3. anywhere else: a new ring forms, and the one left behind goes dark
        fn[f"recall/reforge_{c}"] = [
            f"function {NS}:ring/store_owner", f"function {NS}:ring/new_serial", set_serial(c),
            f"tag @s remove gl_legacy_{c}", f"function {NS}:ring/save_serials",
            *give_ring(c),
            f"tag @s add gl_member_{c}",
            f"particle minecraft:dust {rgb[0] / 255:.2f} {rgb[1] / 255:.2f} {rgb[2] / 255:.2f} 1.5 ~ ~1.2 ~ 0.4 0.6 0.4 0 60 force",
            "playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.6",
            tellraw("@s", [{"text": f"Your {name} ring answers your call and forms on you. ", "color": col},
                           {"text": "The ring you left behind has gone dark.", "color": "gray", "italic": True}]),
        ]

    # ---------------------------------------------------------------- forging
    # A bearer can forge a new ring for a recruit by speaking their corps' oath: in chat with KubeJS
    # (the words must match the oath), or with /trigger gl_forge or /ring forge, which recite it for
    # them. They must wear a valid ring of that corps; it costs FORGE_COST charge and the forge then
    # rests for #forge_cd seconds. The new ring is unbound and marked with its maker, so it never binds
    # to them (it can't replace or darken their own ring); it binds to the next player who holds it.
    load += ["scoreboard objectives add gl_forge trigger", "scoreboard objectives add gl_fcd dummy",
             "execute unless score #forge gl_cfg matches 0.. run scoreboard players set #forge gl_cfg 1",
             f"execute unless score #forge_cd gl_cfg matches 0.. run scoreboard players set #forge_cd gl_cfg {FORGE_COOLDOWN}"]
    fn["forge/trigger"] = [
        "scoreboard players operation #v gl_tmp = @s gl_forge",
        "scoreboard players set @s gl_forge 0",
        "scoreboard players enable @s gl_forge",
        f"execute if score #v gl_tmp matches 1 run function {NS}:forge/recite_any",
        *[f"execute if score #v gl_tmp matches {10 + idx[c]} run function {NS}:forge/recite_{c}" for c in corps],
    ]
    fn["forge/recite_any"] = [  # the first corps whose ring you wear
        "scoreboard players set #done gl_tmp 0",
        *[f"execute if score #done gl_tmp matches 0 if entity @s[tag=gl_{c}] run function {NS}:forge/recite_{c}"
          for c in corps],
        "execute if score #done gl_tmp matches 0 run "
        + tellraw("@s", [{"text": "Wear your ring to forge another.", "color": "gray"}]),
    ]
    for c in corps:
        rgb = corps_table[c]["color"]
        col = color(rgb if c != "black" else (170, 175, 190))
        name = corps_table[c]["name"]
        power = f"{NS}:{c}_lantern"
        oath = corps_table[c]["oath"]
        recite = [tellraw("@a[distance=..24]", ([{"selector": "@s", "color": col}, {"text": ": ", "color": "gray"}]
                                                if i == 0 else [{"text": "   "}])
                          + [{"translate": f"oath.{NS}.{c}.{i + 1}", "color": col, "italic": True}])
                  for i in range(len(oath))]
        fn[f"forge/recite_{c}"] = ["scoreboard players set #done gl_tmp 1", *recite, f"function {NS}:forge/request_{c}"]
        fn[f"forge/request_{c}"] = [  # the oath has been spoken: as and at the bearer
            f"execute if score #forge gl_cfg matches 0 run "
            + tellraw("@s", [{"text": "Forging new rings is turned off on this server.", "color": "gray"}]),
            f"execute if score #forge gl_cfg matches 1.. run function {NS}:forge/try_{c}",
        ]
        fn[f"forge/try_{c}"] = [
            "scoreboard players set #ok gl_tmp 1",
            f"scoreboard players add @s gl_ser_{c} 0",
            f"execute unless entity @s[tag=gl_{c}] run scoreboard players set #ok gl_tmp 0",
            f"execute if score @s gl_ser_{c} matches -1 run scoreboard players set #ok gl_tmp 0",
            f"execute if score @s gl_ser_{c} matches 0 unless entity @s[tag=gl_legacy_{c}] run scoreboard players set #ok gl_tmp 0",
            f"execute if score #ok gl_tmp matches 0 run "
            + tellraw("@s", [{"text": f"Your words echo, but no ring answers. Wear your own {name} ring to forge another.",
                              "color": "gray", "italic": True}]),
            f"execute if score #ok gl_tmp matches 1 if score @s gl_fcd matches 1.. run function {NS}:forge/resting",
            f"execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s {power} ring_charge",
            f"execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..{FORGE_COST - 1} run "
            f"function {NS}:forge/low_charge",
            f"execute if score #ok gl_tmp matches 1 run function {NS}:forge/do_{c}",
        ]
        fn[f"forge/do_{c}"] = [
            f"energybar value subtract @s {power} ring_charge {FORGE_COST}",
            "scoreboard players operation @s gl_fcd = #forge_cd gl_cfg",
            f"function {NS}:ring/store_giver",
            *give_ring(f"giver_{c}"),
            f"particle minecraft:dust {rgb[0] / 255:.2f} {rgb[1] / 255:.2f} {rgb[2] / 255:.2f} 2 ~ ~1.2 ~ 0.5 0.8 0.5 0 150 force",
            "particle minecraft:flash ~ ~1.2 ~ 0 0 0 0 1 force",
            "playsound minecraft:block.anvil.use player @a[distance=..24] ~ ~ ~ 0.6 1.6",
            "playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.2",
            "title @s times 10 50 15",
            "title @s subtitle " + json.dumps({"text": "Give it to someone worthy: it binds to the next one who holds it.",
                                               "color": "gray"}),
            "title @s title " + json.dumps({"text": f"A new {name} ring is forged", "color": col}),
            tellraw("@a[distance=0.1..24]", [{"selector": "@s", "color": col},
                                             {"text": f" forged a new {name} ring!", "color": "white"}]),
        ]
    fn["forge/resting"] = [
        "scoreboard players set #ok gl_tmp 0",
        tellraw("@s", [{"text": "Your ring is still recovering from the last forging. Try again in ", "color": "gray"},
                       {"score": {"name": "@s", "objective": "gl_fcd"}, "color": "white"}, {"text": " s.", "color": "gray"}]),
    ]
    fn["forge/low_charge"] = [
        "scoreboard players set #ok gl_tmp 0",
        tellraw("@s", [{"text": f"Forging a ring takes {FORGE_COST} charge. Recharge at your Power Battery first.",
                        "color": "gray"}]),
    ]
    for state, value in (("on", 1), ("off", 0)):
        fn[f"admin/forging_{state}"] = [
            f"scoreboard players set #forge gl_cfg {value}",
            tellraw("@s", [{"text": f"Ring forging is {state.upper()}.", "color": "green" if value else "red"}])]

    # ---------------------------------------------------------------- emotions
    feed = []
    for e in EMOTIONS:
        for i, (crit, w) in enumerate(SOURCES[e]):
            src = f"gl_s_{e}{i}"
            track = f"gl_tr_{e}{i}"  # lifetime points from this source, for the Emotional Spectrum menu
            if w == 1:
                feed.append(f"scoreboard players operation @s gl_e_{e} += @s {src}")
                feed.append(f"scoreboard players operation @s {track} += @s {src}")
                feed.append(f"scoreboard players set @s {src} 0")
            elif w > 1:
                feed += [f"scoreboard players operation @s gl_tmp = @s {src}",
                         f"scoreboard players operation @s gl_tmp *= #w{w} gl_cfg",
                         f"scoreboard players operation @s gl_e_{e} += @s gl_tmp",
                         f"scoreboard players operation @s {track} += @s gl_tmp",
                         f"scoreboard players set @s {src} 0"]
            else:  # divide, keeping the remainder for next time
                feed += [f"scoreboard players operation @s gl_tmp = @s {src}",
                         f"scoreboard players operation @s gl_tmp /= #w{-w} gl_cfg",
                         f"scoreboard players operation @s gl_e_{e} += @s gl_tmp",
                         f"scoreboard players operation @s {track} += @s gl_tmp",
                         f"scoreboard players operation @s {src} %= #w{-w} gl_cfg"]
    fn["emotion/feed"] = [f"scoreboard players add @s gl_e_{e} 0" for e in EMOTIONS] + feed
    # ---------------------------------------------------------------- ring offers
    def offer_ok(c):  # never a revoked or removed bearer (gl_ser -1): only an admin can offer them that ring again
        return f"@a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_{c},scores={{gl_cd_{c}=..0,gl_ser_{c}=0..}}]"

    offer_scan = [f"scoreboard players add @a gl_cd_{c} 0" for c in corps] + [
        f"scoreboard players add @a gl_ser_{c} 0" for c in corps]
    for c in corps:
        if c == "white":
            cond = " ".join(f"if score @s gl_e_{EMOTION_OF[s]} >= #threshold gl_cfg" for s in SPECTRUM)
        else:
            cond = f"if score @s gl_e_{EMOTION_OF[c]} >= #threshold gl_cfg"
        offer_scan.append(f"execute as {offer_ok(c)} {cond} run function {NS}:offer/start_{c}")

    for c in corps:
        rgb = corps_table[c]["color"]
        col = color(rgb if c != "black" else (170, 175, 190))
        emo = "great strength in every emotion" if c == "white" else f"great {EMOTION_NAME[EMOTION_OF[c]]}"
        fn[f"offer/start_{c}"] = [
            f"tag @s add gl_offer_{c}", "tag @s add gl_offer_any",
            f"scoreboard players set @s gl_offer {OFFER_SECONDS}",
            "scoreboard players enable @s gl_accept", "scoreboard players enable @s gl_decline",
            "scoreboard players operation #cur gl_id = @s gl_id",
            "execute anchored eyes positioned ^ ^ ^1.6 run summon minecraft:item_display ~ ~6 ~ "
            f'{{Tags:["gl_offer_disp","gl_offer_new"],item:{{id:"{ring(c)}",Count:1b}},billboard:"center",'
            f'brightness:{{sky:15,block:15}},{DISPLAY_TRANSFORM}}}',
            "scoreboard players operation @e[type=minecraft:item_display,tag=gl_offer_new] gl_id = #cur gl_id",
            "tag @e[type=minecraft:item_display,tag=gl_offer_new] remove gl_offer_new",
            "playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.5",
            tellraw("@s", [{"text": "✦ ", "color": col}, {"text": f"A {CORPS_TITLE[c].replace(' Corps', '')} ring "
                                                                 "streaks down from the sky.", "color": col}]),
            tellraw("@s", [{"selector": "@s", "color": col}, {"text": f", you have {emo}. Welcome to the "
                                                                    f"{CORPS_TITLE[c]}. Do you accept?", "color": "white"}]),
            tellraw("@s", [
                {"text": "  [ACCEPT]", "color": "green", "bold": True,
                 "clickEvent": {"action": "run_command", "value": f"/trigger gl_accept set {idx[c]}"},
                 "hoverEvent": {"action": "show_text", "contents": f"Join the {CORPS_TITLE[c]}"}},
                {"text": "   "},
                {"text": "[DECLINE]", "color": "red", "bold": True,
                 "clickEvent": {"action": "run_command", "value": f"/trigger gl_decline set {idx[c]}"},
                 "hoverEvent": {"action": "show_text", "contents": "Send the ring away"}},
                {"text": "   (or type yes / no in chat)", "color": "dark_gray", "italic": True}]),
        ]
        fn[f"offer/accept_{c}"] = [
            f"function {NS}:ring/store_owner",
            f"function {NS}:ring/new_serial",
            set_serial(c), f"tag @s remove gl_legacy_{c}", f"function {NS}:ring/save_serials",
            *give_ring(c),
            # the ring brings its power battery with it (/give drops it at your feet if you're full)
            f"give @s {NS}:{c}_power_battery",
            f"tag @s add gl_member_{c}",
            f"function {NS}:offer/clear",
            f"title @s times 10 60 20",
            "title @s subtitle " + json.dumps({"text": "Your ring is bound to you.", "color": "gray"}),
            "title @s title " + json.dumps({"text": f"Welcome to the {CORPS_TITLE[c]}", "color": col}),
            f"particle minecraft:dust {rgb[0] / 255:.2f} {rgb[1] / 255:.2f} {rgb[2] / 255:.2f} 2 ~ ~1 ~ 0.6 1 0.6 0 120 force",
            "playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1",
            tellraw("@a", [{"selector": "@s", "color": col}, {"text": f" has been chosen by the {CORPS_TITLE[c]}!",
                                                              "color": "white"}]),
            tellraw("@s", [{"text": "Your ring brought its Power Battery. ", "color": col},
                           {"text": "Right-click it (placed, or held in your hand) to recharge your ring.",
                            "color": "gray"}]),
        ]
        fn[f"offer/decline_{c}"] = [
            f"scoreboard players set @s gl_cd_{c} {DECLINE_COOLDOWN}",
            f"function {NS}:offer/send_away",
            f"function {NS}:offer/clear",
            tellraw("@s", [{"text": "The ring hesitates... then streaks away to search for another.", "color": col,
                            "italic": True}]),
            "playsound minecraft:entity.firework_rocket.launch player @s ~ ~ ~ 1 0.8",
        ]
    fn["offer/clear"] = [f"tag @s remove gl_offer_{c}" for c in corps] + [
        "tag @s remove gl_offer_any", "scoreboard players set @s gl_offer 0",
        "scoreboard players set @s gl_accept 0", "scoreboard players set @s gl_decline 0",
        "scoreboard players operation #cur gl_id = @s gl_id",
        "execute as @e[type=minecraft:item_display,tag=gl_offer_disp] if score @s gl_id = #cur gl_id run kill @s",
    ]
    # the ring rises and fades away
    fn["offer/send_away"] = [
        "scoreboard players operation #cur gl_id = @s gl_id",
        "execute as @e[type=minecraft:item_display,tag=gl_offer_disp] if score @s gl_id = #cur gl_id at @s run "
        "summon minecraft:item_display ~ ~ ~ {Tags:[\"gl_leaving\",\"gl_leave_new\"],billboard:\"center\","
        "brightness:{sky:15,block:15}," + DISPLAY_TRANSFORM + "}",
        "execute as @e[type=minecraft:item_display,tag=gl_offer_disp] if score @s gl_id = #cur gl_id run "
        "data modify entity @e[type=minecraft:item_display,tag=gl_leave_new,limit=1,sort=nearest] item set from entity @s item",
        "scoreboard players set @e[type=minecraft:item_display,tag=gl_leave_new] gl_tmp 30",
        "tag @e[type=minecraft:item_display,tag=gl_leave_new] add gl_leave_go",
        "tag @e[type=minecraft:item_display,tag=gl_leave_new] remove gl_leave_new",
    ]
    fn["offer/follow"] = [
        "scoreboard players operation #cur gl_id = @s gl_id",
        "execute anchored eyes positioned ^ ^ ^1.6 as @e[type=minecraft:item_display,tag=gl_offer_disp] "
        "if score @s gl_id = #cur gl_id run tp @s ~ ~ ~",
    ]
    fn["offer/accept_trigger"] = [
        *[f"execute if score @s gl_accept matches {idx[c]} if entity @s[tag=gl_offer_{c}] run function {NS}:offer/accept_{c}"
          for c in corps],
        "scoreboard players set @s gl_accept 0",
    ]
    fn["offer/decline_trigger"] = [
        *[f"execute if score @s gl_decline matches {idx[c]} if entity @s[tag=gl_offer_{c}] run function {NS}:offer/decline_{c}"
          for c in corps],
        "scoreboard players set @s gl_decline 0",
    ]
    fn["offer/chat_yes"] = [f"execute if entity @s[tag=gl_offer_any] run function {NS}:offer/accept_chat"]
    fn["offer/chat_no"] = [f"execute if entity @s[tag=gl_offer_any] run function {NS}:offer/decline_chat"]
    fn["offer/accept_chat"] = [f"execute if entity @s[tag=gl_offer_{c}] run function {NS}:offer/accept_{c}" for c in corps]
    fn["offer/decline_chat"] = [f"execute if entity @s[tag=gl_offer_{c}] run function {NS}:offer/decline_{c}" for c in corps]
    fn["offer/timeout"] = [f"execute if entity @s[tag=gl_offer_{c}] run function {NS}:offer/decline_{c}" for c in corps]

    # ---------------------------------------------------------------- leaders
    for c in corps:
        rgb = corps_table[c]["color"]
        col = color(rgb if c != "black" else (170, 175, 190))
        # strip: take every ring of this corps from the player (inventory, hands and Curios ring slots)
        fn[f"ring/strip_{c}"] = [
            f"execute store result score #stripped gl_tmp run clear @s {ring(c)}",
            f"scoreboard players set #strip gl_tmp {idx[c]}",
            f"function {NS}:ring/curios_strip",
            f"tag @s remove gl_member_{c}",
            f"tag @s remove gl_leader_{c}",
            f"scoreboard players set @s gl_ser_{c} -1",  # and it can't be recalled
            f"tag @s remove gl_legacy_{c}", f"function {NS}:ring/save_serials",
        ]
        fn[f"leader/revoke_{c}"] = [  # run as the leader: revoke the nearest bearer of this corps' ring
            "tag @s add gl_revoker",
            f"execute as @p[tag=gl_{c},tag=!gl_revoker,tag=!gl_leader_{c},distance=..8] run "
            f"function {NS}:leader/revoke_target_{c}",
            f"execute unless entity @p[tag=gl_revoked,distance=..8] run "
            + tellraw("@s", [{"text": "No member of your corps is close enough.", "color": "gray"}]),
            "tag @a remove gl_revoked",
            "tag @s remove gl_revoker",
        ]
        fn[f"leader/revoke_target_{c}"] = [  # run as the member; the leader has tag gl_revoker
            f"execute unless entity @s[tag=gl_leader_{c}] run function {NS}:leader/revoke_do_{c}",
        ]
        fn[f"leader/revoke_do_{c}"] = [  # leaders can't revoke each other
            f"function {NS}:ring/strip_{c}",
            "tag @s add gl_revoked",
            f"execute if score #stripped gl_tmp matches 1.. as @a[tag=gl_revoker,limit=1] at @s run "
            f"function {NS}:leader/give_revoked_{c}",
            tellraw("@s", [{"text": "Your corps leader has revoked your ring.", "color": col}]),
            tellraw("@a[tag=gl_revoker]", [{"text": "You revoked the ring of ", "color": col}, {"selector": "@s"},
                                           {"text": ". It is unbound and won't bind to you: hand it to your next "
                                                    "recruit.", "color": col}]),
            "particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force",
            "playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 1",
        ]
        fn[f"leader/give_revoked_{c}"] = [f"function {NS}:ring/store_giver", *give_ring(f"giver_{c}")]
        fn[f"leader/revoke_id_{c}"] = [  # run as the leader with #target gl_tmp set
            "tag @s add gl_revoker",
            f"execute as @a if score @s gl_id = #target gl_tmp run function {NS}:leader/revoke_target_{c}",
            "tag @a remove gl_revoked",
            "tag @s remove gl_revoker",
        ]
        fn[f"leader/roster_{c}"] = [
            "tag @s add gl_viewer",
            tellraw("@s", [{"text": f"{CORPS_TITLE[c]} roster (online)", "color": col, "bold": True}]),
            f"execute as @a[tag=gl_member_{c}] run "
            + tellraw("@a[tag=gl_viewer]", [{"text": "  "}, {"selector": "@s"}, {"text": "  id ", "color": "gray"},
                                            {"score": {"name": "@s", "objective": "gl_id"}, "color": "yellow"}]),
            tellraw("@s", [{"text": "Revoke with ", "color": "gray"}, {"text": "/trigger gl_revoke set <id>",
                                                                        "color": "yellow"}]),
            "tag @s remove gl_viewer",
        ]
    fn["leader/revoke_trigger"] = [
        "scoreboard players operation #target gl_tmp = @s gl_revoke",
        *[f"execute if entity @s[tag=gl_leader_{c}] run function {NS}:leader/revoke_id_{c}" for c in corps],
        "scoreboard players set @s gl_revoke 0",
    ]
    fn["leader/roster_trigger"] = [
        *[f"execute if entity @s[tag=gl_leader_{c}] run function {NS}:leader/roster_{c}" for c in corps],
        "scoreboard players set @s gl_roster 0",
    ]
    fn["leader/update_any"] = ["tag @s remove gl_leader_any"] + [
        f"execute if entity @s[tag=gl_leader_{c}] run tag @s add gl_leader_any" for c in corps]

    # ---------------------------------------------------------------- admin (run "as <player>")
    for c in corps:
        col = color(corps_table[c]["color"] if c != "black" else (170, 175, 190))
        fn[f"admin/give/{c}"] = [f"function {NS}:ring/store_owner", f"function {NS}:ring/new_serial", set_serial(c),
                                 f"tag @s remove gl_legacy_{c}", f"function {NS}:ring/save_serials",
                                 *give_ring(c), f"tag @s add gl_member_{c}"]
        fn[f"admin/give_unbound/{c}"] = [f"give @s {ring(c)}"]
        fn[f"admin/battery/{c}"] = [f"give @s {NS}:{c}_power_battery"]
        fn[f"admin/leader/{c}"] = [
            f"tag @s add gl_leader_{c}", f"tag @s add gl_member_{c}", f"function {NS}:leader/update_any",
            tellraw("@s", [{"text": f"You are now a leader of the {CORPS_TITLE[c]}. ", "color": col},
                           {"text": "Use the Revoke Ring ability, /trigger gl_roster and /trigger gl_revoke set <id>.",
                            "color": "gray"}]),
        ]
        fn[f"admin/unleader/{c}"] = [f"tag @s remove gl_leader_{c}", f"function {NS}:leader/update_any"]
        fn[f"admin/remove/{c}"] = [f"function {NS}:ring/strip_{c}", f"function {NS}:leader/update_any"]
        fn[f"admin/offer/{c}"] = [f"function {NS}:offer/clear", f"scoreboard players set @s gl_cd_{c} 0",
                                  f"execute if score @s gl_ser_{c} matches -1 run scoreboard players set @s gl_ser_{c} 0",
                                  f"function {NS}:ring/save_serials",
                                  f"function {NS}:offer/start_{c}"]
        fn[f"admin/emotion/max_{EMOTION_OF.get(c, 'all')}"] = (
            [f"scoreboard players operation @s gl_e_{e} = #threshold gl_cfg" for e in EMOTIONS] if c == "white"
            else [f"scoreboard players operation @s gl_e_{EMOTION_OF[c]} = #threshold gl_cfg"])
    fn["admin/remove_all"] = [f"function {NS}:ring/strip_{c}" for c in corps] + [f"function {NS}:leader/update_any"]
    fn["admin/unbind"] = [  # the holder won't re-bind it: it binds to the next player who holds it
        f"execute unless predicate {NS}:ring_mainhand run "
        + tellraw("@s", [{"text": "Hold the ring in your main hand to unbind it.", "color": "gray"}]),
        f"execute if predicate {NS}:ring_mainhand run function {NS}:ring/store_giver",
        *[f"execute if predicate {NS}:held/{c}_mainhand run scoreboard players set @s gl_ser_{c} -1" for c in corps],
        *[f"execute if predicate {NS}:held/{c}_mainhand run tag @s remove gl_legacy_{c}" for c in corps],
        f"execute if predicate {NS}:ring_mainhand run function {NS}:ring/save_serials",
        f"execute if predicate {NS}:ring_mainhand run item modify entity @s weapon.mainhand {NS}:unbind",
        f"execute if predicate {NS}:ring_mainhand run "
        + tellraw("@s", [{"text": "The ring in your hand is unbound. It will bind to the next player who holds it.",
                          "color": "gray"}]),
    ]
    fn["admin/reset_emotions"] = [f"scoreboard players set @s gl_e_{e} 0" for e in EMOTIONS]
    fn["admin/reset_cooldowns"] = [f"scoreboard players set @s gl_cd_{c} 0" for c in corps]
    fn["admin/show"] = [
        f"function {NS}:emotion/show",
        tellraw("@s", [{"text": "  id ", "color": "gray"}, {"score": {"name": "@s", "objective": "gl_id"}}]),
    ]
    fn["admin/enable"] = ["scoreboard players set #enabled gl_cfg 1",
                          tellraw("@s", [{"text": "Ring offers and emotions are ON.", "color": "green"}])]
    fn["admin/disable"] = ["scoreboard players set #enabled gl_cfg 0",
                           tellraw("@s", [{"text": "Ring offers and emotions are OFF.", "color": "red"}])]
    fn["admin/help"] = [tellraw("@s", [{"text": line, "color": "gray" if i else "gold"}]) for i, line in enumerate([
        "Lantern Corps admin (with KubeJS use /lantern, otherwise run these functions):",
        "/lantern give|unbound|battery <player> <corps>  -  execute as <player> run function greenlantern:admin/give/<corps>",
        "/lantern emotion <player> <emotion> set|add <n>  -  scoreboard players set <player> gl_e_<emotion> <n>",
        "  emotions: " + ", ".join(EMOTIONS),
        "/lantern leader|unleader <player> <corps>  -  function greenlantern:admin/leader/<corps>",
        "/lantern remove <player> <corps> | removeall <player>  -  function greenlantern:admin/remove/<corps>",
        "/lantern offer <player> <corps>  -  makes that corps' ring choose the player now",
        "/lantern unbind <player>  -  unbinds the ring in their main hand",
        "/lantern threshold <n>  -  scoreboard players set #threshold gl_cfg <n>",
        "Players: /trigger gl_recall (or /ring recall [corps], or 'ring, come to me' in chat) calls their rings back",
        "  one ring: /trigger gl_recall set " + ", ".join(f"{10 + idx[c]} {c}" for c in corps),
        f"Players: say their corps' oath (or /trigger gl_forge, /ring forge) to forge an unbound ring ({FORGE_COST} charge)",
        "/lantern forging on|off  |  /lantern forgecooldown <seconds>  -  ring forging",
        "/lantern reset <player> | show <player> | enable | disable",
        "corps: " + ", ".join(corps),
    ])]

    # ---------------------------------------------------------------- tick wiring
    tick += [
        f"execute as @a at @s run function {NS}:ring/bind_check",
        # rings worn in Curios slots, twice a second, for players a ring is powering
        f"execute if score #second gl_cfg matches 5 as @a[tag=gl_ring] at @s run function {NS}:ring/serial_check",
        f"execute if score #second gl_cfg matches 15 as @a[tag=gl_ring] at @s run function {NS}:ring/serial_check",
        f"execute if score #second gl_cfg matches 0 as @a at @s run function {NS}:ring/carry_check",
        f"execute if score #second gl_cfg matches 10 as @a at @s run function {NS}:ring/carry_check",
        f"execute as @a[scores={{gl_recall=1..}}] at @s run function {NS}:recall/trigger",
        f"execute as @a[scores={{gl_forge=1..}}] at @s run function {NS}:forge/trigger",
        "scoreboard players set @a[scores={gl_recall=..-1}] gl_recall 0",
        "scoreboard players set @a[scores={gl_forge=..-1}] gl_forge 0",
        f"execute as @a[tag=gl_offer_any] at @s run function {NS}:offer/follow",
        f"execute as @a[scores={{gl_accept=1..}}] at @s run function {NS}:offer/accept_trigger",
        f"execute as @a[scores={{gl_decline=1..}}] at @s run function {NS}:offer/decline_trigger",
        f"execute as @a[scores={{gl_revoke=1..}}] at @s run function {NS}:leader/revoke_trigger",
        f"execute as @a[scores={{gl_roster=1..}}] run function {NS}:leader/roster_trigger",
        # leaving rings rise and vanish
        "execute as @e[type=minecraft:item_display,tag=gl_leave_go] at @s run tp @s ~ ~0.6 ~",
        "scoreboard players remove @e[type=minecraft:item_display,tag=gl_leave_go] gl_tmp 1",
        "kill @e[type=minecraft:item_display,tag=gl_leave_go,scores={gl_tmp=..0}]",
        # once per second
        "scoreboard players add #second gl_cfg 1",
        f"execute if score #second gl_cfg matches 20.. run function {NS}:second",
    ]
    fn["second"] = [
        "scoreboard players set #second gl_cfg 0",
        f"execute if score #enabled gl_cfg matches 1 as @a run function {NS}:emotion/feed",
        f"execute if score #enabled gl_cfg matches 1 run function {NS}:offer/scan",
        *[f"scoreboard players remove @a[scores={{gl_cd_{c}=1..}}] gl_cd_{c} 1" for c in corps],
        "scoreboard players remove @a[tag=gl_offer_any] gl_offer 1",
        f"execute as @a[tag=gl_offer_any,scores={{gl_offer=..0}}] at @s run function {NS}:offer/timeout",
        "scoreboard players enable @a[tag=gl_offer_any] gl_accept",
        "scoreboard players enable @a[tag=gl_offer_any] gl_decline",
        "scoreboard players enable @a[tag=gl_leader_any] gl_revoke",
        "scoreboard players enable @a[tag=gl_leader_any] gl_roster",
        "scoreboard players enable @a gl_emotions",
        "scoreboard players enable @a gl_recall",
        "scoreboard players enable @a gl_forge",
        "scoreboard players remove @a[scores={gl_fcd=1..}] gl_fcd 1",
        "scoreboard players remove @a[scores={gl_reser=1..}] gl_reser 1",
        f"execute as @a[tag=gl_hasid] run function {NS}:id/verify",
        f"execute as @a[tag=gl_hasid,tag=!gl_sersaved] run function {NS}:ring/save_serials",
        "tag @a[tag=gl_reser,scores={gl_reser=..0}] remove gl_reser",
        "scoreboard players remove @a[scores={gl_rcd=1..}] gl_rcd 1",
    ]
    fn["offer/scan"] = offer_scan

    write_kubejs(corps_table, write_text)
    return load, tick, fn


def write_kubejs(corps_table, write_text):
    """Optional /lantern, /ring and /emotions commands and looser chat wordings when KubeJS is installed."""
    corps = list(corps_table)
    script = (KUBEJS_TEMPLATE.replace("__CORPS__", json.dumps(corps)).replace("__EMOTIONS__", json.dumps(EMOTIONS))
              .replace("__OATHS__", json.dumps({c: " ".join(corps_table[c]["oath"]) for c in corps}, indent=2))
              .replace("__PHRASES__", json.dumps(sorted(chat_phrases(corps_table)))))
    write_text(f"data/{NS}/kubejs_scripts/lantern_commands.js", script)
    return script


KUBEJS_TEMPLATE = r"""// Lantern Corps: the /lantern admin command, /ring recall|forge, /emotions, and looser chat wordings for calling
// your ring and speaking your oath. Loaded by Palladium's KubeJS integration when KubeJS is installed (or copy it
// into kubejs/server_scripts). Without KubeJS the exact phrases still work through Palladium, and the rest is
// available through /trigger and /function greenlantern:admin/...
const CORPS = __CORPS__
const EMOTIONS = __EMOTIONS__
const OATHS = __OATHS__
// answered by Palladium itself (exact messages), so the script leaves them alone
const PALLADIUM_PHRASES = __PHRASES__
console.info('[Lantern Corps] KubeJS script loaded: /lantern, /ring and /emotions')

ServerEvents.commandRegistry(event => {
  const { commands: Commands, arguments: Arguments } = event

  const run = (ctx, cmd) => {
    ctx.source.server.runCommandSilent(cmd)
    return 1
  }
  // run a function as the player who typed the command (by UUID), or directly from the console
  const runSelf = (ctx, fn) => {
    const player = ctx.source.player
    return run(ctx, player ? `execute as ${player.getStringUUID()} at @s run function ${fn}` : `function ${fn}`)
  }
  // corps names, filtered by what has been typed
  const suggestCorps = (builder) => {
    const typed = String(builder.getRemaining()).toLowerCase()
    CORPS.forEach(c => { if (c.indexOf(typed) === 0) builder.suggest(c) })
    return builder.buildFuture()
  }
  const playerName = (ctx) => Arguments.PLAYER.getResult(ctx, 'player').getGameProfile().getName()
  const corpsArg = (then) => Commands.argument('corps', Arguments.WORD.create(event))
    .suggests((ctx, builder) => suggestCorps(builder))
    .executes(then)
  const asPlayer = (ctx, fn) => run(ctx, `execute as ${playerName(ctx)} at @s run function greenlantern:${fn}`)
  const checkCorps = (ctx) => {
    const c = String(Arguments.WORD.getResult(ctx, 'corps')).toLowerCase()
    if (CORPS.indexOf(c) < 0) {
      ctx.source.sendFailure(Text.of(`Unknown corps '${c}'. Use one of: ${CORPS.join(', ')}`))
      return null
    }
    return c
  }
  const perCorps = (name, fn) => Commands.literal(name).then(
    Commands.argument('player', Arguments.PLAYER.create(event)).then(corpsArg(ctx => {
      const c = checkCorps(ctx)
      return c ? asPlayer(ctx, `${fn}/${c}`) : 0
    })))
  const perPlayer = (name, fn) => Commands.literal(name).then(
    Commands.argument('player', Arguments.PLAYER.create(event)).executes(ctx => asPlayer(ctx, fn)))

  event.register(Commands.literal('lantern')
    .requires(src => src.hasPermission(2))
    .executes(ctx => runSelf(ctx, 'greenlantern:admin/help'))
    .then(perCorps('give', 'admin/give'))
    .then(perCorps('unbound', 'admin/give_unbound'))
    .then(perCorps('battery', 'admin/battery'))
    .then(perCorps('leader', 'admin/leader'))
    .then(perCorps('unleader', 'admin/unleader'))
    .then(perCorps('remove', 'admin/remove'))
    .then(perCorps('offer', 'admin/offer'))
    .then(perPlayer('removeall', 'admin/remove_all'))
    .then(perPlayer('unbind', 'admin/unbind'))
    .then(perPlayer('reset', 'admin/reset_emotions'))
    .then(perPlayer('cooldowns', 'admin/reset_cooldowns'))
    .then(perPlayer('show', 'admin/show'))
    .then(Commands.literal('emotion').then(Commands.argument('player', Arguments.PLAYER.create(event))
      .then(Commands.argument('emotion', Arguments.WORD.create(event))
        .suggests((ctx, builder) => { EMOTIONS.forEach(e => builder.suggest(e)); return builder.buildFuture() })
        .then(Commands.literal('set').then(Commands.argument('amount', Arguments.INTEGER.create(event)).executes(ctx =>
          run(ctx, `scoreboard players set ${playerName(ctx)} gl_e_${Arguments.WORD.getResult(ctx, 'emotion')} ${Arguments.INTEGER.getResult(ctx, 'amount')}`))))
        .then(Commands.literal('add').then(Commands.argument('amount', Arguments.INTEGER.create(event)).executes(ctx =>
          run(ctx, `scoreboard players add ${playerName(ctx)} gl_e_${Arguments.WORD.getResult(ctx, 'emotion')} ${Arguments.INTEGER.getResult(ctx, 'amount')}`)))))))
    .then(Commands.literal('threshold').then(Commands.argument('amount', Arguments.INTEGER.create(event)).executes(ctx =>
      run(ctx, `scoreboard players set #threshold gl_cfg ${Arguments.INTEGER.getResult(ctx, 'amount')}`))))
    .then(Commands.literal('forging')
      .then(Commands.literal('on').executes(ctx => runSelf(ctx, 'greenlantern:admin/forging_on')))
      .then(Commands.literal('off').executes(ctx => runSelf(ctx, 'greenlantern:admin/forging_off'))))
    .then(Commands.literal('forgecooldown').then(Commands.argument('seconds', Arguments.INTEGER.create(event)).executes(ctx =>
      run(ctx, `scoreboard players set #forge_cd gl_cfg ${Math.max(0, Arguments.INTEGER.getResult(ctx, 'seconds'))}`))))
    .then(Commands.literal('enable').executes(ctx => runSelf(ctx, 'greenlantern:admin/enable')))
    .then(Commands.literal('disable').executes(ctx => runSelf(ctx, 'greenlantern:admin/disable')))
  )

  // /ring recall [corps]: anyone can call their own rings back (no permission needed)
  const recall = (ctx, corps) => {
    const player = ctx.source.player
    if (!player) {
      ctx.source.sendFailure(Text.of('Only players can call their rings.'))
      return 0
    }
    if (corps && CORPS.indexOf(corps) < 0) {
      ctx.source.sendFailure(Text.of(`Unknown corps '${corps}'. Use one of: ${CORPS.join(', ')}`))
      return 0
    }
    callRing(ctx.source.server, player, corps)
    return 1
  }
  // /ring forge [corps]: recite your corps' oath and forge a new ring for a recruit
  const forge = (ctx, corps) => {
    const player = ctx.source.player
    if (!player) {
      ctx.source.sendFailure(Text.of('Only players can forge rings.'))
      return 0
    }
    if (corps && CORPS.indexOf(corps) < 0) {
      ctx.source.sendFailure(Text.of(`Unknown corps '${corps}'. Use one of: ${CORPS.join(', ')}`))
      return 0
    }
    const fn = corps ? `greenlantern:forge/recite_${corps}` : 'greenlantern:forge/recite_any'
    ctx.source.server.runCommandSilent(`execute as ${player.getStringUUID()} at @s run function ${fn}`)
    return 1
  }
  const corpsArgument = (then) => Commands.argument('corps', Arguments.WORD.create(event))
    .suggests((ctx, builder) => suggestCorps(builder))
    .executes(then)
  event.register(Commands.literal('emotions').executes(ctx => runSelf(ctx, 'greenlantern:emotion/menu')))
  event.register(Commands.literal('ring')
    .then(Commands.literal('recall')
      .executes(ctx => recall(ctx, null))
      .then(corpsArgument(ctx => recall(ctx, String(Arguments.WORD.getResult(ctx, 'corps')).toLowerCase()))))
    .then(Commands.literal('forge')
      .executes(ctx => forge(ctx, null))
      .then(corpsArgument(ctx => forge(ctx, String(Arguments.WORD.getResult(ctx, 'corps')).toLowerCase()))))
  )
})

// Recall runs as the player (by UUID, so any name works).
const callRing = (server, player, corps) => {
  const fn = corps ? `greenlantern:recall/request_${corps}` : 'greenlantern:recall/request'
  server.runCommandSilent(`execute as ${player.getStringUUID()} at @s run function ${fn}`)
}

// Chat phrases that call your ring. The whole message must be a call (punctuation ignored), so
// ordinary talk about rings never triggers it:
//   "ring, come to me" / "green ring, come back" / "my star sapphire ring, return"
//   "return to me, green ring" / "come back, blue ring"
//   "I summon my ring" / "I call my red ring"      "ring, to me"
// Naming a corps (or, failing that, its emotion) calls only that ring.
const CALLS = [
  /^(?:(?:my|the|o)\s+)?(?:\w+\s+){0,2}ring\s+(?:come|return)(?:\s+back)?(?:\s+(?:to\s+me|here))?(?:\s+now)?$/,
  /^(?:come\s+back|come|return)(?:\s+to\s+me)?\s+(?:(?:my|the)\s+)?(?:\w+\s+){0,2}ring$/,
  /^i\s+(?:summon|call)\s+(?:(?:my|the)\s+)?(?:\w+\s+){0,2}ring(?:\s+to\s+me)?$/,
  /^(?:(?:my|the)\s+)?(?:\w+\s+){0,2}ring\s+to\s+me$/
]
const normalized = (text) => String(text).toLowerCase().replace(/[^a-z ]+/g, ' ').replace(/\s+/g, ' ').trim()
const isCall = (text) => {
  const t = normalized(text)
  return CALLS.some(re => re.test(t))
}
const CORPS_NAMES = {
  green: ['green'], yellow: ['yellow', 'sinestro'], red: ['red'], orange: ['orange'], blue: ['blue'],
  violet: ['violet', 'star sapphire', 'sapphire'], indigo: ['indigo'], white: ['white'], black: ['black']
}
const EMOTION_NAMES = {
  green: ['will', 'willpower'], yellow: ['fear'], red: ['rage'], orange: ['greed', 'avarice'], blue: ['hope'],
  violet: ['love'], indigo: ['compassion'], white: ['life'], black: ['death']
}
const namedIn = (t, names) => {
  let found = null
  CORPS.forEach(c => {
    (names[c] || []).forEach(w => {
      if (!found && (' ' + t + ' ').indexOf(' ' + w + ' ') >= 0) found = c
    })
  })
  return found
}
const namedCorps = (text) => {
  const t = normalized(text)
  return namedIn(t, CORPS_NAMES) || namedIn(t, EMOTION_NAMES)
}

// Speaking your corps' oath forges a new ring. Small slips are fine: the words must match at least
// OATH_MATCH of the oath, in order (punctuation and capitals don't matter).
const OATH_MATCH = 0.8
const oathWords = (text) => String(text).toLowerCase().replace(/[^a-z ]+/g, ' ').split(' ').filter(w => w.length > 0)
const OATH_WORDS = {}
CORPS.forEach(c => { OATH_WORDS[c] = oathWords(OATHS[c]) })
const inOrder = (a, b) => {  // longest common subsequence of two word lists
  let prev = []
  for (let j = 0; j <= b.length; j++) prev.push(0)
  for (let i = 1; i <= a.length; i++) {
    let cur = [0]  // not const: the KubeJS Rhino fork keeps a loop-body const's first value
    for (let j = 1; j <= b.length; j++) {
      cur.push(a[i - 1] === b[j - 1] ? prev[j - 1] + 1 : Math.max(prev[j], cur[j - 1]))
    }
    prev = cur
  }
  return prev[b.length]
}
const spokenOath = (msg) => {
  const words = oathWords(msg)
  let best = null
  let bestScore = 0
  CORPS.forEach(c => {
    const oath = OATH_WORDS[c]
    if (words.length < oath.length * OATH_MATCH) return
    const score = inOrder(words, oath) / oath.length
    if (score > bestScore) { bestScore = score; best = c }
  })
  return bestScore >= OATH_MATCH ? best : null
}

// Call your ring with a phrase, or forge a ring by speaking your oath. (Typing yes / no to a ring's offer, and the
// exact phrases, are answered by Palladium.)
PlayerEvents.chat(event => {
  const player = event.player
  const server = player.server
  const msg = String(event.message).trim().toLowerCase()
  if (PALLADIUM_PHRASES.indexOf(msg) >= 0) return
  const oath = spokenOath(msg)
  if (oath) {  // the oath stays in chat for everyone to hear
    server.runCommandSilent(`execute as ${player.getStringUUID()} at @s run function greenlantern:forge/request_${oath}`)
    return
  }
  if (isCall(msg)) {
    callRing(server, player, namedCorps(msg))  // the words still show in chat
  }
})
"""
