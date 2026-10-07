scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_ranged_1] run function greenlantern:dual/run/green/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_ranged_1] run function greenlantern:dual/run/yellow/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_ranged_1] run function greenlantern:dual/run/red/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_ranged_1] run function greenlantern:dual/run/orange/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_ranged_1] run function greenlantern:dual/run/blue/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_ranged_1] run function greenlantern:dual/run/violet/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_ranged_1] run function greenlantern:dual/run/indigo/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_ranged_1] run function greenlantern:dual/run/white/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_ranged_1] run function greenlantern:dual/run/black/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_ranged_1] run function greenlantern:dual/run/green/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_ranged_1] run function greenlantern:dual/run/yellow/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_ranged_1] run function greenlantern:dual/run/red/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_ranged_1] run function greenlantern:dual/run/orange/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_ranged_1] run function greenlantern:dual/run/blue/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_ranged_1] run function greenlantern:dual/run/violet/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_ranged_1] run function greenlantern:dual/run/indigo/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_ranged_1] run function greenlantern:dual/run/white/gatling
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_ranged_1] run function greenlantern:dual/run/black/gatling
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Gatling isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Ranged Constructs I","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
