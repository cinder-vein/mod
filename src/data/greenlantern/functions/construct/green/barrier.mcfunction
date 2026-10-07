execute unless entity @s[tag=gl_u_green_defense_1] run title @s actionbar [{"text":"Barrier Wall isn't unlocked yet. Buy ","color":"gray"},{"text":"Defense Constructs I","color":"#2EC846"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_green_defense_1] run function greenlantern:construct/green/barrier_try
