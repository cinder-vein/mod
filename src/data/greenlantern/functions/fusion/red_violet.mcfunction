title @s times 5 40 10
title @s subtitle {"text": "Rage + Love", "color": "gray"}
title @s title [{"text": "Crimson ", "color": "#DC1E23"}, {"text": "Passion", "color": "#D737DC"}]
particle minecraft:dust 0.86 0.12 0.14 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:dust 0.84 0.22 0.86 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
execute as @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] run damage @s 6 minecraft:magic
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:wither 6 1 true
execute at @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] run particle minecraft:flame ~ ~1 ~ 0.3 0.6 0.3 0.02 20 force
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:slowness 4 255 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:jump_boost 4 250 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:glowing 6 0 true
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.illusioner.cast_spell player @a[distance=..24] ~ ~ ~ 1 1.2
