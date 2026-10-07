execute if entity @s[tag=gl_eoffer_ophidian] run tellraw @s ["",{"text":"Ophidian turns away from you.","color":"#FA8214","italic":true}]
tag @s remove gl_eoffer_ophidian
scoreboard players set @s gl_edc_ophidian 1800
