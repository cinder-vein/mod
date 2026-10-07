clear @s greenlantern:construct_shield
particle minecraft:dust 0.18 0.78 0.27 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 20 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 1.8
title @s actionbar [{"text":"Tower Shield dismissed.","color":"gray"}]
