execute unless score #state_predator gl_ent matches 0 run tellraw @s ["",{"text":"The Predator isn't free (it's out, hosted or sealed). Reset it first: function greenlantern:entity/admin/reset","color":"gray"}]
execute if score #state_predator gl_ent matches 0 run function greenlantern:entity/predator/manifest
