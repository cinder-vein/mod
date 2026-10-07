tag @s add gl_eoffer_proselyte
scoreboard players set @s gl_eofft 60
scoreboard players enable @s gl_entity
tellraw @s ["",{"text":"\nThe Proselyte","color":"#693CE6","bold":true},{"text":", the compassion entity, senses the strength of your compassion and offers to make you its host. ","color":"gray"},{"text":"[ACCEPT]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 7"}},{"text":"  "},{"text":"[DECLINE]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 17"}}]
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 0.7
