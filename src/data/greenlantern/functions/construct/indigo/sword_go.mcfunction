energybar value subtract @s greenlantern:indigo_lantern ring_charge 30
scoreboard players set @s gl_cc_sword 10
tag @s add gl_user
function greenlantern:construct/free_main
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:construct_sword{CustomModelData:7,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_sword{CustomModelData:7,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run tellraw @s [{"text":"Your hand is busy, so the construct formed in your inventory.","color":"gray","italic":true}]
particle minecraft:dust 0.41 0.24 0.90 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.8
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Sword","color":"#693CE6"}]
