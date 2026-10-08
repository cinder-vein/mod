function final_lanterns:ring/strip_yellow
tag @s add gl_revoked
execute if score #stripped gl_tmp matches 1.. as @a[tag=gl_revoker,limit=1] at @s run function final_lanterns:leader/give_revoked_yellow
tellraw @s [{"text":"Your corps leader has revoked your ring.","color":"#F5CD1E"}]
tellraw @a[tag=gl_revoker] [{"text":"You revoked the ring of ","color":"#F5CD1E"},{"selector":"@s"},{"text":". It is unbound and won't bind to you: hand it to your next recruit.","color":"#F5CD1E"}]
particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 1
