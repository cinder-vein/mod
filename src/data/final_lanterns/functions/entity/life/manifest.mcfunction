scoreboard players set #placed gl_tmp 0
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^9 ^20 if block ~ ~ ~ #minecraft:replaceable run function final_lanterns:entity/life/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^4 ^12 if block ~ ~ ~ #minecraft:replaceable run function final_lanterns:entity/life/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^1 ^6 if block ~ ~ ~ #minecraft:replaceable run function final_lanterns:entity/life/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function final_lanterns:entity/life/place
function final_lanterns:entity/life/arrive
