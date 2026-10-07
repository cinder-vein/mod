energybar value subtract @s greenlantern:black_lantern ring_charge 40
scoreboard players set @s gl_cc_mace 10
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Mace","color":"#AAAFBE"}]
tag @s add gl_user
function greenlantern:construct/free_main
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:construct_mace{CustomModelData:9,gl_construct:1b}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_mace{CustomModelData:9,gl_construct:1b}
particle minecraft:dust 0.59 0.61 0.67 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.8
tag @s remove gl_user
