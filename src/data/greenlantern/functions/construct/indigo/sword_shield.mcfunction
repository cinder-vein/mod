execute unless entity @s[tag=gl_u_indigo_melee_1] run title @s actionbar [{"text":"Sword & Shield isn't unlocked yet. Buy ","color":"gray"},{"text":"Melee Constructs I","color":"#693CE6"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_indigo_melee_1] run function greenlantern:construct/indigo/sword_shield_try
