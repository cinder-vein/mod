scoreboard players set #placed gl_tmp 0
execute rotated ~ 0 positioned ^ ^1 ^6 run function final_lanterns:entity/adara/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function final_lanterns:entity/adara/place
function final_lanterns:entity/adara/arrive
