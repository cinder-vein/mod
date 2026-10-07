execute store result score #owner gl_tmp run data get entity @s Inventory[{Slot:-106b}].tag.gl_owner
execute unless score #owner gl_tmp = @s gl_id run function greenlantern:ring/eject_offhand
execute if score #owner gl_tmp = @s gl_id run function greenlantern:ring/legacy_own_offhand
