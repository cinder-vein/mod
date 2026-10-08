scoreboard players set @s gl_qn_hope 2
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc1 0
scoreboard players operation #qsum gl_tmp += @s gl_qc1
scoreboard players operation @s gl_qs_hope = #qsum gl_tmp
scoreboard players set @s gl_qp_hope 0
scoreboard players set @s gl_qd_hope 0
