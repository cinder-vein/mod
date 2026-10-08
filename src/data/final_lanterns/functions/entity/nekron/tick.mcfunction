execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_nekron,limit=1] Rotation
execute store result bossbar final_lanterns:nekron value run data get entity @s Health
bossbar set final_lanterns:nekron players @a[distance=..64]
execute store result score #hp gl_tmp run data get entity @s Health
execute if score #hp gl_tmp matches ..48 run function final_lanterns:entity/nekron/yield
