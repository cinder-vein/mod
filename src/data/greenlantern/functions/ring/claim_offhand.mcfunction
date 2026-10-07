scoreboard players set #giver gl_tmp 0
execute if predicate greenlantern:giver_ring_offhand store result score #giver gl_tmp run data get entity @s Inventory[{Slot:-106b}].tag.gl_giver
execute if score #giver gl_tmp = @s gl_id run function greenlantern:ring/giver_held_offhand
execute unless score #giver gl_tmp = @s gl_id run function greenlantern:ring/bind_offhand
