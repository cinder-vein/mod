scoreboard players set #hit gl_tmp 1
energybar value add @s final_lanterns:pinklantern love 1000
particle minecraft:dust 0.84 0.22 0.86 1.5 ~ ~1 ~ 0.4 0.8 0.4 0 60 force
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.6
title @s actionbar [{"text": "The Predator's light fills your ring.", "color": "#D737DC"}]
