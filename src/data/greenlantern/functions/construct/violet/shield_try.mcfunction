scoreboard players set #have gl_tmp 0
execute store result score #h gl_tmp run clear @s greenlantern:construct_shield 0
scoreboard players operation #have gl_tmp += #h gl_tmp
execute if score #have gl_tmp matches 1.. run function greenlantern:construct/violet/shield_dismiss
execute if score #have gl_tmp matches 0 run function greenlantern:construct/violet/shield_check
