data remove storage greenlantern:binding carry
data modify storage greenlantern:binding carry set from entity @s Inventory
execute if data storage greenlantern:binding carry[0] run function greenlantern:ring/carry_next
