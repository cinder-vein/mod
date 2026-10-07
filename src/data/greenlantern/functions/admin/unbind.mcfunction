execute unless predicate greenlantern:ring_mainhand run tellraw @s [{"text":"Hold the ring in your main hand to unbind it.","color":"gray"}]
execute if predicate greenlantern:ring_mainhand run function greenlantern:ring/store_giver
execute if predicate greenlantern:held/green_mainhand run scoreboard players set @s gl_ser_green -1
execute if predicate greenlantern:held/yellow_mainhand run scoreboard players set @s gl_ser_yellow -1
execute if predicate greenlantern:held/red_mainhand run scoreboard players set @s gl_ser_red -1
execute if predicate greenlantern:held/orange_mainhand run scoreboard players set @s gl_ser_orange -1
execute if predicate greenlantern:held/blue_mainhand run scoreboard players set @s gl_ser_blue -1
execute if predicate greenlantern:held/violet_mainhand run scoreboard players set @s gl_ser_violet -1
execute if predicate greenlantern:held/indigo_mainhand run scoreboard players set @s gl_ser_indigo -1
execute if predicate greenlantern:held/white_mainhand run scoreboard players set @s gl_ser_white -1
execute if predicate greenlantern:held/black_mainhand run scoreboard players set @s gl_ser_black -1
execute if predicate greenlantern:ring_mainhand run item modify entity @s weapon.mainhand greenlantern:unbind
execute if predicate greenlantern:ring_mainhand run tellraw @s [{"text":"The ring in your hand is unbound. It will bind to the next player who holds it.","color":"gray"}]
