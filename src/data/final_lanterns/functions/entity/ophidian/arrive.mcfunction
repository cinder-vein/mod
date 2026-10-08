scoreboard players set #state_ophidian gl_ent 1
scoreboard players add #ser_ophidian gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_ophidian gl_ent
scoreboard players set #life_ophidian gl_ent 600
scoreboard players set #miss_ophidian gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
title @s times 10 60 20
title @s subtitle {"text": "A great serpent coils in the dark, eyeing your treasure. Throw it a block of gold.", "color": "gray"}
title @s title {"text": "Ophidian", "color": "#FA8214", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
