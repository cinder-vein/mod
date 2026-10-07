function greenlantern:dual/read
execute if score #ready gl_tmp matches 2 if entity @s[tag=gl_du_shared_light] run function greenlantern:dual/shared_light
execute if score #ready gl_tmp matches 2 if entity @s[tag=gl_du_resonance] run function greenlantern:dual/resonance
