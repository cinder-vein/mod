scoreboard players add @s gl_e_love 1500
scoreboard players add @s gl_tr_love_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Matchmaker ","color":"#D737DC"},{"text":"(+1,500 love)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Matchmaker", "color": "#D737DC"}
title @s title {"text": "+1,500 Love", "color": "#D737DC"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function greenlantern:emotion/quest/love/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Let Them Eat Cake","color":"#D737DC"},{"text":" - Eat 14 slices of cake.","color":"gray"}]
