scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_defense_2] run function greenlantern:dual/run/green/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_defense_2] run function greenlantern:dual/run/yellow/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_defense_2] run function greenlantern:dual/run/red/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_defense_2] run function greenlantern:dual/run/orange/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_defense_2] run function greenlantern:dual/run/blue/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_defense_2] run function greenlantern:dual/run/violet/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_defense_2] run function greenlantern:dual/run/indigo/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_defense_2] run function greenlantern:dual/run/white/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_defense_2] run function greenlantern:dual/run/black/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_defense_2] run function greenlantern:dual/run/green/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_defense_2] run function greenlantern:dual/run/yellow/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_defense_2] run function greenlantern:dual/run/red/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_defense_2] run function greenlantern:dual/run/orange/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_defense_2] run function greenlantern:dual/run/blue/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_defense_2] run function greenlantern:dual/run/violet/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_defense_2] run function greenlantern:dual/run/indigo/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_defense_2] run function greenlantern:dual/run/white/dome
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_defense_2] run function greenlantern:dual/run/black/dome
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Dome isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Defense Constructs II","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
