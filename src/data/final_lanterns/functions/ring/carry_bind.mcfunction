function final_lanterns:ring/store_owner
function final_lanterns:ring/new_serial
execute if score #slot gl_tmp matches 0 run item modify entity @s container.0 final_lanterns:bind
execute if score #slot gl_tmp matches 1 run item modify entity @s container.1 final_lanterns:bind
execute if score #slot gl_tmp matches 2 run item modify entity @s container.2 final_lanterns:bind
execute if score #slot gl_tmp matches 3 run item modify entity @s container.3 final_lanterns:bind
execute if score #slot gl_tmp matches 4 run item modify entity @s container.4 final_lanterns:bind
execute if score #slot gl_tmp matches 5 run item modify entity @s container.5 final_lanterns:bind
execute if score #slot gl_tmp matches 6 run item modify entity @s container.6 final_lanterns:bind
execute if score #slot gl_tmp matches 7 run item modify entity @s container.7 final_lanterns:bind
execute if score #slot gl_tmp matches 8 run item modify entity @s container.8 final_lanterns:bind
execute if score #slot gl_tmp matches 9 run item modify entity @s container.9 final_lanterns:bind
execute if score #slot gl_tmp matches 10 run item modify entity @s container.10 final_lanterns:bind
execute if score #slot gl_tmp matches 11 run item modify entity @s container.11 final_lanterns:bind
execute if score #slot gl_tmp matches 12 run item modify entity @s container.12 final_lanterns:bind
execute if score #slot gl_tmp matches 13 run item modify entity @s container.13 final_lanterns:bind
execute if score #slot gl_tmp matches 14 run item modify entity @s container.14 final_lanterns:bind
execute if score #slot gl_tmp matches 15 run item modify entity @s container.15 final_lanterns:bind
execute if score #slot gl_tmp matches 16 run item modify entity @s container.16 final_lanterns:bind
execute if score #slot gl_tmp matches 17 run item modify entity @s container.17 final_lanterns:bind
execute if score #slot gl_tmp matches 18 run item modify entity @s container.18 final_lanterns:bind
execute if score #slot gl_tmp matches 19 run item modify entity @s container.19 final_lanterns:bind
execute if score #slot gl_tmp matches 20 run item modify entity @s container.20 final_lanterns:bind
execute if score #slot gl_tmp matches 21 run item modify entity @s container.21 final_lanterns:bind
execute if score #slot gl_tmp matches 22 run item modify entity @s container.22 final_lanterns:bind
execute if score #slot gl_tmp matches 23 run item modify entity @s container.23 final_lanterns:bind
execute if score #slot gl_tmp matches 24 run item modify entity @s container.24 final_lanterns:bind
execute if score #slot gl_tmp matches 25 run item modify entity @s container.25 final_lanterns:bind
execute if score #slot gl_tmp matches 26 run item modify entity @s container.26 final_lanterns:bind
execute if score #slot gl_tmp matches 27 run item modify entity @s container.27 final_lanterns:bind
execute if score #slot gl_tmp matches 28 run item modify entity @s container.28 final_lanterns:bind
execute if score #slot gl_tmp matches 29 run item modify entity @s container.29 final_lanterns:bind
execute if score #slot gl_tmp matches 30 run item modify entity @s container.30 final_lanterns:bind
execute if score #slot gl_tmp matches 31 run item modify entity @s container.31 final_lanterns:bind
execute if score #slot gl_tmp matches 32 run item modify entity @s container.32 final_lanterns:bind
execute if score #slot gl_tmp matches 33 run item modify entity @s container.33 final_lanterns:bind
execute if score #slot gl_tmp matches 34 run item modify entity @s container.34 final_lanterns:bind
execute if score #slot gl_tmp matches 35 run item modify entity @s container.35 final_lanterns:bind
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
function final_lanterns:ring/save_serials
tellraw @s [{"text":"The ring binds itself to you. Wear it in a ring slot to use its power.","color":"gray","italic":true}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
