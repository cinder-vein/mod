execute unless score #state_nekron gl_ent matches 0 run tellraw @s ["",{"text":"Nekron isn't free (it's out, hosted or sealed). Reset it first: function final_lanterns:entity/admin/reset","color":"gray"}]
execute if score #state_nekron gl_ent matches 0 run function final_lanterns:entity/nekron/manifest
