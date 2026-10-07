effect give @s minecraft:slowness 6 2 true
effect give @s minecraft:nausea 8 0 true
effect give @s minecraft:strength 6 1 true
particle minecraft:heart ~ ~2 ~ 0.5 0.5 0.5 0 10 force
scoreboard players remove @s[scores={gl_e_compassion=150..}] gl_e_compassion 150
particle minecraft:dust 0.84 0.22 0.86 2.0 ~ ~1 ~ 0.6 1 0.6 0 80 force
title @s times 5 40 10
title @s title {"text": "The Predator takes control", "color": "#D737DC"}
playsound minecraft:entity.warden.heartbeat player @a[distance=..24] ~ ~ ~ 1 0.8
