function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_blue = #serial gl_cfg
tag @s remove gl_legacy_blue
function greenlantern:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/blue
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/blue
execute if score #given gl_tmp matches 0 at @s run function greenlantern:ring/secure_drop
give @s greenlantern:blue_power_battery
tag @s add gl_member_blue
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Blue Lantern Corps", "color": "#2882FF"}
particle minecraft:dust 0.16 0.51 1.00 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#2882FF"},{"text":" has been chosen by the Blue Lantern Corps!","color":"white"}]
tellraw @s [{"text":"Your ring brought its Power Battery. ","color":"#2882FF"},{"text":"Right-click it (placed, or held in your hand) to recharge your ring.","color":"gray"}]
