clear @s greenlantern:construct_drill
particle minecraft:dust 0.84 0.22 0.86 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 20 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 1.8
title @s actionbar [{"text":"Mining Drill dismissed.","color":"gray"}]
