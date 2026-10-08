function final_lanterns:ring/store_owner
function final_lanterns:ring/new_serial
scoreboard players operation @s gl_ser_red = #serial gl_cfg
tag @s remove gl_legacy_red
function final_lanterns:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot final_lanterns:rings/red
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot final_lanterns:rings/red
execute if score #given gl_tmp matches 0 at @s run function final_lanterns:ring/secure_drop
give @s kubejs:redlanternbattery
tag @s add gl_member_red
function final_lanterns:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Red Lantern Corps", "color": "#DC1E23"}
particle minecraft:dust 0.86 0.12 0.14 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#DC1E23"},{"text":" has been chosen by the Red Lantern Corps!","color":"white"}]
tellraw @s [{"text":"Your ring brought its lantern. ","color":"#DC1E23"},{"text":"Wear the ring in your Lantern Ring slot; right-click the lantern (placed, or held in your hand) to recharge it.","color":"gray"}]
