scoreboard players set #d gl_tmp 0
execute if score #d gl_tmp matches 0 anchored eyes positioned ^ ^ ^1 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 1
execute if score #d gl_tmp matches 1 anchored eyes positioned ^ ^ ^2 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 2
execute if score #d gl_tmp matches 2 anchored eyes positioned ^ ^ ^3 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 3
execute if score #d gl_tmp matches 3 anchored eyes positioned ^ ^ ^4 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 4
execute if score #d gl_tmp matches 4 anchored eyes positioned ^ ^ ^5 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 5
execute if score #d gl_tmp matches 5 anchored eyes positioned ^ ^ ^6 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 6
execute if score #d gl_tmp matches 6 anchored eyes positioned ^ ^ ^7 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 7
execute if score #d gl_tmp matches 7 anchored eyes positioned ^ ^ ^8 if block ~ ~ ~ #minecraft:replaceable if block ~ ~-1 ~ #minecraft:replaceable run scoreboard players set #d gl_tmp 8
execute if score #d gl_tmp matches 1 anchored eyes positioned ^ ^ ^1 run tp @s ~ ~-1.62 ~
execute if score #d gl_tmp matches 2 anchored eyes positioned ^ ^ ^2 run tp @s ~ ~-1.62 ~
execute if score #d gl_tmp matches 3 anchored eyes positioned ^ ^ ^3 run tp @s ~ ~-1.62 ~
execute if score #d gl_tmp matches 4 anchored eyes positioned ^ ^ ^4 run tp @s ~ ~-1.62 ~
execute if score #d gl_tmp matches 5 anchored eyes positioned ^ ^ ^5 run tp @s ~ ~-1.62 ~
execute if score #d gl_tmp matches 6 anchored eyes positioned ^ ^ ^6 run tp @s ~ ~-1.62 ~
execute if score #d gl_tmp matches 7 anchored eyes positioned ^ ^ ^7 run tp @s ~ ~-1.62 ~
execute if score #d gl_tmp matches 8 anchored eyes positioned ^ ^ ^8 run tp @s ~ ~-1.62 ~
particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force
playsound minecraft:entity.ender_dragon.flap player @a[distance=..24] ~ ~ ~ 1 1.6
