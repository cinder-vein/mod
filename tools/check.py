"""The Final Lanterns check: say "lantern check" in chat, run /function final_lanterns:check or /lantern check.

It tells the player what's working and why a ring hasn't come for them yet: whether the datapack is ticking, whether
the KubeJS script (for /lantern, /ring, /emotions) is loaded, whether ring offers are on, their game mode, and for each
corps how close they are (or why it won't come: they already bear it, they declined it lately). Then the entities.
"""
from common import CORPS, NS, SPECTRUM, tellraw
from systems import BLACK_COUNT, EMOTION_NAME, EMOTION_OF

OK, BAD, NOTE = "✔ ", "✘ ", "• "


def line(cond, parts):
    return f"execute {cond} run " + tellraw("@s", ["", *parts])


def generate():
    """Returns (load, tick, functions)."""
    load = ["execute unless score #kubejs gl_cfg matches 0.. run scoreboard players set #kubejs gl_cfg 0",
            "execute unless score #ticks gl_cfg matches 0.. run scoreboard players set #ticks gl_cfg 0"]
    tick = ["scoreboard players add #ticks gl_cfg 1"]
    green, red, gray, white = "green", "red", "gray", "white"
    lines = [
        tellraw("@s", ["", {"text": "\n⬢ Final Lanterns check", "color": white, "bold": True}]),
        line("if score #ticks gl_cfg matches 1..", [{"text": OK, "color": green},
                                                     {"text": "The datapack is running.", "color": gray}]),
        line("unless score #ticks gl_cfg matches 1..", [
            {"text": BAD, "color": red},
            {"text": "The datapack's tick isn't running: nothing happens on its own. Check logs/latest.log for "
                     "\"final_lanterns\" errors, and remove the old Lantern Corps jar.", "color": gray}]),
        line("if score #kubejs gl_cfg matches 1..", [{"text": OK, "color": green},
                                                      {"text": "KubeJS commands loaded: /lantern, /ring, /emotions.",
                                                       "color": gray}]),
        line("unless score #kubejs gl_cfg matches 1..", [
            {"text": BAD, "color": red},
            {"text": "The Final Lanterns KubeJS script isn't loaded, so /lantern and /ring don't work (an old copy "
                     "in your kubejs folder can make them do nothing). Delete lantern_commands.js and lantern_keys.js "
                     "from kubejs/server_scripts and kubejs/client_scripts, then copy in the new lantern_commands.js. "
                     "Without KubeJS everything still works through chat, /trigger and ", "color": gray},
            {"text": f"/function {NS}:admin/help", "color": "aqua",
             "clickEvent": {"action": "run_command", "value": f"/function {NS}:admin/help"}},
            {"text": ".", "color": gray}]),
        line("unless score #enabled gl_cfg matches 1", [{"text": BAD, "color": red},
                                                        {"text": "Ring offers and emotions are turned off (/lantern "
                                                                 "enable).", "color": gray}]),
        line("if entity @s[gamemode=spectator]", [{"text": BAD, "color": red},
                                                  {"text": "You're in spectator mode: rings and entities don't come to "
                                                           "spectators.", "color": gray}]),
        line("if entity @s[tag=gl_offer_any]", [{"text": NOTE, "color": "gold"},
                                                {"text": "A ring is waiting for your answer right now.",
                                                 "color": gray}]),
        tellraw("@s", ["", {"text": " Rings (they come at ", "color": gray},
                       {"score": {"name": "#threshold", "objective": "gl_cfg"}, "color": white},
                       {"text": "):", "color": gray}]),
    ]
    for c, data in CORPS.items():
        col = "#%02X%02X%02X" % (data["color"] if c != "black" else (170, 175, 190))
        name = {"text": f"  {data['name']}: ", "color": col}
        lines += [f"scoreboard players add @s gl_cd_{c} 0", f"scoreboard players add @s gl_ser_{c} 0",
                  line(f"if entity @s[tag=gl_member_{c}]", [name, {"text": "you bear its ring.", "color": gray}]),
                  line(f"unless entity @s[tag=gl_member_{c}] if score @s gl_ser_{c} matches ..-1",
                       [name, {"text": "your ring was taken away: only an admin can offer it again.", "color": gray}]),
                  line(f"unless entity @s[tag=gl_member_{c}] if score @s gl_cd_{c} matches 1..",
                       [name, {"text": "you turned it away; it may come again in ", "color": gray},
                        {"score": {"name": "@s", "objective": f"gl_cd_{c}"}, "color": white},
                        {"text": " s.", "color": gray}])]
        ready = f"unless entity @s[tag=gl_member_{c}] if score @s gl_cd_{c} matches ..0 if score @s gl_ser_{c} matches 0.."
        if c == "white":
            lines.append(line(ready, [name, {"text": "comes when all seven spectrum emotions reach the threshold.",
                                             "color": gray}]))
        elif c == "black":
            lines += ["scoreboard players set #low gl_tmp 0",
                      *[f"execute if score @s gl_e_{EMOTION_OF[s]} < #black_floor gl_cfg run "
                        "scoreboard players add #low gl_tmp 1" for s in SPECTRUM],
                      line(ready, [name, {"text": "comes when ", "color": gray},
                                   {"text": f"{BLACK_COUNT}+", "color": white},
                                   {"text": " spectrum emotions are below ", "color": gray},
                                   {"score": {"name": "#black_floor", "objective": "gl_cfg"}, "color": white},
                                   {"text": "; you have ", "color": gray},
                                   {"score": {"name": "#low", "objective": "gl_tmp"}, "color": white},
                                   {"text": ".", "color": gray}])]
        else:
            e = EMOTION_OF[c]
            lines.append(line(ready, [name, {"text": f"{EMOTION_NAME[e]} ", "color": gray},
                                      {"score": {"name": "@s", "objective": f"gl_e_{e}"}, "color": white},
                                      {"text": " / ", "color": gray},
                                      {"score": {"name": "#threshold", "objective": "gl_cfg"}, "color": white}]))
    lines += [
        line("unless score #entities gl_cfg matches 1", [{"text": NOTE, "color": "gold"},
                                                         {"text": "Entities don't appear on their own (/lantern "
                                                                  "entity on).", "color": gray}]),
        "scoreboard players add @s gl_ehcd 0",
        line("if score @s gl_ehcd matches 1..", [{"text": NOTE, "color": "gold"},
                                                 {"text": "No entity will choose you for another ", "color": gray},
                                                 {"score": {"name": "@s", "objective": "gl_ehcd"}, "color": white},
                                                 {"text": " s (you lost one lately).", "color": gray}]),
        f"function {NS}:entity/admin/status",
    ]
    return load, tick, {"check": lines}
