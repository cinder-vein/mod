function greenlantern:offer/clear
scoreboard players set @s gl_cd_yellow 0
execute if score @s gl_ser_yellow matches -1 run scoreboard players set @s gl_ser_yellow 0
function greenlantern:offer/start_yellow
