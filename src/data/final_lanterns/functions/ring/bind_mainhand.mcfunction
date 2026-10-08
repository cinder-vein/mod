function final_lanterns:ring/rebind_mainhand
execute if predicate final_lanterns:held/green_mainhand run tag @s add gl_member_green
execute if predicate final_lanterns:held/yellow_mainhand run tag @s add gl_member_yellow
execute if predicate final_lanterns:held/red_mainhand run tag @s add gl_member_red
execute if predicate final_lanterns:held/orange_mainhand run tag @s add gl_member_orange
execute if predicate final_lanterns:held/blue_mainhand run tag @s add gl_member_blue
execute if predicate final_lanterns:held/violet_mainhand run tag @s add gl_member_violet
execute if predicate final_lanterns:held/indigo_mainhand run tag @s add gl_member_indigo
execute if predicate final_lanterns:held/white_mainhand run tag @s add gl_member_white
execute if predicate final_lanterns:held/black_mainhand run tag @s add gl_member_black
tellraw @s [{"text":"The ring is now bound to you.","color":"gray","italic":true}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
