execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/red
tag @s add gl_member_red
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Red Lantern Corps", "color": "#DC1E23"}
particle minecraft:dust 0.86 0.12 0.14 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#DC1E23"},{"text":" has been chosen by the Red Lantern Corps!","color":"white"}]
