execute as @e[tag=gl_ent_adara] at @s run function greenlantern:entity/remove_body
superpower add greenlantern:host_adara @s
tag @s add gl_host
tag @s add gl_host_adara
scoreboard players operation #host_adara gl_ent = @s gl_id
scoreboard players set #state_adara gl_ent 2
tag @a remove gl_hunted_adara
tag @a remove gl_eoffer_adara
particle minecraft:dust 0.16 0.51 1.00 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host Adara", "color": "#2882FF", "bold": true}
tellraw @a [{"selector": "@s", "color": "#2882FF"}, {"text": " is now the host of Adara, the hope entity.", "color": "#2882FF"}]
