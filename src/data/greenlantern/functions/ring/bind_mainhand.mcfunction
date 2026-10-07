function greenlantern:ring/rebind_mainhand
execute if predicate greenlantern:held/green_mainhand run tag @s add gl_member_green
execute if predicate greenlantern:held/yellow_mainhand run tag @s add gl_member_yellow
execute if predicate greenlantern:held/red_mainhand run tag @s add gl_member_red
execute if predicate greenlantern:held/orange_mainhand run tag @s add gl_member_orange
execute if predicate greenlantern:held/blue_mainhand run tag @s add gl_member_blue
execute if predicate greenlantern:held/violet_mainhand run tag @s add gl_member_violet
execute if predicate greenlantern:held/indigo_mainhand run tag @s add gl_member_indigo
execute if predicate greenlantern:held/white_mainhand run tag @s add gl_member_white
execute if predicate greenlantern:held/black_mainhand run tag @s add gl_member_black
tellraw @s [{"text":"The ring is now bound to you.","color":"gray","italic":true}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
