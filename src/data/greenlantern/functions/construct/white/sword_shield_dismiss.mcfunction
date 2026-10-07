clear @s greenlantern:construct_sword
clear @s greenlantern:construct_shield
particle minecraft:dust 0.92 0.95 0.98 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 20 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 1.8
title @s actionbar [{"text":"Sword & Shield dismissed.","color":"gray"}]
