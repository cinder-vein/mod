scoreboard players set #keep gl_tmp 0
scoreboard players add @s gl_ser_green 0
scoreboard players add @s gl_ser_yellow 0
scoreboard players add @s gl_ser_red 0
scoreboard players add @s gl_ser_orange 0
scoreboard players add @s gl_ser_blue 0
scoreboard players add @s gl_ser_violet 0
scoreboard players add @s gl_ser_indigo 0
scoreboard players add @s gl_ser_white 0
scoreboard players add @s gl_ser_black 0
execute if predicate final_lanterns:held/green_offhand if score @s gl_ser_green matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/green_offhand if score @s gl_ser_green matches 0 if entity @s[tag=gl_legacy_green] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/yellow_offhand if score @s gl_ser_yellow matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/yellow_offhand if score @s gl_ser_yellow matches 0 if entity @s[tag=gl_legacy_yellow] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/red_offhand if score @s gl_ser_red matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/red_offhand if score @s gl_ser_red matches 0 if entity @s[tag=gl_legacy_red] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/orange_offhand if score @s gl_ser_orange matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/orange_offhand if score @s gl_ser_orange matches 0 if entity @s[tag=gl_legacy_orange] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/blue_offhand if score @s gl_ser_blue matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/blue_offhand if score @s gl_ser_blue matches 0 if entity @s[tag=gl_legacy_blue] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/violet_offhand if score @s gl_ser_violet matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/violet_offhand if score @s gl_ser_violet matches 0 if entity @s[tag=gl_legacy_violet] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/indigo_offhand if score @s gl_ser_indigo matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/indigo_offhand if score @s gl_ser_indigo matches 0 if entity @s[tag=gl_legacy_indigo] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/white_offhand if score @s gl_ser_white matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/white_offhand if score @s gl_ser_white matches 0 if entity @s[tag=gl_legacy_white] run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/black_offhand if score @s gl_ser_black matches 1.. run scoreboard players set #keep gl_tmp 1
execute if predicate final_lanterns:held/black_offhand if score @s gl_ser_black matches 0 if entity @s[tag=gl_legacy_black] run scoreboard players set #keep gl_tmp 1
execute if score #keep gl_tmp matches 0 run function final_lanterns:ring/giver_drop_offhand
