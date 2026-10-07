function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
execute if score #slot gl_tmp matches 0 run item modify entity @s container.0 greenlantern:bind
execute if score #slot gl_tmp matches 1 run item modify entity @s container.1 greenlantern:bind
execute if score #slot gl_tmp matches 2 run item modify entity @s container.2 greenlantern:bind
execute if score #slot gl_tmp matches 3 run item modify entity @s container.3 greenlantern:bind
execute if score #slot gl_tmp matches 4 run item modify entity @s container.4 greenlantern:bind
execute if score #slot gl_tmp matches 5 run item modify entity @s container.5 greenlantern:bind
execute if score #slot gl_tmp matches 6 run item modify entity @s container.6 greenlantern:bind
execute if score #slot gl_tmp matches 7 run item modify entity @s container.7 greenlantern:bind
execute if score #slot gl_tmp matches 8 run item modify entity @s container.8 greenlantern:bind
execute if score #slot gl_tmp matches 9 run item modify entity @s container.9 greenlantern:bind
execute if score #slot gl_tmp matches 10 run item modify entity @s container.10 greenlantern:bind
execute if score #slot gl_tmp matches 11 run item modify entity @s container.11 greenlantern:bind
execute if score #slot gl_tmp matches 12 run item modify entity @s container.12 greenlantern:bind
execute if score #slot gl_tmp matches 13 run item modify entity @s container.13 greenlantern:bind
execute if score #slot gl_tmp matches 14 run item modify entity @s container.14 greenlantern:bind
execute if score #slot gl_tmp matches 15 run item modify entity @s container.15 greenlantern:bind
execute if score #slot gl_tmp matches 16 run item modify entity @s container.16 greenlantern:bind
execute if score #slot gl_tmp matches 17 run item modify entity @s container.17 greenlantern:bind
execute if score #slot gl_tmp matches 18 run item modify entity @s container.18 greenlantern:bind
execute if score #slot gl_tmp matches 19 run item modify entity @s container.19 greenlantern:bind
execute if score #slot gl_tmp matches 20 run item modify entity @s container.20 greenlantern:bind
execute if score #slot gl_tmp matches 21 run item modify entity @s container.21 greenlantern:bind
execute if score #slot gl_tmp matches 22 run item modify entity @s container.22 greenlantern:bind
execute if score #slot gl_tmp matches 23 run item modify entity @s container.23 greenlantern:bind
execute if score #slot gl_tmp matches 24 run item modify entity @s container.24 greenlantern:bind
execute if score #slot gl_tmp matches 25 run item modify entity @s container.25 greenlantern:bind
execute if score #slot gl_tmp matches 26 run item modify entity @s container.26 greenlantern:bind
execute if score #slot gl_tmp matches 27 run item modify entity @s container.27 greenlantern:bind
execute if score #slot gl_tmp matches 28 run item modify entity @s container.28 greenlantern:bind
execute if score #slot gl_tmp matches 29 run item modify entity @s container.29 greenlantern:bind
execute if score #slot gl_tmp matches 30 run item modify entity @s container.30 greenlantern:bind
execute if score #slot gl_tmp matches 31 run item modify entity @s container.31 greenlantern:bind
execute if score #slot gl_tmp matches 32 run item modify entity @s container.32 greenlantern:bind
execute if score #slot gl_tmp matches 33 run item modify entity @s container.33 greenlantern:bind
execute if score #slot gl_tmp matches 34 run item modify entity @s container.34 greenlantern:bind
execute if score #slot gl_tmp matches 35 run item modify entity @s container.35 greenlantern:bind
execute if score #corps gl_tmp matches 1 run scoreboard players operation @s gl_ser_green = #serial gl_cfg
execute if score #corps gl_tmp matches 1 run tag @s remove gl_legacy_green
execute if score #corps gl_tmp matches 1 run tag @s add gl_member_green
execute if score #corps gl_tmp matches 2 run scoreboard players operation @s gl_ser_yellow = #serial gl_cfg
execute if score #corps gl_tmp matches 2 run tag @s remove gl_legacy_yellow
execute if score #corps gl_tmp matches 2 run tag @s add gl_member_yellow
execute if score #corps gl_tmp matches 3 run scoreboard players operation @s gl_ser_red = #serial gl_cfg
execute if score #corps gl_tmp matches 3 run tag @s remove gl_legacy_red
execute if score #corps gl_tmp matches 3 run tag @s add gl_member_red
execute if score #corps gl_tmp matches 4 run scoreboard players operation @s gl_ser_orange = #serial gl_cfg
execute if score #corps gl_tmp matches 4 run tag @s remove gl_legacy_orange
execute if score #corps gl_tmp matches 4 run tag @s add gl_member_orange
execute if score #corps gl_tmp matches 5 run scoreboard players operation @s gl_ser_blue = #serial gl_cfg
execute if score #corps gl_tmp matches 5 run tag @s remove gl_legacy_blue
execute if score #corps gl_tmp matches 5 run tag @s add gl_member_blue
execute if score #corps gl_tmp matches 6 run scoreboard players operation @s gl_ser_violet = #serial gl_cfg
execute if score #corps gl_tmp matches 6 run tag @s remove gl_legacy_violet
execute if score #corps gl_tmp matches 6 run tag @s add gl_member_violet
execute if score #corps gl_tmp matches 7 run scoreboard players operation @s gl_ser_indigo = #serial gl_cfg
execute if score #corps gl_tmp matches 7 run tag @s remove gl_legacy_indigo
execute if score #corps gl_tmp matches 7 run tag @s add gl_member_indigo
execute if score #corps gl_tmp matches 8 run scoreboard players operation @s gl_ser_white = #serial gl_cfg
execute if score #corps gl_tmp matches 8 run tag @s remove gl_legacy_white
execute if score #corps gl_tmp matches 8 run tag @s add gl_member_white
execute if score #corps gl_tmp matches 9 run scoreboard players operation @s gl_ser_black = #serial gl_cfg
execute if score #corps gl_tmp matches 9 run tag @s remove gl_legacy_black
execute if score #corps gl_tmp matches 9 run tag @s add gl_member_black
function greenlantern:ring/save_serials
tellraw @s [{"text":"The ring binds itself to you. Wear it in a ring slot to use its power.","color":"gray","italic":true}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
