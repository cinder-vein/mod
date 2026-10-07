execute if entity @s[tag=gl_eoffer_life] run tellraw @s ["",{"text":"The Life Entity turns away from you.","color":"#EBF2FA","italic":true}]
tag @s remove gl_eoffer_life
scoreboard players set @s gl_edc_life 1800
