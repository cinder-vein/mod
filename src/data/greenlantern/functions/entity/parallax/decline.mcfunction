execute if entity @s[tag=gl_eoffer_parallax] run tellraw @s ["",{"text":"Parallax turns away from you.","color":"#F5CD1E","italic":true}]
tag @s remove gl_eoffer_parallax
scoreboard players set @s gl_edc_parallax 1800
