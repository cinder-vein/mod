execute as @e[tag=gl_ent_proselyte] at @s run particle minecraft:dust 0.41 0.24 0.90 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_proselyte] at @s run function greenlantern:entity/remove_body
scoreboard players set #state_proselyte gl_ent 0
tag @a remove gl_hunted_proselyte
tag @a remove gl_eoffer_proselyte
tellraw @a[distance=..64] [{"text": "The Proselyte fades away.", "color": "#693CE6", "italic": true}]
