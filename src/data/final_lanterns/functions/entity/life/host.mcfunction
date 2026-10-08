execute as @e[tag=gl_ent_life] at @s run function final_lanterns:entity/remove_body
superpower add final_lanterns:host_life @s
tag @s add gl_host
tag @s add gl_host_life
scoreboard players operation #host_life gl_ent = @s gl_id
scoreboard players set #state_life gl_ent 2
tag @a remove gl_hunted_life
tag @a remove gl_eoffer_life
particle minecraft:dust 0.92 0.95 0.98 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host The Life Entity", "color": "#EBF2FA", "bold": true}
tellraw @a [{"selector": "@s", "color": "#EBF2FA"}, {"text": " is now the host of The Life Entity, the entity of life itself.", "color": "#EBF2FA"}]
