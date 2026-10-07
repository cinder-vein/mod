scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc5 0
scoreboard players operation #qsum gl_tmp += @s gl_qc5
scoreboard players operation @s gl_qp_love = #qsum gl_tmp
scoreboard players operation @s gl_qp_love -= @s gl_qs_love
scoreboard players operation @s gl_qd_love = @s gl_qp_love
execute if score @s gl_qp_love matches 14.. run function greenlantern:emotion/quest/love/done_2
