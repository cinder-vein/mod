execute if entity @s[tag=gl_host] run tellraw @s ["",{"text":"You already host an entity: release it first.","color":"gray"}]
execute if score #state_proselyte gl_ent matches 2 run tellraw @s ["",{"text":"The Proselyte already has a host.","color":"gray"}]
execute if score #state_proselyte gl_ent matches 3 run tellraw @s ["",{"text":"The Proselyte is sealed in a lantern.","color":"gray"}]
execute if entity @s[tag=!gl_host] if score #state_proselyte gl_ent matches 0..1 at @s run function final_lanterns:entity/proselyte/host
