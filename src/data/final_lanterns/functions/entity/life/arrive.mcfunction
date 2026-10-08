scoreboard players set #state_life gl_ent 1
scoreboard players add #ser_life gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_life gl_ent
scoreboard players set #life_life gl_ent 600
scoreboard players set #miss_life gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
title @s times 10 60 20
title @s subtitle {"text": "The Life Entity descends: every color of the spectrum shines in you.", "color": "gray"}
title @s title {"text": "The Life Entity", "color": "#EBF2FA", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
