scoreboard players set @s gl_qn_rage 1
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc3 0
scoreboard players operation #qsum gl_tmp += @s gl_qc3
scoreboard players operation @s gl_qs_rage = #qsum gl_tmp
scoreboard players set @s gl_qp_rage 0
scoreboard players set @s gl_qd_rage 0
