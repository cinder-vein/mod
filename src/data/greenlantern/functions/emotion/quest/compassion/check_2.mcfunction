scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc8 0
scoreboard players operation #qsum gl_tmp += @s gl_qc8
scoreboard players operation @s gl_qp_compassion = #qsum gl_tmp
scoreboard players operation @s gl_qp_compassion -= @s gl_qs_compassion
scoreboard players operation @s gl_qd_compassion = @s gl_qp_compassion
execute if score @s gl_qp_compassion matches 12.. run function greenlantern:emotion/quest/compassion/done_2
