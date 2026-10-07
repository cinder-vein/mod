scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc23 0
scoreboard players operation #qsum gl_tmp += @s gl_qc23
scoreboard players add @s gl_qc22 0
scoreboard players operation #qsum gl_tmp += @s gl_qc22
scoreboard players operation @s gl_qp_greed = #qsum gl_tmp
scoreboard players operation @s gl_qp_greed -= @s gl_qs_greed
scoreboard players operation @s gl_qd_greed = @s gl_qp_greed
execute if score @s gl_qp_greed matches 24.. run function greenlantern:emotion/quest/greed/done_2
