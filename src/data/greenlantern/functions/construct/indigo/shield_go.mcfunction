energybar value subtract @s greenlantern:indigo_lantern ring_charge 30
scoreboard players set @s gl_cc_shield 10
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Tower Shield","color":"#693CE6"}]
tag @s add gl_user
function greenlantern:construct/free_off
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.offhand with greenlantern:construct_shield{CustomModelData:7,gl_construct:1b}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_shield{CustomModelData:7,gl_construct:1b}
particle minecraft:dust 0.41 0.24 0.90 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.8
tag @s remove gl_user
