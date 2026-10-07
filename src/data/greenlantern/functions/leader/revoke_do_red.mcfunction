function greenlantern:ring/strip_red
tag @s add gl_revoked
execute if score #stripped gl_tmp matches 1.. run give @a[tag=gl_revoker,limit=1] greenlantern:red_lantern_ring
tellraw @s [{"text":"Your corps leader has revoked your ring.","color":"#DC1E23"}]
tellraw @a[tag=gl_revoker] [{"text":"You revoked the ring of ","color":"#DC1E23"},{"selector":"@s"},{"text":". It is unbound and yours to pass on.","color":"#DC1E23"}]
particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 1
