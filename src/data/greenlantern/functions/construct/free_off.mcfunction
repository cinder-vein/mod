scoreboard players set #free gl_tmp 1
execute if data entity @s Inventory[{Slot:-106b}] run scoreboard players set #free gl_tmp 0
execute if score #free gl_tmp matches 0 unless predicate greenlantern:ring_offhand run function greenlantern:construct/stash_off
