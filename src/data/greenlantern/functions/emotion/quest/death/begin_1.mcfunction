scoreboard players set @s gl_qn_death 1
scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc7 0
scoreboard players operation #qsum gl_tmp += @s gl_qc7
scoreboard players operation @s gl_qs_death = #qsum gl_tmp
scoreboard players set @s gl_qp_death 0
scoreboard players set @s gl_qd_death 0
