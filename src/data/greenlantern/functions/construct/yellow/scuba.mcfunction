execute unless entity @s[tag=gl_u_yellow_utility_1] run title @s actionbar [{"text":"Scuba Gear isn't unlocked yet. Buy ","color":"gray"},{"text":"Utility Constructs I","color":"#F5CD1E"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_yellow_utility_1] run function greenlantern:construct/yellow/scuba_try
