tag @s add gl_sersaved
data modify storage greenlantern:binding me set value {}
execute store result storage greenlantern:binding me.id int 1 run scoreboard players get @s gl_id
scoreboard players add @s gl_ser_green 0
scoreboard players add @s gl_ser_yellow 0
scoreboard players add @s gl_ser_red 0
scoreboard players add @s gl_ser_orange 0
scoreboard players add @s gl_ser_blue 0
scoreboard players add @s gl_ser_violet 0
scoreboard players add @s gl_ser_indigo 0
scoreboard players add @s gl_ser_white 0
scoreboard players add @s gl_ser_black 0
execute store result storage greenlantern:binding me.green int 1 run scoreboard players get @s gl_ser_green
execute store result storage greenlantern:binding me.yellow int 1 run scoreboard players get @s gl_ser_yellow
execute store result storage greenlantern:binding me.red int 1 run scoreboard players get @s gl_ser_red
execute store result storage greenlantern:binding me.orange int 1 run scoreboard players get @s gl_ser_orange
execute store result storage greenlantern:binding me.blue int 1 run scoreboard players get @s gl_ser_blue
execute store result storage greenlantern:binding me.violet int 1 run scoreboard players get @s gl_ser_violet
execute store result storage greenlantern:binding me.indigo int 1 run scoreboard players get @s gl_ser_indigo
execute store result storage greenlantern:binding me.white int 1 run scoreboard players get @s gl_ser_white
execute store result storage greenlantern:binding me.black int 1 run scoreboard players get @s gl_ser_black
data modify storage greenlantern:binding rest set value []
execute if data storage greenlantern:binding sers[0] run function greenlantern:ring/save_next
data modify storage greenlantern:binding sers set from storage greenlantern:binding rest
data modify storage greenlantern:binding sers append from storage greenlantern:binding me
