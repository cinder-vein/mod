"""The Emotional Spectrum menu: every player's eight emotions, what raised them, and quests.

Open it with /trigger gl_emotions, by saying "emotions" in chat, with /emotions (KubeJS), or with the Emotional
Spectrum ability on a ring's bar. It's a clickable chat menu:
- the main page: each emotion's amount, its percentage of the ring threshold, its level (one per 10%) and a bar;
- a page per emotion: the actions that raised it (lifetime points from each) and its quests.

Each emotion has a chain of three quests. They run on their own, one at a time: when one is done its reward lands
and the next begins. Quest counters are their own scoreboard objectives (vanilla statistics), never reset.

Every player is born with a spark of each emotion: the first time they join, each emotion gets a random
START_MIN-START_MAX (emotion/roll; 1.20.1 has no /random, so 13 coin-flip predicates make a number).

gen_final.py calls generate() and merges the returned lines and functions; systems.py's emotion/feed adds the
lifetime tracking (gl_tr_<emotion><source>).
"""
import json

from common import NS, SPECTRUM
from systems import BLACK_COUNT, CORPS_TITLE, EMOTION_NAME, EMOTION_OF, EMOTIONS, SOURCES, tellraw

START_MIN, START_MAX = 10000, 15000
ROLL_BITS = 13  # 0-8191, scaled to 0-(START_MAX - START_MIN)

TITLE = {"will": "Willpower", "fear": "Fear", "rage": "Rage", "greed": "Avarice", "hope": "Hope", "love": "Love",
         "compassion": "Compassion", "death": "Death"}
CORPS_OF = {e: c for c, e in EMOTION_OF.items()}
EMOTION_COLOR = {"will": "#2EC846", "fear": "#F5CD1E", "rage": "#DC1E23", "greed": "#FA8214", "hope": "#2882FF",
                 "love": "#D737DC", "compassion": "#7A50F0", "death": "#9A9EAE"}

# What each source in systems.SOURCES is, for the menu: (label, how much it gives). Sources sharing a label (the
# two kinds of diamond ore, ...) show as one line.
SOURCE_LABELS = {
    "will": [("Taking damage", "20 per heart"), ("Blocking with a shield", "40 per heart"),
             ("Absorbing damage", "20 per heart")],
    "fear": [("Dying", "600 per death"), ("Sneaking", "1,200 per minute")],
    "rage": [("Dealing damage", "20 per heart"), ("Defeating players", "500 each")],
    "greed": [("Trading with villagers", "100 per trade"), ("Opening chests", "20 each"), ("Opening barrels", "20 each"),
              ("Mining diamond ore", "300 each"), ("Mining diamond ore", "300 each"),
              ("Mining emerald ore", "300 each"), ("Mining emerald ore", "300 each"),
              ("Mining gold ore", "50 each"), ("Mining gold ore", "50 each"), ("Mining ancient debris", "500 each")],
    "hope": [("Winning raids", "5,000 per raid"), ("Sleeping through the night", "200 per night"),
             ("Ringing bells", "50 per ring"), ("Time played", "1 per second")],
    "love": [("Breeding animals", "200 per animal"), ("Eating cake", "50 per slice")],
    "compassion": [("Talking to villagers", "25 each"), ("Potting flowers", "100 each"),
                   ("Filling cauldrons", "20 each")],
    "death": [("Defeating creatures", "100 each"), ("Dying", "300 per death")],
}

