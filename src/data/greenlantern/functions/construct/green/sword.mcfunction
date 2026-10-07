execute unless entity @s[tag=gl_u_green_constructs] run title @s actionbar [{"text":"Sword isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#2EC846"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_green_constructs] run function greenlantern:construct/green/sword_try
