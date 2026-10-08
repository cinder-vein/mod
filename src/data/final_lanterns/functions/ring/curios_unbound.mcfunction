function final_lanterns:ring/curios_pop
tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject
tellraw @s [{"text":"A ring has to bind to you before you can wear it. It binds when you carry it, unless you already bear a ring of its corps or you're handing it on.","color":"gray","italic":true}]