# Quests per emotion, in order: (title, task, statistics counted, target in statistic units, display unit,
# statistic units per display unit, reward in emotion points). Damage statistics count 20 per heart.
CUSTOM = "minecraft.custom:minecraft."
QUESTS = {
    "will": [("Stand Your Ground", "Block 25 hearts of damage with a shield", [CUSTOM + "damage_blocked_by_shield"],
              500, "hearts", 20, 1500),
             ("Hold the Line", "Take 150 hearts of damage and keep going", [CUSTOM + "damage_taken"], 3000, "hearts", 20,
              3000),
             ("Will Conquers All", "Defeat the Ender Dragon", ["minecraft.killed:minecraft.ender_dragon"], 1, "", 1, 6000)],
    "fear": [("Lurker", "Sneak for 10 minutes", [CUSTOM + "sneak_time"], 12000, "minutes", 1200, 1500),
             ("Sleepless", "Defeat 10 phantoms", ["minecraft.killed:minecraft.phantom"], 10, "", 1, 3000),
             ("Face the Dark", "Defeat the Warden", ["minecraft.killed:minecraft.warden"], 1, "", 1, 6000)],
    "rage": [("Bloodied", "Deal 200 hearts of damage", [CUSTOM + "damage_dealt"], 4000, "hearts", 20, 1500),
             ("Berserker", "Defeat 150 mobs", [CUSTOM + "mob_kills"], 150, "", 1, 3000),
             ("Rage Against the Raid", "Defeat 3 ravagers", ["minecraft.killed:minecraft.ravager"], 3, "", 1, 6000)],
    "greed": [("Haggler", "Trade with villagers 30 times", [CUSTOM + "traded_with_villager"], 30, "", 1, 1500),
              ("Diamond Fever", "Mine 24 diamond ore",
               ["minecraft.mined:minecraft.diamond_ore", "minecraft.mined:minecraft.deepslate_diamond_ore"], 24, "", 1,
               3000),
              ("Netherite Hoard", "Mine 12 ancient debris", ["minecraft.mined:minecraft.ancient_debris"], 12, "", 1,
               6000)],
    "hope": [("Good Night", "Sleep in a bed 7 times", [CUSTOM + "sleep_in_bed"], 7, "", 1, 1500),
             ("Ring the Bells", "Ring a bell 25 times", [CUSTOM + "bell_ring"], 25, "", 1, 3000),
             ("Hero of the Village", "Win 2 raids", [CUSTOM + "raid_win"], 2, "", 1, 6000)],
    "love": [("Matchmaker", "Breed 20 animals", [CUSTOM + "animals_bred"], 20, "", 1, 1500),
             ("Let Them Eat Cake", "Eat 14 slices of cake", [CUSTOM + "eat_cake_slice"], 14, "", 1, 3000),
             ("Family", "Breed 100 animals", [CUSTOM + "animals_bred"], 100, "", 1, 6000)],
    "compassion": [("A Kind Word", "Talk to villagers 40 times", [CUSTOM + "talked_to_villager"], 40, "", 1, 1500),
                   ("Gardener", "Pot 12 flowers", [CUSTOM + "pot_flower"], 12, "", 1, 3000),
                   ("Remedies", "Brew at a brewing stand 25 times", [CUSTOM + "interact_with_brewingstand"], 25, "", 1,
                    6000)],
    "death": [("Reaper", "Defeat 100 mobs", [CUSTOM + "mob_kills"], 100, "", 1, 1500),
              ("Lay Them to Rest", "Defeat 40 zombies or skeletons",
               ["minecraft.killed:minecraft.zombie", "minecraft.killed:minecraft.skeleton"], 40, "", 1, 3000),
              ("Lord of the Dead", "Defeat the Wither", ["minecraft.killed:minecraft.wither"], 1, "", 1, 6000)],
}
ROMAN = ["I", "II", "III"]
BAR = 10  # bar segments


def label_groups(e):
    """[(label, rate, [source indexes])] in order."""
    groups = []
    for i, (label, rate) in enumerate(SOURCE_LABELS[e]):
        for g in groups:
            if g[0] == label:
                g[2].append(i)
                break
        else:
            groups.append((label, rate, [i]))
    return groups


