execute unless entity @s[tag=gl_u_blue_ranged_1] run title @s actionbar [{"text":"Gatling isn't unlocked yet. Buy ","color":"gray"},{"text":"Ranged Constructs I","color":"#2882FF"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_blue_ranged_1] run function greenlantern:construct/blue/gatling_try
