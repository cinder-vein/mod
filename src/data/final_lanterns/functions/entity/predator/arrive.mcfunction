scoreboard players set #state_predator gl_ent 1
scoreboard players add #ser_predator gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_predator gl_ent
scoreboard players set #life_predator gl_ent 1200
scoreboard players set #miss_predator gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
tag @a remove gl_hunted_predator
tag @s add gl_hunted_predator
title @s times 10 60 20
title @s subtitle {"text": "Something is stalking you. It wants your heart...", "color": "gray"}
title @s title {"text": "The Predator", "color": "#D737DC", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
