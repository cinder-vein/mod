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
CURIOS_SLOTS = 16  # ring slots checked (Curios merges slot counts from every pack)
DECLINE_COOLDOWN = 3600  # seconds before a declined corps asks again
DEFAULT_THRESHOLD = 20000

# Main-inventory slot numbers -> /item slot names (for leader revokes and admin removal we use /clear).
DISPLAY_TRANSFORM = ("transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],"
                     "translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}")


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
        f"execute if entity @s[tag=gl_b{i}] run scoreboard players add @s gl_id {2 ** i}" for i in range(ID_BITS)]
    to_tags = ["scoreboard players operation #v gl_tmp = @s gl_id"]
    for i in range(ID_BITS):
        to_tags += [f"tag @s remove gl_b{i}",
                    "scoreboard players operation #bit gl_tmp = #v gl_tmp",
                    "scoreboard players operation #bit gl_tmp %= #2 gl_cfg",
                    f"execute if score #bit gl_tmp matches 1 run tag @s add gl_b{i}",
                    "scoreboard players operation #v gl_tmp /= #2 gl_cfg"]
    fn["id/to_tags"] = to_tags + ["tag @s add gl_hasid"]
    tick += [
        f"execute as @a unless score @s gl_id matches 1.. run function {NS}:id/assign",
        # players from before 9.0 have an id but no tags yet
        f"execute as @a[tag=!gl_hasid] run function {NS}:id/to_tags",
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
                 {"source": "bits", "target": "gl_ob", "op": "replace"}]},
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

    # owner id and id bits of @s, for the bind modifier
    fn["ring/store_owner"] = [
        f"execute store result storage {STORAGE} owner int 1 run scoreboard players get @s gl_id",
        f"data modify storage {STORAGE} bits set value {{{','.join(f'b{i}:0b' for i in range(ID_BITS))}}}",
        *[f"execute if entity @s[tag=gl_b{i}] run data modify storage {STORAGE} bits.b{i} set value 1b"
          for i in range(ID_BITS)],
    ]
    fn["ring/store_giver"] = [f"execute store result storage {STORAGE} giver int 1 run scoreboard players get @s gl_id"]

    def give_ring(table):
        """Gives a ring from a loot table; drops it at your feet when your inventory is full."""
        return [f"execute store result score #given gl_tmp run loot give @s loot {NS}:rings/{table}",
                f"execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot {NS}:rings/{table}"]

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
            f"execute unless score #giver gl_tmp = @s gl_id run function {NS}:ring/bind_{hand}",
        ]
        fn[f"ring/bind_{hand}"] = [
            f"function {NS}:ring/rebind_{hand}",
            *[f"execute if data entity @s {held_ring(c)} run tag @s add gl_member_{c}" for c in corps],
            tellraw("@s", [{"text": "The ring is now bound to you.", "color": "gray", "italic": True}]),
            "playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6",
        ]
        fn[f"ring/rebind_{hand}"] = [f"function {NS}:ring/store_owner", f"item modify entity @s {slot} {NS}:bind"]
        check = [f"execute if predicate {NS}:legacy_ring_{hand} run function {NS}:ring/legacy_{hand}"]
        for i in range(ID_BITS):
            check += [f"execute if entity @s[tag=gl_b{i}] if predicate {NS}:ob/{hand}_{i}_0 run function {NS}:ring/eject_{hand}",
                      f"execute if entity @s[tag=!gl_b{i}] if predicate {NS}:ob/{hand}_{i}_1 run function {NS}:ring/eject_{hand}"]
        fn[f"ring/check_{hand}"] = check
        fn[f"ring/legacy_{hand}"] = [  # a pre-9.0 ring: compare ids once, then upgrade it or throw it out
            f"execute store result score #owner gl_tmp run data get entity @s {path}.tag.gl_owner",
            f"execute if score #owner gl_tmp = @s gl_id run function {NS}:ring/rebind_{hand}",
            f"execute unless score #owner gl_tmp = @s gl_id run function {NS}:ring/eject_{hand}",
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
    ]
    fn["ring/curios_pop"] = [  # throw the ring in storage `cur` out of its Curios slot (#slot)
        eject_summon,
        f"data modify entity {newest_eject} Item set from storage {STORAGE} cur",
        f"data remove entity {newest_eject} Item.Slot",
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
        tellraw("@s", [{"text": "Hold a new ring in your hand once to bind it to you, then wear it.",
                        "color": "gray", "italic": True}]),
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
        f"execute if score #lantern gl_tmp matches 1 run function #{NS}:curios_clear_slot",
        "execute if score #lantern gl_tmp matches 1 run scoreboard players add #stripped gl_tmp 1",
        f"execute if data storage {STORAGE} rings[0] run function {NS}:ring/curios_strip_next",
    ]

    # ---------------------------------------------------------------- emotions
    feed = []
    for e in EMOTIONS:
        for i, (crit, w) in enumerate(SOURCES[e]):
            src = f"gl_s_{e}{i}"
            if w == 1:
                feed.append(f"scoreboard players operation @s gl_e_{e} += @s {src}")
                feed.append(f"scoreboard players set @s {src} 0")
            elif w > 1:
                feed += [f"scoreboard players operation @s gl_tmp = @s {src}",
                         f"scoreboard players operation @s gl_tmp *= #w{w} gl_cfg",
                         f"scoreboard players operation @s gl_e_{e} += @s gl_tmp",
                         f"scoreboard players set @s {src} 0"]
            else:  # divide, keeping the remainder for next time
                feed += [f"scoreboard players operation @s gl_tmp = @s {src}",
                         f"scoreboard players operation @s gl_tmp /= #w{-w} gl_cfg",
                         f"scoreboard players operation @s gl_e_{e} += @s gl_tmp",
                         f"scoreboard players operation @s {src} %= #w{-w} gl_cfg"]
    fn["emotion/feed"] = [f"scoreboard players add @s gl_e_{e} 0" for e in EMOTIONS] + feed
    fn["emotion/show"] = [
        tellraw("@s", [{"text": "Your emotional spectrum", "color": "white", "bold": True}]),
        *[tellraw("@s", [{"text": f"  {EMOTION_NAME[e].capitalize()}: ", "color": "gray"},
                         {"score": {"name": "@s", "objective": f"gl_e_{e}"}, "color": "white"},
                         {"text": " / ", "color": "dark_gray"},
                         {"score": {"name": "#threshold", "objective": "gl_cfg"}, "color": "dark_gray"}])
          for e in EMOTIONS],
    ]

    # ---------------------------------------------------------------- ring offers
    def offer_ok(c):
        return f"@a[gamemode=survival,tag=!gl_offer_any,tag=!gl_member_{c},scores={{gl_cd_{c}=..0}}]"

    offer_scan = [f"scoreboard players add @a gl_cd_{c} 0" for c in corps]
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
        ]
        fn[f"leader/revoke_{c}"] = [  # run as the leader: revoke the nearest bearer of this corps' ring
            "tag @s add gl_revoker",
            f"execute as @p[tag=gl_{c},tag=!gl_revoker,distance=..8] run function {NS}:leader/revoke_target_{c}",
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
        fn[f"admin/give/{c}"] = [f"function {NS}:ring/store_owner", *give_ring(c), f"tag @s add gl_member_{c}"]
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
                                  f"function {NS}:offer/start_{c}"]
        fn[f"admin/emotion/max_{EMOTION_OF.get(c, 'all')}"] = (
            [f"scoreboard players operation @s gl_e_{e} = #threshold gl_cfg" for e in EMOTIONS] if c == "white"
            else [f"scoreboard players operation @s gl_e_{EMOTION_OF[c]} = #threshold gl_cfg"])
    fn["admin/remove_all"] = [f"function {NS}:ring/strip_{c}" for c in corps] + [f"function {NS}:leader/update_any"]
    fn["admin/unbind"] = [  # the holder won't re-bind it: it binds to the next player who holds it
        f"execute unless predicate {NS}:ring_mainhand run "
        + tellraw("@s", [{"text": "Hold the ring in your main hand to unbind it.", "color": "gray"}]),
        f"execute if predicate {NS}:ring_mainhand run function {NS}:ring/store_giver",
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
        "/lantern reset <player> | show <player> | enable | disable",
        "corps: " + ", ".join(corps),
    ])]

    # ---------------------------------------------------------------- tick wiring
    tick += [
        f"execute as @a at @s run function {NS}:ring/bind_check",
        # rings worn in Curios slots, twice a second, for players a ring is powering
        f"execute if score #second gl_cfg matches 5 as @a[tag=gl_ring] at @s run function {NS}:ring/curios_check",
        f"execute if score #second gl_cfg matches 15 as @a[tag=gl_ring] at @s run function {NS}:ring/curios_check",
        f"execute as @a[tag=gl_offer_any] at @s run function {NS}:offer/follow",
        f"execute as @a[scores={{gl_accept=1..}}] at @s run function {NS}:offer/accept_trigger",
        f"execute as @a[scores={{gl_decline=1..}}] at @s run function {NS}:offer/decline_trigger",
        f"execute as @a[scores={{gl_revoke=1..}}] at @s run function {NS}:leader/revoke_trigger",
        f"execute as @a[scores={{gl_roster=1..}}] run function {NS}:leader/roster_trigger",
        f"execute as @a[scores={{gl_emotions=1..}}] run function {NS}:emotion/show",
        "scoreboard players set @a[scores={gl_emotions=1..}] gl_emotions 0",
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
    ]
    fn["offer/scan"] = offer_scan

    write_kubejs(corps, write_text)
    return load, tick, fn


