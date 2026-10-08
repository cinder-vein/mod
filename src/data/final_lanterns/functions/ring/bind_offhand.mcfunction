function final_lanterns:ring/rebind_offhand
execute if predicate final_lanterns:held/green_offhand run tag @s add gl_member_green
execute if predicate final_lanterns:held/yellow_offhand run tag @s add gl_member_yellow
execute if predicate final_lanterns:held/red_offhand run tag @s add gl_member_red
execute if predicate final_lanterns:held/orange_offhand run tag @s add gl_member_orange
execute if predicate final_lanterns:held/blue_offhand run tag @s add gl_member_blue
execute if predicate final_lanterns:held/violet_offhand run tag @s add gl_member_violet
execute if predicate final_lanterns:held/indigo_offhand run tag @s add gl_member_indigo
execute if predicate final_lanterns:held/white_offhand run tag @s add gl_member_white
execute if predicate final_lanterns:held/black_offhand run tag @s add gl_member_black
tellraw @s [{"text":"The ring is now bound to you.","color":"gray","italic":true}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
