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
execute if score @s gl_ser_green matches 1.. run function greenlantern:recall/green
execute if score @s gl_ser_green matches 0 if entity @s[tag=gl_legacy_green] run function greenlantern:recall/green
execute if score @s gl_ser_yellow matches 1.. run function greenlantern:recall/yellow
execute if score @s gl_ser_yellow matches 0 if entity @s[tag=gl_legacy_yellow] run function greenlantern:recall/yellow
execute if score @s gl_ser_red matches 1.. run function greenlantern:recall/red
execute if score @s gl_ser_red matches 0 if entity @s[tag=gl_legacy_red] run function greenlantern:recall/red
execute if score @s gl_ser_orange matches 1.. run function greenlantern:recall/orange
execute if score @s gl_ser_orange matches 0 if entity @s[tag=gl_legacy_orange] run function greenlantern:recall/orange
execute if score @s gl_ser_blue matches 1.. run function greenlantern:recall/blue
execute if score @s gl_ser_blue matches 0 if entity @s[tag=gl_legacy_blue] run function greenlantern:recall/blue
execute if score @s gl_ser_violet matches 1.. run function greenlantern:recall/violet
execute if score @s gl_ser_violet matches 0 if entity @s[tag=gl_legacy_violet] run function greenlantern:recall/violet
execute if score @s gl_ser_indigo matches 1.. run function greenlantern:recall/indigo
execute if score @s gl_ser_indigo matches 0 if entity @s[tag=gl_legacy_indigo] run function greenlantern:recall/indigo
execute if score @s gl_ser_white matches 1.. run function greenlantern:recall/white
execute if score @s gl_ser_white matches 0 if entity @s[tag=gl_legacy_white] run function greenlantern:recall/white
execute if score @s gl_ser_black matches 1.. run function greenlantern:recall/black
execute if score @s gl_ser_black matches 0 if entity @s[tag=gl_legacy_black] run function greenlantern:recall/black
execute if score #called gl_tmp matches 0 run tellraw @s [{"text":"No ring has chosen you yet.","color":"gray"}]
