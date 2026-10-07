energybar value subtract @s greenlantern:blue_lantern ring_charge 60
scoreboard players set @s gl_cc_blocks 40
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Construct Blocks","color":"#2882FF"}]
tag @s add gl_user
give @s greenlantern:blue_construct_block 64
particle minecraft:dust 0.16 0.51 1.00 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.amethyst_block.chime player @a[distance=..24] ~ ~ ~ 1 1.4
tag @s remove gl_user
