scoreboard players set @s gl_exo 0
execute if entity @a[tag=gl_exo_target,tag=gl_host_ion] run function final_lanterns:entity/ion/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_parallax] run function final_lanterns:entity/parallax/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_butcher] run function final_lanterns:entity/butcher/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_ophidian] run function final_lanterns:entity/ophidian/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_adara] run function final_lanterns:entity/adara/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_predator] run function final_lanterns:entity/predator/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_proselyte] run function final_lanterns:entity/proselyte/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_life] run function final_lanterns:entity/life/sealed
execute if entity @a[tag=gl_exo_target,tag=gl_host_nekron] run function final_lanterns:entity/nekron/sealed
tag @a remove gl_exo_target
