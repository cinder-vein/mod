function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_red = #serial gl_cfg
tag @s remove gl_legacy_red
function greenlantern:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/red
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/red
execute if score #given gl_tmp matches 0 at @s run function greenlantern:ring/secure_drop
tag @s add gl_member_red
particle minecraft:dust 0.86 0.12 0.14 1.5 ~ ~1.2 ~ 0.4 0.6 0.4 0 60 force
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.6
tellraw @s [{"text":"Your Red Lantern ring answers your call and forms on you. ","color":"#DC1E23"},{"text":"The ring you left behind has gone dark.","color":"gray","italic":true}]
