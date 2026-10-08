execute as @e[tag=gl_ent_life] unless score @s gl_eser = #ser_life gl_ent run function final_lanterns:entity/remove_body
execute unless score #state_life gl_ent matches 1 as @e[tag=gl_ent_life] at @s run function final_lanterns:entity/remove_body
execute if score #state_life gl_ent matches 1 run scoreboard players remove #life_life gl_ent 1
execute if score #state_life gl_ent matches 1 if score #life_life gl_ent matches ..0 run function final_lanterns:entity/life/depart
execute if score #state_life gl_ent matches 1 unless entity @e[tag=gl_ent_life] run scoreboard players add #miss_life gl_ent 1
execute if score #state_life gl_ent matches 1 if entity @e[tag=gl_ent_life] run scoreboard players set #miss_life gl_ent 0
execute if score #state_life gl_ent matches 1 if score #miss_life gl_ent matches 20.. run scoreboard players set #state_life gl_ent 0
execute as @a[tag=gl_host_life] unless score #state_life gl_ent matches 2 run function final_lanterns:entity/life/strip
execute as @a[tag=gl_host_life] unless score @s gl_id = #host_life gl_ent run function final_lanterns:entity/life/strip
execute as @a[tag=gl_host_life] run superpower add final_lanterns:host_life @s
execute as @a[tag=!gl_host_life] run superpower remove final_lanterns:host_life @s
execute if score #state_life gl_ent matches 1 at @e[tag=gl_ent_life] as @a[tag=gl_white,distance=..24] at @s run function final_lanterns:entity/life/near_ring
execute if score #state_life gl_ent matches 3 run scoreboard players remove #life_life gl_ent 1
execute if score #state_life gl_ent matches 3 if score #life_life gl_ent matches ..0 run function final_lanterns:entity/life/break_free
