energybar value subtract @s greenlantern:orange_lantern ring_charge 200
scoreboard players set @s gl_cc_signature 200
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Grasping Hands","color":"#FA8214"}]
tag @s add gl_user
execute anchored eyes positioned ^ ^-0.4 ^2 run summon minecraft:item_display ~ ~ ~ {Tags:["gl_construct","gl_new","gl_hand"],item:{id:"greenlantern:construct_hand",Count:1b,tag:{CustomModelData:4}},item_display:"none",brightness:{sky:15,block:15},view_range:2f,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.2f,0.2f,0.2f]}}
execute anchored eyes positioned ^ ^-0.4 ^2 run tp @e[type=minecraft:item_display,tag=gl_new,limit=1,sort=nearest] ~ ~ ~ ~ 0
execute at @e[type=#greenlantern:greed_prey,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..14] run particle minecraft:dust 0.98 0.51 0.08 1.5 ~ ~1 ~ 0.3 0.6 0.3 0 20 force
execute rotated ~ 0 positioned ^ ^ ^2 run tp @e[type=#greenlantern:greed_prey,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..14] ~ ~ ~
effect give @e[type=#greenlantern:greed_prey,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..4] minecraft:weakness 8 1 true
effect give @e[type=#greenlantern:greed_prey,tag=!gl_greed_minion,tag=!gl_dead_minion,distance=..4] minecraft:slowness 8 1 true
playsound minecraft:entity.evoker.cast_spell player @a[distance=..24] ~ ~ ~ 1 0.7
playsound minecraft:item.armor.equip_chain player @a[distance=..24] ~ ~ ~ 1 0.6
tag @s remove gl_user
