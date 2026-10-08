scoreboard players add @s gl_e_death 1500
scoreboard players add @s gl_tr_death_quests 1500
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Reaper ","color":"#9A9EAE"},{"text":"(+1,500 a closeness to death)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Reaper", "color": "#9A9EAE"}
title @s title {"text": "+1,500 Death", "color": "#9A9EAE"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
function final_lanterns:emotion/quest/death/begin_2
tellraw @s ["",{"text":"Next quest: ","color":"gray"},{"text":"Lay Them to Rest","color":"#9A9EAE"},{"text":" - Defeat 40 zombies or skeletons.","color":"gray"}]
