scoreboard players set #qsum gl_tmp 0
scoreboard players add @s gl_qc20 0
scoreboard players operation #qsum gl_tmp += @s gl_qc20
scoreboard players add @s gl_qc17 0
scoreboard players operation #qsum gl_tmp += @s gl_qc17
scoreboard players operation @s gl_qp_death = #qsum gl_tmp
scoreboard players operation @s gl_qp_death -= @s gl_qs_death
scoreboard players operation @s gl_qd_death = @s gl_qp_death
execute if score @s gl_qp_death matches 40.. run function greenlantern:emotion/quest/death/done_2
