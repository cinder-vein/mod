tag @s add gl_shooter
execute anchored eyes positioned ^ ^ ^ run summon minecraft:marker ~ ~ ~ {Tags:["gl_v0"]}
execute anchored eyes positioned ^ ^ ^1 run summon minecraft:marker ~ ~ ~ {Tags:["gl_v1"]}
execute store result score #x0 gl_tmp run data get entity @e[type=minecraft:marker,tag=gl_v0,limit=1] Pos[0] 1000
execute store result score #x1 gl_tmp run data get entity @e[type=minecraft:marker,tag=gl_v1,limit=1] Pos[0] 1000
scoreboard players operation #x1 gl_tmp -= #x0 gl_tmp
execute store result score #y0 gl_tmp run data get entity @e[type=minecraft:marker,tag=gl_v0,limit=1] Pos[1] 1000
execute store result score #y1 gl_tmp run data get entity @e[type=minecraft:marker,tag=gl_v1,limit=1] Pos[1] 1000
scoreboard players operation #y1 gl_tmp -= #y0 gl_tmp
execute store result score #z0 gl_tmp run data get entity @e[type=minecraft:marker,tag=gl_v0,limit=1] Pos[2] 1000
execute store result score #z1 gl_tmp run data get entity @e[type=minecraft:marker,tag=gl_v1,limit=1] Pos[2] 1000
scoreboard players operation #z1 gl_tmp -= #z0 gl_tmp
execute as @e[type=palladium:custom_projectile,tag=gl_proj_new] run function greenlantern:construct/launch/1_6
kill @e[type=minecraft:marker,tag=gl_v0]
kill @e[type=minecraft:marker,tag=gl_v1]
tag @s remove gl_shooter
