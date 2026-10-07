execute store result score #s gl_tmp run data get storage greenlantern:binding cur.tag.gl_serial
scoreboard players add @s gl_ser_green 0
scoreboard players add @s gl_ser_yellow 0
scoreboard players add @s gl_ser_red 0
scoreboard players add @s gl_ser_orange 0
scoreboard players add @s gl_ser_blue 0
scoreboard players add @s gl_ser_violet 0
scoreboard players add @s gl_ser_indigo 0
scoreboard players add @s gl_ser_white 0
scoreboard players add @s gl_ser_black 0
execute if entity @s[tag=gl_reser] if score @s gl_ser_green matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:green_lantern_ring"} run scoreboard players operation @s gl_ser_green = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_yellow matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:yellow_lantern_ring"} run scoreboard players operation @s gl_ser_yellow = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_red matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:red_lantern_ring"} run scoreboard players operation @s gl_ser_red = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_orange matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:orange_lantern_ring"} run scoreboard players operation @s gl_ser_orange = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_blue matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:blue_lantern_ring"} run scoreboard players operation @s gl_ser_blue = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_violet matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:violet_lantern_ring"} run scoreboard players operation @s gl_ser_violet = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_indigo matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:indigo_lantern_ring"} run scoreboard players operation @s gl_ser_indigo = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_white matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:white_lantern_ring"} run scoreboard players operation @s gl_ser_white = #s gl_tmp
execute if entity @s[tag=gl_reser] if score @s gl_ser_black matches 0 if score #s gl_tmp matches 1.. if data storage greenlantern:binding cur{id:"greenlantern:black_lantern_ring"} run scoreboard players operation @s gl_ser_black = #s gl_tmp
execute if score #s gl_tmp matches 0 if score @s gl_ser_green matches 0 if data storage greenlantern:binding cur{id:"greenlantern:green_lantern_ring"} run tag @s add gl_legacy_green
execute if score #s gl_tmp matches 0 if score @s gl_ser_yellow matches 0 if data storage greenlantern:binding cur{id:"greenlantern:yellow_lantern_ring"} run tag @s add gl_legacy_yellow
execute if score #s gl_tmp matches 0 if score @s gl_ser_red matches 0 if data storage greenlantern:binding cur{id:"greenlantern:red_lantern_ring"} run tag @s add gl_legacy_red
execute if score #s gl_tmp matches 0 if score @s gl_ser_orange matches 0 if data storage greenlantern:binding cur{id:"greenlantern:orange_lantern_ring"} run tag @s add gl_legacy_orange
execute if score #s gl_tmp matches 0 if score @s gl_ser_blue matches 0 if data storage greenlantern:binding cur{id:"greenlantern:blue_lantern_ring"} run tag @s add gl_legacy_blue
execute if score #s gl_tmp matches 0 if score @s gl_ser_violet matches 0 if data storage greenlantern:binding cur{id:"greenlantern:violet_lantern_ring"} run tag @s add gl_legacy_violet
execute if score #s gl_tmp matches 0 if score @s gl_ser_indigo matches 0 if data storage greenlantern:binding cur{id:"greenlantern:indigo_lantern_ring"} run tag @s add gl_legacy_indigo
execute if score #s gl_tmp matches 0 if score @s gl_ser_white matches 0 if data storage greenlantern:binding cur{id:"greenlantern:white_lantern_ring"} run tag @s add gl_legacy_white
execute if score #s gl_tmp matches 0 if score @s gl_ser_black matches 0 if data storage greenlantern:binding cur{id:"greenlantern:black_lantern_ring"} run tag @s add gl_legacy_black
execute if data storage greenlantern:binding cur{id:"greenlantern:green_lantern_ring"} unless score #s gl_tmp = @s gl_ser_green run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:yellow_lantern_ring"} unless score #s gl_tmp = @s gl_ser_yellow run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:red_lantern_ring"} unless score #s gl_tmp = @s gl_ser_red run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:orange_lantern_ring"} unless score #s gl_tmp = @s gl_ser_orange run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:blue_lantern_ring"} unless score #s gl_tmp = @s gl_ser_blue run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:violet_lantern_ring"} unless score #s gl_tmp = @s gl_ser_violet run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:indigo_lantern_ring"} unless score #s gl_tmp = @s gl_ser_indigo run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:white_lantern_ring"} unless score #s gl_tmp = @s gl_ser_white run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:black_lantern_ring"} unless score #s gl_tmp = @s gl_ser_black run function greenlantern:ring/curios_dark
execute if entity @s[tag=gl_reser] run function greenlantern:ring/save_serials
