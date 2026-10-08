execute as @e[tag=gl_ent_parallax] at @s run function final_lanterns:entity/remove_body
superpower add final_lanterns:host_parallax @s
tag @s add gl_host
tag @s add gl_host_parallax
scoreboard players operation #host_parallax gl_ent = @s gl_id
scoreboard players set #state_parallax gl_ent 2
tag @a remove gl_hunted_parallax
tag @a remove gl_eoffer_parallax
particle minecraft:dust 0.96 0.80 0.12 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host Parallax", "color": "#F5CD1E", "bold": true}
tellraw @a [{"selector": "@s", "color": "#F5CD1E"}, {"text": " is now the host of Parallax, the fear entity.", "color": "#F5CD1E"}]
