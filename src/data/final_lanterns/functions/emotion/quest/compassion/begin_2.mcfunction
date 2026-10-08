scoreboard players set @s gl_qn_compassion 2
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc8 0
scoreboard players operation #qsum gl_tmp += @s gl_qc8
scoreboard players operation @s gl_qs_compassion = #qsum gl_tmp
scoreboard players set @s gl_qp_compassion 0
scoreboard players set @s gl_qd_compassion 0
