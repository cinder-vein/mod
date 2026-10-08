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
execute if score @s gl_ser_violet matches 1.. run function final_lanterns:recall/violet
execute if score @s gl_ser_violet matches 0 if entity @s[tag=gl_legacy_violet] run function final_lanterns:recall/violet
execute if score #called gl_tmp matches 0 run tellraw @s [{"text":"No Star Sapphire ring has chosen you.","color":"gray"}]
