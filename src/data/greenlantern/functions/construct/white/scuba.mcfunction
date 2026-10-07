execute unless entity @s[tag=gl_u_white_utility_1] run title @s actionbar [{"text":"Scuba Gear isn't unlocked yet. Buy ","color":"gray"},{"text":"Utility Constructs I","color":"#EBF2FA"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_white_utility_1] run function greenlantern:construct/white/scuba_try
