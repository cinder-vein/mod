execute unless entity @s[tag=gl_u_indigo_ranged_2] run title @s actionbar [{"text":"Cannon isn't unlocked yet. Buy ","color":"gray"},{"text":"Ranged Constructs II","color":"#693CE6"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_indigo_ranged_2] run function greenlantern:construct/indigo/cannon_try
