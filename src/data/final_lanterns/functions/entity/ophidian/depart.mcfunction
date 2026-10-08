execute as @e[tag=gl_ent_ophidian] at @s run particle minecraft:dust 0.98 0.51 0.08 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_ophidian] at @s run function final_lanterns:entity/remove_body
scoreboard players set #state_ophidian gl_ent 0
tag @a remove gl_hunted_ophidian
tag @a remove gl_eoffer_ophidian
tellraw @a[distance=..64] [{"text": "Ophidian fades away.", "color": "#FA8214", "italic": true}]
