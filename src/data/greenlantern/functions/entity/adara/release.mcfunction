function greenlantern:entity/adara/strip
scoreboard players set #state_adara gl_ent 0
scoreboard players set #host_adara gl_ent 0
scoreboard players set @s gl_edc_adara 3600
particle minecraft:dust 0.16 0.51 1.00 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"Adara leaves you and returns to the world.","color":"#2882FF"}]
