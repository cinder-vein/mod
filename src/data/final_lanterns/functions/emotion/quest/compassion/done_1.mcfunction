scoreboard players add @s gl_e_compassion 1500
scoreboard players add @s gl_tr_compassion_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"A Kind Word ","color":"#7A50F0"},{"text":"(+1,500 compassion)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: A Kind Word", "color": "#7A50F0"}
title @s title {"text": "+1,500 Compassion", "color": "#7A50F0"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/compassion/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Gardener","color":"#7A50F0"},{"text":" - Pot 12 flowers.","color":"gray"}]
