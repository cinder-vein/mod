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
execute if score @s gl_ser_green matches 1.. run function final_lanterns:recall/green
execute if score @s gl_ser_green matches 0 if entity @s[tag=gl_legacy_green] run function final_lanterns:recall/green
execute if score @s gl_ser_yellow matches 1.. run function final_lanterns:recall/yellow
execute if score @s gl_ser_yellow matches 0 if entity @s[tag=gl_legacy_yellow] run function final_lanterns:recall/yellow
execute if score @s gl_ser_red matches 1.. run function final_lanterns:recall/red
execute if score @s gl_ser_red matches 0 if entity @s[tag=gl_legacy_red] run function final_lanterns:recall/red
execute if score @s gl_ser_orange matches 1.. run function final_lanterns:recall/orange
execute if score @s gl_ser_orange matches 0 if entity @s[tag=gl_legacy_orange] run function final_lanterns:recall/orange
execute if score @s gl_ser_blue matches 1.. run function final_lanterns:recall/blue
execute if score @s gl_ser_blue matches 0 if entity @s[tag=gl_legacy_blue] run function final_lanterns:recall/blue
execute if score @s gl_ser_violet matches 1.. run function final_lanterns:recall/violet
execute if score @s gl_ser_violet matches 0 if entity @s[tag=gl_legacy_violet] run function final_lanterns:recall/violet
execute if score @s gl_ser_indigo matches 1.. run function final_lanterns:recall/indigo
execute if score @s gl_ser_indigo matches 0 if entity @s[tag=gl_legacy_indigo] run function final_lanterns:recall/indigo
execute if score @s gl_ser_white matches 1.. run function final_lanterns:recall/white
execute if score @s gl_ser_white matches 0 if entity @s[tag=gl_legacy_white] run function final_lanterns:recall/white
execute if score @s gl_ser_black matches 1.. run function final_lanterns:recall/black
execute if score @s gl_ser_black matches 0 if entity @s[tag=gl_legacy_black] run function final_lanterns:recall/black
execute if score #called gl_tmp matches 0 run tellraw @s [{"text":"No ring has chosen you yet.","color":"gray"}]
