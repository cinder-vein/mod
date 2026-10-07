scoreboard players set @s gl_qn_greed 1
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc13 0
scoreboard players operation #qsum gl_tmp += @s gl_qc13
scoreboard players operation @s gl_qs_greed = #qsum gl_tmp
scoreboard players set @s gl_qp_greed 0
scoreboard players set @s gl_qd_greed 0
