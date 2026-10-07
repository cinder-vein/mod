scoreboard players add @s gl_e_hope 1500
scoreboard players add @s gl_tr_hope_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Good Night ","color":"#2882FF"},{"text":"(+1,500 hope)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Good Night", "color": "#2882FF"}
title @s title {"text": "+1,500 Hope", "color": "#2882FF"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function greenlantern:emotion/quest/hope/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Ring the Bells","color":"#2882FF"},{"text":" - Ring a bell 25 times.","color":"gray"}]
