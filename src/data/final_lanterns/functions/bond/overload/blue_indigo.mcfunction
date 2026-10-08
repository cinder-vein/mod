particle minecraft:dust 0.16 0.51 1.00 3.0 ~ ~1 ~ 6 2 6 0 400 force
particle minecraft:dust 0.41 0.24 0.90 3.0 ~ ~1 ~ 6 2 6 0 400 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 3 force
execute as @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12] run damage @s 24 minecraft:player_attack by @p[tag=gl_user]
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12] minecraft:levitation 2 4 true
effect give @s minecraft:strength 15 1 true
effect give @s minecraft:resistance 15 1 true
effect give @s minecraft:speed 15 1 true
title @s times 5 40 10
title @s title [{"text": "Spectrum ", "color": "#2882FF"}, {"text": "Overload", "color": "#693CE6"}]
playsound minecraft:entity.generic.explode player @a[distance=..24] ~ ~ ~ 1 0.6
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.6
