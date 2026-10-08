execute as @e[tag=gl_ent_predator] unless score @s gl_eser = #ser_predator gl_ent run function final_lanterns:entity/remove_body
execute unless score #state_predator gl_ent matches 1 as @e[tag=gl_ent_predator] at @s run function final_lanterns:entity/remove_body
execute if score #state_predator gl_ent matches 1 run scoreboard players remove #life_predator gl_ent 1
execute if score #state_predator gl_ent matches 1 if score #life_predator gl_ent matches ..0 run function final_lanterns:entity/predator/depart
execute if score #state_predator gl_ent matches 1 unless entity @e[tag=gl_ent_predator] run scoreboard players add #miss_predator gl_ent 1
execute if score #state_predator gl_ent matches 1 if entity @e[tag=gl_ent_predator] run scoreboard players set #miss_predator gl_ent 0
execute if score #state_predator gl_ent matches 1 if score #miss_predator gl_ent matches 20.. run scoreboard players set #state_predator gl_ent 0
execute as @a[tag=gl_host_predator] unless score #state_predator gl_ent matches 2 run function final_lanterns:entity/predator/strip
execute as @a[tag=gl_host_predator] unless score @s gl_id = #host_predator gl_ent run function final_lanterns:entity/predator/strip
execute as @a[tag=gl_host_predator] run superpower add final_lanterns:host_predator @s
execute as @a[tag=!gl_host_predator] run superpower remove final_lanterns:host_predator @s
execute if score #state_predator gl_ent matches 1 at @e[tag=gl_ent_predator] as @a[tag=gl_violet,distance=..24] at @s run function final_lanterns:entity/predator/near_ring
execute if score #state_predator gl_ent matches 3 run scoreboard players remove #life_predator gl_ent 1
execute if score #state_predator gl_ent matches 3 if score #life_predator gl_ent matches ..0 run function final_lanterns:entity/predator/break_free
