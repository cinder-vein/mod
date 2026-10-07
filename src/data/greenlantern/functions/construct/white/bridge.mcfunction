execute unless entity @s[tag=gl_u_white_utility_2] run title @s actionbar [{"text":"Bridge isn't unlocked yet. Buy ","color":"gray"},{"text":"Utility Constructs II","color":"#EBF2FA"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_white_utility_2] run function greenlantern:construct/white/bridge_try
