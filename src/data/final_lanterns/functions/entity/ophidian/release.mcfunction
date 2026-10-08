function final_lanterns:entity/ophidian/strip
scoreboard players set #state_ophidian gl_ent 0
scoreboard players set #host_ophidian gl_ent 0
particle minecraft:dust 0.98 0.51 0.08 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"Ophidian leaves you and returns to the world.","color":"#FA8214"}]
