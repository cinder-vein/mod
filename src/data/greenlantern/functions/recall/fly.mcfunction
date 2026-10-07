scoreboard players set #found gl_tmp 2
data merge entity @s {PickupDelay:0s,Age:-32768s}
execute at @s run particle minecraft:end_rod ~ ~0.5 ~ 0.2 0.2 0.2 0.05 20 force
execute at @a[tag=gl_caller,limit=1] run tp @s ~ ~0.5 ~
