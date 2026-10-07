function greenlantern:ring/curios_pop
particle minecraft:end_rod ~ ~1 ~ 0.2 0.2 0.2 0.05 20 force
tellraw @s [{"text":"This ring has already chosen its bearer. It returns to them.","color":"gray","italic":true}]
playsound minecraft:entity.enderman.teleport player @a[distance=..16] ~ ~ ~ 1 1.4
execute as @a if score @s gl_id = #owner gl_tmp at @s run function greenlantern:ring/return_to_owner
tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject
