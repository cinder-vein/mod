scoreboard players set #state_butcher gl_ent 1
scoreboard players add #ser_butcher gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_butcher gl_ent
scoreboard players set #life_butcher gl_ent 1200
scoreboard players set #miss_butcher gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
title @s times 10 60 20
title @s subtitle {"text": "The Butcher has come for blood!", "color": "gray"}
title @s title {"text": "The Butcher", "color": "#DC1E23", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
