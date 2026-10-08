execute unless entity @s[tag=gl_eoffer_adara] run tellraw @s ["",{"text":"Adara hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_adara] unless score #state_adara gl_ent matches 1 run tellraw @s ["",{"text":"Adara is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_adara,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_adara,tag=!gl_host,scores={gl_ehcd=1..}] run tellraw @s ["",{"text":"No entity will join you yet: you lost one too recently. ","color":"gray"},{"text":"(see your Emotional Spectrum menu)","color":"dark_gray"}]
execute if entity @s[tag=gl_eoffer_adara,tag=!gl_host,scores={gl_ehcd=..0}] if score #state_adara gl_ent matches 1 at @s run function final_lanterns:entity/adara/host
tag @s remove gl_eoffer_adara
