scoreboard players set @s gl_qn_will 3
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc14 0
scoreboard players operation #qsum gl_tmp += @s gl_qc14
scoreboard players operation @s gl_qs_will = #qsum gl_tmp
scoreboard players set @s gl_qp_will 0
scoreboard players set @s gl_qd_will 0
