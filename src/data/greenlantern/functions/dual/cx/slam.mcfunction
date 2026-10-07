scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_melee_2] run function greenlantern:dual/run/green/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_melee_2] run function greenlantern:dual/run/yellow/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_melee_2] run function greenlantern:dual/run/red/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_melee_2] run function greenlantern:dual/run/orange/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_melee_2] run function greenlantern:dual/run/blue/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_melee_2] run function greenlantern:dual/run/violet/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_melee_2] run function greenlantern:dual/run/indigo/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_melee_2] run function greenlantern:dual/run/white/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_melee_2] run function greenlantern:dual/run/black/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_melee_2] run function greenlantern:dual/run/green/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_melee_2] run function greenlantern:dual/run/yellow/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_melee_2] run function greenlantern:dual/run/red/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_melee_2] run function greenlantern:dual/run/orange/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_melee_2] run function greenlantern:dual/run/blue/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_melee_2] run function greenlantern:dual/run/violet/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_melee_2] run function greenlantern:dual/run/indigo/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_melee_2] run function greenlantern:dual/run/white/slam
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_melee_2] run function greenlantern:dual/run/black/slam
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Hammer Slam isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Melee Constructs II","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
