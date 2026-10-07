function greenlantern:offer/clear
scoreboard players set @s gl_cd_indigo 0
execute if score @s gl_ser_indigo matches -1 run scoreboard players set @s gl_ser_indigo 0
function greenlantern:ring/save_serials
function greenlantern:offer/start_indigo
