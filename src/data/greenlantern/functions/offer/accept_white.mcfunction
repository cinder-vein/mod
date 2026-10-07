execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/white
tag @s add gl_member_white
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the White Lantern Corps", "color": "#EBF2FA"}
particle minecraft:dust 0.92 0.95 0.98 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#EBF2FA"},{"text":" has been chosen by the White Lantern Corps!","color":"white"}]
