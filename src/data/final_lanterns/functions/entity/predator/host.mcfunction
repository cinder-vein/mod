execute as @e[tag=gl_ent_predator] at @s run function final_lanterns:entity/remove_body
superpower add final_lanterns:host_predator @s
tag @s add gl_host
tag @s add gl_host_predator
scoreboard players operation #host_predator gl_ent = @s gl_id
scoreboard players set #state_predator gl_ent 2
tag @a remove gl_hunted_predator
tag @a remove gl_eoffer_predator
particle minecraft:dust 0.84 0.22 0.86 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host The Predator", "color": "#D737DC", "bold": true}
tellraw @a [{"selector": "@s", "color": "#D737DC"}, {"text": " is now the host of The Predator, the love entity.", "color": "#D737DC"}]
