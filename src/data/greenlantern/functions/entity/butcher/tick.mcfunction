execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_butcher,limit=1] Rotation
execute store result bossbar greenlantern:butcher value run data get entity @s Health
bossbar set greenlantern:butcher players @a[distance=..64]
execute store result score #hp gl_tmp run data get entity @s Health
execute if score #hp gl_tmp matches ..60 run function greenlantern:entity/butcher/yield
