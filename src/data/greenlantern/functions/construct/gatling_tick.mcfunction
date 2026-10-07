scoreboard players add @s gl_gat 1
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/green_mainhand run function greenlantern:construct/green/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/yellow_mainhand run function greenlantern:construct/yellow/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/red_mainhand run function greenlantern:construct/red/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/orange_mainhand run function greenlantern:construct/orange/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/blue_mainhand run function greenlantern:construct/blue/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/violet_mainhand run function greenlantern:construct/violet/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/indigo_mainhand run function greenlantern:construct/indigo/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/white_mainhand run function greenlantern:construct/white/gatling_shot
execute if score @s gl_gat matches 3.. if predicate greenlantern:construct_held/black_mainhand run function greenlantern:construct/black/gatling_shot
execute if score @s gl_gat matches 3.. run scoreboard players set @s gl_gat 0
