scoreboard players add @s gl_e_fear 6000
scoreboard players add @s gl_tr_fear_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Face the Dark ","color":"#F5CD1E"},{"text":"(+6,000 fear)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Face the Dark", "color": "#F5CD1E"}
title @s title {"text": "+6,000 Fear", "color": "#F5CD1E"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_fear 4
