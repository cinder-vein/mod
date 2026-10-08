execute if entity @s[tag=gl_eoffer_butcher] run tellraw @s ["",{"text":"The Butcher turns away from you.","color":"#DC1E23","italic":true}]
tag @s remove gl_eoffer_butcher
scoreboard players set @s gl_edc_butcher 1800
