tag @s add gl_user
execute rotated 0 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 0 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated 45 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 45 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated 90 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 90 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated 135 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 135 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated 180 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 180 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated 225 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 225 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated 270 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 270 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated 315 0 positioned ^ ^ ^3 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_spike"],item:{id:"greenlantern:construct_spike",Count:1b,tag:{CustomModelData:2}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute rotated 315 0 positioned ^ ^ ^3 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute as @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..5] run damage @s 10 minecraft:player_attack by @p[tag=gl_user]
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..5] minecraft:slowness 6 2 true
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..5] minecraft:darkness 6 0 true
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..5] minecraft:weakness 6 1 true
particle minecraft:dust 0.96 0.80 0.12 2.0 ~ ~0.5 ~ 3 0.5 3 0 150 force
playsound minecraft:block.pointed_dripstone.land player @a[distance=..24] ~ ~ ~ 1 0.6
playsound minecraft:entity.warden.sonic_charge player @a[distance=..24] ~ ~ ~ 1 1.4
tag @s remove gl_user
