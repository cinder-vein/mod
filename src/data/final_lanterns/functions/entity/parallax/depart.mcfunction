execute as @e[tag=gl_ent_parallax] at @s run particle minecraft:dust 0.96 0.80 0.12 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_parallax] at @s run function final_lanterns:entity/remove_body
scoreboard players set #state_parallax gl_ent 0
tag @a remove gl_hunted_parallax
tag @a remove gl_eoffer_parallax
tellraw @a[distance=..64] [{"text": "Parallax fades away.", "color": "#F5CD1E", "italic": true}]
