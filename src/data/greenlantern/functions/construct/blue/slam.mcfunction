execute unless entity @s[tag=gl_u_blue_melee_2] run title @s actionbar [{"text":"Hammer Slam isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs II","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_melee_2] run function greenlantern:construct/blue/slam_try
