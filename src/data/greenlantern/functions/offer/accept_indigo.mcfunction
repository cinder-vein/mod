execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/indigo
tag @s add gl_member_indigo
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Indigo Tribe", "color": "#693CE6"}
particle minecraft:dust 0.41 0.24 0.90 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#693CE6"},{"text":" has been chosen by the Indigo Tribe!","color":"white"}]
