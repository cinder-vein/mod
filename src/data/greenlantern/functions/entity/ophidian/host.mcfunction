execute as @e[tag=gl_ent_ophidian] at @s run function greenlantern:entity/remove_body
superpower add greenlantern:host_ophidian @s
tag @s add gl_host
tag @s add gl_host_ophidian
scoreboard players operation #host_ophidian gl_ent = @s gl_id
scoreboard players set #state_ophidian gl_ent 2
tag @a remove gl_hunted_ophidian
tag @a remove gl_eoffer_ophidian
particle minecraft:dust 0.98 0.51 0.08 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host Ophidian", "color": "#FA8214", "bold": true}
tellraw @a [{"selector": "@s", "color": "#FA8214"}, {"text": " is now the host of Ophidian, the avarice entity.", "color": "#FA8214"}]
