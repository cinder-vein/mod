execute unless predicate final_lanterns:ring_mainhand run tellraw @s [{"text":"Hold the ring in your main hand to unbind it.","color":"gray"}]
execute if predicate final_lanterns:ring_mainhand run function final_lanterns:ring/store_giver
execute if predicate final_lanterns:held/green_mainhand run scoreboard players set @s gl_ser_green -1
execute if predicate final_lanterns:held/yellow_mainhand run scoreboard players set @s gl_ser_yellow -1
execute if predicate final_lanterns:held/red_mainhand run scoreboard players set @s gl_ser_red -1
execute if predicate final_lanterns:held/orange_mainhand run scoreboard players set @s gl_ser_orange -1
execute if predicate final_lanterns:held/blue_mainhand run scoreboard players set @s gl_ser_blue -1
execute if predicate final_lanterns:held/violet_mainhand run scoreboard players set @s gl_ser_violet -1
execute if predicate final_lanterns:held/indigo_mainhand run scoreboard players set @s gl_ser_indigo -1
execute if predicate final_lanterns:held/white_mainhand run scoreboard players set @s gl_ser_white -1
execute if predicate final_lanterns:held/black_mainhand run scoreboard players set @s gl_ser_black -1
execute if predicate final_lanterns:held/green_mainhand run tag @s remove gl_legacy_green
execute if predicate final_lanterns:held/yellow_mainhand run tag @s remove gl_legacy_yellow
execute if predicate final_lanterns:held/red_mainhand run tag @s remove gl_legacy_red
execute if predicate final_lanterns:held/orange_mainhand run tag @s remove gl_legacy_orange
execute if predicate final_lanterns:held/blue_mainhand run tag @s remove gl_legacy_blue
execute if predicate final_lanterns:held/violet_mainhand run tag @s remove gl_legacy_violet
execute if predicate final_lanterns:held/indigo_mainhand run tag @s remove gl_legacy_indigo
execute if predicate final_lanterns:held/white_mainhand run tag @s remove gl_legacy_white
execute if predicate final_lanterns:held/black_mainhand run tag @s remove gl_legacy_black
execute if predicate final_lanterns:ring_mainhand run function final_lanterns:ring/save_serials
execute if predicate final_lanterns:ring_mainhand run item modify entity @s weapon.mainhand final_lanterns:unbind
execute if predicate final_lanterns:ring_mainhand run tellraw @s [{"text":"The ring in your hand is unbound. It will bind to the next player who holds it.","color":"gray"}]
