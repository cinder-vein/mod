execute unless predicate greenlantern:ring_mainhand run tellraw @s [{"text":"Hold the ring in your main hand to unbind it.","color":"gray"}]
execute if predicate greenlantern:ring_mainhand run function greenlantern:ring/store_giver
execute if predicate greenlantern:ring_mainhand run item modify entity @s weapon.mainhand greenlantern:unbind
execute if predicate greenlantern:ring_mainhand run tellraw @s [{"text":"The ring in your hand is unbound. It will bind to the next player who holds it.","color":"gray"}]
