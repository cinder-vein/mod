scoreboard players set @s gl_cd_yellow 3600
function greenlantern:offer/send_away
function greenlantern:offer/clear
tellraw @s [{"text":"The ring hesitates... then streaks away to search for another.","color":"#F5CD1E","italic":true}]
playsound minecraft:entity.firework_rocket.launch player @s ~ ~ ~ 1 0.8
