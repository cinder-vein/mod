scoreboard players set #ok gl_tmp 1
execute if score @s gl_cc_missiles matches 1.. run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run title @s actionbar [{"text":"Missile Barrage is recharging...","color":"gray"}]
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:yellow_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..119 run function greenlantern:construct/low_charge
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/yellow/missiles_go
