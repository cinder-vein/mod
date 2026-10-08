scoreboard players set @s gl_qn_fear 3
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc18 0
scoreboard players operation #qsum gl_tmp += @s gl_qc18
scoreboard players operation @s gl_qs_fear = #qsum gl_tmp
scoreboard players set @s gl_qp_fear 0
scoreboard players set @s gl_qd_fear 0
