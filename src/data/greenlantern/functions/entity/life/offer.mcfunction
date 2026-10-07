tag @s add gl_eoffer_life
scoreboard players set @s gl_eofft 60
scoreboard players enable @s gl_entity
tellraw @s ["",{"text":"\nThe Life Entity","color":"#EBF2FA","bold":true},{"text":", the entity of life itself, senses the strength of your spirit and offers to make you its host. ","color":"gray"},{"text":"[ACCEPT]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 8"}},{"text":"  "},{"text":"[DECLINE]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 18"}}]
playsound minecraft:block.amethyst_block.resonate player @a[distance=..24] ~ ~ ~ 1 0.7
