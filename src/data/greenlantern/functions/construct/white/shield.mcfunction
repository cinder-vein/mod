execute unless entity @s[tag=gl_u_white_constructs] run title @s actionbar [{"text":"Tower Shield isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#EBF2FA"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_white_constructs] run function greenlantern:construct/white/shield_try
