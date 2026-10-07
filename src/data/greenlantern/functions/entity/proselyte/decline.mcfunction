execute if entity @s[tag=gl_eoffer_proselyte] run tellraw @s ["",{"text":"The Proselyte turns away from you.","color":"#693CE6","italic":true}]
tag @s remove gl_eoffer_proselyte
scoreboard players set @s gl_edc_proselyte 1800
