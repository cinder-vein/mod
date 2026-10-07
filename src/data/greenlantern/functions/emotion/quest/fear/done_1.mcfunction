scoreboard players add @s gl_e_fear 1500
scoreboard players add @s gl_tr_fear_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Lurker ","color":"#F5CD1E"},{"text":"(+1,500 fear)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Lurker", "color": "#F5CD1E"}
title @s title {"text": "+1,500 Fear", "color": "#F5CD1E"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function greenlantern:emotion/quest/fear/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Sleepless","color":"#F5CD1E"},{"text":" - Defeat 10 phantoms.","color":"gray"}]
