scoreboard players add @s gl_e_will 6000
scoreboard players add @s gl_tr_will_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Will Conquers All ","color":"#2EC846"},{"text":"(+6,000 willpower)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Will Conquers All", "color": "#2EC846"}
title @s title {"text": "+6,000 Willpower", "color": "#2EC846"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_will 4
