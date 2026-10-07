function greenlantern:entity/proselyte/strip
scoreboard players set #state_proselyte gl_ent 0
scoreboard players set #host_proselyte gl_ent 0
scoreboard players set @s gl_edc_proselyte 3600
particle minecraft:dust 0.41 0.24 0.90 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"The Proselyte leaves you and returns to the world.","color":"#693CE6"}]
