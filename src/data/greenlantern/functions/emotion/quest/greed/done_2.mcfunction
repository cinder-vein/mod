scoreboard players add @s gl_e_greed 3000
scoreboard players add @s gl_tr_greed_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Diamond Fever ","color":"#FA8214"},{"text":"(+3,000 avarice)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Diamond Fever", "color": "#FA8214"}
title @s title {"text": "+3,000 Avarice", "color": "#FA8214"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function greenlantern:emotion/quest/greed/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Netherite Hoard","color":"#FA8214"},{"text":" - Mine 12 ancient debris.","color":"gray"}]
