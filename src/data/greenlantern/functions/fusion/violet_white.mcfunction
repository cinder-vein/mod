title @s times 5 40 10
title @s subtitle {"text": "Love + Life", "color": "gray"}
title @s title [{"text": "Love ", "color": "#D737DC"}, {"text": "Eternal", "color": "#EBF2FA"}]
particle minecraft:dust 0.84 0.22 0.86 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:dust 0.92 0.95 0.98 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:slowness 4 255 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:jump_boost 4 250 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:glowing 6 0 true
effect give @a[distance=..10] minecraft:instant_health 1 2 true
effect give @e[distance=..10,type=!minecraft:item,type=!minecraft:experience_orb] minecraft:instant_health 1 1 true
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.illusioner.cast_spell player @a[distance=..24] ~ ~ ~ 1 1.2
