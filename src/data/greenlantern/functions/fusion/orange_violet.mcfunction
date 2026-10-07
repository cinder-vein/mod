title @s times 5 40 10
title @s subtitle {"text": "Avarice + Love", "color": "gray"}
title @s title [{"text": "Covetous ", "color": "#FA8214"}, {"text": "Heart", "color": "#D737DC"}]
particle minecraft:dust 0.98 0.51 0.08 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:dust 0.84 0.22 0.86 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
execute as @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] run damage @s 6 minecraft:magic
effect give @s minecraft:instant_health 1 1 true
effect give @s minecraft:absorption 30 2 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:slowness 4 255 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:jump_boost 4 250 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:glowing 6 0 true
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.illusioner.cast_spell player @a[distance=..24] ~ ~ ~ 1 1.2
