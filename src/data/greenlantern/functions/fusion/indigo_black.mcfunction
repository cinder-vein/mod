title @s times 5 40 10
title @s subtitle {"text": "Compassion + Death", "color": "gray"}
title @s title [{"text": "Last ", "color": "#693CE6"}, {"text": "Rites", "color": "#5F626E"}]
particle minecraft:dust 0.41 0.24 0.90 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:dust 0.37 0.38 0.43 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:weakness 8 254 true
effect give @a[distance=..10] minecraft:instant_health 1 0 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:wither 8 2 true
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:darkness 6 0 true
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.illusioner.cast_spell player @a[distance=..24] ~ ~ ~ 1 1.2
