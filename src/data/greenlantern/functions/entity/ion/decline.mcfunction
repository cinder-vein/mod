execute if entity @s[tag=gl_eoffer_ion] run tellraw @s ["",{"text":"Ion turns away from you.","color":"#2EC846","italic":true}]
tag @s remove gl_eoffer_ion
scoreboard players set @s gl_edc_ion 1800
