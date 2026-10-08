execute unless score #state_predator gl_ent matches 0 run tellraw @s ["",{"text":"The Predator isn't free (it's out, hosted or sealed). Reset it first: function final_lanterns:entity/admin/reset","color":"gray"}]
execute if score #state_predator gl_ent matches 0 run function final_lanterns:entity/predator/manifest
