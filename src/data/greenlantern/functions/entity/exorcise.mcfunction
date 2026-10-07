tag @s add gl_exorcist
tag @a remove gl_exo_target
scoreboard players set #hit gl_tmp 0
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^1.0 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^1.5 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^2.0 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^2.5 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^3.0 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^3.5 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^4.0 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^4.5 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^5.0 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^5.5 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 anchored eyes positioned ^ ^ ^6.0 positioned ~ ~-0.9 ~ as @a[tag=gl_host,tag=!gl_exorcist,distance=..1.1,limit=1,sort=nearest] run function greenlantern:entity/exorcise_hit
execute if score #hit gl_tmp matches 0 run scoreboard players set @s gl_exo 0
execute if score #hit gl_tmp matches 1 run scoreboard players add @s gl_exo 1
execute if score #hit gl_tmp matches 1 at @a[tag=gl_exo_target] run particle minecraft:end_rod ~ ~1 ~ 0.4 0.8 0.4 0.05 6 force
execute if score #hit gl_tmp matches 1 run particle minecraft:enchant ~ ~1.2 ~ 0.3 0.3 0.3 1 12 force
execute if score #hit gl_tmp matches 1 run title @s actionbar [{"text":"Drawing the entity out... ","color":"gold"},{"score":{"name":"@s","objective":"gl_exo"},"color":"white"},{"text":"/100","color":"gray"}]
execute if score #hit gl_tmp matches 1 as @a[tag=gl_exo_target] run title @s actionbar [{"text":"Someone is drawing your entity out with a lantern! Get away!","color":"red"}]
execute if score @s gl_exo matches 100.. run function greenlantern:entity/exorcise_done
tag @s remove gl_exorcist