def write_kubejs(corps, write_text):
    """Optional /lantern command and chat replies when KubeJS is installed."""
    script = KUBEJS_TEMPLATE.replace("__CORPS__", json.dumps(corps)).replace("__EMOTIONS__", json.dumps(EMOTIONS))
    write_text(f"data/{NS}/kubejs_scripts/lantern_commands.js", script)


KUBEJS_TEMPLATE = r"""// Lantern Corps: /lantern admin command and chat replies to ring offers.
// Loaded by Palladium's KubeJS integration when KubeJS is installed; without KubeJS the
// same features are available through /function greenlantern:admin/... and /trigger.
const CORPS = __CORPS__
const EMOTIONS = __EMOTIONS__

ServerEvents.commandRegistry(event => {
  const { commands: Commands, arguments: Arguments } = event

  const run = (ctx, cmd) => {
    ctx.source.server.runCommandSilent(cmd)
    return 1
  }
  const playerName = (ctx) => Arguments.PLAYER.getResult(ctx, 'player').getGameProfile().getName()
  const corpsArg = (then) => Commands.argument('corps', Arguments.WORD.create(event))
    .suggests((ctx, builder) => { CORPS.forEach(c => builder.suggest(c)); return builder.buildFuture() })
    .executes(then)
  const asPlayer = (ctx, fn) => run(ctx, `execute as ${playerName(ctx)} at @s run function greenlantern:${fn}`)
  const checkCorps = (ctx) => {
    const c = Arguments.WORD.getResult(ctx, 'corps')
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
    .executes(ctx => run(ctx, `execute as ${ctx.source.textName} run function greenlantern:admin/help`))
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
    .then(Commands.literal('enable').executes(ctx => run(ctx, `execute as ${ctx.source.textName} run function greenlantern:admin/enable`)))
    .then(Commands.literal('disable').executes(ctx => run(ctx, `execute as ${ctx.source.textName} run function greenlantern:admin/disable`)))
  )
})

// Answer a ring's offer by typing yes / no in chat.
PlayerEvents.chat(event => {
  const player = event.player
  if (!player.tags.contains('gl_offer_any')) return
  const name = event.username
  const server = player.server
  const msg = String(event.message).trim().toLowerCase()
  if (['yes', 'y', 'accept', 'i accept'].indexOf(msg) >= 0) {
    server.runCommandSilent(`execute as ${name} at @s run function greenlantern:offer/accept_chat`)
    event.cancel()
  } else if (['no', 'n', 'decline', 'i decline'].indexOf(msg) >= 0) {
    server.runCommandSilent(`execute as ${name} at @s run function greenlantern:offer/decline_chat`)
    event.cancel()
  }
})
"""
