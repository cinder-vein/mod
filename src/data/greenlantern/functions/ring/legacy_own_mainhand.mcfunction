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
execute if predicate greenlantern:held/green_mainhand if score @s gl_ser_green matches 0 if entity @s[tag=gl_member_green] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/yellow_mainhand if score @s gl_ser_yellow matches 0 if entity @s[tag=gl_member_yellow] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/red_mainhand if score @s gl_ser_red matches 0 if entity @s[tag=gl_member_red] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/orange_mainhand if score @s gl_ser_orange matches 0 if entity @s[tag=gl_member_orange] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/blue_mainhand if score @s gl_ser_blue matches 0 if entity @s[tag=gl_member_blue] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/violet_mainhand if score @s gl_ser_violet matches 0 if entity @s[tag=gl_member_violet] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/indigo_mainhand if score @s gl_ser_indigo matches 0 if entity @s[tag=gl_member_indigo] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/white_mainhand if score @s gl_ser_white matches 0 if entity @s[tag=gl_member_white] run scoreboard players set #keep gl_tmp 1
execute if predicate greenlantern:held/black_mainhand if score @s gl_ser_black matches 0 if entity @s[tag=gl_member_black] run scoreboard players set #keep gl_tmp 1
execute if score #keep gl_tmp matches 1 run function greenlantern:ring/rebind_mainhand
execute if score #keep gl_tmp matches 0 run function greenlantern:ring/dark_mainhand
