scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc14 0
scoreboard players operation #qsum gl_tmp += @s gl_qc14
scoreboard players operation @s gl_qp_will = #qsum gl_tmp
scoreboard players operation @s gl_qp_will -= @s gl_qs_will
scoreboard players operation @s gl_qd_will = @s gl_qp_will
execute if score @s gl_qp_will matches 1.. run function greenlantern:emotion/quest/will/done_3
