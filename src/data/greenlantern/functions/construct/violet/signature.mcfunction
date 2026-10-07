execute unless entity @s[tag=gl_u_violet_signature] run title @s actionbar [{"text":"Crystal Spear isn't unlocked yet. Buy ","color":"gray"},{"text":"Crystal Spear","color":"#D737DC"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_violet_signature] run function greenlantern:construct/violet/signature_try
