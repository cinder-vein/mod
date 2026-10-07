scoreboard players add @s gl_e_rage 6000
scoreboard players add @s gl_tr_rage_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Rage Against the Raid ","color":"#DC1E23"},{"text":"(+6,000 rage)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Rage Against the Raid", "color": "#DC1E23"}
title @s title {"text": "+6,000 Rage", "color": "#DC1E23"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_rage 4
