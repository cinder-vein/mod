execute unless entity @s[tag=gl_u_black_melee_2] run title @s actionbar [{"text":"Hammer Slam isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs II","color":"#AAAFBE"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_black_melee_2] run function greenlantern:construct/black/slam_try
