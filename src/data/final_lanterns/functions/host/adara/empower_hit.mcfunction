scoreboard players set #hit gl_tmp 1
energybar value add @s final_lanterns:bluelantern hope 1000
particle minecraft:dust 0.16 0.51 1.00 1.5 ~ ~1 ~ 0.4 0.8 0.4 0 60 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.6
title @s actionbar [{"text": "Adara's light fills your ring.", "color": "#2882FF"}]
