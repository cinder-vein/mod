scoreboard players add @s gl_e_death 3000
scoreboard players add @s gl_tr_death_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Lay Them to Rest ","color":"#9A9EAE"},{"text":"(+3,000 a closeness to death)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Lay Them to Rest", "color": "#9A9EAE"}
title @s title {"text": "+3,000 Death", "color": "#9A9EAE"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function greenlantern:emotion/quest/death/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Lord of the Dead","color":"#9A9EAE"},{"text":" - Defeat the Wither.","color":"gray"}]
