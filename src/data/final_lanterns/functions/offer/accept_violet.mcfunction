function final_lanterns:ring/store_owner
function final_lanterns:ring/new_serial
scoreboard players operation @s gl_ser_violet = #serial gl_cfg
tag @s remove gl_legacy_violet
function final_lanterns:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot final_lanterns:rings/violet
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot final_lanterns:rings/violet
execute if score #given gl_tmp matches 0 at @s run function final_lanterns:ring/secure_drop
give @s kubejs:pinklanternbattery
tag @s add gl_member_violet
function final_lanterns:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Star Sapphires", "color": "#D737DC"}
particle minecraft:dust 0.84 0.22 0.86 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#D737DC"},{"text":" has been chosen by the Star Sapphires!","color":"white"}]
tellraw @s [{"text":"Your ring brought its lantern. ","color":"#D737DC"},{"text":"Wear the ring in your Lantern Ring slot; right-click the lantern (placed, or held in your hand) to recharge it.","color":"gray"}]
