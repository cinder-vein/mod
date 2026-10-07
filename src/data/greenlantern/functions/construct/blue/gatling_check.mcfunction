scoreboard players set #ok gl_tmp 1
execute if score @s gl_cc_gatling matches 1.. run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run title @s actionbar [{"text":"Gatling is recharging...","color":"gray"}]
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:blue_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..39 run function greenlantern:construct/low_charge
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/blue/gatling_go
