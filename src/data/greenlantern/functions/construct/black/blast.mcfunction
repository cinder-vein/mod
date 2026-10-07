execute unless entity @s[tag=gl_u_black_constructs] run title @s actionbar [{"text":"Blast isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#AAAFBE"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_black_constructs] run function greenlantern:construct/black/blast_try
