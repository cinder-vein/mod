execute as @e[tag=gl_ent_proselyte] at @s run function greenlantern:entity/remove_body
superpower add greenlantern:host_proselyte @s
tag @s add gl_host
tag @s add gl_host_proselyte
scoreboard players operation #host_proselyte gl_ent = @s gl_id
scoreboard players set #state_proselyte gl_ent 2
tag @a remove gl_hunted_proselyte
tag @a remove gl_eoffer_proselyte
particle minecraft:dust 0.41 0.24 0.90 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host The Proselyte", "color": "#693CE6", "bold": true}
tellraw @a [{"selector": "@s", "color": "#693CE6"}, {"text": " is now the host of The Proselyte, the compassion entity.", "color": "#693CE6"}]
