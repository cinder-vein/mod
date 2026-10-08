execute as @e[tag=gl_ent_parallax] unless score @s gl_eser = #ser_parallax gl_ent run function final_lanterns:entity/remove_body
execute unless score #state_parallax gl_ent matches 1 as @e[tag=gl_ent_parallax] at @s run function final_lanterns:entity/remove_body
execute if score #state_parallax gl_ent matches 1 run scoreboard players remove #life_parallax gl_ent 1
execute if score #state_parallax gl_ent matches 1 if score #life_parallax gl_ent matches ..0 run function final_lanterns:entity/parallax/depart
execute if score #state_parallax gl_ent matches 1 unless entity @e[tag=gl_ent_parallax] run scoreboard players add #miss_parallax gl_ent 1
execute if score #state_parallax gl_ent matches 1 if entity @e[tag=gl_ent_parallax] run scoreboard players set #miss_parallax gl_ent 0
execute if score #state_parallax gl_ent matches 1 if score #miss_parallax gl_ent matches 20.. run scoreboard players set #state_parallax gl_ent 0
execute as @a[tag=gl_host_parallax] unless score #state_parallax gl_ent matches 2 run function final_lanterns:entity/parallax/strip
execute as @a[tag=gl_host_parallax] unless score @s gl_id = #host_parallax gl_ent run function final_lanterns:entity/parallax/strip
execute as @a[tag=gl_host_parallax] run superpower add final_lanterns:host_parallax @s
execute as @a[tag=!gl_host_parallax] run superpower remove final_lanterns:host_parallax @s
execute if score #state_parallax gl_ent matches 1 at @e[tag=gl_ent_parallax] as @a[tag=gl_yellow,distance=..24] at @s run function final_lanterns:entity/parallax/near_ring
execute if score #state_parallax gl_ent matches 3 run scoreboard players remove #life_parallax gl_ent 1
execute if score #state_parallax gl_ent matches 3 if score #life_parallax gl_ent matches ..0 run function final_lanterns:entity/parallax/break_free
