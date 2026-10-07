execute unless entity @s[tag=gl_u_white_melee_1] run title @s actionbar [{"text":"Mace isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"#EBF2FA"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_white_melee_1] run function greenlantern:construct/white/mace_try
