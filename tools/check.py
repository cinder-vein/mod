"""The Final Lanterns check: /trigger gl_check, say "lantern check" in chat, /lantern check, or
/function final_lanterns:check.

It tells the player what's working and why a ring hasn't come for them yet: whether each part of the datapack loaded
and is running (setup, tick, the once-a-second function), whether Palladium gave them the Emotional Spectrum power
(chat phrases), whether the KubeJS script (for /lantern, /ring, /emotions) is loaded, whether ring offers are on,
their game mode, and for each corps how close they are (or why it won't come: they already bear it, they declined it
lately). Then the entities.

The check doesn't depend on the rest of the datapack: it has its own load and tick functions (fl/check_load,
fl/check_tick, each its own entry in the function tags) and only vanilla commands, so it still answers when the main
functions failed to load, and says which one. Minecraft drops a whole function file when one line in it fails to
parse, so each part leaves a mark when it runs: #load_ok (fl/load), #ticks (fl/tick), #seconds (second), and the
Emotional Spectrum power sets gl_spirit on its holder every tick.
"""
from common import CORPS, NS, SPECTRUM, ring_item, tellraw
from systems import BLACK_COUNT, CURIOS_SLOT, EMOTION_NAME, EMOTION_OF

OK, BAD, NOTE = "✔ ", "✘ ", "• "
GREEN, RED, GRAY, WHITE, GOLD = "green", "red", "gray", "white", "gold"
LOG = "logs/latest.log"


def line(cond, parts):
    return f"execute {cond} run " + tellraw("@s", ["", *parts])


def bad(cond, text, *more):
    return line(cond, [{"text": BAD, "color": RED}, {"text": text, "color": GRAY}, *more])


def good(cond, text):
    return line(cond, [{"text": OK, "color": GREEN}, {"text": text, "color": GRAY}])


def code(text):
    return {"text": text, "color": "aqua"}


