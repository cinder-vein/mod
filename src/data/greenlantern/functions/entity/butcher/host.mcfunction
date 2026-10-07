execute as @e[tag=gl_ent_butcher] at @s run function greenlantern:entity/remove_body
superpower add greenlantern:host_butcher @s
tag @s add gl_host
tag @s add gl_host_butcher
scoreboard players operation #host_butcher gl_ent = @s gl_id
scoreboard players set #state_butcher gl_ent 2
tag @a remove gl_hunted_butcher
tag @a remove gl_eoffer_butcher
bossbar set greenlantern:butcher players
particle minecraft:dust 0.86 0.12 0.14 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host The Butcher", "color": "#DC1E23", "bold": true}
tellraw @a [{"selector": "@s", "color": "#DC1E23"}, {"text": " is now the host of The Butcher, the rage entity.", "color": "#DC1E23"}]
