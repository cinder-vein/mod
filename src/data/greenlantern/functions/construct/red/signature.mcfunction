execute unless entity @s[tag=gl_u_red_signature] run title @s actionbar [{"text":"Blood Claws isn't unlocked yet. Buy ","color":"gray"},{"text":"Blood Claws","color":"#DC1E23"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_red_signature] run function greenlantern:construct/red/signature_try
