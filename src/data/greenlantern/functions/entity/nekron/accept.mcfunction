execute unless entity @s[tag=gl_eoffer_nekron] run tellraw @s ["",{"text":"Nekron hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_nekron] unless score #state_nekron gl_ent matches 1 run tellraw @s ["",{"text":"Nekron is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_nekron,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_nekron,tag=!gl_host] if score #state_nekron gl_ent matches 1 at @s run function greenlantern:entity/nekron/host
tag @s remove gl_eoffer_nekron
