execute unless entity @s[tag=gl_u_black_signature] run title @s actionbar [{"text":"Black Hand isn't unlocked yet. Buy ","color":"gray"},{"text":"Black Hand","color":"#AAAFBE"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_black_signature] run function greenlantern:construct/black/signature_try
