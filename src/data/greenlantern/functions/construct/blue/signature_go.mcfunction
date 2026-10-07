energybar value subtract @s greenlantern:blue_lantern ring_charge 250
scoreboard players set @s gl_cc_signature 400
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Sanctuary","color":"#2882FF"}]
tag @s add gl_user
execute align xyz run function greenlantern:construct/blue/dome
effect give @a[distance=..5] minecraft:regeneration 15 1 true
effect give @a[distance=..5] minecraft:resistance 15 1 true
effect give @a[distance=..5] minecraft:instant_health 1 0 true
particle minecraft:dust 0.16 0.51 1.00 2.0 ~ ~1 ~ 3 2 3 0 200 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 1.6
tag @s remove gl_user
