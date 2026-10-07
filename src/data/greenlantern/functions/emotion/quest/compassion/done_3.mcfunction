scoreboard players add @s gl_e_compassion 6000
scoreboard players add @s gl_tr_compassion_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Remedies ","color":"#7A50F0"},{"text":"(+6,000 compassion)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Remedies", "color": "#7A50F0"}
title @s title {"text": "+6,000 Compassion", "color": "#7A50F0"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_compassion 4
