function final_lanterns:entity/ion/strip
scoreboard players set #state_ion gl_ent 0
scoreboard players set #host_ion gl_ent 0
particle minecraft:dust 0.18 0.78 0.27 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"Ion leaves you and returns to the world.","color":"#2EC846"}]
