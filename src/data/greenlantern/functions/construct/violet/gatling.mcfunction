execute unless entity @s[tag=gl_u_violet_ranged_1] run title @s actionbar [{"text":"Gatling isn't unlocked yet. Buy ","color":"gray"},{"text":"Ranged Constructs I","color":"#D737DC"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_violet_ranged_1] run function greenlantern:construct/violet/gatling_try
