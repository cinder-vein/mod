energybar value subtract @s greenlantern:orange_lantern ring_charge 20
scoreboard players set @s gl_cc_scuba 10
tag @s add gl_user
tag @s add gl_scuba_orange
particle minecraft:dust 0.98 0.51 0.08 1.0 ~ ~1.7 ~ 0.4 0.4 0.4 0 40 force
playsound minecraft:item.armor.equip_turtle player @a[distance=..24] ~ ~ ~ 1 1.2
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Scuba Gear","color":"#FA8214"}]
