tag @s add gl_eoffer_adara
scoreboard players set @s gl_eofft 60
scoreboard players enable @s gl_entity
tellraw @s ["",{"text":"\nAdara","color":"#2882FF","bold":true},{"text":", the hope entity, senses the strength of your hope and offers to make you its host. ","color":"gray"},{"text":"[ACCEPT]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 5"}},{"text":"  "},{"text":"[DECLINE]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 15"}}]
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 0.7
