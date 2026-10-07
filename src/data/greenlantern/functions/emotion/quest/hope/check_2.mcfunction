scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc1 0
scoreboard players operation #qsum gl_tmp += @s gl_qc1
scoreboard players operation @s gl_qp_hope = #qsum gl_tmp
scoreboard players operation @s gl_qp_hope -= @s gl_qs_hope
scoreboard players operation @s gl_qd_hope = @s gl_qp_hope
execute if score @s gl_qp_hope matches 25.. run function greenlantern:emotion/quest/hope/done_2
