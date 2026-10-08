tag @s add gl_rolled
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_will 0
scoreboard players operation @s gl_e_will += #r gl_tmp
scoreboard players operation @s gl_tr_will_start = #r gl_tmp
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_fear 0
scoreboard players operation @s gl_e_fear += #r gl_tmp
scoreboard players operation @s gl_tr_fear_start = #r gl_tmp
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_rage 0
scoreboard players operation @s gl_e_rage += #r gl_tmp
scoreboard players operation @s gl_tr_rage_start = #r gl_tmp
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_greed 0
scoreboard players operation @s gl_e_greed += #r gl_tmp
scoreboard players operation @s gl_tr_greed_start = #r gl_tmp
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_hope 0
scoreboard players operation @s gl_e_hope += #r gl_tmp
scoreboard players operation @s gl_tr_hope_start = #r gl_tmp
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_love 0
scoreboard players operation @s gl_e_love += #r gl_tmp
scoreboard players operation @s gl_tr_love_start = #r gl_tmp
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_compassion 0
scoreboard players operation @s gl_e_compassion += #r gl_tmp
scoreboard players operation @s gl_tr_compassion_start = #r gl_tmp
function final_lanterns:emotion/roll_value
scoreboard players add @s gl_e_death 0
scoreboard players operation @s gl_e_death += #r gl_tmp
scoreboard players operation @s gl_tr_death_start = #r gl_tmp
tellraw @s ["",{"text":"\u2b22 ","color":"#7A50F0"},{"text":"The emotional spectrum stirs in you. ","color":"white"},{"text":"[See your emotions]","color":"aqua","clickEvent":{"action":"run_command","value":"/trigger gl_emotions set 1"},"hoverEvent":{"action":"show_text","contents":"Open your Emotional Spectrum"}},{"text":"  (or say \"emotions\" in chat)","color":"dark_gray"}]
