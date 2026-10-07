execute unless entity @s[tag=gl_u_orange_defense_1] run title @s actionbar [{"text":"Barrier Wall isn't unlocked yet. Buy ","color":"gray"},{"text":"Defense Constructs I","color":"#FA8214"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_orange_defense_1] run function greenlantern:construct/orange/barrier_try
