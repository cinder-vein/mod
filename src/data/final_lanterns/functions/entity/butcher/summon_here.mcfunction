scoreboard players set #placed gl_tmp 0
execute rotated ~ 0 positioned ^ ^0 ^6 run function final_lanterns:entity/butcher/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function final_lanterns:entity/butcher/place
function final_lanterns:entity/butcher/arrive
