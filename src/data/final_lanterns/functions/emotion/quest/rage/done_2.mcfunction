scoreboard players add @s gl_e_rage 3000
scoreboard players add @s gl_tr_rage_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Berserker ","color":"#DC1E23"},{"text":"(+3,000 rage)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Berserker", "color": "#DC1E23"}
title @s title {"text": "+3,000 Rage", "color": "#DC1E23"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/rage/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Rage Against the Raid","color":"#DC1E23"},{"text":" - Defeat 3 ravagers.","color":"gray"}]
