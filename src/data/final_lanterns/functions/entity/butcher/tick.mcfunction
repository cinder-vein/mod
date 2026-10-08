execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_butcher,limit=1] Rotation
execute store result bossbar final_lanterns:butcher value run data get entity @s Health
bossbar set final_lanterns:butcher players @a[distance=..64]
execute store result score #hp gl_tmp run data get entity @s Health
execute if score #hp gl_tmp matches ..60 run function final_lanterns:entity/butcher/yield
