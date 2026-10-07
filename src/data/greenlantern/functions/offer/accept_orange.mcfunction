function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_orange = #serial gl_cfg
tag @s remove gl_legacy_orange
function greenlantern:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/orange
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/orange
execute if score #given gl_tmp matches 0 at @s run function greenlantern:ring/secure_drop
give @s greenlantern:orange_power_battery
tag @s add gl_member_orange
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Orange Lanterns", "color": "#FA8214"}
particle minecraft:dust 0.98 0.51 0.08 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#FA8214"},{"text":" has been chosen by the Orange Lanterns!","color":"white"}]
tellraw @s [{"text":"Your ring brought its Power Battery. ","color":"#FA8214"},{"text":"Right-click it (placed, or held in your hand) to recharge your ring.","color":"gray"}]