def generate():
    """Returns (load, tick, second, functions)."""
    for e in EMOTIONS:
        assert len(SOURCE_LABELS[e]) == len(SOURCES[e]), e
    fn, load, tick, second = {}, [], [], []
    files = {"predicates/random/half.json": {"condition": "minecraft:random_chance", "chance": 0.5}}
    criteria = sorted({crit for e in EMOTIONS for q in QUESTS[e] for crit in q[2]})
    counter = {crit: f"gl_qc{i}" for i, crit in enumerate(criteria)}
    load += [f"scoreboard objectives add {obj} {crit}" for crit, obj in counter.items()]
    load += ["scoreboard players set #100 gl_cfg 100", "scoreboard players set #10 gl_cfg 10"]
    divisors = sorted({q[5] for e in EMOTIONS for q in QUESTS[e] if q[5] > 1})
    load += [f"scoreboard players set #d{d} gl_cfg {d}" for d in divisors]
    for e in EMOTIONS:
        load += [f"scoreboard objectives add {o}_{e} dummy" for o in ("gl_qn", "gl_qs", "gl_qp", "gl_qd", "gl_ep", "gl_el")]
        load += [f"scoreboard objectives add gl_tr_{e}{i} dummy" for i in range(len(SOURCES[e]))]
        load.append(f"scoreboard objectives add gl_tr_{e}_quests dummy")
        load.append(f"scoreboard objectives add gl_tr_{e}_start dummy")

    # --- the spark every player is born with --------------------------------------------------------
    span = START_MAX - START_MIN + 1
    load += [f"scoreboard players set #span gl_cfg {span}", f"scoreboard players set #bits gl_cfg {2 ** ROLL_BITS}"]
    fn["emotion/roll_value"] = ["scoreboard players set #r gl_tmp 0", *[
        f"execute if predicate {NS}:random/half run scoreboard players add #r gl_tmp {2 ** b}" for b in range(ROLL_BITS)],
        "scoreboard players operation #r gl_tmp *= #span gl_cfg", "scoreboard players operation #r gl_tmp /= #bits gl_cfg",
        f"scoreboard players add #r gl_tmp {START_MIN}"]
    roll = ["tag @s add gl_rolled"]
    for e in EMOTIONS:
        roll += [f"function {NS}:emotion/roll_value", f"scoreboard players add @s gl_e_{e} 0",
                 f"scoreboard players operation @s gl_e_{e} += #r gl_tmp",
                 f"scoreboard players operation @s gl_tr_{e}_start = #r gl_tmp"]
    fn["emotion/roll"] = roll + [
        tellraw("@s", ["", {"text": "⬢ ", "color": "#7A50F0"},
                       {"text": "The emotional spectrum stirs in you. ", "color": "white"},
                       {"text": "[See your emotions]", "color": "aqua",
                        "clickEvent": {"action": "run_command", "value": "/trigger gl_emotions set 1"},
                        "hoverEvent": {"action": "show_text", "contents": "Open your Emotional Spectrum"}},
                       {"text": "  (or say \"emotions\" in chat)  ", "color": "dark_gray"},
                       {"text": "[Lantern check]", "color": "dark_aqua",
                        "clickEvent": {"action": "run_command", "value": "/trigger gl_check"},
                        "hoverEvent": {"action": "show_text",
                                       "contents": "What's working, and how close each ring is to choosing you"}}])]
    fn["emotion/reroll"] = [*[f"scoreboard players operation @s gl_e_{e} -= @s gl_tr_{e}_start" for e in EMOTIONS],
                            f"function {NS}:emotion/roll"]
    # before anything else reads a new player's emotions (the Black Lantern ring looks for empty ones)
    tick.append(f"execute as @a[tag=!gl_rolled] run function {NS}:emotion/roll")

    # --- quests: checked every second for every player -------------------------------------------
    check_all = []
    for e in EMOTIONS:
        color = EMOTION_COLOR[e]
        check_all += [f"execute unless score @s gl_qn_{e} matches 1.. run function {NS}:emotion/quest/{e}/begin_1",
                      *[f"execute if score @s gl_qn_{e} matches {n} run function {NS}:emotion/quest/{e}/check_{n}"
                        for n in range(1, len(QUESTS[e]) + 1)]]
        for n, (title, task, crits, target, unit, per, reward) in enumerate(QUESTS[e], 1):
            total = ["scoreboard players set #qsum gl_tmp 0",
                     *[line for crit in crits for line in (f"scoreboard players add @s {counter[crit]} 0",
                                                           f"scoreboard players operation #qsum gl_tmp += @s {counter[crit]}")]]
            fn[f"emotion/quest/{e}/begin_{n}"] = [f"scoreboard players set @s gl_qn_{e} {n}", *total,
                                                   f"scoreboard players operation @s gl_qs_{e} = #qsum gl_tmp",
                                                   f"scoreboard players set @s gl_qp_{e} 0",
                                                   f"scoreboard players set @s gl_qd_{e} 0"]
            fn[f"emotion/quest/{e}/check_{n}"] = [
                *total,
                f"scoreboard players operation @s gl_qp_{e} = #qsum gl_tmp",
                f"scoreboard players operation @s gl_qp_{e} -= @s gl_qs_{e}",
                f"scoreboard players operation @s gl_qd_{e} = @s gl_qp_{e}",
                *([f"scoreboard players operation @s gl_qd_{e} /= #d{per} gl_cfg"] if per > 1 else []),
                f"execute if score @s gl_qp_{e} matches {target}.. run function {NS}:emotion/quest/{e}/done_{n}",
            ]
            last = n == len(QUESTS[e])
            fn[f"emotion/quest/{e}/done_{n}"] = [
                f"scoreboard players add @s gl_e_{e} {reward}",
                f"scoreboard players add @s gl_tr_{e}_quests {reward}",
                tellraw("@s", ["", {"text": "Quest complete: ", "color": "gold", "bold": True},
                               {"text": f"{title} ", "color": color},
                               {"text": f"(+{reward:,} {EMOTION_NAME[e]})", "color": "gray"}]),
                "title @s times 5 40 10",
                "title @s subtitle " + json.dumps({"text": f"Quest complete: {title}", "color": color}),
                "title @s title " + json.dumps({"text": f"+{reward:,} {TITLE[e]}", "color": color}),
                "playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2",
                f"scoreboard players set @s gl_qn_{e} {n + 1}" if last else f"function {NS}:emotion/quest/{e}/begin_{n + 1}",
                *([] if last else [tellraw("@s", ["", {"text": "Next quest: ", "color": "gray"},
                                                  {"text": QUESTS[e][n][0], "color": color},
                                                  {"text": f" - {QUESTS[e][n][1]}.", "color": "gray"}])]),
            ]
    fn["emotion/quests"] = check_all
    second.append(f"execute as @a run function {NS}:emotion/quests")

    # --- the menu ------------------------------------------------------------------------------
    def compute(e):
        return [f"scoreboard players add @s gl_e_{e} 0",
                f"scoreboard players operation @s gl_ep_{e} = @s gl_e_{e}",
                f"scoreboard players operation @s gl_ep_{e} *= #100 gl_cfg",
                f"scoreboard players operation @s gl_ep_{e} /= #threshold gl_cfg",
                f"scoreboard players operation @s gl_el_{e} = @s gl_e_{e}",
                f"scoreboard players operation @s gl_el_{e} *= #10 gl_cfg",
                f"scoreboard players operation @s gl_el_{e} /= #threshold gl_cfg"]

    def bar_lines(e, prefix, suffix):
        """One tellraw per bar length, picked by the percentage."""
        lines = []
        for filled in range(BAR + 1):
            pct = "100.." if filled == BAR else f"{filled * 10}..{filled * 10 + 9}"
            bar = [{"text": "█" * filled, "color": EMOTION_COLOR[e]}, {"text": "█" * (BAR - filled), "color": "dark_gray"}]
            lines.append(f"execute if score @s gl_ep_{e} matches {pct} run " + tellraw("@s", ["", *prefix, *bar, *suffix]))
        return lines

    def stats(e):
        return [{"text": " ", "color": "gray"}, {"score": {"name": "@s", "objective": f"gl_ep_{e}"}, "color": "white"},
                {"text": "%", "color": "white"}, {"text": "  Lv ", "color": "gray"},
                {"score": {"name": "@s", "objective": f"gl_el_{e}"}, "color": "white"},
                {"text": "  ", "color": "gray"}, {"score": {"name": "@s", "objective": f"gl_e_{e}"}, "color": "white"},
                {"text": "/", "color": "dark_gray"}, {"score": {"name": "#threshold", "objective": "gl_cfg"}, "color": "dark_gray"}]

    def button(text, value, hover, color="aqua"):
        return {"text": text, "color": color,
                "clickEvent": {"action": "run_command", "value": f"/trigger gl_emotions set {value}"},
                "hoverEvent": {"action": "show_text", "contents": hover}}

    menu = [f"function {NS}:emotion/quests", "scoreboard players enable @s gl_emotions",
            "execute unless score #threshold gl_cfg matches 1.. run scoreboard players set #threshold gl_cfg 1"]
    for e in EMOTIONS:
        menu += compute(e)
    menu.append(tellraw("@s", ["", {"text": "\n⬢ Your Emotional Spectrum", "color": "white", "bold": True},
                               {"text": "  click an emotion for what raises it and its quests", "color": "dark_gray",
                                "italic": True}]))
    for i, e in enumerate(EMOTIONS, 1):
        name = [button(TITLE[e], 10 + i, f"{TITLE[e]}: what raises it, and its quests", EMOTION_COLOR[e]),
                {"text": " "}]
        menu += bar_lines(e, name, stats(e))
    import entities  # the entity you host, if any
    for ent in entities.ENTITIES:
        menu.append(f"execute if entity @s[tag=gl_host_{ent.key}] run " + tellraw("@s", [
            "", {"text": " You host ", "color": "gray"}, {"text": ent.name, "color": ent.color, "bold": True},
            {"text": f", {ent.title}.", "color": "gray"}]))
    menu += [  # the entities' cooldown after losing one, in minutes (rounded up)
        "scoreboard players set #m gl_tmp 0",
        "execute if score @s gl_ehcd matches 1.. run scoreboard players operation #m gl_tmp = @s gl_ehcd",
        "execute if score @s gl_ehcd matches 1.. run scoreboard players add #m gl_tmp 59",
        "execute if score @s gl_ehcd matches 1.. run scoreboard players operation #m gl_tmp /= #60 gl_cfg",
        "execute if score @s gl_ehcd matches 1.. run " + tellraw("@s", [
            "", {"text": " No entity will choose you for another ", "color": "gray"},
            {"score": {"name": "#m", "objective": "gl_tmp"}, "color": "white"}, {"text": " min.", "color": "gray"}])]
    menu.append(tellraw("@s", ["", {"text": " At 100% that corps' ring comes for you. The White Lantern ring comes when all "
                                        "seven spectrum emotions (not Death) are at 100%. The Black Lantern ring comes to "
                                        f"the emotionally dead: {BLACK_COUNT} or more spectrum emotions still below ",
                                "color": "dark_gray"},
                               {"score": {"name": "#black_floor", "objective": "gl_cfg"}, "color": "gray"},
                               {"text": ".", "color": "dark_gray"}]))
    fn["emotion/menu"] = menu
    fn["emotion/show"] = [f"function {NS}:emotion/menu"]

    for i, e in enumerate(EMOTIONS, 1):
        corps = CORPS_OF[e]
        page = [f"function {NS}:emotion/quests", "scoreboard players enable @s gl_emotions",
                "execute unless score #threshold gl_cfg matches 1.. run scoreboard players set #threshold gl_cfg 1",
                *compute(e),
                tellraw("@s", ["", {"text": f"\n⬢ {TITLE[e]}", "color": EMOTION_COLOR[e], "bold": True},
                               {"text": (f"  the {CORPS_TITLE[corps]} ring comes at 100%" if e != "death" else
                                         "  how close you have come to death"), "color": "dark_gray"}])]
        page += bar_lines(e, [{"text": " "}], stats(e))
        page.append(tellraw("@s", ["", {"text": " What has raised it:", "color": "white"}]))
        for label, rate, idxs in label_groups(e):
            if len(idxs) > 1:  # sum the sources sharing this label
                page += [f"scoreboard players add @s gl_tr_{e}{j} 0" for j in idxs]
                page.append(f"scoreboard players operation #tr gl_tmp = @s gl_tr_{e}{idxs[0]}")
                page += [f"scoreboard players operation #tr gl_tmp += @s gl_tr_{e}{j}" for j in idxs[1:]]
                amount = {"score": {"name": "#tr", "objective": "gl_tmp"}, "color": "white"}
            else:
                page.append(f"scoreboard players add @s gl_tr_{e}{idxs[0]} 0")
                amount = {"score": {"name": "@s", "objective": f"gl_tr_{e}{idxs[0]}"}, "color": "white"}
            page.append(tellraw("@s", ["", {"text": f"  • {label}: +", "color": "gray"}, amount,
                                       {"text": f"  ({rate})", "color": "dark_gray"}]))
        page += [f"scoreboard players add @s gl_tr_{e}_start 0",
                 tellraw("@s", ["", {"text": "  • Born with: +", "color": "gray"},
                                {"score": {"name": "@s", "objective": f"gl_tr_{e}_start"}, "color": "white"}]),
                 f"scoreboard players add @s gl_tr_{e}_quests 0",
                 tellraw("@s", ["", {"text": "  • Quests: +", "color": "gray"},
                                {"score": {"name": "@s", "objective": f"gl_tr_{e}_quests"}, "color": "white"}]),
                 tellraw("@s", ["", {"text": " Quests:", "color": "white"}])]
        for n, (title, task, crits, target, unit, per, reward) in enumerate(QUESTS[e], 1):
            head = [{"text": f"  {ROMAN[n - 1]}. ", "color": "gray"}]
            shown = f"{target // per}{' ' + unit if unit else ''}"
            page += [
                f"execute if score @s gl_qn_{e} matches {n + 1}.. run " + tellraw("@s", ["", 
                    *head, {"text": "✔ ", "color": "green"}, {"text": title, "color": "dark_green"},
                    {"text": f" - {task}", "color": "dark_gray"}]),
                f"execute if score @s gl_qn_{e} matches {n} run " + tellraw("@s", ["", 
                    *head, {"text": "▶ ", "color": "gold"}, {"text": title, "color": EMOTION_COLOR[e]},
                    {"text": f" - {task}: ", "color": "gray"},
                    {"score": {"name": "@s", "objective": f"gl_qd_{e}"}, "color": "white"},
                    {"text": f"/{shown}", "color": "white"}, {"text": f"  reward +{reward:,}", "color": "dark_gray"}]),
                f"execute unless score @s gl_qn_{e} matches {n}.. run " + tellraw("@s", ["", 
                    *head, {"text": "○ ", "color": "dark_gray"}, {"text": title, "color": "dark_gray"},
                    {"text": f" - {task} (reward +{reward:,})", "color": "dark_gray"}]),
            ]
        page.append(tellraw("@s", ["", {"text": " "}, button("[‹ All emotions]", 1, "Back to the whole spectrum")]))
        fn[f"emotion/page/{e}"] = page

    fn["emotion/trigger"] = [
        "scoreboard players operation #v gl_tmp = @s gl_emotions",
        "scoreboard players set @s gl_emotions 0",
        "scoreboard players enable @s gl_emotions",
        f"execute unless score #v gl_tmp matches 11..{10 + len(EMOTIONS)} run function {NS}:emotion/menu",
        *[f"execute if score #v gl_tmp matches {10 + i} run function {NS}:emotion/page/{e}"
          for i, e in enumerate(EMOTIONS, 1)],
    ]
    tick.append(f"execute as @a[scores={{gl_emotions=1..}}] run function {NS}:emotion/trigger")
    assert all(EMOTION_OF[c] in EMOTIONS for c in SPECTRUM)
    load.append("scoreboard players set #60 gl_cfg 60")
    return load, tick, second, fn, files
