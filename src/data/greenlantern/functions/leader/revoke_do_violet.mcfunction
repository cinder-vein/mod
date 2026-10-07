function greenlantern:ring/strip_violet
tag @s add gl_revoked
execute if score #stripped gl_tmp matches 1.. as @a[tag=gl_revoker,limit=1] at @s run function greenlantern:leader/give_revoked_violet
tellraw @s [{"text":"Your corps leader has revoked your ring.","color":"#D737DC"}]
tellraw @a[tag=gl_revoker] [{"text":"You revoked the ring of ","color":"#D737DC"},{"selector":"@s"},{"text":". It is unbound and won't bind to you: hand it to your next recruit.","color":"#D737DC"}]
particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 1
