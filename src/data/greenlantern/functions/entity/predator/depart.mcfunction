execute as @e[tag=gl_ent_predator] at @s run particle minecraft:dust 0.84 0.22 0.86 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_predator] at @s run function greenlantern:entity/remove_body
scoreboard players set #state_predator gl_ent 0
tag @a remove gl_hunted_predator
tag @a remove gl_eoffer_predator
tellraw @a[distance=..64] [{"text": "The Predator fades away.", "color": "#D737DC", "italic": true}]
