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
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_green matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/green_offhand run scoreboard players operation @s gl_ser_green = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_yellow matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/yellow_offhand run scoreboard players operation @s gl_ser_yellow = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_red matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/red_offhand run scoreboard players operation @s gl_ser_red = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_orange matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/orange_offhand run scoreboard players operation @s gl_ser_orange = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_blue matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/blue_offhand run scoreboard players operation @s gl_ser_blue = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_violet matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/violet_offhand run scoreboard players operation @s gl_ser_violet = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_indigo matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/indigo_offhand run scoreboard players operation @s gl_ser_indigo = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_white matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/white_offhand run scoreboard players operation @s gl_ser_white = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_black matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/black_offhand run scoreboard players operation @s gl_ser_black = #s gl_tmp
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/green_offhand unless score #s gl_tmp = @s gl_ser_green run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/yellow_offhand unless score #s gl_tmp = @s gl_ser_yellow run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/red_offhand unless score #s gl_tmp = @s gl_ser_red run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/orange_offhand unless score #s gl_tmp = @s gl_ser_orange run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/blue_offhand unless score #s gl_tmp = @s gl_ser_blue run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/violet_offhand unless score #s gl_tmp = @s gl_ser_violet run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/indigo_offhand unless score #s gl_tmp = @s gl_ser_indigo run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/white_offhand unless score #s gl_tmp = @s gl_ser_white run function greenlantern:ring/dark_offhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/black_offhand unless score #s gl_tmp = @s gl_ser_black run function greenlantern:ring/dark_offhand
