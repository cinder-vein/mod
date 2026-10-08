scoreboard players add @s gl_e_greed 1500
scoreboard players add @s gl_tr_greed_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Haggler ","color":"#FA8214"},{"text":"(+1,500 avarice)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Haggler", "color": "#FA8214"}
title @s title {"text": "+1,500 Avarice", "color": "#FA8214"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/greed/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Diamond Fever","color":"#FA8214"},{"text":" - Mine 24 diamond ore.","color":"gray"}]
