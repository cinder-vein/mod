execute unless entity @s[tag=gl_u_indigo_utility_1] run title @s actionbar [{"text":"Scuba Gear isn't unlocked yet. Buy ","color":"gray"},{"text":"Utility Constructs I","color":"#693CE6"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_indigo_utility_1] run function greenlantern:construct/indigo/scuba_try
