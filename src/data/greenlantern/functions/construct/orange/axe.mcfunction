execute unless entity @s[tag=gl_u_orange_melee_1] run title @s actionbar [{"text":"Battle Axe isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"#FA8214"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_orange_melee_1] run function greenlantern:construct/orange/axe_try
