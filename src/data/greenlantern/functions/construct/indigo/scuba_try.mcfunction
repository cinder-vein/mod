execute store success score #on gl_tmp if entity @s[tag=gl_scuba_indigo]
execute if score #on gl_tmp matches 1 run function greenlantern:construct/indigo/scuba_dismiss
execute if score #on gl_tmp matches 0 run function greenlantern:construct/indigo/scuba_check
