execute if entity @s[tag=gl_eoffer_nekron] run tellraw @s ["",{"text":"Nekron turns away from you.","color":"#969BAA","italic":true}]
tag @s remove gl_eoffer_nekron
scoreboard players set @s gl_edc_nekron 1800
