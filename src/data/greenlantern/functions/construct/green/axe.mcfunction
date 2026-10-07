execute unless entity @s[tag=gl_u_green_melee_1] run title @s actionbar [{"text":"Battle Axe isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"#2EC846"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_green_melee_1] run function greenlantern:construct/green/axe_try
