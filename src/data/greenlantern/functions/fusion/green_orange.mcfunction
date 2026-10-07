title @s times 5 40 10
title @s subtitle {"text": "Willpower + Avarice", "color": "gray"}
title @s title [{"text": "Unbreakable ", "color": "#2EC846"}, {"text": "Grasp", "color": "#FA8214"}]
particle minecraft:dust 0.18 0.78 0.27 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:dust 0.98 0.51 0.08 2.5 ~ ~1 ~ 4 1.5 4 0 220 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 2 force
execute as @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] run damage @s 10 minecraft:player_attack
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] minecraft:levitation 1 3 true
execute as @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,distance=0.5..10] run damage @s 6 minecraft:magic
effect give @s minecraft:instant_health 1 1 true
effect give @s minecraft:absorption 30 2 true
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.8
playsound minecraft:entity.illusioner.cast_spell player @a[distance=..24] ~ ~ ~ 1 1.2
