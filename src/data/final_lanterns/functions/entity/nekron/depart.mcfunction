execute as @e[tag=gl_ent_nekron] at @s run particle minecraft:dust 0.59 0.61 0.67 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_nekron] at @s run function final_lanterns:entity/remove_body
scoreboard players set #state_nekron gl_ent 0
tag @a remove gl_hunted_nekron
tag @a remove gl_eoffer_nekron
tellraw @a[distance=..64] [{"text": "Nekron fades away.", "color": "#969BAA", "italic": true}]
