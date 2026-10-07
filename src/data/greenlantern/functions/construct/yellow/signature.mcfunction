execute unless entity @s[tag=gl_u_yellow_signature] run title @s actionbar [{"text":"Fear Spikes isn't unlocked yet. Buy ","color":"gray"},{"text":"Fear Spikes","color":"#F5CD1E"},{"text":" in the powers menu.","color":"gray"}]
execute if entity @s[tag=gl_u_yellow_signature] run function greenlantern:construct/yellow/signature_try
