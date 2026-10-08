scoreboard players set #placed gl_tmp 0
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^1 ^10 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable run function final_lanterns:entity/ophidian/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^1 ^8 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable run function final_lanterns:entity/ophidian/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^1 ^6 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable run function final_lanterns:entity/ophidian/place
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^1 ^4 if block ~ ~ ~ #minecraft:replaceable if block ~ ~1 ~ #minecraft:replaceable run function final_lanterns:entity/ophidian/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function final_lanterns:entity/ophidian/place
function final_lanterns:entity/ophidian/arrive
