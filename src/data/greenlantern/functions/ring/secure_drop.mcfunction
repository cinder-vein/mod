tag @s add gl_giving
execute as @e[type=minecraft:item,distance=..1.5,nbt={Item:{tag:{gl_bound:1b}}},limit=1,sort=nearest] run function greenlantern:ring/secure_item
tag @s remove gl_giving
tellraw @s [{"text":"Your inventory is full: your ring waits at your feet.","color":"gray"}]
