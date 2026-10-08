scoreboard players add @s gl_e_love 3000
scoreboard players add @s gl_tr_love_quests 3000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Let Them Eat Cake ","color":"#D737DC"},{"text":"(+3,000 love)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Let Them Eat Cake", "color": "#D737DC"}
title @s title {"text": "+3,000 Love", "color": "#D737DC"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/love/begin_3
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Family","color":"#D737DC"},{"text":" - Breed 100 animals.","color":"gray"}]
