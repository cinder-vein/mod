execute unless entity @s[tag=gl_eoffer_ion] run tellraw @s ["",{"text":"Ion hasn't offered itself to you.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_ion] unless score #state_ion gl_ent matches 1 run tellraw @s ["",{"text":"Ion is gone.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_ion,tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if entity @s[tag=gl_eoffer_ion,tag=!gl_host] if score #state_ion gl_ent matches 1 at @s run function greenlantern:entity/ion/host
tag @s remove gl_eoffer_ion
