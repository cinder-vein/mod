function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_yellow = #serial gl_cfg
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/yellow
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/yellow
execute if score #given gl_tmp matches 0 at @s run function greenlantern:ring/secure_drop
tag @s add gl_member_yellow
particle minecraft:dust 0.96 0.80 0.12 1.5 ~ ~1.2 ~ 0.4 0.6 0.4 0 60 force
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.6
tellraw @s [{"text":"Your Sinestro Corps ring answers your call and forms on you. ","color":"#F5CD1E"},{"text":"The ring you left behind has gone dark.","color":"gray","italic":true}]
