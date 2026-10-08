scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc0 0
scoreboard players operation #qsum gl_tmp += @s gl_qc0
scoreboard players operation @s gl_qp_love = #qsum gl_tmp
scoreboard players operation @s gl_qp_love -= @s gl_qs_love
scoreboard players operation @s gl_qd_love = @s gl_qp_love
execute if score @s gl_qp_love matches 100.. run function final_lanterns:emotion/quest/love/done_3
