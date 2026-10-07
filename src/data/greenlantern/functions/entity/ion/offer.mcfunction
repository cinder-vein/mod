tag @s add gl_eoffer_ion
scoreboard players set @s gl_eofft 60
scoreboard players enable @s gl_entity
tellraw @s ["",{"text":"\nIon","color":"#2EC846","bold":true},{"text":", the willpower entity, senses the strength of your will and offers to make you its host. ","color":"gray"},{"text":"[ACCEPT]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 1"}},{"text":"  "},{"text":"[DECLINE]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 11"}}]
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 0.7
