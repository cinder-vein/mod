function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_white = #serial gl_cfg
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/white
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/white
tag @s add gl_member_white
particle minecraft:dust 0.92 0.95 0.98 1.5 ~ ~1.2 ~ 0.4 0.6 0.4 0 60 force
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.6
tellraw @s [{"text":"Your White Lantern ring answers your call and forms on you. ","color":"#EBF2FA"},{"text":"The ring you left behind has gone dark.","color":"gray","italic":true}]
