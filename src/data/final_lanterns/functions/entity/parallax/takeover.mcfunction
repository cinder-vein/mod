effect give @s minecraft:darkness 6 0 true
effect give @s minecraft:nausea 8 0 true
effect give @a[distance=0.1..8] minecraft:darkness 6 0 true
effect give @a[distance=0.1..8] minecraft:slowness 6 1 true
scoreboard players remove @s[scores={gl_e_will=150..}] gl_e_will 150
particle minecraft:dust 0.96 0.80 0.12 2.0 ~ ~1 ~ 0.6 1 0.6 0 80 force
title @s times 5 40 10
title @s title {"text": "Parallax takes control", "color": "#F5CD1E"}
playsound minecraft:entity.warden.heartbeat player @a[distance=..24] ~ ~ ~ 1 0.8
