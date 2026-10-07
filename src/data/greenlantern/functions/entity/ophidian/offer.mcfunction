tag @s add gl_eoffer_ophidian
scoreboard players set @s gl_eofft 60
scoreboard players enable @s gl_entity
tellraw @s ["",{"text":"\nOphidian","color":"#FA8214","bold":true},{"text":", the avarice entity, senses the strength of your greed and offers to make you its host. ","color":"gray"},{"text":"[ACCEPT]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 4"}},{"text":"  "},{"text":"[DECLINE]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 14"}}]
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 0.7
