scoreboard players set #placed gl_tmp 0
execute if score #placed gl_tmp matches 0 rotated ~180 0 positioned ^ ^4 ^22 run function final_lanterns:entity/parallax/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function final_lanterns:entity/parallax/place
scoreboard players set #state_parallax gl_ent 1
scoreboard players add #ser_parallax gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_parallax gl_ent
scoreboard players set #life_parallax gl_ent 1200
scoreboard players set #miss_parallax gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
tag @a remove gl_hunted_parallax
tag @s add gl_hunted_parallax
title @s times 10 60 20
title @s subtitle {"text": "Something is hunting you. You can feel it feeding on your fear...", "color": "gray"}
title @s title {"text": "Parallax", "color": "#F5CD1E", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
