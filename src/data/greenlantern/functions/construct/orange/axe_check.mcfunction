scoreboard players set #ok gl_tmp 1
execute if score @s gl_cc_axe matches 1.. run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run title @s actionbar [{"text":"Battle Axe is recharging...","color":"gray"}]
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:orange_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..39 run function greenlantern:construct/low_charge
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/orange/axe_go
