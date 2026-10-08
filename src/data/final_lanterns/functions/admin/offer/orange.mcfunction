function final_lanterns:offer/clear
scoreboard players set @s gl_cd_orange 0
execute if score @s gl_ser_orange matches -1 run scoreboard players set @s gl_ser_orange 0
function final_lanterns:ring/save_serials
function final_lanterns:offer/start_orange
