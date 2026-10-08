tag @s add gl_sersaved
data modify storage final_lanterns:binding me set value {}
execute store result storage final_lanterns:binding me.id int 1 run scoreboard players get @s gl_id
scoreboard players add @s gl_ser_green 0
scoreboard players add @s gl_ser_yellow 0
scoreboard players add @s gl_ser_red 0
scoreboard players add @s gl_ser_orange 0
scoreboard players add @s gl_ser_blue 0
scoreboard players add @s gl_ser_violet 0
scoreboard players add @s gl_ser_indigo 0
scoreboard players add @s gl_ser_white 0
scoreboard players add @s gl_ser_black 0
execute store result storage final_lanterns:binding me.green int 1 run scoreboard players get @s gl_ser_green
execute store result storage final_lanterns:binding me.yellow int 1 run scoreboard players get @s gl_ser_yellow
execute store result storage final_lanterns:binding me.red int 1 run scoreboard players get @s gl_ser_red
execute store result storage final_lanterns:binding me.orange int 1 run scoreboard players get @s gl_ser_orange
execute store result storage final_lanterns:binding me.blue int 1 run scoreboard players get @s gl_ser_blue
execute store result storage final_lanterns:binding me.violet int 1 run scoreboard players get @s gl_ser_violet
execute store result storage final_lanterns:binding me.indigo int 1 run scoreboard players get @s gl_ser_indigo
execute store result storage final_lanterns:binding me.white int 1 run scoreboard players get @s gl_ser_white
execute store result storage final_lanterns:binding me.black int 1 run scoreboard players get @s gl_ser_black
data modify storage final_lanterns:binding rest set value []
execute if data storage final_lanterns:binding sers[0] run function final_lanterns:ring/save_next
data modify storage final_lanterns:binding sers set from storage final_lanterns:binding rest
data modify storage final_lanterns:binding sers append from storage final_lanterns:binding me
