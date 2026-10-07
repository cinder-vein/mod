scoreboard players set @s gl_id 0
execute if entity @s[tag=gl_b0] run scoreboard players add @s gl_id 1
execute if entity @s[tag=gl_b1] run scoreboard players add @s gl_id 2
execute if entity @s[tag=gl_b2] run scoreboard players add @s gl_id 4
execute if entity @s[tag=gl_b3] run scoreboard players add @s gl_id 8
execute if entity @s[tag=gl_b4] run scoreboard players add @s gl_id 16
execute if entity @s[tag=gl_b5] run scoreboard players add @s gl_id 32
execute if entity @s[tag=gl_b6] run scoreboard players add @s gl_id 64
execute if entity @s[tag=gl_b7] run scoreboard players add @s gl_id 128
execute if entity @s[tag=gl_b8] run scoreboard players add @s gl_id 256
execute if entity @s[tag=gl_b9] run scoreboard players add @s gl_id 512
execute if entity @s[tag=gl_b10] run scoreboard players add @s gl_id 1024
execute if entity @s[tag=gl_b11] run scoreboard players add @s gl_id 2048
execute if entity @s[tag=gl_b12] run scoreboard players add @s gl_id 4096
execute if entity @s[tag=gl_b13] run scoreboard players add @s gl_id 8192
execute if entity @s[tag=gl_b14] run scoreboard players add @s gl_id 16384
execute if entity @s[tag=gl_b15] run scoreboard players add @s gl_id 32768
scoreboard players reset @s gl_ser_green
scoreboard players reset @s gl_ser_yellow
scoreboard players reset @s gl_ser_red
scoreboard players reset @s gl_ser_orange
scoreboard players reset @s gl_ser_blue
scoreboard players reset @s gl_ser_violet
scoreboard players reset @s gl_ser_indigo
scoreboard players reset @s gl_ser_white
scoreboard players reset @s gl_ser_black
function greenlantern:ring/load_serials
tag @s add gl_reser
scoreboard players set @s gl_reser 60
