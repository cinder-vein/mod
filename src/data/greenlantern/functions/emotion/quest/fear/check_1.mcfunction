scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc11 0
scoreboard players operation #qsum gl_tmp += @s gl_qc11
scoreboard players operation @s gl_qp_fear = #qsum gl_tmp
scoreboard players operation @s gl_qp_fear -= @s gl_qs_fear
scoreboard players operation @s gl_qd_fear = @s gl_qp_fear
scoreboard players operation @s gl_qd_fear /= #d1200 gl_cfg
execute if score @s gl_qp_fear matches 12000.. run function greenlantern:emotion/quest/fear/done_1
