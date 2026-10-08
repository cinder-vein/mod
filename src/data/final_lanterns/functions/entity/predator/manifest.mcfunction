scoreboard players set #placed gl_tmp 0
execute if score #placed gl_tmp matches 0 rotated ~180 0 positioned ^ ^4 ^22 run function final_lanterns:entity/predator/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function final_lanterns:entity/predator/place
function final_lanterns:entity/predator/arrive
