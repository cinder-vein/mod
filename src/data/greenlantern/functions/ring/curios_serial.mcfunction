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
execute if data storage greenlantern:binding cur{id:"greenlantern:green_lantern_ring"} unless score #s gl_tmp = @s gl_ser_green run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:yellow_lantern_ring"} unless score #s gl_tmp = @s gl_ser_yellow run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:red_lantern_ring"} unless score #s gl_tmp = @s gl_ser_red run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:orange_lantern_ring"} unless score #s gl_tmp = @s gl_ser_orange run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:blue_lantern_ring"} unless score #s gl_tmp = @s gl_ser_blue run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:violet_lantern_ring"} unless score #s gl_tmp = @s gl_ser_violet run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:indigo_lantern_ring"} unless score #s gl_tmp = @s gl_ser_indigo run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:white_lantern_ring"} unless score #s gl_tmp = @s gl_ser_white run function greenlantern:ring/curios_dark
execute if data storage greenlantern:binding cur{id:"greenlantern:black_lantern_ring"} unless score #s gl_tmp = @s gl_ser_black run function greenlantern:ring/curios_dark
