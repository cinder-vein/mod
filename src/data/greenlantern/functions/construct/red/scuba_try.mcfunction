execute store success score #on gl_tmp if entity @s[tag=gl_scuba_red]
execute if score #on gl_tmp matches 1 run function greenlantern:construct/red/scuba_dismiss
execute if score #on gl_tmp matches 0 run function greenlantern:construct/red/scuba_check
