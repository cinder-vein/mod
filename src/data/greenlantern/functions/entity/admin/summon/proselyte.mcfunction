execute unless score #state_proselyte gl_ent matches 0 run tellraw @s ["",{"text":"The Proselyte isn't free (it's out, hosted or sealed). Reset it first: function greenlantern:entity/admin/reset","color":"gray"}]
execute if score #state_proselyte gl_ent matches 0 run function greenlantern:entity/proselyte/manifest
