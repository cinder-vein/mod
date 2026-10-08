scoreboard players set @s gl_qn_love 2
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc5 0
scoreboard players operation #qsum gl_tmp += @s gl_qc5
scoreboard players operation @s gl_qs_love = #qsum gl_tmp
scoreboard players set @s gl_qp_love 0
scoreboard players set @s gl_qd_love 0
