scoreboard players set #placed gl_tmp 0
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^ ^12 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable if block ~ ~2 ~ #minecraft:replaceable run function final_lanterns:entity/nekron/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^ ^10 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable if block ~ ~2 ~ #minecraft:replaceable run function final_lanterns:entity/nekron/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^ ^8 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable if block ~ ~2 ~ #minecraft:replaceable run function final_lanterns:entity/nekron/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^ ^6 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable if block ~ ~2 ~ #minecraft:replaceable run function final_lanterns:entity/nekron/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^ ^4 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable if block ~ ~2 ~ #minecraft:replaceable run function final_lanterns:entity/nekron/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function final_lanterns:entity/nekron/place
function final_lanterns:entity/nekron/arrive
