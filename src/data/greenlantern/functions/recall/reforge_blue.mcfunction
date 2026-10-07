function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_blue = #serial gl_cfg
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/blue
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/blue
tag @s add gl_member_blue
particle minecraft:dust 0.16 0.51 1.00 1.5 ~ ~1.2 ~ 0.4 0.6 0.4 0 60 force
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.6
tellraw @s [{"text":"Your Blue Lantern ring answers your call and forms on you. ","color":"#2882FF"},{"text":"The ring you left behind has gone dark.","color":"gray","italic":true}]
