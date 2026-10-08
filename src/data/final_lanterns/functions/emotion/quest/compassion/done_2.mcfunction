scoreboard players add @s gl_e_compassion 3000
scoreboard players add @s gl_tr_compassion_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Gardener ","color":"#7A50F0"},{"text":"(+3,000 compassion)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Gardener", "color": "#7A50F0"}
title @s title {"text": "+3,000 Compassion", "color": "#7A50F0"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/compassion/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Remedies","color":"#7A50F0"},{"text":" - Brew at a brewing stand 25 times.","color":"gray"}]
