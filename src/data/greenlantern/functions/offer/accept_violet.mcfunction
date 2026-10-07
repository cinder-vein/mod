execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/violet
tag @s add gl_member_violet
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Star Sapphires", "color": "#D737DC"}
particle minecraft:dust 0.84 0.22 0.86 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#D737DC"},{"text":" has been chosen by the Star Sapphires!","color":"white"}]
