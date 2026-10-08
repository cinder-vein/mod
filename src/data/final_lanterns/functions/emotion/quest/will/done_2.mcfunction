scoreboard players add @s gl_e_will 3000
scoreboard players add @s gl_tr_will_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Hold the Line ","color":"#2EC846"},{"text":"(+3,000 willpower)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Hold the Line", "color": "#2EC846"}
title @s title {"text": "+3,000 Willpower", "color": "#2EC846"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/will/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Will Conquers All","color":"#2EC846"},{"text":" - Defeat the Ender Dragon.","color":"gray"}]
