scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_green,tag=gl_u_green_signature] run function greenlantern:dual/run/green/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_yellow,tag=gl_u_yellow_signature] run function greenlantern:dual/run/yellow/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_red,tag=gl_u_red_signature] run function greenlantern:dual/run/red/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_orange,tag=gl_u_orange_signature] run function greenlantern:dual/run/orange/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_blue,tag=gl_u_blue_signature] run function greenlantern:dual/run/blue/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_violet,tag=gl_u_violet_signature] run function greenlantern:dual/run/violet/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_indigo,tag=gl_u_indigo_signature] run function greenlantern:dual/run/indigo/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_white,tag=gl_u_white_signature] run function greenlantern:dual/run/white/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p1_black,tag=gl_u_black_signature] run function greenlantern:dual/run/black/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_green,tag=gl_u_green_signature] run function greenlantern:dual/run/green/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_yellow,tag=gl_u_yellow_signature] run function greenlantern:dual/run/yellow/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_red,tag=gl_u_red_signature] run function greenlantern:dual/run/red/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_orange,tag=gl_u_orange_signature] run function greenlantern:dual/run/orange/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_blue,tag=gl_u_blue_signature] run function greenlantern:dual/run/blue/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_violet,tag=gl_u_violet_signature] run function greenlantern:dual/run/violet/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_indigo,tag=gl_u_indigo_signature] run function greenlantern:dual/run/indigo/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_white,tag=gl_u_white_signature] run function greenlantern:dual/run/white/signature
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_p2_black,tag=gl_u_black_signature] run function greenlantern:dual/run/black/signature
execute if score #done gl_tmp matches 0 run title @s actionbar [{"text":"Neither ring's signature construct is unlocked yet (all four construct branches).","color":"gray"}]
