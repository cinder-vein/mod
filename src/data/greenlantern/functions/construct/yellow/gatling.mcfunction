execute unless entity @s[tag=gl_u_yellow_ranged_1] run title @s actionbar [{"text":"Gatling isn't unlocked yet. Buy ","color":"gray"},{"text":"Ranged Constructs I","color":"#F5CD1E"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_yellow_ranged_1] run function greenlantern:construct/yellow/gatling_try
