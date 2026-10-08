scoreboard players set @s gl_cd_red 3600
function final_lanterns:offer/send_away
function final_lanterns:offer/clear
tellraw @s [{"text":"The ring hesitates... then streaks away to search for another.","color":"#DC1E23","italic":true}]
playsound minecraft:entity.firework_rocket.launch player @s ~ ~ ~ 1 0.8
