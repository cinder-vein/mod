energybar value subtract @s greenlantern:blue_lantern ring_charge 150
scoreboard players set @s gl_cc_cage 100
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Cage","color":"#2882FF"}]
tag @s add gl_user
execute at @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] positioned ~ ~1 ~ run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_cage"],item:{id:"greenlantern:construct_cage",Count:1b,tag:{CustomModelData:5}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute at @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] positioned ~ ~1 ~ run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute as @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] at @s run particle minecraft:dust 0.16 0.51 1.00 2.0 ~ ~1 ~ 0.6 1.0 0.6 0 120 force
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:slowness 6 6 true
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:weakness 6 2 true
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:glowing 6 0 true
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 0.8
tag @s remove gl_user
