execute if score #forge gl_cfg matches 0 run tellraw @s [{"text":"Forging new rings is turned off on this server.","color":"gray"}]
execute if score #forge gl_cfg matches 1.. run function greenlantern:forge/try_blue
