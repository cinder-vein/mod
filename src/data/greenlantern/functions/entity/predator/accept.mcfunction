execute unless entity @s[tag=gl_eoffer_predator] run tellraw @s ["",{"text":"The Predator hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_predator] unless score #state_predator gl_ent matches 1 run tellraw @s ["",{"text":"The Predator is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_predator,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_predator,tag=!gl_host] if score #state_predator gl_ent matches 1 at @s run function greenlantern:entity/predator/host
tag @s remove gl_eoffer_predator
