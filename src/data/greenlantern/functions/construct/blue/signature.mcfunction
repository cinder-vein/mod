execute unless entity @s[tag=gl_u_blue_signature] run title @s actionbar [{"text":"Sanctuary isn't unlocked yet. Buy ","color":"gray"},{"text":"Sanctuary","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_signature] run function greenlantern:construct/blue/signature_try
