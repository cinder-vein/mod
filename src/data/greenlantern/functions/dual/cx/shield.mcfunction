scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_constructs] run function greenlantern:dual/run/green/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_constructs] run function greenlantern:dual/run/yellow/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_constructs] run function greenlantern:dual/run/red/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_constructs] run function greenlantern:dual/run/orange/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_constructs] run function greenlantern:dual/run/blue/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_constructs] run function greenlantern:dual/run/violet/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_constructs] run function greenlantern:dual/run/indigo/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_constructs] run function greenlantern:dual/run/white/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_constructs] run function greenlantern:dual/run/black/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_constructs] run function greenlantern:dual/run/green/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_constructs] run function greenlantern:dual/run/yellow/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_constructs] run function greenlantern:dual/run/red/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_constructs] run function greenlantern:dual/run/orange/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_constructs] run function greenlantern:dual/run/blue/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_constructs] run function greenlantern:dual/run/violet/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_constructs] run function greenlantern:dual/run/indigo/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_constructs] run function greenlantern:dual/run/white/shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_constructs] run function greenlantern:dual/run/black/shield
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Tower Shield isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Constructs","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
