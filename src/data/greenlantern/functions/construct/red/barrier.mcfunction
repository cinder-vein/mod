execute unless entity @s[tag=gl_u_red_defense_1] run title @s actionbar [{"text":"Barrier Wall isn't unlocked yet. Buy ","color":"gray"},{"text":"Defense Constructs I","color":"#DC1E23"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_red_defense_1] run function greenlantern:construct/red/barrier_try
