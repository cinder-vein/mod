execute if score #slot gl_tmp matches 0..31 run function final_lanterns:ring/curios_pop_slot
execute if score #slot gl_tmp matches 32.. run tellraw @s [{"text":"Lantern rings only work in the first 32 ring slots.","color":"gray"}]
