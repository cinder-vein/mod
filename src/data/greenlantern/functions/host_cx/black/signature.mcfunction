tag @s add gl_user
execute at @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] positioned ~ ~1 ~ run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_hand"],item:{id:"greenlantern:construct_hand",Count:1b,tag:{CustomModelData:9}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute at @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] positioned ~ ~1 ~ run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute as @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] at @s run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.03 40 force
execute rotated ~ 0 positioned ^ ^ ^1.5 run tp @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] ~ ~ ~
execute as @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] run damage @s 8 minecraft:magic by @p[tag=gl_user]
effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:wither 6 2 true
effect give @s minecraft:instant_health 1 0 true
playsound minecraft:entity.wither.shoot player @a[distance=..24] ~ ~ ~ 1 0.6
tag @s remove gl_user
