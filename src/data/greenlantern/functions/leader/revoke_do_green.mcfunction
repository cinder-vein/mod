function greenlantern:ring/strip_green
tag @s add gl_revoked
execute if score #stripped gl_tmp matches 1.. as @a[tag=gl_revoker,limit=1] at @s run function greenlantern:leader/give_revoked_green
tellraw @s [{"text":"Your corps leader has revoked your ring.","color":"#2EC846"}]
tellraw @a[tag=gl_revoker] [{"text":"You revoked the ring of ","color":"#2EC846"},{"selector":"@s"},{"text":". It is unbound and won't bind to you: hand it to your next recruit.","color":"#2EC846"}]
particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 1
