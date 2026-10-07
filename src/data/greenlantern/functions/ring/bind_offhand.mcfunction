function greenlantern:ring/rebind_offhand
execute if predicate greenlantern:held/green_offhand run tag @s add gl_member_green
execute if predicate greenlantern:held/yellow_offhand run tag @s add gl_member_yellow
execute if predicate greenlantern:held/red_offhand run tag @s add gl_member_red
execute if predicate greenlantern:held/orange_offhand run tag @s add gl_member_orange
execute if predicate greenlantern:held/blue_offhand run tag @s add gl_member_blue
execute if predicate greenlantern:held/violet_offhand run tag @s add gl_member_violet
execute if predicate greenlantern:held/indigo_offhand run tag @s add gl_member_indigo
execute if predicate greenlantern:held/white_offhand run tag @s add gl_member_white
execute if predicate greenlantern:held/black_offhand run tag @s add gl_member_black
tellraw @s [{"text":"The ring is now bound to you.","color":"gray","italic":true}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
