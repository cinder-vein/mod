execute unless entity @s[tag=gl_eoffer_life] run tellraw @s ["",{"text":"The Life Entity hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_life] unless score #state_life gl_ent matches 1 run tellraw @s ["",{"text":"The Life Entity is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_life,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_life,tag=!gl_host] if score #state_life gl_ent matches 1 at @s run function greenlantern:entity/life/host
tag @s remove gl_eoffer_life
