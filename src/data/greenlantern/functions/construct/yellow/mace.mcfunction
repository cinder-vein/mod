execute unless entity @s[tag=gl_u_yellow_melee_1] run title @s actionbar [{"text":"Mace isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"#F5CD1E"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_yellow_melee_1] run function greenlantern:construct/yellow/mace_try
