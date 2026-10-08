function final_lanterns:offer/clear
scoreboard players set @s gl_cd_indigo 0
execute if score @s gl_ser_indigo matches -1 run scoreboard players set @s gl_ser_indigo 0
function final_lanterns:ring/save_serials
function final_lanterns:offer/start_indigo
