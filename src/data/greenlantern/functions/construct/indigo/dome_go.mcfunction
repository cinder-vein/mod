energybar value subtract @s greenlantern:indigo_lantern ring_charge 200
scoreboard players set @s gl_cc_dome 300
tag @s add gl_user
execute align xyz run function greenlantern:construct/indigo/dome
particle minecraft:dust 0.41 0.24 0.90 2.0 ~ ~1 ~ 3 2 3 0 150 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.2
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Dome","color":"#693CE6"}]
