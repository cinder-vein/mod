clear @s greenlantern:construct_sword
particle minecraft:dust 0.37 0.38 0.43 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 20 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 1.8
title @s actionbar [{"text":"Sword dismissed.","color":"gray"}]
