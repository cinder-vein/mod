scoreboard players operation #v gl_tmp = @s gl_forge
scoreboard players set @s gl_forge 0
scoreboard players enable @s gl_forge
execute if score #v gl_tmp matches 1 run function greenlantern:forge/recite_any
execute if score #v gl_tmp matches 11 run function greenlantern:forge/recite_green
execute if score #v gl_tmp matches 12 run function greenlantern:forge/recite_yellow
execute if score #v gl_tmp matches 13 run function greenlantern:forge/recite_red
execute if score #v gl_tmp matches 14 run function greenlantern:forge/recite_orange
execute if score #v gl_tmp matches 15 run function greenlantern:forge/recite_blue
execute if score #v gl_tmp matches 16 run function greenlantern:forge/recite_violet
execute if score #v gl_tmp matches 17 run function greenlantern:forge/recite_indigo
execute if score #v gl_tmp matches 18 run function greenlantern:forge/recite_white
execute if score #v gl_tmp matches 19 run function greenlantern:forge/recite_black
