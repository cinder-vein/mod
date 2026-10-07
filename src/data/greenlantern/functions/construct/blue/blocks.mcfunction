execute unless entity @s[tag=gl_u_blue_constructs] run title @s actionbar [{"text":"Construct Blocks isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_constructs] run function greenlantern:construct/blue/blocks_try
