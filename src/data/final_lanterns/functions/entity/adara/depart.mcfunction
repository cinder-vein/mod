execute as @e[tag=gl_ent_adara] at @s run particle minecraft:dust 0.16 0.51 1.00 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_adara] at @s run function final_lanterns:entity/remove_body
scoreboard players set #state_adara gl_ent 0
tag @a remove gl_hunted_adara
tag @a remove gl_eoffer_adara
tellraw @a[distance=..64] [{"text": "Adara fades away.", "color": "#2882FF", "italic": true}]
