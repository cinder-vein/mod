execute unless entity @s[tag=gl_u_indigo_signature] run title @s actionbar [{"text":"Indigo Staff isn't unlocked yet. Buy ","color":"gray"},{"text":"Indigo Staff","color":"#693CE6"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_indigo_signature] run function greenlantern:construct/indigo/signature_try
