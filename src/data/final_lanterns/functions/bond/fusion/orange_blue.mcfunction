title @s times 5 40 10
title @s subtitle {"text": "Avarice + Hope", "color": "gray"}
title @s title [{"text": "Hope ", "color": "#FA8214"}, {"text": "Hoarded", "color": "#2882FF"}]
particle minecraft:dust 0.98 0.51 0.08 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:dust 0.16 0.51 1.00 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
execute as @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..10] run damage @s 8 minecraft:player_attack by @p[tag=gl_user]
execute rotated ~ 0 positioned ^ ^ ^2 run tp @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,type=!minecraft:player] ~ ~ ~
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..10] minecraft:weakness 8 1 true
effect give @a[distance=..10] minecraft:regeneration 10 1 true
effect give @a[distance=..10] minecraft:resistance 10 0 true
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.illusioner.cast_spell player @a[distance=..24] ~ ~ ~ 1 1.2
