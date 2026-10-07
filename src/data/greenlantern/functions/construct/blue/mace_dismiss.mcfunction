clear @s greenlantern:construct_mace
particle minecraft:dust 0.16 0.51 1.00 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 20 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 1.8
title @s actionbar [{"text":"Mace dismissed.","color":"gray"}]
