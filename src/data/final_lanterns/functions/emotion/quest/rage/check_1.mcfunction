scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc3 0
scoreboard players operation #qsum gl_tmp += @s gl_qc3
scoreboard players operation @s gl_qp_rage = #qsum gl_tmp
scoreboard players operation @s gl_qp_rage -= @s gl_qs_rage
scoreboard players operation @s gl_qd_rage = @s gl_qp_rage
scoreboard players operation @s gl_qd_rage /= #d20 gl_cfg
execute if score @s gl_qp_rage matches 4000.. run function final_lanterns:emotion/quest/rage/done_1
