energybar value subtract @s greenlantern:blue_lantern ring_charge 200
scoreboard players set @s gl_cc_dome 300
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Dome","color":"#2882FF"}]
tag @s add gl_user
execute align xyz run function greenlantern:construct/blue/dome
particle minecraft:dust 0.16 0.51 1.00 2.0 ~ ~1 ~ 3 2 3 0 150 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.2
tag @s remove gl_user
