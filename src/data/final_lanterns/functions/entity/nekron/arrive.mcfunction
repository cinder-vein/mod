scoreboard players set #state_nekron gl_ent 1
scoreboard players add #ser_nekron gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_nekron gl_ent
scoreboard players set #life_nekron gl_ent 1200
scoreboard players set #miss_nekron gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
title @s times 10 60 20
title @s subtitle {"text": "Nekron rises from the deep dark!", "color": "gray"}
title @s title {"text": "Nekron", "color": "#969BAA", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
