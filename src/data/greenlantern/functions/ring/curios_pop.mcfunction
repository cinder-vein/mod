execute if score #slot gl_tmp matches 0..15 run function greenlantern:ring/curios_pop_slot
execute if score #slot gl_tmp matches 16.. run tellraw @s [{"text":"Lantern rings only work in the first 16 ring slots.","color":"gray"}]
