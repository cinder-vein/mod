execute unless entity @s[tag=gl_u_yellow_constructs] run title @s actionbar [{"text":"Blast isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#F5CD1E"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_yellow_constructs] run function greenlantern:construct/yellow/blast_try
