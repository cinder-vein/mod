execute unless entity @s[tag=gl_u_blue_melee_1] run title @s actionbar [{"text":"Sword & Shield isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_melee_1] run function greenlantern:construct/blue/sword_shield_try
