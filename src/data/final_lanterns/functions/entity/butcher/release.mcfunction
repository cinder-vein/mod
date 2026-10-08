function final_lanterns:entity/butcher/strip
scoreboard players set #state_butcher gl_ent 0
scoreboard players set #host_butcher gl_ent 0
particle minecraft:dust 0.86 0.12 0.14 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"The Butcher leaves you and returns to the world.","color":"#DC1E23"}]
