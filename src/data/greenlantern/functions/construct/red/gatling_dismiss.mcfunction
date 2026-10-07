clear @s greenlantern:construct_gatling
particle minecraft:dust 0.86 0.12 0.14 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 20 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 1.8
title @s actionbar [{"text":"Gatling dismissed.","color":"gray"}]
