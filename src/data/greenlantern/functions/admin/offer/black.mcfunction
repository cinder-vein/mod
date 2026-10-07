function greenlantern:offer/clear
scoreboard players set @s gl_cd_black 0
execute if score @s gl_ser_black matches -1 run scoreboard players set @s gl_ser_black 0
function greenlantern:offer/start_black
