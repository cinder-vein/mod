function greenlantern:ring/store_giver
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/giver_white
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/giver_white
