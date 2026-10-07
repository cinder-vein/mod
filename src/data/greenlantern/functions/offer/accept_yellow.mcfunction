execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/yellow
tag @s add gl_member_yellow
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Sinestro Corps", "color": "#F5CD1E"}
particle minecraft:dust 0.96 0.80 0.12 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#F5CD1E"},{"text":" has been chosen by the Sinestro Corps!","color":"white"}]
