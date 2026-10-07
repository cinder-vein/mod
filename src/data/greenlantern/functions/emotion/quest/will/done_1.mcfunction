scoreboard players add @s gl_e_will 1500
scoreboard players add @s gl_tr_will_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Stand Your Ground ","color":"#2EC846"},{"text":"(+1,500 willpower)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Stand Your Ground", "color": "#2EC846"}
title @s title {"text": "+1,500 Willpower", "color": "#2EC846"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function greenlantern:emotion/quest/will/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Hold the Line","color":"#2EC846"},{"text":" - Take 150 hearts of damage and keep going.","color":"gray"}]
