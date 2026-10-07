scoreboard players set #placed gl_tmp 0
execute if score #placed gl_tmp matches 0 rotated ~ 0 positioned ^ ^9 ^20 run function greenlantern:entity/ion/place
execute if score #placed gl_tmp matches 0 positioned ~ ~3 ~ run function greenlantern:entity/ion/place
scoreboard players set #state_ion gl_ent 1
scoreboard players add #ser_ion gl_ent 1
scoreboard players operation @e[tag=gl_ent_new] gl_eser = #ser_ion gl_ent
scoreboard players set #life_ion gl_ent 600
scoreboard players set #miss_ion gl_ent 0
tag @e[tag=gl_ent_new] remove gl_ent_new
title @s times 10 60 20
title @s subtitle {"text": "A vast green leviathan swims through the sky toward you.", "color": "gray"}
title @s title {"text": "Ion", "color": "#2EC846", "bold": true}
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 0.5
