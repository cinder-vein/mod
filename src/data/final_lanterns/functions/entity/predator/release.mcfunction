function final_lanterns:entity/predator/strip
scoreboard players set #state_predator gl_ent 0
scoreboard players set #host_predator gl_ent 0
particle minecraft:dust 0.84 0.22 0.86 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"The Predator leaves you and returns to the world.","color":"#D737DC"}]
