function final_lanterns:ring/curios_pop
tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject
tellraw @s [{"text":"A ring has to bind to you before you can wear it: it binds a moment after it's in your inventory (it falls back to you now), then put it on again. It won't bind if you already bear a ring of its corps or you're handing it on.","color":"gray","italic":true}]
