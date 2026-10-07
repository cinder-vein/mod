function greenlantern:ring/store_owner
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/indigo
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/indigo
tag @s add gl_member_indigo
