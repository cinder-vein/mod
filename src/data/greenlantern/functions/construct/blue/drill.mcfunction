execute unless entity @s[tag=gl_u_blue_utility_1] run title @s actionbar [{"text":"Mining Drill isn't unlocked yet. Buy ","color":"gray"},{"text":"Utility Constructs I","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_utility_1] run function greenlantern:construct/blue/drill_try
