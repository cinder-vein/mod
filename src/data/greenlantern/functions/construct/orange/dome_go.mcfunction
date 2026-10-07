energybar value subtract @s greenlantern:orange_lantern ring_charge 200
scoreboard players set @s gl_cc_dome 300
tag @s add gl_user
execute align xyz run function greenlantern:construct/orange/dome
particle minecraft:dust 0.98 0.51 0.08 2.0 ~ ~1 ~ 3 2 3 0 150 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.2
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Dome","color":"#FA8214"}]
