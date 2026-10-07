function greenlantern:ring/strip_orange
tag @s add gl_revoked
execute if score #stripped gl_tmp matches 1.. run give @a[tag=gl_revoker,limit=1] greenlantern:orange_lantern_ring
tellraw @s [{"text":"Your corps leader has revoked your ring.","color":"#FA8214"}]
tellraw @a[tag=gl_revoker] [{"text":"You revoked the ring of ","color":"#FA8214"},{"selector":"@s"},{"text":". It is unbound and yours to pass on.","color":"#FA8214"}]
particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0.05 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 1
