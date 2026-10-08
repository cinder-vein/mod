scoreboard players set #t gl_tmp 0
execute if entity @s[tag=gl_b0] run scoreboard players add #t gl_tmp 1
execute if entity @s[tag=gl_b1] run scoreboard players add #t gl_tmp 2
execute if entity @s[tag=gl_b2] run scoreboard players add #t gl_tmp 4
execute if entity @s[tag=gl_b3] run scoreboard players add #t gl_tmp 8
execute if entity @s[tag=gl_b4] run scoreboard players add #t gl_tmp 16
execute if entity @s[tag=gl_b5] run scoreboard players add #t gl_tmp 32
execute if entity @s[tag=gl_b6] run scoreboard players add #t gl_tmp 64
execute if entity @s[tag=gl_b7] run scoreboard players add #t gl_tmp 128
execute if entity @s[tag=gl_b8] run scoreboard players add #t gl_tmp 256
execute if entity @s[tag=gl_b9] run scoreboard players add #t gl_tmp 512
execute if entity @s[tag=gl_b10] run scoreboard players add #t gl_tmp 1024
execute if entity @s[tag=gl_b11] run scoreboard players add #t gl_tmp 2048
execute if entity @s[tag=gl_b12] run scoreboard players add #t gl_tmp 4096
execute if entity @s[tag=gl_b13] run scoreboard players add #t gl_tmp 8192
execute if entity @s[tag=gl_b14] run scoreboard players add #t gl_tmp 16384
execute if entity @s[tag=gl_b15] run scoreboard players add #t gl_tmp 32768
execute unless score @s gl_id = #t gl_tmp run function final_lanterns:id/from_tags
