energybar value subtract @s greenlantern:blue_lantern ring_charge 100
scoreboard players set @s gl_cc_barrier 120
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Barrier Wall","color":"#2882FF"}]
tag @s add gl_user
execute if entity @s[y_rotation=-45..45] rotated ~ 0 positioned ^ ^ ^3 align xyz run function greenlantern:construct/blue/wall_x
execute if entity @s[y_rotation=135..-135] rotated ~ 0 positioned ^ ^ ^3 align xyz run function greenlantern:construct/blue/wall_x
execute if entity @s[y_rotation=45..135] rotated ~ 0 positioned ^ ^ ^3 align xyz run function greenlantern:construct/blue/wall_z
execute if entity @s[y_rotation=-135..-45] rotated ~ 0 positioned ^ ^ ^3 align xyz run function greenlantern:construct/blue/wall_z
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 0.7
tag @s remove gl_user
