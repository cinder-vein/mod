scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_defense_1] run function greenlantern:dual/run/green/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_defense_1] run function greenlantern:dual/run/yellow/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_defense_1] run function greenlantern:dual/run/red/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_defense_1] run function greenlantern:dual/run/orange/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_defense_1] run function greenlantern:dual/run/blue/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_defense_1] run function greenlantern:dual/run/violet/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_defense_1] run function greenlantern:dual/run/indigo/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_defense_1] run function greenlantern:dual/run/white/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_defense_1] run function greenlantern:dual/run/black/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_defense_1] run function greenlantern:dual/run/green/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_defense_1] run function greenlantern:dual/run/yellow/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_defense_1] run function greenlantern:dual/run/red/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_defense_1] run function greenlantern:dual/run/orange/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_defense_1] run function greenlantern:dual/run/blue/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_defense_1] run function greenlantern:dual/run/violet/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_defense_1] run function greenlantern:dual/run/indigo/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_defense_1] run function greenlantern:dual/run/white/cage
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_defense_1] run function greenlantern:dual/run/black/cage
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Cage isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Defense Constructs I","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
