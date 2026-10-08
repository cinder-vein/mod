execute unless entity @s[tag=gl_host] run tellraw @s ["",{"text":"You host no entity.","color":"gray"}]
scoreboard players enable @s gl_entity
execute if entity @s[tag=gl_host] run tellraw @s ["",{"text":"Give up the entity you host? Its powers leave with it. ","color":"gray"},{"text":"[RELEASE IT]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_entity set 40"}}]
