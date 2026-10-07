scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_constructs] run function greenlantern:dual/run/green/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_constructs] run function greenlantern:dual/run/yellow/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_constructs] run function greenlantern:dual/run/red/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_constructs] run function greenlantern:dual/run/orange/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_constructs] run function greenlantern:dual/run/blue/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_constructs] run function greenlantern:dual/run/violet/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_constructs] run function greenlantern:dual/run/indigo/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_constructs] run function greenlantern:dual/run/white/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_constructs] run function greenlantern:dual/run/black/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_constructs] run function greenlantern:dual/run/green/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_constructs] run function greenlantern:dual/run/yellow/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_constructs] run function greenlantern:dual/run/red/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_constructs] run function greenlantern:dual/run/orange/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_constructs] run function greenlantern:dual/run/blue/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_constructs] run function greenlantern:dual/run/violet/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_constructs] run function greenlantern:dual/run/indigo/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_constructs] run function greenlantern:dual/run/white/blocks
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_constructs] run function greenlantern:dual/run/black/blocks
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Construct Blocks isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Constructs","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
