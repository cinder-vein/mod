function greenlantern:ring/store_giver
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/giver_yellow
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/giver_yellow
execute if score #given gl_tmp matches 0 at @s run data merge entity @e[type=minecraft:item,distance=..1.5,nbt={Item:{tag:{gl_gv:1b}}},limit=1,sort=nearest] {Age:-32768s}
