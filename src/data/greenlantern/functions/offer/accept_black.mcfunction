execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/black
tag @s add gl_member_black
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Black Lantern Corps", "color": "#AAAFBE"}
particle minecraft:dust 0.37 0.38 0.43 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#AAAFBE"},{"text":" has been chosen by the Black Lantern Corps!","color":"white"}]
