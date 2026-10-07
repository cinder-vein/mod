execute unless entity @s[tag=gl_u_red_melee_1] run title @s actionbar [{"text":"Sword & Shield isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"#DC1E23"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_red_melee_1] run function greenlantern:construct/red/sword_shield_try
