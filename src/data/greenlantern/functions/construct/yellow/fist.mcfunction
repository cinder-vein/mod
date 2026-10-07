execute unless entity @s[tag=gl_u_yellow_melee_2] run title @s actionbar [{"text":"Giant Fist isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs II","color":"#F5CD1E"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_yellow_melee_2] run function greenlantern:construct/yellow/fist_try
