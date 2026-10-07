"""The Spectrum Bond: two rings worn at once (datapack side), and the keys for switching ring modes.

gen_corps.py builds the greenlantern:spectrum_lantern power (its ability bar and its skill tree). This module:
- grants that power to players wearing two rings and takes it away when they're down to one;
- tags the two bonded rings: gl_p1_<corps> (first in CORPS order, worn on the right hand) and gl_p2_<corps>;
- mirrors both rings' charge into the power's Spectrum Charge bar;
- holds the functions the bond's abilities run: merged constructs, Twin Blast, Scan, Spectrum Fusion,
  Spectrum Overload, and the Harmony skills (Shared Light, Twin Batteries, Resonance);
- switches between beam mode and blast mode (ring/mode) and keeps the Ctrl state the KubeJS client script sends.
"""
import json

from constructs import BAR, CATALOG, NODES, NS, SIGNATURES, TARGETS, actionbar, burst, hexcolor, sound

POWER = f"{NS}:spectrum_lantern"
SPECTRUM_BAR = "spectrum_charge"
# charge each bonded ring pays (merged constructs cost their own ring, see run_construct)
COSTS = {"blast": 20, "scan": 5, "fusion_1": 125, "fusion_2": 75, "overload": 400}
OVERLOAD_RADIUS = 12


