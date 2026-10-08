playsound minecraft:entity.experience_orb.pickup player @s
scoreboard players add @s rings_sacrificed 1
title @s actionbar [{"text":"Rings Sacrificed ","color":"gold","bold":true},{"score":{"name":"@s","objective":"rings_sacrificed"},"color":"gold","bold":true},{"text":"/10 ","color":"gold","bold":true}]
