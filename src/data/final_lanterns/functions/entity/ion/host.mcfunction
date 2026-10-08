execute as @e[tag=gl_ent_ion] at @s run function final_lanterns:entity/remove_body
superpower add final_lanterns:host_ion @s
tag @s add gl_host
tag @s add gl_host_ion
scoreboard players operation #host_ion gl_ent = @s gl_id
scoreboard players set #state_ion gl_ent 2
tag @a remove gl_hunted_ion
tag @a remove gl_eoffer_ion
particle minecraft:dust 0.18 0.78 0.27 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host Ion", "color": "#2EC846", "bold": true}
tellraw @a [{"selector": "@s", "color": "#2EC846"}, {"text": " is now the host of Ion, the willpower entity.", "color": "#2EC846"}]
