function greenlantern:ring/store_owner
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/green
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/green
give @s greenlantern:green_power_battery
tag @s add gl_member_green
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Green Lantern Corps", "color": "#2EC846"}
particle minecraft:dust 0.18 0.78 0.27 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#2EC846"},{"text":" has been chosen by the Green Lantern Corps!","color":"white"}]
tellraw @s [{"text":"Your ring brought its Power Battery. ","color":"#2EC846"},{"text":"Right-click it (placed, or held in your hand) to recharge your ring.","color":"gray"}]
