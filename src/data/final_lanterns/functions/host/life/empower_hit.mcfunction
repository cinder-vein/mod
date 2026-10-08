scoreboard players set #hit gl_tmp 1
energybar value add @s final_lanterns:whitelantern life 1000
particle minecraft:dust 0.92 0.95 0.98 1.5 ~ ~1 ~ 0.4 0.8 0.4 0 60 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.6
title @s actionbar [{"text": "The Life Entity's light fills your ring.", "color": "#EBF2FA"}]
