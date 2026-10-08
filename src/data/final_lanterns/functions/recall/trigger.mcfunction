scoreboard players operation #v gl_tmp = @s gl_recall
scoreboard players set @s gl_recall 0
scoreboard players enable @s gl_recall
execute if score #v gl_tmp matches 1 run function final_lanterns:recall/request
execute if score #v gl_tmp matches 11 run function final_lanterns:recall/request_green
execute if score #v gl_tmp matches 12 run function final_lanterns:recall/request_yellow
execute if score #v gl_tmp matches 13 run function final_lanterns:recall/request_red
execute if score #v gl_tmp matches 14 run function final_lanterns:recall/request_orange
execute if score #v gl_tmp matches 15 run function final_lanterns:recall/request_blue
execute if score #v gl_tmp matches 16 run function final_lanterns:recall/request_violet
execute if score #v gl_tmp matches 17 run function final_lanterns:recall/request_indigo
execute if score #v gl_tmp matches 18 run function final_lanterns:recall/request_white
execute if score #v gl_tmp matches 19 run function final_lanterns:recall/request_black
execute unless score #v gl_tmp matches 1 unless score #v gl_tmp matches 11..19 run tellraw @s [{"text":"/trigger gl_recall calls all your rings. One ring: /trigger gl_recall set 11 (green), 12 (yellow), 13 (red), 14 (orange), 15 (blue), 16 (violet), 17 (indigo), 18 (white), 19 (black)","color":"gray"}]
