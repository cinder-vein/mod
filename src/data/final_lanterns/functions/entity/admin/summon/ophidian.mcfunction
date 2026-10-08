execute unless score #state_ophidian gl_ent matches 0 run tellraw @s ["",{"text":"Ophidian isn't free (it's out, hosted or sealed). Reset it first: function final_lanterns:entity/admin/reset","color":"gray"}]
execute if score #state_ophidian gl_ent matches 0 run function final_lanterns:entity/ophidian/manifest
