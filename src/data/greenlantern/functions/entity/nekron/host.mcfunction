execute as @e[tag=gl_ent_nekron] at @s run function greenlantern:entity/remove_body
superpower add greenlantern:host_nekron @s
tag @s add gl_host
tag @s add gl_host_nekron
scoreboard players operation #host_nekron gl_ent = @s gl_id
scoreboard players set #state_nekron gl_ent 2
tag @a remove gl_hunted_nekron
tag @a remove gl_eoffer_nekron
bossbar set greenlantern:nekron players
particle minecraft:dust 0.59 0.61 0.67 3.0 ~ ~1 ~ 1 2 1 0 250 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
playsound minecraft:block.end_portal.spawn player @a[distance=..24] ~ ~ ~ 1 0.7
title @s times 10 70 20
title @s subtitle {"text": "Open the powers menu to grow its power", "color": "gray"}
title @s title {"text": "You host Nekron", "color": "#969BAA", "bold": true}
tellraw @a [{"selector": "@s", "color": "#969BAA"}, {"text": " is now the host of Nekron, the lord of the dead.", "color": "#969BAA"}]
