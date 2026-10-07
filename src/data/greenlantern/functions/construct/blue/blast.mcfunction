execute unless entity @s[tag=gl_u_blue_constructs] run title @s actionbar [{"text":"Blast isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_constructs] run function greenlantern:construct/blue/blast_try
