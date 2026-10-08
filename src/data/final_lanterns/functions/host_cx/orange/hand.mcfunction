execute at @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] positioned ~ ~1 ~ run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_hand"],item:{id:"final_lanterns:construct_hand",Count:1b,tag:{CustomModelData:4}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute at @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] positioned ~ ~1 ~ run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute rotated ~ 0 positioned ^ ^ ^2 run tp @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] ~ ~ ~
execute as @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] at @s run particle minecraft:dust 0.98 0.51 0.08 2.0 ~ ~1 ~ 0.6 1.0 0.6 0 120 force
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:slowness 8 255 true
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:jump_boost 8 250 true
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:mining_fatigue 8 4 true
effect give @e[type=!#final_lanterns:not_creatures,tag=!gl_user,tag=!gl_dead_minion,distance=..12,limit=1,sort=nearest] minecraft:glowing 8 0 true
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 0.8
