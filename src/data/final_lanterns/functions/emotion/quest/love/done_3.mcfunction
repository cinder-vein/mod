scoreboard players add @s gl_e_love 6000
scoreboard players add @s gl_tr_love_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Family ","color":"#D737DC"},{"text":"(+6,000 love)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Family", "color": "#D737DC"}
title @s title {"text": "+6,000 Love", "color": "#D737DC"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_love 4
