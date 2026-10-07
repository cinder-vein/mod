execute if entity @s[tag=gl_eoffer_adara] run tellraw @s ["",{"text":"Adara turns away from you.","color":"#2882FF","italic":true}]
tag @s remove gl_eoffer_adara
scoreboard players set @s gl_edc_adara 1800
