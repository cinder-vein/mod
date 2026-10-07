execute unless entity @s[tag=gl_u_violet_constructs] run title @s actionbar [{"text":"Sword isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#D737DC"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_violet_constructs] run function greenlantern:construct/violet/sword_try
