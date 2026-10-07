energybar value subtract @s greenlantern:white_lantern ring_charge 30
scoreboard players set @s gl_cc_sword 10
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Sword","color":"#EBF2FA"}]
tag @s add gl_user
function greenlantern:construct/free_main
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:construct_sword{CustomModelData:8,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_sword{CustomModelData:8,Unbreakable:1b,gl_construct:1b,HideFlags:4}
execute if score #free gl_tmp matches 0 run tellraw @s [{"text":"Your ring is in that hand, so the construct formed in your inventory. Wear the ring in a Curios ring slot (or the other hand) to wield constructs.","color":"gray","italic":true}]
particle minecraft:dust 0.92 0.95 0.98 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.8
tag @s remove gl_user
