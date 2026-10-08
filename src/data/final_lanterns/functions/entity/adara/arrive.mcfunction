scoreboard players set #state_adara gl_ent 1
scoreboard players add #ser_adara gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_adara gl_ent
scoreboard players set #life_adara gl_ent 600
scoreboard players set #miss_adara gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
title @s times 10 60 20
title @s subtitle {"text": "A blue bird of light circles above you. Hope has found you.", "color": "gray"}
title @s title {"text": "Adara", "color": "#2882FF", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
