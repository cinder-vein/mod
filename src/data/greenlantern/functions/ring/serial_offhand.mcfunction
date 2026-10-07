data modify storage greenlantern:binding held set from entity @s Inventory[{Slot:-106b}].tag
execute store result score #owner gl_tmp run data get storage greenlantern:binding held.gl_owner
execute store result score #s gl_tmp run data get storage greenlantern:binding held.gl_serial
scoreboard players add @s gl_ser_green 0
scoreboard players add @s gl_ser_yellow 0
scoreboard players add @s gl_ser_red 0
scoreboard players add @s gl_ser_orange 0
scoreboard players add @s gl_ser_blue 0
scoreboard players add @s gl_ser_violet 0
scoreboard players add @s gl_ser_indigo 0
scoreboard players add @s gl_ser_white 0
scoreboard players add @s gl_ser_black 0
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/green_offhand unless score #s gl_tmp = @s gl_ser_green run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/yellow_offhand unless score #s gl_tmp = @s gl_ser_yellow run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/red_offhand unless score #s gl_tmp = @s gl_ser_red run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/orange_offhand unless score #s gl_tmp = @s gl_ser_orange run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/blue_offhand unless score #s gl_tmp = @s gl_ser_blue run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/violet_offhand unless score #s gl_tmp = @s gl_ser_violet run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/indigo_offhand unless score #s gl_tmp = @s gl_ser_indigo run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/white_offhand unless score #s gl_tmp = @s gl_ser_white run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/black_offhand unless score #s gl_tmp = @s gl_ser_black run function greenlantern:ring/dark_offhand
