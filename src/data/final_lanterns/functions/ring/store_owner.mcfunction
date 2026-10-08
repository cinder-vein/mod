execute store result storage final_lanterns:binding owner int 1 run scoreboard players get @s gl_id
data modify storage final_lanterns:binding bits set value {b0:0b,b1:0b,b2:0b,b3:0b,b4:0b,b5:0b,b6:0b,b7:0b,b8:0b,b9:0b,b10:0b,b11:0b,b12:0b,b13:0b,b14:0b,b15:0b}
execute if entity @s[tag=gl_b0] run data modify storage final_lanterns:binding bits.b0 set value 1b
execute if entity @s[tag=gl_b1] run data modify storage final_lanterns:binding bits.b1 set value 1b
execute if entity @s[tag=gl_b2] run data modify storage final_lanterns:binding bits.b2 set value 1b
execute if entity @s[tag=gl_b3] run data modify storage final_lanterns:binding bits.b3 set value 1b
execute if entity @s[tag=gl_b4] run data modify storage final_lanterns:binding bits.b4 set value 1b
execute if entity @s[tag=gl_b5] run data modify storage final_lanterns:binding bits.b5 set value 1b
execute if entity @s[tag=gl_b6] run data modify storage final_lanterns:binding bits.b6 set value 1b
execute if entity @s[tag=gl_b7] run data modify storage final_lanterns:binding bits.b7 set value 1b
execute if entity @s[tag=gl_b8] run data modify storage final_lanterns:binding bits.b8 set value 1b
execute if entity @s[tag=gl_b9] run data modify storage final_lanterns:binding bits.b9 set value 1b
execute if entity @s[tag=gl_b10] run data modify storage final_lanterns:binding bits.b10 set value 1b
execute if entity @s[tag=gl_b11] run data modify storage final_lanterns:binding bits.b11 set value 1b
execute if entity @s[tag=gl_b12] run data modify storage final_lanterns:binding bits.b12 set value 1b
execute if entity @s[tag=gl_b13] run data modify storage final_lanterns:binding bits.b13 set value 1b
execute if entity @s[tag=gl_b14] run data modify storage final_lanterns:binding bits.b14 set value 1b
execute if entity @s[tag=gl_b15] run data modify storage final_lanterns:binding bits.b15 set value 1b
