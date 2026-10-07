execute unless entity @s[tag=gl_eoffer_proselyte] run tellraw @s ["",{"text":"The Proselyte hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_proselyte] unless score #state_proselyte gl_ent matches 1 run tellraw @s ["",{"text":"The Proselyte is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_proselyte,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_proselyte,tag=!gl_host] if score #state_proselyte gl_ent matches 1 at @s run function greenlantern:entity/proselyte/host
tag @s remove gl_eoffer_proselyte
