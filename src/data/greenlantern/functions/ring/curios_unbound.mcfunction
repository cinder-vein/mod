function greenlantern:ring/curios_pop
tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject
tellraw @s [{"text":"Hold a new ring in your hand once to bind it to you, then wear it.","color":"gray","italic":true}]
