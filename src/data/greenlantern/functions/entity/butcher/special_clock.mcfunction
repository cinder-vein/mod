scoreboard players add @s gl_ent 1
execute if score @s gl_ent matches 8.. run function greenlantern:entity/butcher/special
execute if score @s gl_ent matches 8.. run scoreboard players set @s gl_ent 0
