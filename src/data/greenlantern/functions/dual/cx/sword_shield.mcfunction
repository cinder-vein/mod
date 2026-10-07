scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_melee_1] run function greenlantern:dual/run/green/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_melee_1] run function greenlantern:dual/run/yellow/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_melee_1] run function greenlantern:dual/run/red/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_melee_1] run function greenlantern:dual/run/orange/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_melee_1] run function greenlantern:dual/run/blue/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_melee_1] run function greenlantern:dual/run/violet/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_melee_1] run function greenlantern:dual/run/indigo/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_melee_1] run function greenlantern:dual/run/white/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_melee_1] run function greenlantern:dual/run/black/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_melee_1] run function greenlantern:dual/run/green/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_melee_1] run function greenlantern:dual/run/yellow/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_melee_1] run function greenlantern:dual/run/red/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_melee_1] run function greenlantern:dual/run/orange/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_melee_1] run function greenlantern:dual/run/blue/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_melee_1] run function greenlantern:dual/run/violet/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_melee_1] run function greenlantern:dual/run/indigo/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_melee_1] run function greenlantern:dual/run/white/sword_shield
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_melee_1] run function greenlantern:dual/run/black/sword_shield
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Sword & Shield isn't unlocked in either ring yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"white"},{"text":" in a ring's powers menu.","color":"gray"}]
