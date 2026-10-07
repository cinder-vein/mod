execute store result storage greenlantern:binding owner int 1 run scoreboard players get @s gl_id
loot give @s loot greenlantern:rings/green
tag @s add gl_member_green
function greenlantern:offer/clear
title @s times 10 60 20
title @s subtitle {"text": "Your ring is bound to you.", "color": "gray"}
title @s title {"text": "Welcome to the Green Lantern Corps", "color": "#2EC846"}
particle minecraft:dust 0.18 0.78 0.27 2 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
tellraw @a [{"selector":"@s","color":"#2EC846"},{"text":" has been chosen by the Green Lantern Corps!","color":"white"}]
