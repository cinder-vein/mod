function greenlantern:entity/life/strip
scoreboard players set #state_life gl_ent 0
scoreboard players set #host_life gl_ent 0
scoreboard players set @s gl_edc_life 3600
particle minecraft:dust 0.92 0.95 0.98 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"The Life Entity leaves you and returns to the world.","color":"#EBF2FA"}]
