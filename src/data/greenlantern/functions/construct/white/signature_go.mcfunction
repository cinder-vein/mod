energybar value subtract @s greenlantern:white_lantern ring_charge 250
scoreboard players set @s gl_cc_signature 400
tag @s add gl_user
effect give @a[distance=..8] minecraft:absorption 30 5 true
effect give @a[distance=..8] minecraft:regeneration 10 0 true
particle minecraft:end_rod ~ ~1 ~ 3 1.5 3 0.02 200 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.6
playsound minecraft:item.totem.use player @a[distance=..24] ~ ~ ~ 1 1.4
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Radiant Aegis","color":"#EBF2FA"}]
