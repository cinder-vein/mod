execute unless entity @s[tag=gl_u_green_ranged_1] run title @s actionbar [{"text":"Missile Barrage isn't unlocked yet. Buy ","color":"gray"},{"text":"Ranged Constructs I","color":"#2EC846"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_green_ranged_1] run function greenlantern:construct/green/missiles_try
