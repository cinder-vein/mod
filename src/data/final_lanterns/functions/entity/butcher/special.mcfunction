execute at @s run particle minecraft:dust 0.86 0.12 0.14 2.5 ~ ~1 ~ 3 1 3 0 150 force
execute at @s as @a[distance=..7] run damage @s 8 minecraft:mob_attack by @e[tag=gl_ent_butcher,limit=1]
execute at @s run effect give @a[distance=..7] minecraft:levitation 1 3 true
execute at @s run effect give @a[distance=..7] minecraft:wither 4 0 true
execute at @s run playsound minecraft:entity.ravager.roar player @a[distance=..24] ~ ~ ~ 1 0.6
