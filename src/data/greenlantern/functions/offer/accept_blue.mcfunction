execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/blue
tag @s add gl_member_blue
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Blue Lantern Corps", "color": "#2882FF"}
particle minecraft:dust 0.16 0.51 1.00 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#2882FF"},{"text":" has been chosen by the Blue Lantern Corps!","color":"white"}]
