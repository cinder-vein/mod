energybar value subtract @s greenlantern:red_lantern ring_charge 100
scoreboard players set @s gl_cc_fist 60
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Giant Fist","color":"#DC1E23"}]
tag @s add gl_user
execute anchored eyes positioned ^ ^-0.4 ^2.6 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_claw"],item:{id:"greenlantern:construct_claw",Count:1b,tag:{CustomModelData:3}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute anchored eyes positioned ^ ^-0.4 ^2.6 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute anchored eyes positioned ^ ^ ^3 run particle minecraft:dust 0.86 0.12 0.14 2.5 ~ ~ ~ 0.8 0.8 0.8 0 60 force
execute anchored eyes positioned ^ ^ ^3 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..2.5] run damage @s 12 minecraft:player_attack by @p[tag=gl_user]
execute anchored eyes positioned ^ ^ ^3 run effect give @e[type=!#greenlantern:not_creatures,tag=!gl_user,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..2.5] minecraft:levitation 1 3 true
playsound minecraft:entity.iron_golem.attack player @a[distance=..24] ~ ~ ~ 1 0.6
tag @s remove gl_user
