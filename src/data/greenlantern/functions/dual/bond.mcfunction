superpower add greenlantern:spectrum_lantern @s
tag @s add gl_dual
scoreboard players set @s gl_dlast -1
execute if entity @s[tag=gl_p1_green,tag=gl_p2_yellow] run function greenlantern:dual/hello/green_yellow
execute if entity @s[tag=gl_p1_green,tag=gl_p2_red] run function greenlantern:dual/hello/green_red
execute if entity @s[tag=gl_p1_green,tag=gl_p2_orange] run function greenlantern:dual/hello/green_orange
execute if entity @s[tag=gl_p1_green,tag=gl_p2_blue] run function greenlantern:dual/hello/green_blue
execute if entity @s[tag=gl_p1_green,tag=gl_p2_violet] run function greenlantern:dual/hello/green_violet
execute if entity @s[tag=gl_p1_green,tag=gl_p2_indigo] run function greenlantern:dual/hello/green_indigo
execute if entity @s[tag=gl_p1_green,tag=gl_p2_white] run function greenlantern:dual/hello/green_white
execute if entity @s[tag=gl_p1_green,tag=gl_p2_black] run function greenlantern:dual/hello/green_black
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_red] run function greenlantern:dual/hello/yellow_red
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_orange] run function greenlantern:dual/hello/yellow_orange
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_blue] run function greenlantern:dual/hello/yellow_blue
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_violet] run function greenlantern:dual/hello/yellow_violet
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_indigo] run function greenlantern:dual/hello/yellow_indigo
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_white] run function greenlantern:dual/hello/yellow_white
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_black] run function greenlantern:dual/hello/yellow_black
execute if entity @s[tag=gl_p1_red,tag=gl_p2_orange] run function greenlantern:dual/hello/red_orange
execute if entity @s[tag=gl_p1_red,tag=gl_p2_blue] run function greenlantern:dual/hello/red_blue
execute if entity @s[tag=gl_p1_red,tag=gl_p2_violet] run function greenlantern:dual/hello/red_violet
execute if entity @s[tag=gl_p1_red,tag=gl_p2_indigo] run function greenlantern:dual/hello/red_indigo
execute if entity @s[tag=gl_p1_red,tag=gl_p2_white] run function greenlantern:dual/hello/red_white
execute if entity @s[tag=gl_p1_red,tag=gl_p2_black] run function greenlantern:dual/hello/red_black
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_blue] run function greenlantern:dual/hello/orange_blue
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_violet] run function greenlantern:dual/hello/orange_violet
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_indigo] run function greenlantern:dual/hello/orange_indigo
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_white] run function greenlantern:dual/hello/orange_white
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_black] run function greenlantern:dual/hello/orange_black
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_violet] run function greenlantern:dual/hello/blue_violet
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_indigo] run function greenlantern:dual/hello/blue_indigo
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_white] run function greenlantern:dual/hello/blue_white
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_black] run function greenlantern:dual/hello/blue_black
execute if entity @s[tag=gl_p1_violet,tag=gl_p2_indigo] run function greenlantern:dual/hello/violet_indigo
execute if entity @s[tag=gl_p1_violet,tag=gl_p2_white] run function greenlantern:dual/hello/violet_white
execute if entity @s[tag=gl_p1_violet,tag=gl_p2_black] run function greenlantern:dual/hello/violet_black
execute if entity @s[tag=gl_p1_indigo,tag=gl_p2_white] run function greenlantern:dual/hello/indigo_white
execute if entity @s[tag=gl_p1_indigo,tag=gl_p2_black] run function greenlantern:dual/hello/indigo_black
execute if entity @s[tag=gl_p1_white,tag=gl_p2_black] run function greenlantern:dual/hello/white_black
execute unless entity @s[tag=gl_bond_seen] run tellraw @s [{"text": "Your two rings bond. ", "color": "white", "bold": true}, {"text": "Their beams, constructs, force fields, ring light and suit merge into the Spectrum Bond bar (each ring keeps its own specials page), and the Spectrum Bond has its own skill tree in the powers menu. Choose a merged suit in the accessories menu.", "color": "gray"}]
tag @s add gl_bond_seen
