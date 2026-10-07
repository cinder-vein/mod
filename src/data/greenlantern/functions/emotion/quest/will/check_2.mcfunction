scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc4 0
scoreboard players operation #qsum gl_tmp += @s gl_qc4
scoreboard players operation @s gl_qp_will = #qsum gl_tmp
scoreboard players operation @s gl_qp_will -= @s gl_qs_will
scoreboard players operation @s gl_qd_will = @s gl_qp_will
scoreboard players operation @s gl_qd_will /= #d20 gl_cfg
execute if score @s gl_qp_will matches 3000.. run function greenlantern:emotion/quest/will/done_2
