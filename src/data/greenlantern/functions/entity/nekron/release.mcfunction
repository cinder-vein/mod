function greenlantern:entity/nekron/strip
scoreboard players set #state_nekron gl_ent 0
scoreboard players set #host_nekron gl_ent 0
scoreboard players set @s gl_edc_nekron 3600
particle minecraft:dust 0.59 0.61 0.67 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"Nekron leaves you and returns to the world.","color":"#969BAA"}]
