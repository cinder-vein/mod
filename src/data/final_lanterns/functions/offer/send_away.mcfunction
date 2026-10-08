scoreboard players operation #cur gl_id = @s gl_id
execute as @e[type=minecraft:item_display,tag=gl_offer_disp] if score @s gl_id = #cur gl_id at @s run summon minecraft:item_display ~ ~ ~ {Tags:["gl_leaving","gl_leave_new"],billboard:"center",brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
execute as @e[type=minecraft:item_display,tag=gl_offer_disp] if score @s gl_id = #cur gl_id run data modify entity @e[type=minecraft:item_display,tag=gl_leave_new,limit=1,sort=nearest] item set from entity @s item
scoreboard players set @e[type=minecraft:item_display,tag=gl_leave_new] gl_tmp 30
tag @e[type=minecraft:item_display,tag=gl_leave_new] add gl_leave_go
tag @e[type=minecraft:item_display,tag=gl_leave_new] remove gl_leave_new
