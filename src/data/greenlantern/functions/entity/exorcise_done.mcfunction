scoreboard players set @s gl_exo 0
execute if entity @a[tag=gl_exo_target,tag=gl_host_ion] run function greenlantern:entity/ion/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_parallax] run function greenlantern:entity/parallax/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_butcher] run function greenlantern:entity/butcher/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_ophidian] run function greenlantern:entity/ophidian/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_adara] run function greenlantern:entity/adara/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_predator] run function greenlantern:entity/predator/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_proselyte] run function greenlantern:entity/proselyte/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_life] run function greenlantern:entity/life/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_nekron] run function greenlantern:entity/nekron/sealed
tag @a remove gl_exo_target
