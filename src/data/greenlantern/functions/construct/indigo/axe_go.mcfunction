energybar value subtract @s greenlantern:indigo_lantern ring_charge 40
scoreboard players set @s gl_cc_axe 10
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Battle Axe","color":"#693CE6"}]
tag @s add gl_user
function greenlantern:construct/free_main
execute if score #free gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:construct_axe{CustomModelData:7,gl_construct:1b}
execute if score #free gl_tmp matches 0 run give @s greenlantern:construct_axe{CustomModelData:7,gl_construct:1b}
execute if score #free gl_tmp matches 0 run tellraw @s [{"text":"Your ring is in that hand, so the construct formed in your inventory. Wear the ring in a Curios ring slot (or the other hand) to wield constructs.","color":"gray","italic":true}]
particle minecraft:dust 0.41 0.24 0.90 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.8
tag @s remove gl_user
