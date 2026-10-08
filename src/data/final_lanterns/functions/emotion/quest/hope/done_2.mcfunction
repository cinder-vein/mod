scoreboard players add @s gl_e_hope 3000
scoreboard players add @s gl_tr_hope_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Ring the Bells ","color":"#2882FF"},{"text":"(+3,000 hope)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Ring the Bells", "color": "#2882FF"}
title @s title {"text": "+3,000 Hope", "color": "#2882FF"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/hope/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Hero of the Village","color":"#2882FF"},{"text":" - Win 2 raids.","color":"gray"}]
