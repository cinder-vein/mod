energybar value subtract @s greenlantern:black_lantern ring_charge 20
scoreboard players set @s gl_cc_scuba 10
tag @s add gl_user
tag @s add gl_scuba_black
particle minecraft:dust 0.59 0.61 0.67 1.0 ~ ~1.7 ~ 0.4 0.4 0.4 0 40 force
playsound minecraft:item.armor.equip_turtle player @a[distance=..24] ~ ~ ~ 1 1.2
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Scuba Gear","color":"#AAAFBE"}]
