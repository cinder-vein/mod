execute unless entity @s[tag=gl_u_orange_signature] run title @s actionbar [{"text":"Grasping Hands isn't unlocked yet. Buy ","color":"gray"},{"text":"Grasping Hands","color":"#FA8214"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_orange_signature] run function greenlantern:construct/orange/signature_try
