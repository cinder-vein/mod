execute store result score #slot gl_tmp run data get storage final_lanterns:binding cur.Slot
execute unless score #slot gl_tmp matches 0..35 run scoreboard players set #corps gl_tmp 0
scoreboard players set #giver gl_tmp 0
execute if data storage final_lanterns:binding cur.tag{gl_gv:1b} store result score #giver gl_tmp run data get storage final_lanterns:binding cur.tag.gl_giver
execute if score #giver gl_tmp = @s gl_id run scoreboard players set #corps gl_tmp 0
scoreboard players add @s gl_ser_green 0
scoreboard players add @s gl_ser_yellow 0
scoreboard players add @s gl_ser_red 0
scoreboard players add @s gl_ser_orange 0
scoreboard players add @s gl_ser_blue 0
scoreboard players add @s gl_ser_violet 0
scoreboard players add @s gl_ser_indigo 0
scoreboard players add @s gl_ser_white 0
scoreboard players add @s gl_ser_black 0
execute if score #corps gl_tmp matches 1 if score @s gl_ser_green matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 1 if score @s gl_ser_green matches 0 if entity @s[tag=gl_legacy_green] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 2 if score @s gl_ser_yellow matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 2 if score @s gl_ser_yellow matches 0 if entity @s[tag=gl_legacy_yellow] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 3 if score @s gl_ser_red matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 3 if score @s gl_ser_red matches 0 if entity @s[tag=gl_legacy_red] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 4 if score @s gl_ser_orange matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 4 if score @s gl_ser_orange matches 0 if entity @s[tag=gl_legacy_orange] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 5 if score @s gl_ser_blue matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 5 if score @s gl_ser_blue matches 0 if entity @s[tag=gl_legacy_blue] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 6 if score @s gl_ser_violet matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 6 if score @s gl_ser_violet matches 0 if entity @s[tag=gl_legacy_violet] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 7 if score @s gl_ser_indigo matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 7 if score @s gl_ser_indigo matches 0 if entity @s[tag=gl_legacy_indigo] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 8 if score @s gl_ser_white matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 8 if score @s gl_ser_white matches 0 if entity @s[tag=gl_legacy_white] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 9 if score @s gl_ser_black matches 1.. run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 9 if score @s gl_ser_black matches 0 if entity @s[tag=gl_legacy_black] run scoreboard players set #corps gl_tmp 0
execute if score #corps gl_tmp matches 1.. run function final_lanterns:ring/carry_bind
