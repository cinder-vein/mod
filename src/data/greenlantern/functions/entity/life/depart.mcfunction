execute as @e[tag=gl_ent_life] at @s run particle minecraft:dust 0.92 0.95 0.98 3.0 ~ ~1 ~ 2 2 2 0 150 force
execute as @e[tag=gl_ent_life] at @s run function greenlantern:entity/remove_body
scoreboard players set #state_life gl_ent 0
tag @a remove gl_hunted_life
tag @a remove gl_eoffer_life
tellraw @a[distance=..64] [{"text": "The Life Entity fades away.", "color": "#EBF2FA", "italic": true}]
