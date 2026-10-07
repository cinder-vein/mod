data modify storage greenlantern:binding held set from entity @s SelectedItem.tag
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
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_green matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/green_mainhand run scoreboard players operation @s gl_ser_green = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_yellow matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/yellow_mainhand run scoreboard players operation @s gl_ser_yellow = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_red matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/red_mainhand run scoreboard players operation @s gl_ser_red = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_orange matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/orange_mainhand run scoreboard players operation @s gl_ser_orange = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_blue matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/blue_mainhand run scoreboard players operation @s gl_ser_blue = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_violet matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/violet_mainhand run scoreboard players operation @s gl_ser_violet = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_indigo matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/indigo_mainhand run scoreboard players operation @s gl_ser_indigo = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_white matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/white_mainhand run scoreboard players operation @s gl_ser_white = #s gl_tmp
execute if entity @s[tag=gl_reser] if score #owner gl_tmp = @s gl_id if score @s gl_ser_black matches 0 if score #s gl_tmp matches 1.. if predicate greenlantern:held/black_mainhand run scoreboard players operation @s gl_ser_black = #s gl_tmp
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_green matches 0 if predicate greenlantern:held/green_mainhand run tag @s add gl_legacy_green
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_yellow matches 0 if predicate greenlantern:held/yellow_mainhand run tag @s add gl_legacy_yellow
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_red matches 0 if predicate greenlantern:held/red_mainhand run tag @s add gl_legacy_red
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_orange matches 0 if predicate greenlantern:held/orange_mainhand run tag @s add gl_legacy_orange
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_blue matches 0 if predicate greenlantern:held/blue_mainhand run tag @s add gl_legacy_blue
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_violet matches 0 if predicate greenlantern:held/violet_mainhand run tag @s add gl_legacy_violet
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_indigo matches 0 if predicate greenlantern:held/indigo_mainhand run tag @s add gl_legacy_indigo
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_white matches 0 if predicate greenlantern:held/white_mainhand run tag @s add gl_legacy_white
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp matches 0 if score @s gl_ser_black matches 0 if predicate greenlantern:held/black_mainhand run tag @s add gl_legacy_black
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/green_mainhand unless score #s gl_tmp = @s gl_ser_green run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/yellow_mainhand unless score #s gl_tmp = @s gl_ser_yellow run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/red_mainhand unless score #s gl_tmp = @s gl_ser_red run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/orange_mainhand unless score #s gl_tmp = @s gl_ser_orange run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/blue_mainhand unless score #s gl_tmp = @s gl_ser_blue run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/violet_mainhand unless score #s gl_tmp = @s gl_ser_violet run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/indigo_mainhand unless score #s gl_tmp = @s gl_ser_indigo run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/white_mainhand unless score #s gl_tmp = @s gl_ser_white run function greenlantern:ring/dark_mainhand
execute if score #owner gl_tmp = @s gl_id if predicate greenlantern:held/black_mainhand unless score #s gl_tmp = @s gl_ser_black run function greenlantern:ring/dark_mainhand
execute if entity @s[tag=gl_reser] run function greenlantern:ring/save_serials
