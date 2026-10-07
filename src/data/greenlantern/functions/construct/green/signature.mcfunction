execute unless entity @s[tag=gl_u_green_signature] run title @s actionbar [{"text":"Construct Train isn't unlocked yet. Buy ","color":"gray"},{"text":"Construct Train","color":"#2EC846"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_green_signature] run function greenlantern:construct/green/signature_try
