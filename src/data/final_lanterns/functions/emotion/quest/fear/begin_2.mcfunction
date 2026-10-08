scoreboard players set @s gl_qn_fear 2
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc15 0
scoreboard players operation #qsum gl_tmp += @s gl_qc15
scoreboard players operation @s gl_qs_fear = #qsum gl_tmp
scoreboard players set @s gl_qp_fear 0
scoreboard players set @s gl_qd_fear 0
