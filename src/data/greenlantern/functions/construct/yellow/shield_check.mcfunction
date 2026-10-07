scoreboard players set #ok gl_tmp 1
execute if score @s gl_cc_shield matches 1.. run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run title @s actionbar [{"text":"Tower Shield is recharging...","color":"gray"}]
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:yellow_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..29 run function greenlantern:construct/low_charge
execute if score #ok gl_tmp matches 1 run scoreboard players set #need gl_tmp 0
execute if score #ok gl_tmp matches 1 run execute if data entity @s Inventory[{Slot:-106b}] run scoreboard players add #need gl_tmp 1
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/count_free
execute if score #ok gl_tmp matches 1 if score #fs gl_tmp < #need gl_tmp run function greenlantern:construct/no_room
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/yellow/shield_go
