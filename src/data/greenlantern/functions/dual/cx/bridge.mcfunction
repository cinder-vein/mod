scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_utility_2] run function greenlantern:dual/run/green/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_utility_2] run function greenlantern:dual/run/yellow/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_utility_2] run function greenlantern:dual/run/red/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_utility_2] run function greenlantern:dual/run/orange/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_utility_2] run function greenlantern:dual/run/blue/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_utility_2] run function greenlantern:dual/run/violet/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_utility_2] run function greenlantern:dual/run/indigo/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_utility_2] run function greenlantern:dual/run/white/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_utility_2] run function greenlantern:dual/run/black/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_utility_2] run function greenlantern:dual/run/green/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_utility_2] run function greenlantern:dual/run/yellow/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_utility_2] run function greenlantern:dual/run/red/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_utility_2] run function greenlantern:dual/run/orange/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_utility_2] run function greenlantern:dual/run/blue/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_utility_2] run function greenlantern:dual/run/violet/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_utility_2] run function greenlantern:dual/run/indigo/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_utility_2] run function greenlantern:dual/run/white/bridge
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_utility_2] run function greenlantern:dual/run/black/bridge
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Bridge isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Utility Constructs II","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
