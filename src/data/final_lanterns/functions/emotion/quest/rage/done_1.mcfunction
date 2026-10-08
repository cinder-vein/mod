scoreboard players add @s gl_e_rage 1500
scoreboard players add @s gl_tr_rage_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Bloodied ","color":"#DC1E23"},{"text":"(+1,500 rage)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Bloodied", "color": "#DC1E23"}
title @s title {"text": "+1,500 Rage", "color": "#DC1E23"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/rage/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Berserker","color":"#DC1E23"},{"text":" - Defeat 150 mobs.","color":"gray"}]
