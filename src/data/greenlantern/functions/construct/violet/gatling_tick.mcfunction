scoreboard players add @s gl_gat 1
execute if score @s gl_gat matches 3.. run function greenlantern:construct/violet/gatling_shot
execute if score @s gl_gat matches 3.. run scoreboard players set @s gl_gat 0
