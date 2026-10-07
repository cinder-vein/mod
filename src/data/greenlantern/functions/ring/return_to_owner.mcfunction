tp @e[type=minecraft:item,tag=gl_eject] ~ ~0.5 ~
data merge entity @e[type=minecraft:item,tag=gl_eject,limit=1] {PickupDelay:0s}
particle minecraft:end_rod ~ ~1 ~ 0.3 0.5 0.3 0.05 20 force
tellraw @s [{"text":"Your ring returns to you.","color":"gray","italic":true}]
