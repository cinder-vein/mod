scoreboard players operation #v gl_tmp = @s gl_recall
scoreboard players set @s gl_recall 0
scoreboard players enable @s gl_recall
execute if score #v gl_tmp matches 1 run function greenlantern:recall/request
execute if score #v gl_tmp matches 11 run function greenlantern:recall/request_green
execute if score #v gl_tmp matches 12 run function greenlantern:recall/request_yellow
execute if score #v gl_tmp matches 13 run function greenlantern:recall/request_red
execute if score #v gl_tmp matches 14 run function greenlantern:recall/request_orange
execute if score #v gl_tmp matches 15 run function greenlantern:recall/request_blue
execute if score #v gl_tmp matches 16 run function greenlantern:recall/request_violet
execute if score #v gl_tmp matches 17 run function greenlantern:recall/request_indigo
execute if score #v gl_tmp matches 18 run function greenlantern:recall/request_white
execute if score #v gl_tmp matches 19 run function greenlantern:recall/request_black
