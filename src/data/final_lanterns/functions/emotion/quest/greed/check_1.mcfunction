scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc13 0
scoreboard players operation #qsum gl_tmp += @s gl_qc13
scoreboard players operation @s gl_qp_greed = #qsum gl_tmp
scoreboard players operation @s gl_qp_greed -= @s gl_qs_greed
scoreboard players operation @s gl_qd_greed = @s gl_qp_greed
execute if score @s gl_qp_greed matches 30.. run function final_lanterns:emotion/quest/greed/done_1
