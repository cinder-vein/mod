execute unless entity @s[tag=gl_u_indigo_constructs] run title @s actionbar [{"text":"Scan isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#693CE6"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_indigo_constructs] run function greenlantern:construct/indigo/scan_try
