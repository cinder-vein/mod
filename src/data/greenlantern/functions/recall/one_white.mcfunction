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
execute if score @s gl_ser_white matches 1.. run function greenlantern:recall/white
execute if score @s gl_ser_white matches 0 if entity @s[tag=gl_legacy_white] run function greenlantern:recall/white
execute if score #called gl_tmp matches 0 run tellraw @s [{"text":"No White Lantern ring has chosen you.","color":"gray"}]