def generate():
    """Returns (load, tick, functions, check_load, check_tick).

    load and tick go into fl/load and fl/tick (their marks); check_load and check_tick are the check's own functions,
    for the function tags (check_load must run before fl/load: it clears the marks)."""
    load = ["scoreboard players set #load_ok gl_cfg 1"]  # fl/load's last line: it only runs if fl/load loaded
    tick = ["scoreboard players add #ticks gl_cfg 1"]
    check_load = [
        "scoreboard objectives add gl_cfg dummy",
        "scoreboard objectives add gl_check trigger",
        "scoreboard objectives add gl_spirit dummy",
        "scoreboard objectives add gl_tmp dummy",
        "scoreboard players set #load_ok gl_cfg 0",
        "scoreboard players set #ticks gl_cfg 0",
        "scoreboard players set #seconds gl_cfg 0",
        "execute unless score #kubejs gl_cfg matches 0.. run scoreboard players set #kubejs gl_cfg 0",
    ]
    check_tick = [
        "scoreboard players remove @a[scores={gl_spirit=1..}] gl_spirit 1",
        "scoreboard players enable @a gl_check",
        f"execute as @a[scores={{gl_check=1..}}] at @s run function {NS}:fl/check_trigger",
        "scoreboard players set @a[scores={gl_check=..-1}] gl_check 0",
    ]
    fn = {}
    fn["fl/check_trigger"] = ["scoreboard players set @s gl_check 0", f"function {NS}:check"]

    fn["check"] = [
        tellraw("@s", ["", {"text": "\n⬢ Final Lanterns check", "color": WHITE, "bold": True}]),
        bad("unless score #load_ok gl_cfg matches 1",
            "The datapack's setup function didn't load, so nothing else can work. Search ", code(LOG),
            {"text": " for ", "color": GRAY}, code(f"{NS}:fl/load"),
            {"text": ": the error under it names the line Minecraft rejected. Remove the old Lantern Corps "
                     "(greenlantern) jar if it's still in your mods folder.", "color": GRAY}),
        good("if score #ticks gl_cfg matches 1..", "The datapack is running."),
        bad("unless score #ticks gl_cfg matches 1..",
            "The datapack's tick isn't running: nothing happens on its own. Search ", code(LOG),
            {"text": " for ", "color": GRAY}, code(f"{NS}:fl/tick"), {"text": ".", "color": GRAY}),
        bad("if score #ticks gl_cfg matches 40.. unless score #seconds gl_cfg matches 1..",
            "The once-a-second function isn't running, so no ring offers, emotion changes or entity visits. Search ",
            code(LOG), {"text": " for ", "color": GRAY}, code(f"{NS}:second"), {"text": ".", "color": GRAY}),
        good("if score @s gl_spirit matches 1..",
             "Chat phrases work (\"ring, come to me\", \"emotions\", \"lantern check\")."),
        bad("if score #ticks gl_cfg matches 40.. unless score @s gl_spirit matches 1..",
            "You don't have the Emotional Spectrum power, so chat phrases (\"ring, come to me\", \"emotions\", "
            "\"lantern check\") do nothing. Use the /trigger commands instead (", code("/trigger gl_emotions"),
            {"text": ", ", "color": GRAY}, code("/trigger gl_recall"), {"text": ", ", "color": GRAY},
            code("/trigger gl_check"),
            {"text": "). Palladium may have failed to load it: search ", "color": GRAY}, code(LOG),
            {"text": " for ", "color": GRAY}, code("emotional_spectrum"), {"text": ".", "color": GRAY}),
        good("if score #kubejs gl_cfg matches 1..", "KubeJS commands loaded: /lantern, /ring, /emotions."),
        bad("unless score #kubejs gl_cfg matches 1..",
            "The Final Lanterns KubeJS script isn't loaded, so /lantern and /ring don't work (an old copy in your "
            "kubejs folder can make them do nothing). Delete lantern_commands.js and lantern_keys.js from "
            "kubejs/server_scripts and kubejs/client_scripts, then copy in the new lantern_commands.js. Without "
            "KubeJS everything still works through chat, /trigger and ",
            {"text": f"/function {NS}:admin/help", "color": "aqua",
             "clickEvent": {"action": "run_command", "value": f"/function {NS}:admin/help"}},
            {"text": ".", "color": GRAY}),
        f"function {NS}:check/rings",
        f"execute if score #load_ok gl_cfg matches 1 run function {NS}:check/details",
        tellraw("@s", ["", {"text": " Run this check again: ", "color": "dark_gray"},
                       {"text": "/trigger gl_check", "color": "dark_aqua",
                        "clickEvent": {"action": "run_command", "value": "/trigger gl_check"}},
                       {"text": " (anyone), say \"lantern check\", or /lantern check.", "color": "dark_gray"}]),
    ]

    details = [
        bad("unless score #enabled gl_cfg matches 1", "Ring offers and emotions are turned off (/lantern enable)."),
        bad("if entity @s[gamemode=spectator]", "You're in spectator mode: rings and entities don't come to spectators."),
        line("if entity @s[tag=gl_offer_any]", [{"text": NOTE, "color": GOLD},
                                                {"text": "A ring is waiting for your answer right now.", "color": GRAY}]),
        tellraw("@s", ["", {"text": " Rings (they come at ", "color": GRAY},
                       {"score": {"name": "#threshold", "objective": "gl_cfg"}, "color": WHITE},
                       {"text": "):", "color": GRAY}]),
    ]
    for c, data in CORPS.items():
        col = "#%02X%02X%02X" % (data["color"] if c != "black" else (170, 175, 190))
        name = {"text": f"  {data['name']}: ", "color": col}
        details += [f"scoreboard players add @s gl_cd_{c} 0", f"scoreboard players add @s gl_ser_{c} 0",
                    line(f"if entity @s[tag=gl_member_{c}]", [name, {"text": "you bear its ring.", "color": GRAY}]),
                    line(f"unless entity @s[tag=gl_member_{c}] if score @s gl_ser_{c} matches ..-1",
                         [name, {"text": "your ring was taken away: only an admin can offer it again.", "color": GRAY}]),
                    line(f"unless entity @s[tag=gl_member_{c}] if score @s gl_cd_{c} matches 1..",
                         [name, {"text": "you turned it away; it may come again in ", "color": GRAY},
                          {"score": {"name": "@s", "objective": f"gl_cd_{c}"}, "color": WHITE},
                          {"text": " s.", "color": GRAY}])]
        ready = (f"unless entity @s[tag=gl_member_{c}] if score @s gl_cd_{c} matches ..0 "
                 f"if score @s gl_ser_{c} matches 0..")
        if c == "white":
            details.append(line(ready, [name, {"text": "comes when all seven spectrum emotions reach the threshold.",
                                               "color": GRAY}]))
        elif c == "black":
            details += ["scoreboard players set #low gl_tmp 0",
                        *[f"execute if score @s gl_e_{EMOTION_OF[s]} < #black_floor gl_cfg run "
                          "scoreboard players add #low gl_tmp 1" for s in SPECTRUM],
                        line(ready, [name, {"text": "comes when ", "color": GRAY},
                                     {"text": f"{BLACK_COUNT}+", "color": WHITE},
                                     {"text": " spectrum emotions are below ", "color": GRAY},
                                     {"score": {"name": "#black_floor", "objective": "gl_cfg"}, "color": WHITE},
                                     {"text": "; you have ", "color": GRAY},
                                     {"score": {"name": "#low", "objective": "gl_tmp"}, "color": WHITE},
                                     {"text": ".", "color": GRAY}])]
        else:
            e = EMOTION_OF[c]
            details.append(line(ready, [name, {"text": f"{EMOTION_NAME[e]} ", "color": GRAY},
                                        {"score": {"name": "@s", "objective": f"gl_e_{e}"}, "color": WHITE},
                                        {"text": " / ", "color": GRAY},
                                        {"score": {"name": "#threshold", "objective": "gl_cfg"}, "color": WHITE}]))
    details += [
        line("unless score #entities gl_cfg matches 1", [{"text": NOTE, "color": GOLD},
                                                         {"text": "Entities don't appear on their own (/lantern "
                                                                  "entity on).", "color": GRAY}]),
        "scoreboard players add @s gl_ehcd 0",
        line("if score @s gl_ehcd matches 1..", [{"text": NOTE, "color": GOLD},
                                                 {"text": "No entity will choose you for another ", "color": GRAY},
                                                 {"score": {"name": "@s", "objective": "gl_ehcd"}, "color": WHITE},
                                                 {"text": " s (you lost one lately).", "color": GRAY}]),
        f"function {NS}:entity/admin/status",
    ]
    fn["check/details"] = details
    fn["check/rings"] = rings()
    return load, tick, fn, check_load, check_tick


