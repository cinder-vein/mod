energybar value subtract @s greenlantern:black_lantern ring_charge 80
scoreboard players set @s gl_cc_bridge 60
tag @s add gl_user
execute if entity @s[y_rotation=-45..45] align xyz run function greenlantern:construct/black/bridge_s
execute if entity @s[y_rotation=135..-135] align xyz run function greenlantern:construct/black/bridge_n
execute if entity @s[y_rotation=45..135] align xyz run function greenlantern:construct/black/bridge_w
execute if entity @s[y_rotation=-135..-45] align xyz run function greenlantern:construct/black/bridge_e
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.0
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Bridge","color":"#AAAFBE"}]
