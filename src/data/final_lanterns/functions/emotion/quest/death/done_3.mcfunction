scoreboard players add @s gl_e_death 6000
scoreboard players add @s gl_tr_death_quests 6000
tellraw @s ["",{"text":"Quest complete: ","color":"gold","bold":true},{"text":"Lord of the Dead ","color":"#9A9EAE"},{"text":"(+6,000 a closeness to death)","color":"gray"}]
title @s times 5 40 10
title @s subtitle {"text": "Quest complete: Lord of the Dead", "color": "#9A9EAE"}
title @s title {"text": "+6,000 Death", "color": "#9A9EAE"}
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.8 1.2
scoreboard players set @s gl_qn_death 4
