execute as @e[tag=gl_ent_proselyte] unless score @s gl_eser = #ser_proselyte gl_ent run function greenlantern:entity/remove_body
execute unless score #state_proselyte gl_ent matches 1 as @e[tag=gl_ent_proselyte] at @s run function greenlantern:entity/remove_body
execute if score #state_proselyte gl_ent matches 1 run scoreboard players remove #life_proselyte gl_ent 1
execute if score #state_proselyte gl_ent matches 1 if score #life_proselyte gl_ent matches ..0 run function greenlantern:entity/proselyte/depart
execute if score #state_proselyte gl_ent matches 1 unless entity @e[tag=gl_ent_proselyte] run scoreboard players add #miss_proselyte gl_ent 1
execute if score #state_proselyte gl_ent matches 1 if entity @e[tag=gl_ent_proselyte] run scoreboard players set #miss_proselyte gl_ent 0
execute if score #state_proselyte gl_ent matches 1 if score #miss_proselyte gl_ent matches 20.. run scoreboard players set #state_proselyte gl_ent 0
execute as @a[tag=gl_host_proselyte] unless score #state_proselyte gl_ent matches 2 run function greenlantern:entity/proselyte/strip
execute as @a[tag=gl_host_proselyte] unless score @s gl_id = #host_proselyte gl_ent run function greenlantern:entity/proselyte/strip
execute as @a[tag=gl_host_proselyte] run superpower add greenlantern:host_proselyte @s
execute as @a[tag=!gl_host_proselyte] run superpower remove greenlantern:host_proselyte @s
execute if score #state_proselyte gl_ent matches 3 run scoreboard players remove #life_proselyte gl_ent 1
execute if score #state_proselyte gl_ent matches 3 if score #life_proselyte gl_ent matches ..0 run function greenlantern:entity/proselyte/break_free
