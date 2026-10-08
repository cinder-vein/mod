superpower add final_lanterns:spectrum_bond @s
tag @s add gl_dual
execute if entity @s[tag=gl_p1_green,tag=gl_p2_yellow] run function final_lanterns:bond/hello/green_yellow
execute if entity @s[tag=gl_p1_green,tag=gl_p2_red] run function final_lanterns:bond/hello/green_red
execute if entity @s[tag=gl_p1_green,tag=gl_p2_orange] run function final_lanterns:bond/hello/green_orange
execute if entity @s[tag=gl_p1_green,tag=gl_p2_blue] run function final_lanterns:bond/hello/green_blue
execute if entity @s[tag=gl_p1_green,tag=gl_p2_violet] run function final_lanterns:bond/hello/green_violet
execute if entity @s[tag=gl_p1_green,tag=gl_p2_indigo] run function final_lanterns:bond/hello/green_indigo
execute if entity @s[tag=gl_p1_green,tag=gl_p2_white] run function final_lanterns:bond/hello/green_white
execute if entity @s[tag=gl_p1_green,tag=gl_p2_black] run function final_lanterns:bond/hello/green_black
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_red] run function final_lanterns:bond/hello/yellow_red
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_orange] run function final_lanterns:bond/hello/yellow_orange
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_blue] run function final_lanterns:bond/hello/yellow_blue
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_violet] run function final_lanterns:bond/hello/yellow_violet
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_indigo] run function final_lanterns:bond/hello/yellow_indigo
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_white] run function final_lanterns:bond/hello/yellow_white
execute if entity @s[tag=gl_p1_yellow,tag=gl_p2_black] run function final_lanterns:bond/hello/yellow_black
execute if entity @s[tag=gl_p1_red,tag=gl_p2_orange] run function final_lanterns:bond/hello/red_orange
execute if entity @s[tag=gl_p1_red,tag=gl_p2_blue] run function final_lanterns:bond/hello/red_blue
execute if entity @s[tag=gl_p1_red,tag=gl_p2_violet] run function final_lanterns:bond/hello/red_violet
execute if entity @s[tag=gl_p1_red,tag=gl_p2_indigo] run function final_lanterns:bond/hello/red_indigo
execute if entity @s[tag=gl_p1_red,tag=gl_p2_white] run function final_lanterns:bond/hello/red_white
execute if entity @s[tag=gl_p1_red,tag=gl_p2_black] run function final_lanterns:bond/hello/red_black
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_blue] run function final_lanterns:bond/hello/orange_blue
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_violet] run function final_lanterns:bond/hello/orange_violet
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_indigo] run function final_lanterns:bond/hello/orange_indigo
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_white] run function final_lanterns:bond/hello/orange_white
execute if entity @s[tag=gl_p1_orange,tag=gl_p2_black] run function final_lanterns:bond/hello/orange_black
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_violet] run function final_lanterns:bond/hello/blue_violet
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_indigo] run function final_lanterns:bond/hello/blue_indigo
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_white] run function final_lanterns:bond/hello/blue_white
execute if entity @s[tag=gl_p1_blue,tag=gl_p2_black] run function final_lanterns:bond/hello/blue_black
execute if entity @s[tag=gl_p1_violet,tag=gl_p2_indigo] run function final_lanterns:bond/hello/violet_indigo
execute if entity @s[tag=gl_p1_violet,tag=gl_p2_white] run function final_lanterns:bond/hello/violet_white
execute if entity @s[tag=gl_p1_violet,tag=gl_p2_black] run function final_lanterns:bond/hello/violet_black
execute if entity @s[tag=gl_p1_indigo,tag=gl_p2_white] run function final_lanterns:bond/hello/indigo_white
execute if entity @s[tag=gl_p1_indigo,tag=gl_p2_black] run function final_lanterns:bond/hello/indigo_black
execute if entity @s[tag=gl_p1_white,tag=gl_p2_black] run function final_lanterns:bond/hello/white_black
execute unless entity @s[tag=gl_bond_seen] run tellraw @s ["",{"text":"Your two rings bond. ","color":"white","bold":true},{"text":"The Spectrum Bond adds its own bar (Twin Beam, Twin Constructs, Spectrum Fusion, Prismatic Shield, Spectrum Overload) and its own skill tree in the powers menu; each ring keeps its own. Pick a merged suit in the accessories menu (Spectrum Suit).","color":"gray"}]
tag @s add gl_bond_seen
