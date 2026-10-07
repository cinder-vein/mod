execute unless score #state_adara gl_ent matches 0 run tellraw @s ["",{"text":"Adara isn't free (it's out, hosted or sealed). Reset it first: function greenlantern:entity/admin/reset","color":"gray"}]
execute if score #state_adara gl_ent matches 0 run function greenlantern:entity/adara/manifest
