function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
scoreboard players operation @s gl_ser_green = #serial gl_cfg
tag @s remove gl_legacy_green
function greenlantern:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/green
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/green
execute if score #given gl_tmp matches 0 at @s run function greenlantern:ring/secure_drop
tag @s add gl_member_green
