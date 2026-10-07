energybar value subtract @s greenlantern:white_lantern ring_charge 80
scoreboard players set @s gl_cc_bridge 60
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Bridge","color":"#EBF2FA"}]
tag @s add gl_user
execute if entity @s[y_rotation=-45..45] align xyz run function greenlantern:construct/white/bridge_s
execute if entity @s[y_rotation=135..-135] align xyz run function greenlantern:construct/white/bridge_n
execute if entity @s[y_rotation=45..135] align xyz run function greenlantern:construct/white/bridge_w
execute if entity @s[y_rotation=-135..-45] align xyz run function greenlantern:construct/white/bridge_e
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.0
tag @s remove gl_user
