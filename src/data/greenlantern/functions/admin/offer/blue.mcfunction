function greenlantern:offer/clear
scoreboard players set @s gl_cd_blue 0
execute if score @s gl_ser_blue matches -1 run scoreboard players set @s gl_ser_blue 0
function greenlantern:offer/start_blue
