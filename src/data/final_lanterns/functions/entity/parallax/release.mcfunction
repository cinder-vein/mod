function final_lanterns:entity/parallax/strip
scoreboard players set #state_parallax gl_ent 0
scoreboard players set #host_parallax gl_ent 0
particle minecraft:dust 0.96 0.80 0.12 3.0 ~ ~1 ~ 1 2 1 0 200 force
playsound minecraft:block.beacon.deactivate player @a[distance=..24] ~ ~ ~ 1 0.6
tellraw @s ["",{"text":"Parallax leaves you and returns to the world.","color":"#F5CD1E"}]
