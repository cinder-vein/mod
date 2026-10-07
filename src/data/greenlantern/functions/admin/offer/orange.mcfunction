function greenlantern:offer/clear
scoreboard players set @s gl_cd_orange 0
execute if score @s gl_ser_orange matches -1 run scoreboard players set @s gl_ser_orange 0
function greenlantern:ring/save_serials
function greenlantern:offer/start_orange
