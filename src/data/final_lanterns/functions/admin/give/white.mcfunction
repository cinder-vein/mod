function final_lanterns:ring/store_owner
function final_lanterns:ring/new_serial
scoreboard players operation @s gl_ser_white = #serial gl_cfg
tag @s remove gl_legacy_white
function final_lanterns:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot final_lanterns:rings/white
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot final_lanterns:rings/white
execute if score #given gl_tmp matches 0 at @s run function final_lanterns:ring/secure_drop
tag @s add gl_member_white