def generate(corps_table, fusion_pairs):
    """Returns (load, tick, second, functions)."""
    corps = list(corps_table)
    fn, load, tick, second = {}, [], [], []
    power = lambda c: f"{NS}:{c}_lantern"  # noqa: E731
    color = lambda c: corps_table[c]["color"] if c != "black" else (150, 155, 170)  # noqa: E731

    load += ["scoreboard objectives add gl_rings dummy", "scoreboard objectives add gl_dmax dummy",
             "scoreboard objectives add gl_dlast dummy", "scoreboard objectives add gl_dtick dummy",
             "scoreboard objectives add gl_kjs dummy",
             *[f"scoreboard objectives add glmax_{c} dummy" for c in corps]]

    # --- which rings are bonded --------------------------------------------------------------------
    # gl_<corps> is set every tick by each worn ring's power; the first two in CORPS order bond.
    tick += ["scoreboard players set @a gl_rings 0"]
    for c in corps:
        tick += [f"tag @a[tag=gl_p1_{c}] remove gl_p1_{c}", f"tag @a[tag=gl_p2_{c}] remove gl_p2_{c}"]
    for c in corps:
        tick += [f"scoreboard players add @a[tag=gl_{c}] gl_rings 1",
                 f"tag @a[tag=gl_{c},scores={{gl_rings=1}}] add gl_p1_{c}",
                 f"tag @a[tag=gl_{c},scores={{gl_rings=2}}] add gl_p2_{c}"]
    tick += [f"execute as @a[tag=!gl_dual,scores={{gl_rings=2..}}] at @s run function {NS}:dual/bond",
             f"execute as @a[tag=gl_dual,scores={{gl_rings=..1}}] run function {NS}:dual/unbond",
             # the Spectrum Charge bar, five times a second
             "scoreboard players add #t gl_dtick 1",
             "execute if score #t gl_dtick matches 4.. run scoreboard players set #t gl_dtick 0",
             f"execute if score #t gl_dtick matches 0 as @a[tag=gl_dual] run function {NS}:dual/mirror"]
    # keep the power in step with the tag, even if something else added or removed it
    second += [f"execute as @a[tag=gl_dual] run superpower add {POWER} @s",
               f"execute as @a[tag=!gl_dual] run superpower remove {POWER} @s",
               "scoreboard players add #s gl_dtick 1",
               "execute if score #s gl_dtick matches 5.. run scoreboard players set @a gl_dlast -1",
               "execute if score #s gl_dtick matches 5.. run scoreboard players set #s gl_dtick 0",
               f"execute as @a[tag=gl_dual] run function {NS}:dual/second"]

    hello = []
    for a, b in fusion_pairs:
        hello.append(f"execute if entity @s[tag=gl_p1_{a},tag=gl_p2_{b}] run function {NS}:dual/hello/{a}_{b}")
        ea, eb = corps_table[a]["emotion"], corps_table[b]["emotion"]
        fn[f"dual/hello/{a}_{b}"] = [
            actionbar([{"text": "Spectrum Bond: ", "color": "white", "bold": True},
                       {"text": ea, "color": hexcolor(color(a))}, {"text": " + ", "color": "gray"},
                       {"text": eb, "color": hexcolor(color(b))}]),
            burst(color(a), 1.4, "0.5 1 0.5", 60), burst(color(b), 1.4, "0.5 1 0.5", 60),
            sound("minecraft:block.beacon.power_select", 1.5),
        ]
    fn["dual/bond"] = [
        f"superpower add {POWER} @s",
        "tag @s add gl_dual",
        "scoreboard players set @s gl_dlast -1",
        *hello,
        "execute unless entity @s[tag=gl_bond_seen] run tellraw @s " + json.dumps([
            {"text": "Your two rings bond. ", "color": "white", "bold": True},
            {"text": "Their beams, constructs, force fields, ring light and suit merge into the Spectrum Bond bar (each "
                     "ring keeps its own specials page), and the Spectrum Bond has its own skill tree in the powers "
                     "menu. Choose a merged suit in the accessories menu.", "color": "gray"}]),
        "tag @s add gl_bond_seen",
    ]
    fn["dual/unbond"] = [
        f"superpower remove {POWER} @s",
        "tag @s remove gl_dual",
        actionbar([{"text": "The Spectrum Bond fades.", "color": "gray"}]),
    ]

    # --- reading both rings ------------------------------------------------------------------------
    # dual/read sets #c1/#c2 (charge), #m1/#m2 (max charge) and #ready (rings whose charge has been restored)
    read = ["scoreboard players set #c1 gl_tmp 0", "scoreboard players set #c2 gl_tmp 0",
            "scoreboard players set #m1 gl_tmp 1000", "scoreboard players set #m2 gl_tmp 1000",
            "scoreboard players set #ready gl_tmp 0"]
    for c in corps:
        for n in (1, 2):
            read.append(f"execute if entity @s[tag=gl_p{n}_{c}] run function {NS}:dual/read{n}/{c}")
            fn[f"dual/read{n}/{c}"] = [
                f"execute store result score #c{n} gl_tmp run energybar value get @s {power(c)} {BAR}",
                f"execute if score @s glmax_{c} matches 1.. run scoreboard players operation #m{n} gl_tmp = @s glmax_{c}",
                f"execute if entity @s[tag=gl_cr_{c}] run scoreboard players add #ready gl_tmp 1",
            ]
    fn["dual/read"] = read

    fn["dual/mirror"] = [
        f"function {NS}:dual/read",
        "scoreboard players operation #sum gl_tmp = #c1 gl_tmp",
        "scoreboard players operation #sum gl_tmp += #c2 gl_tmp",
        "scoreboard players operation @s gl_dmax = #m1 gl_tmp",
        "scoreboard players operation @s gl_dmax += #m2 gl_tmp",
        f"execute unless score @s gl_dlast = #sum gl_tmp run function {NS}:dual/mirror_set",
    ]
    mirror = ["scoreboard players operation #bits gl_tmp = #sum gl_tmp",
              f"execute store success score #set gl_tmp run energybar value set @s {POWER} {SPECTRUM_BAR} 0"]
    for bit in (2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1):  # no macros in 1.20.1: add it bit by bit
        mirror += [f"execute if score #bits gl_tmp matches {bit}.. run energybar value add @s {POWER} {SPECTRUM_BAR} {bit}",
                   f"execute if score #bits gl_tmp matches {bit}.. run scoreboard players remove #bits gl_tmp {bit}"]
    mirror.append("execute if score #set gl_tmp matches 1 run scoreboard players operation @s gl_dlast = #sum gl_tmp")
    fn["dual/mirror_set"] = mirror

    # --- paying with both rings ----------------------------------------------------------------------
    for cost in sorted(set(COSTS.values())):
        fn[f"dual/check_{cost}"] = [  # after dual/read: #ok 1 if both rings hold `cost`
            "scoreboard players set #ok gl_tmp 1",
            f"execute if score #c1 gl_tmp matches ..{cost - 1} run function {NS}:construct/low_charge",
            f"execute if score #ok gl_tmp matches 1 if score #c2 gl_tmp matches ..{cost - 1} run "
            f"function {NS}:construct/low_charge",
        ]
        fn[f"dual/spend_{cost}"] = [f"execute if entity @s[tag=gl_p{n}_{c}] run energybar value subtract @s {power(c)} {BAR} {cost}"
                                    for n in (1, 2) for c in corps]

    def paid(name, body):
        cost = COSTS[name]
        fn[f"dual/{name}"] = [f"function {NS}:dual/read", f"function {NS}:dual/check_{cost}",
                              f"execute if score #ok gl_tmp matches 1 run function {NS}:dual/{name}_go"]
        fn[f"dual/{name}_go"] = [f"function {NS}:dual/spend_{cost}", *body]

    # Twin Blast: one bolt from each hand, in each ring's color
    paid("blast", [*[f"execute if entity @s[tag=gl_p1_{c}] run function {NS}:ring/{c}/blast_fire_right" for c in corps],
                   *[f"execute if entity @s[tag=gl_p2_{c}] run function {NS}:ring/{c}/blast_fire_left" for c in corps]])
    paid("scan", [f"execute if entity @s[tag=gl_p1_{c}] run function {NS}:ring/{c}/scan_fire" for c in corps])
    fusion = [f"execute if entity @s[tag=gl_p1_{a},tag=gl_p2_{b}] run function {NS}:fusion/{a}_{b}" for a, b in fusion_pairs]
    paid("fusion_1", fusion)
    paid("fusion_2", fusion)
    around = TARGETS.format(r=OVERLOAD_RADIUS) + "]"
    paid("overload", [
        "tag @s add gl_user",
        *[f"execute if entity @s[tag=gl_p{n}_{c}] run {burst(color(c), 3.0, '5 2 5', 260)}" for n in (1, 2) for c in corps],
        "particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force",
        f"execute as {around} run damage @s 24 minecraft:player_attack by @p[tag=gl_user]",
        f"effect give {around} minecraft:levitation 2 3 true",
        "effect give @s minecraft:strength 15 1 true",
        "effect give @s minecraft:resistance 15 1 true",
        "effect give @s minecraft:speed 15 1 true",
        "title @s times 5 40 10",
        "title @s title " + json.dumps({"text": "Spectrum Overload", "color": "white", "bold": True}),
        sound("minecraft:entity.generic.explode", 0.6), sound("minecraft:block.beacon.power_select", 0.6),
        "tag @s remove gl_user",
    ])

    # --- merged constructs ---------------------------------------------------------------------------
    # A construct forms from the first ring (right hand) if that ring has it unlocked, otherwise from the
    # second. It costs that ring, in that ring's color; Twin Constructs refunds a quarter of the cost.
    def run_construct(c, key, cost):
        fn[f"dual/run/{c}/{key}"] = [
            "scoreboard players set #done gl_tmp 1",
            "scoreboard players set #ok gl_tmp 0",
            f"function {NS}:construct/{c}/{key}_try",
            f"execute if score #ok gl_tmp matches 1 if entity @s[tag=gl_du_twin_constructs] run "
            f"energybar value add @s {power(c)} {BAR} {cost // 4}",
        ]

    for con in CATALOG:
        node_title = NODES[con.node][0]
        for c in corps:
            run_construct(c, con.key, con.cost)
        fn[f"dual/cx/{con.key}"] = [
            "scoreboard players set #done gl_tmp 0",
            *[f"execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p{n}_{c},tag=gl_u_{c}_{con.node}] run "
              f"function {NS}:dual/run/{c}/{con.key}" for n in (1, 2) for c in corps],
            "execute if score #done gl_tmp matches 0 run "
            + actionbar([{"text": f"{con.name} isn't unlocked in either ring yet. Buy ", "color": "gray"},
                         {"text": node_title, "color": "white"}, {"text": " in a ring's powers menu.", "color": "gray"}]),
        ]
    for c in corps:
        run_construct(c, "signature", SIGNATURES[c].cost)
    fn["dual/cx/sig_1"] = [
        "scoreboard players set #done gl_tmp 0",
        *[f"execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p{n}_{c},tag=gl_u_{c}_signature] run "
          f"function {NS}:dual/run/{c}/signature" for n in (1, 2) for c in corps],
        "execute if score #done gl_tmp matches 0 run "
        + actionbar([{"text": "Neither ring's signature construct is unlocked yet (all four construct branches).",
                      "color": "gray"}]),
    ]
    fn["dual/cx/sig_2"] = [
        "scoreboard players set #done gl_tmp 0",
        "execute unless entity @s[tag=gl_du_twin_signatures] run scoreboard players set #done gl_tmp 2",
        "execute if score #done gl_tmp matches 2 run "
        + actionbar([{"text": "Buy Twin Signatures in the Spectrum Bond tree first.", "color": "gray"}]),
        *[f"execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_{c},tag=gl_u_{c}_signature] run "
          f"function {NS}:dual/run/{c}/signature" for c in corps],
        "execute if score #done gl_tmp matches 0 run "
        + actionbar([{"text": "Your second ring's signature construct isn't unlocked yet.", "color": "gray"}]),
    ]

    # --- Harmony skills ----------------------------------------------------------------------------
    fn["dual/second"] = [
        f"function {NS}:dual/read",
        f"execute if score #ready gl_tmp matches 2 if entity @s[tag=gl_du_shared_light] run function {NS}:dual/shared_light",
        f"execute if score #ready gl_tmp matches 2 if entity @s[tag=gl_du_resonance] run function {NS}:dual/resonance",
    ]
    fn["dual/shared_light"] = [  # charge flows from the fuller ring into the emptier one, up to 10 a second
        "scoreboard players operation #diff gl_tmp = #c1 gl_tmp",
        "scoreboard players operation #diff gl_tmp -= #c2 gl_tmp",
        f"execute if score #diff gl_tmp matches 20.. if score #c2 gl_tmp < #m2 gl_tmp run function {NS}:dual/move/1to2_10",
        f"execute if score #diff gl_tmp matches 2..19 if score #c2 gl_tmp < #m2 gl_tmp run function {NS}:dual/move/1to2_1",
        f"execute if score #diff gl_tmp matches ..-20 if score #c1 gl_tmp < #m1 gl_tmp run function {NS}:dual/move/2to1_10",
        f"execute if score #diff gl_tmp matches -19..-2 if score #c1 gl_tmp < #m1 gl_tmp run function {NS}:dual/move/2to1_1",
    ]
    for src, dst in ((1, 2), (2, 1)):
        for n in (1, 10):
            fn[f"dual/move/{src}to{dst}_{n}"] = [
                *[f"execute if entity @s[tag=gl_p{src}_{c}] run energybar value subtract @s {power(c)} {BAR} {n}" for c in corps],
                *[f"execute if entity @s[tag=gl_p{dst}_{c}] run energybar value add @s {power(c)} {BAR} {n}" for c in corps],
            ]
    fn["dual/resonance"] = [f"execute if entity @s[tag=gl_p{n}_{c}] run energybar value add @s {power(c)} {BAR} 2"
                            for n in (1, 2) for c in corps]
    # Twin Batteries: run by each ring's oath (whenever a ring recharges at its battery)
    fn["dual/twin_battery"] = [f"execute if entity @s[tag=gl_dual,tag=gl_du_twin_batteries] run function {NS}:dual/fill_both"]
    fn["dual/fill_both"] = [f"execute if entity @s[tag=gl_p{n}_{c}] run energybar value add @s {power(c)} {BAR} 100000"
                            for n in (1, 2) for c in corps]

    # --- ring modes and the Ctrl key ---------------------------------------------------------------
    fn["ring/mode"] = [
        "execute store success score #m gl_tmp if entity @s[tag=gl_mode]",
        "execute if score #m gl_tmp matches 1 run tag @s remove gl_mode",
        "execute if score #m gl_tmp matches 0 run tag @s add gl_mode",
        "execute if score #m gl_tmp matches 0 run " + actionbar([{"text": "Blast mode: ", "color": "aqua"},
                                                                 {"text": "Energy Blast and Scan", "color": "white"}]),
        "execute if score #m gl_tmp matches 1 run " + actionbar([{"text": "Beam mode: ", "color": "aqua"},
                                                                 {"text": "Beam and Construct Wheel", "color": "white"}]),
        "playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 0.5 1.8",
    ]
    # The KubeJS client script reports Ctrl when it changes and once a second (a heartbeat): gl_kjs marks
    # players whose client runs it (they switch with Ctrl, not by sneaking) and lapses 3 s after it stops.
    for state, line in (("on", "tag @s add gl_ctrl"), ("off", "tag @s remove gl_ctrl")):
        fn[f"keys/ctrl_{state}"] = [line, "tag @s add gl_kjs", "scoreboard players set @s gl_kjs 60"]
    tick += ["scoreboard players remove @a[scores={gl_kjs=1..}] gl_kjs 1",
             "tag @a[tag=gl_kjs,scores={gl_kjs=..0}] remove gl_ctrl",
             "tag @a[tag=gl_kjs,scores={gl_kjs=..0}] remove gl_kjs"]
    return load, tick, second, fn


