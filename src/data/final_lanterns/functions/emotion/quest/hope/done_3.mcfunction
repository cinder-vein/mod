scoreboard players add @s gl_e_hope 6000
scoreboard players add @s gl_tr_hope_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Hero of the Village ","color":"#2882FF"},{"text":"(+6,000 hope)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Hero of the Village", "color": "#2882FF"}
title @s title {"text": "+6,000 Hope", "color": "#2882FF"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_hope 4