def rings():
    """The Lantern Ring slots, read straight from Curios' save data on the player (vanilla commands only): how many
    there are, which rings are in them, and whether each ring's power is on (its marker, gl_<corps>)."""
    slot = f'ForgeCaps."curios:inventory".Curios[{{Identifier:"{CURIOS_SLOT}"}}].StacksHandler.Stacks'
    out = [
        "scoreboard players set #slots gl_tmp 0",
        f"execute store result score #slots gl_tmp run data get entity @s {slot}.Size",
        "scoreboard players set #worn gl_tmp 0",
        bad("if score #slots gl_tmp matches 0",
            "You have no Lantern Ring slot, so no ring can be worn. Curios didn't add it: check that Curios is "
            "installed and search ", code(LOG), {"text": " for ", "color": GRAY}, code(CURIOS_SLOT),
            {"text": ".", "color": GRAY}),
        bad("if score #slots gl_tmp matches 1",
            "You have only one Lantern Ring slot, so two rings can't be worn (no Spectrum Bond). Another mod or "
            "the Curios config may be limiting it; search ", code(LOG), {"text": " for ", "color": GRAY},
            code(CURIOS_SLOT), {"text": ".", "color": GRAY}),
        line("if score #slots gl_tmp matches 2..", [{"text": OK, "color": GREEN},
                                                    {"text": "Lantern Ring slots: ", "color": GRAY},
                                                    {"score": {"name": "#slots", "objective": "gl_tmp"},
                                                     "color": WHITE},
                                                    {"text": " (open your inventory's Curios tab to wear rings).",
                                                     "color": GRAY}]),
    ]
    for c, data in CORPS.items():
        col = "#%02X%02X%02X" % (data["color"] if c != "black" else (170, 175, 190))
        worn = f'if data entity @s {slot}.Items[{{id:"{ring_item(c)}"}}]'
        name = {"text": f"  {data['name']} ring: ", "color": col}
        out += [
            f"execute {worn} run scoreboard players add #worn gl_tmp 1",
            line(f"{worn} if entity @s[tag=gl_{c}]", [name, {"text": "worn, its power is on.", "color": GRAY}]),
            line(f"{worn} unless entity @s[tag=gl_{c}]", [
                name, {"text": "worn, but its power is off. ", "color": RED},
                {"text": "Palladium may have failed to load it: search ", "color": GRAY}, code(LOG),
                {"text": " for ", "color": GRAY}, code(f"{NS}:{data['power']}"), {"text": ".", "color": GRAY}]),
        ]
    out += [
        line("if score #worn gl_tmp matches 0 if score #slots gl_tmp matches 1..",
             [{"text": NOTE, "color": GOLD}, {"text": "You aren't wearing a lantern ring.", "color": GRAY}]),
        good("if entity @s[tag=gl_dual]", "Spectrum Bond: on (its bar and skill tree are in your powers menu)."),
        line("if score #worn gl_tmp matches 1 if score #slots gl_tmp matches 2..",
             [{"text": NOTE, "color": GOLD},
              {"text": "Wear a second ring of another corps in the other Lantern Ring slot for the Spectrum Bond.",
               "color": GRAY}]),
        bad("if score #worn gl_tmp matches 2.. unless entity @s[tag=gl_dual]",
            "You wear two rings but the Spectrum Bond isn't on: both rings' powers have to be on (see above), and "
            "the datapack's tick has to be running."),
    ]
    return out
