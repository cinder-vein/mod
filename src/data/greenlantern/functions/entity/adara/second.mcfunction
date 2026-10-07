execute as @e[tag=gl_ent_adara] unless score @s gl_eser = #ser_adara gl_ent run function greenlantern:entity/remove_body
execute unless score #state_adara gl_ent matches 1 as @e[tag=gl_ent_adara] at @s run function greenlantern:entity/remove_body
execute if score #state_adara gl_ent matches 1 run scoreboard players remove #life_adara gl_ent 1
execute if score #state_adara gl_ent matches 1 if score #life_adara gl_ent matches ..0 run function greenlantern:entity/adara/depart
execute if score #state_adara gl_ent matches 1 unless entity @e[tag=gl_ent_adara] run scoreboard players add #miss_adara gl_ent 1
execute if score #state_adara gl_ent matches 1 if entity @e[tag=gl_ent_adara] run scoreboard players set #miss_adara gl_ent 0
execute if score #state_adara gl_ent matches 1 if score #miss_adara gl_ent matches 20.. run scoreboard players set #state_adara gl_ent 0
execute as @a[tag=gl_host_adara] unless score #state_adara gl_ent matches 2 run function greenlantern:entity/adara/strip
execute as @a[tag=gl_host_adara] unless score @s gl_id = #host_adara gl_ent run function greenlantern:entity/adara/strip
execute as @a[tag=gl_host_adara] run superpower add greenlantern:host_adara @s
execute as @a[tag=!gl_host_adara] run superpower remove greenlantern:host_adara @s
execute if score #state_adara gl_ent matches 3 run scoreboard players remove #life_adara gl_ent 1
execute if score #state_adara gl_ent matches 3 if score #life_adara gl_ent matches ..0 run function greenlantern:entity/adara/break_free
