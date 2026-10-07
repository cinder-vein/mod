execute unless entity @s[tag=gl_u_orange_constructs] run title @s actionbar [{"text":"Blast isn't unlocked yet. Buy ","color":"gray"},{"text":"Constructs","color":"#FA8214"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_orange_constructs] run function greenlantern:construct/orange/blast_try