KUBEJS_CLIENT = r"""// Lantern Corps: hold Ctrl and press the first ability key to switch your ring between beam mode
// (Beam, Construct Wheel) and blast mode (Energy Blast, Scan). Palladium can't see Ctrl, so this client
// script tells the server while it's held; the first ability slot then shows Switch Mode.
// Loaded by Palladium's KubeJS integration when KubeJS is installed (without it, sneak instead of Ctrl).
let glCtrlDown = false
let glCtrlBeat = 0
let glScreenClass = null
try {
  glScreenClass = Java.loadClass('net.minecraft.client.gui.screens.Screen')
} catch (e) {
  glScreenClass = null
}

ClientEvents.tick(event => {
  const mc = Client
  if (!mc.player) return
  let down = false
  if (mc.screen == null) { // in game only: Ctrl in a menu or chat doesn't count
    try {
      down = glScreenClass ? !!glScreenClass.hasControlDown() : !!mc.options.keySprint.isDown()
    } catch (e) {
      down = false
    }
  }
  glCtrlBeat++
  if (down !== glCtrlDown || glCtrlBeat >= 20) { // on change, and once a second so the server knows we're here
    glCtrlDown = down
    glCtrlBeat = 0
    mc.player.sendData('greenlantern_keys', { ctrl: down })
  }
})
"""

KUBEJS_SERVER = r"""
// Ctrl state from the client script (assets/greenlantern/kubejs_scripts/lantern_keys.js)
NetworkEvents.dataReceived('greenlantern_keys', event => {
  const player = event.player
  if (!player) return
  const data = event.data
  const down = data != null && data.getBoolean('ctrl')
  player.server.runCommandSilent(`execute as ${player.getStringUUID()} run function greenlantern:keys/${down ? 'ctrl_on' : 'ctrl_off'}`)
})
"""
