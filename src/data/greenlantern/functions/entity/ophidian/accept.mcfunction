execute unless entity @s[tag=gl_eoffer_ophidian] run tellraw @s ["",{"text":"Ophidian hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_ophidian] unless score #state_ophidian gl_ent matches 1 run tellraw @s ["",{"text":"Ophidian is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_ophidian,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_ophidian,tag=!gl_host] if score #state_ophidian gl_ent matches 1 at @s run function greenlantern:entity/ophidian/host
tag @s remove gl_eoffer_ophidian
