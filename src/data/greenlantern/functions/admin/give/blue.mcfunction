function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_blue = #serial gl_cfg
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/blue
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/blue
tag @s add gl_member_blue
