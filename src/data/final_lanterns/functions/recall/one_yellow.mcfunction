scoreboard players set #called gl_tmp 0
scoreboard players add @s gl_ser_green 0
scoreboard players add @s gl_ser_yellow 0
scoreboard players add @s gl_ser_red 0
scoreboard players add @s gl_ser_orange 0
scoreboard players add @s gl_ser_blue 0
scoreboard players add @s gl_ser_violet 0
scoreboard players add @s gl_ser_indigo 0
scoreboard players add @s gl_ser_white 0
scoreboard players add @s gl_ser_black 0
execute if score @s gl_ser_yellow matches 1.. run function final_lanterns:recall/yellow
execute if score @s gl_ser_yellow matches 0 if entity @s[tag=gl_legacy_yellow] run function final_lanterns:recall/yellow
execute if score #called gl_tmp matches 0 run tellraw @s [{"text":"No Sinestro Corps ring has chosen you.","color":"gray"}]
