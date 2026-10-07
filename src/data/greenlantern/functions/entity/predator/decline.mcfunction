execute if entity @s[tag=gl_eoffer_predator] run tellraw @s ["",{"text":"The Predator turns away from you.","color":"#D737DC","italic":true}]
tag @s remove gl_eoffer_predator
scoreboard players set @s gl_edc_predator 1800
