execute unless entity @s[tag=gl_u_blue_utility_2] run title @s actionbar [{"text":"Bridge isn't unlocked yet. Buy ","color":"gray"},{"text":"Utility Constructs II","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_utility_2] run function greenlantern:construct/blue/bridge_try
