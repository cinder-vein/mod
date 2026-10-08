function final_lanterns:ring/strip_black
tag @s add gl_revoked
execute if score #stripped gl_tmp matches 1.. as @a[tag=gl_revoker,limit=1] at @s run function final_lanterns:leader/give_revoked_black
tellraw @s [{"text":"Your corps leader has revoked your ring.","color":"#AAAFBE"}]
tellraw @a[tag=gl_revoker] [{"text":"You revoked the ring of ","color":"#AAAFBE"},{"selector":"@s"},{"text":". It is unbound and won't bind to you: hand it to your next recruit.","color":"#AAAFBE"}]
particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 1
