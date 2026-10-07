function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_yellow = #serial gl_cfg
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/yellow
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/yellow
execute if score #given gl_tmp matches 0 at @s run function greenlantern:ring/secure_drop
give @s greenlantern:yellow_power_battery
tag @s add gl_member_yellow
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Sinestro Corps", "color": "#F5CD1E"}
particle minecraft:dust 0.96 0.80 0.12 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#F5CD1E"},{"text":" has been chosen by the Sinestro Corps!","color":"white"}]
tellraw @s [{"text":"Your ring brought its Power Battery. ","color":"#F5CD1E"},{"text":"Right-click it (placed, or held in your hand) to recharge your ring.","color":"gray"}]
