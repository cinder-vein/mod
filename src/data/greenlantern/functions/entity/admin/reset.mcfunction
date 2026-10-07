scoreboard players set #state_ion gl_ent 0
scoreboard players set #host_ion gl_ent 0
scoreboard players set #state_parallax gl_ent 0
scoreboard players set #host_parallax gl_ent 0
scoreboard players set #state_butcher gl_ent 0
scoreboard players set #host_butcher gl_ent 0
scoreboard players set #state_ophidian gl_ent 0
scoreboard players set #host_ophidian gl_ent 0
scoreboard players set #state_adara gl_ent 0
scoreboard players set #host_adara gl_ent 0
scoreboard players set #state_predator gl_ent 0
scoreboard players set #host_predator gl_ent 0
scoreboard players set #state_proselyte gl_ent 0
scoreboard players set #host_proselyte gl_ent 0
scoreboard players set #state_life gl_ent 0
scoreboard players set #host_life gl_ent 0
scoreboard players set #state_nekron gl_ent 0
scoreboard players set #host_nekron gl_ent 0
execute as @e[tag=gl_ent] at @s run function greenlantern:entity/remove_body
tellraw @s ["",{"text":"Every entity is free again (hosts lose them within a second).","color":"green"}]
