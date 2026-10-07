function greenlantern:dual/spend_400
tag @s add gl_user
execute if entity @s[tag=gl_p1_green] run particle minecraft:dust 0.18 0.78 0.27 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_yellow] run particle minecraft:dust 0.96 0.80 0.12 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_red] run particle minecraft:dust 0.86 0.12 0.14 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_orange] run particle minecraft:dust 0.98 0.51 0.08 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_blue] run particle minecraft:dust 0.16 0.51 1.00 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_violet] run particle minecraft:dust 0.84 0.22 0.86 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_indigo] run particle minecraft:dust 0.41 0.24 0.90 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_white] run particle minecraft:dust 0.92 0.95 0.98 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p1_black] run particle minecraft:dust 0.59 0.61 0.67 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_green] run particle minecraft:dust 0.18 0.78 0.27 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_yellow] run particle minecraft:dust 0.96 0.80 0.12 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_red] run particle minecraft:dust 0.86 0.12 0.14 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_orange] run particle minecraft:dust 0.98 0.51 0.08 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_blue] run particle minecraft:dust 0.16 0.51 1.00 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_violet] run particle minecraft:dust 0.84 0.22 0.86 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_indigo] run particle minecraft:dust 0.41 0.24 0.90 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_white] run particle minecraft:dust 0.92 0.95 0.98 3.0 ~ ~1 ~ 5 2 5 0 260 force
execute if entity @s[tag=gl_p2_black] run particle minecraft:dust 0.59 0.61 0.67 3.0 ~ ~1 ~ 5 2 5 0 260 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force
execute as @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12] run damage @s 24 minecraft:player_attack by @p[tag=gl_user]
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12] minecraft:levitation 2 3 true
effect give @s minecraft:strength 15 1 true
effect give @s minecraft:resistance 15 1 true
effect give @s minecraft:speed 15 1 true
title @s times 5 40 10
title @s title {"text": "Spectrum Overload", "color": "white", "bold": true}
playsound minecraft:entity.generic.explode player @a[distance=..24] ~ ~ ~ 1 0.6
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.6
tag @s remove gl_user
