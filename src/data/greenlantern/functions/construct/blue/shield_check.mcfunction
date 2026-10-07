scoreboard players set #ok gl_tmp 1
execute if score @s gl_cc_shield matches 1.. run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run title @s actionbar [{"text":"Tower Shield is recharging...","color":"gray"}]
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:blue_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..29 run function greenlantern:construct/low_charge
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/blue/shield_go
