execute unless entity @s[tag=gl_u_red_constructs] run title @s actionbar [{"text":"Scan isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#DC1E23"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_red_constructs] run function greenlantern:construct/red/scan_try
