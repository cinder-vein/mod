execute unless entity @s[tag=gl_eoffer_butcher] run tellraw @s ["",{"text":"The Butcher hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_butcher] unless score #state_butcher gl_ent matches 1 run tellraw @s ["",{"text":"The Butcher is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_butcher,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_butcher,tag=!gl_host] if score #state_butcher gl_ent matches 1 at @s run function greenlantern:entity/butcher/host
tag @s remove gl_eoffer_butcher
