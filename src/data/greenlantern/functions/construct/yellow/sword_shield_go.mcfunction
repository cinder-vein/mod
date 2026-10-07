energybar value subtract @s greenlantern:yellow_lantern ring_charge 50
scoreboard players set @s gl_cc_sword_shield 10
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Sword & Shield","color":"#F5CD1E"}]
tag @s add gl_user
function greenlantern:construct/free_main
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:construct_sword{CustomModelData:2,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_sword{CustomModelData:2,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run tellraw @s [{"text":"Your ring is in that hand, so the construct formed in your inventory. Wear the ring in a Curios ring slot (or the other hand) to wield constructs.","color":"gray","italic":true}]
function greenlantern:construct/free_off
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.offhand with greenlantern:construct_shield{CustomModelData:2,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_shield{CustomModelData:2,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run tellraw @s [{"text":"Your ring is in that hand, so the construct formed in your inventory. Wear the ring in a Curios ring slot (or the other hand) to wield constructs.","color":"gray","italic":true}]
particle minecraft:dust 0.96 0.80 0.12 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.8
tag @s remove gl_user
