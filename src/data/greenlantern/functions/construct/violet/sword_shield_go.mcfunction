energybar value subtract @s greenlantern:violet_lantern ring_charge 50
scoreboard players set @s gl_cc_sword_shield 10
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Sword & Shield","color":"#D737DC"}]
tag @s add gl_user
function greenlantern:construct/free_main
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:construct_sword{CustomModelData:6,gl_construct:1b}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_sword{CustomModelData:6,gl_construct:1b}
function greenlantern:construct/free_off
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.offhand with greenlantern:construct_shield{CustomModelData:6,gl_construct:1b}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_shield{CustomModelData:6,gl_construct:1b}
particle minecraft:dust 0.84 0.22 0.86 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.8
tag @s remove gl_user
