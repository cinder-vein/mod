execute as @e[tag=gl_ent_ion] at @s run particle minecraft:dust 0.18 0.78 0.27 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_ion] at @s run function final_lanterns:entity/remove_body
scoreboard players set #state_ion gl_ent 0
tag @a remove gl_hunted_ion
tag @a remove gl_eoffer_ion
tellraw @a[distance=..64] [{"text": "Ion fades away.", "color": "#2EC846", "italic": true}]
