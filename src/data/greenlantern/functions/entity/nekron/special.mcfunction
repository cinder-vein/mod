execute at @s as @p[distance=..16] at @s run particle minecraft:soul ~ ~1 ~ 0.3 0.6 0.3 0.03 30 force
execute at @s run tp @p[distance=3..16] ^ ^ ^2
execute at @s run effect give @a[distance=..16] minecraft:darkness 6 0 true
execute at @s run effect give @a[distance=..6] minecraft:wither 6 1 true
execute at @s run summon minecraft:zombie ~1 ~ ~ {Tags:["gl_boss_minion","gl_boss_new"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty"}
execute at @s run summon minecraft:skeleton ~-1 ~ ~ {Tags:["gl_boss_minion","gl_boss_new"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty"}
scoreboard players set @e[tag=gl_boss_new] gl_life 600
tag @e[tag=gl_boss_new] remove gl_boss_new
execute at @s run playsound minecraft:entity.wither.ambient player @a[distance=..24] ~ ~ ~ 1 0.6
