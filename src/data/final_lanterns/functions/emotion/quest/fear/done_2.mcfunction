scoreboard players add @s gl_e_fear 3000
scoreboard players add @s gl_tr_fear_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Sleepless ","color":"#F5CD1E"},{"text":"(+3,000 fear)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Sleepless", "color": "#F5CD1E"}
title @s title {"text": "+3,000 Fear", "color": "#F5CD1E"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/fear/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Face the Dark","color":"#F5CD1E"},{"text":" - Defeat the Warden.","color":"gray"}]
