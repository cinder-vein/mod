scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc15 0
scoreboard players operation #qsum gl_tmp += @s gl_qc15
scoreboard players operation @s gl_qp_fear = #qsum gl_tmp
scoreboard players operation @s gl_qp_fear -= @s gl_qs_fear
scoreboard players operation @s gl_qd_fear = @s gl_qp_fear
execute if score @s gl_qp_fear matches 10.. run function final_lanterns:emotion/quest/fear/done_2
