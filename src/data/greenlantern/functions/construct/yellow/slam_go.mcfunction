energybar value subtract @s greenlantern:yellow_lantern ring_charge 120
scoreboard players set @s gl_cc_slam 80
tag @s add gl_user
execute positioned ~ ~3.4 ~ run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_hammer"],item:{id:"greenlantern:construct_hammer",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute positioned ~ ~3.4 ~ run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
particle minecraft:dust 0.96 0.80 0.12 2.5 ~ ~0.2 ~ 3 0.2 3 0 200 force
execute as @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,type=!minecraft:marker,type=!minecraft:item_display,type=!minecraft:block_display,type=!minecraft:text_display,type=!minecraft:interaction,type=!palladium:custom_projectile,tag=!gl_user,distance=..6] run damage @s 8 minecraft:player_attack by @p[tag=gl_user]
effect give @e[type=!minecraft:item,type=!minecraft:experience_orb,type=!minecraft:armor_stand,type=!minecraft:marker,type=!minecraft:item_display,type=!minecraft:block_display,type=!minecraft:text_display,type=!minecraft:interaction,type=!palladium:custom_projectile,tag=!gl_user,distance=..6] minecraft:levitation 1 5 true
playsound minecraft:entity.generic.explode player @a[distance=..24] ~ ~ ~ 1 1.2
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Hammer Slam","color":"#F5CD1E"}]
