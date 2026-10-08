execute as @e[tag=gl_ent_butcher] at @s run particle minecraft:dust 0.86 0.12 0.14 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_butcher] at @s run function final_lanterns:entity/remove_body
scoreboard players set #state_butcher gl_ent 0
tag @a remove gl_hunted_butcher
tag @a remove gl_eoffer_butcher
tellraw @a[distance=..64] [{"text": "The Butcher fades away.", "color": "#DC1E23", "italic": true}]
