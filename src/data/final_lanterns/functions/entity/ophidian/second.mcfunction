execute as @e[tag=gl_ent_ophidian] unless score @s gl_eser = #ser_ophidian gl_ent run function final_lanterns:entity/remove_body
execute unless score #state_ophidian gl_ent matches 1 as @e[tag=gl_ent_ophidian] at @s run function final_lanterns:entity/remove_body
execute if score #state_ophidian gl_ent matches 1 run scoreboard players remove #life_ophidian gl_ent 1
execute if score #state_ophidian gl_ent matches 1 if score #life_ophidian gl_ent matches ..0 run function final_lanterns:entity/ophidian/depart
execute if score #state_ophidian gl_ent matches 1 unless entity @e[tag=gl_ent_ophidian] run scoreboard players add #miss_ophidian gl_ent 1
execute if score #state_ophidian gl_ent matches 1 if entity @e[tag=gl_ent_ophidian] run scoreboard players set #miss_ophidian gl_ent 0
execute if score #state_ophidian gl_ent matches 1 if score #miss_ophidian gl_ent matches 20.. run scoreboard players set #state_ophidian gl_ent 0
execute as @a[tag=gl_host_ophidian] unless score #state_ophidian gl_ent matches 2 run function final_lanterns:entity/ophidian/strip
execute as @a[tag=gl_host_ophidian] unless score @s gl_id = #host_ophidian gl_ent run function final_lanterns:entity/ophidian/strip
execute as @a[tag=gl_host_ophidian] run superpower add final_lanterns:host_ophidian @s
execute as @a[tag=!gl_host_ophidian] run superpower remove final_lanterns:host_ophidian @s
execute if score #state_ophidian gl_ent matches 1 at @e[tag=gl_ent_ophidian] as @a[tag=gl_orange,distance=..24] at @s run function final_lanterns:entity/ophidian/near_ring
execute if score #state_ophidian gl_ent matches 3 run scoreboard players remove #life_ophidian gl_ent 1
execute if score #state_ophidian gl_ent matches 3 if score #life_ophidian gl_ent matches ..0 run function final_lanterns:entity/ophidian/break_free
