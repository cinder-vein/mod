energybar value subtract @s greenlantern:black_lantern ring_charge 60
scoreboard players set @s gl_cc_blocks 40
tag @s add gl_user
give @s greenlantern:black_construct_block 64
particle minecraft:dust 0.59 0.61 0.67 1.0 ~ ~1.2 ~ 0.3 0.3 0.3 0 30 force
playsound minecraft:block.amethyst_block.chime player @a[distance=..24] ~ ~ ~ 1 1.4
tag @s remove gl_user
title @s actionbar [{"text":"Construct: ","color":"gray"},{"text":"Construct Blocks","color":"#AAAFBE"}]
