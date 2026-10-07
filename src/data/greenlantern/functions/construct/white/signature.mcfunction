execute unless entity @s[tag=gl_u_white_signature] run title @s actionbar [{"text":"Radiant Aegis isn't unlocked yet. Buy ","color":"gray"},{"text":"Radiant Aegis","color":"#EBF2FA"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_white_signature] run function greenlantern:construct/white/signature_try
