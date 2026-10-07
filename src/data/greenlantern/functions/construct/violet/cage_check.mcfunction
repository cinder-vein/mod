scoreboard players set #ok gl_tmp 1
execute if score @s gl_cc_cage matches 1.. run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run title @s actionbar [{"text":"Cage is recharging...","color":"gray"}]
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:violet_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..149 run function greenlantern:construct/low_charge
tag @s add gl_user
execute if score #ok gl_tmp matches 1 unless entity @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,type=!minecraft:marker,type=!minecraft:item_display,type=!minecraft:block_display,type=!minecraft:text_display,type=!minecraft:interaction,type=!palladium:custom_projectile,tag=!gl_user,distance=..12] run function greenlantern:construct/no_target
tag @s remove gl_user
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/violet/cage_go
