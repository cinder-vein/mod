execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
item modify entity @s weapon.mainhand greenlantern:bind
execute if data entity @s SelectedItem{id:"greenlantern:green_lantern_ring"} run tag @s add gl_member_green
execute if data entity @s SelectedItem{id:"greenlantern:yellow_lantern_ring"} run tag @s add gl_member_yellow
execute if data entity @s SelectedItem{id:"greenlantern:red_lantern_ring"} run tag @s add gl_member_red
execute if data entity @s SelectedItem{id:"greenlantern:orange_lantern_ring"} run tag @s add gl_member_orange
execute if data entity @s SelectedItem{id:"greenlantern:blue_lantern_ring"} run tag @s add gl_member_blue
execute if data entity @s SelectedItem{id:"greenlantern:violet_lantern_ring"} run tag @s add gl_member_violet
execute if data entity @s SelectedItem{id:"greenlantern:indigo_lantern_ring"} run tag @s add gl_member_indigo
execute if data entity @s SelectedItem{id:"greenlantern:white_lantern_ring"} run tag @s add gl_member_white
execute if data entity @s SelectedItem{id:"greenlantern:black_lantern_ring"} run tag @s add gl_member_black
tellraw @s [{"text":"The ring is now bound to you.","color":"gray","italic":true}]
playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
