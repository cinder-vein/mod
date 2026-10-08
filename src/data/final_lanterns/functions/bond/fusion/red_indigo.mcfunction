title @s times 5 40 10
title @s subtitle {"text": "Rage + Compassion", "color": "gray"}
title @s title [{"text": "Rage ", "color": "#DC1E23"}, {"text": "Understood", "color": "#693CE6"}]
particle minecraft:dust 0.86 0.12 0.14 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:dust 0.41 0.24 0.90 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
execute as @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..10] run damage @s 8 minecraft:player_attack by @p[tag=gl_user]
execute as @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..10] run data merge entity @s {Fire:100s}
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..10] minecraft:wither 5 1 true
effect give @a[distance=..10] minecraft:instant_health 1 0 true
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..10] minecraft:weakness 10 254 true
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.illusioner.cast_spell player @a[distance=..24] ~ ~ ~ 1 1.2
