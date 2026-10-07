execute unless entity @s[tag=gl_u_white_defense_1] run title @s actionbar [{"text":"Cage isn't unlocked yet. Buy ","color":"gray"},{"text":"Defense Constructs I","color":"#EBF2FA"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_white_defense_1] run function greenlantern:construct/white/cage_try
