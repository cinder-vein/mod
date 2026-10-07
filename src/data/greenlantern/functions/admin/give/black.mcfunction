function greenlantern:ring/store_owner
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/black
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/black
tag @s add gl_member_black
