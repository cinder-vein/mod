scoreboard players add @s gl_e_greed 6000
scoreboard players add @s gl_tr_greed_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Netherite Hoard ","color":"#FA8214"},{"text":"(+6,000 avarice)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Netherite Hoard", "color": "#FA8214"}
title @s title {"text": "+6,000 Avarice", "color": "#FA8214"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_greed 4
