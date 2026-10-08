kill @s
tag @e[tag=gl_ent_ophidian] add gl_ent_fed
execute at @e[tag=gl_ent_ophidian] run particle minecraft:wax_on ~ ~1 ~ 1 1 1 0 40 force
playsound minecraft:entity.player.burp player @a[distance=..24] ~ ~ ~ 1 0.5
