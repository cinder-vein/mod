scoreboard players set #done gl_tmp 0
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_green] run function greenlantern:forge/recite_green
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_yellow] run function greenlantern:forge/recite_yellow
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_red] run function greenlantern:forge/recite_red
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_orange] run function greenlantern:forge/recite_orange
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_blue] run function greenlantern:forge/recite_blue
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_violet] run function greenlantern:forge/recite_violet
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_indigo] run function greenlantern:forge/recite_indigo
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_white] run function greenlantern:forge/recite_white
execute if score #done gl_tmp matches 0 if entity @s[tag=gl_black] run function greenlantern:forge/recite_black
execute if score #done gl_tmp matches 0 run tellraw @s [{"text":"Wear your ring to forge another.","color":"gray"}]
