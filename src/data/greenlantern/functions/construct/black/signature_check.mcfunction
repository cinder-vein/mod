scoreboard players set #ok gl_tmp 1
execute if score @s gl_cc_signature matches 1.. run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run title @s actionbar [{"text":"Black Hand is recharging...","color":"gray"}]
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:black_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..149 run function greenlantern:construct/low_charge
tag @s add gl_user
execute if score #ok gl_tmp matches 1 unless entity @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12] run function greenlantern:construct/no_target
tag @s remove gl_user
execute if score #ok gl_tmp matches 1 run function greenlantern:construct/black/signature_go
