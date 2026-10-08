execute as @e[tag=gl_ent_butcher] unless score @s gl_eser = #ser_butcher gl_ent run function final_lanterns:entity/remove_body
execute unless score #state_butcher gl_ent matches 1 as @e[tag=gl_ent_butcher] at @s run function final_lanterns:entity/remove_body
execute if score #state_butcher gl_ent matches 1 run scoreboard players remove #life_butcher gl_ent 1
execute if score #state_butcher gl_ent matches 1 if score #life_butcher gl_ent matches ..0 run function final_lanterns:entity/butcher/depart
execute if score #state_butcher gl_ent matches 1 unless entity @e[tag=gl_ent_butcher] run scoreboard players add #miss_butcher gl_ent 1
execute if score #state_butcher gl_ent matches 1 if entity @e[tag=gl_ent_butcher] run scoreboard players set #miss_butcher gl_ent 0
execute if score #state_butcher gl_ent matches 1 if score #miss_butcher gl_ent matches 20.. run scoreboard players set #state_butcher gl_ent 0
execute unless score #state_butcher gl_ent matches 1 run bossbar set final_lanterns:butcher players
execute as @a[tag=gl_host_butcher] unless score #state_butcher gl_ent matches 2 run function final_lanterns:entity/butcher/strip
execute as @a[tag=gl_host_butcher] unless score @s gl_id = #host_butcher gl_ent run function final_lanterns:entity/butcher/strip
execute as @a[tag=gl_host_butcher] run superpower add final_lanterns:host_butcher @s
execute as @a[tag=!gl_host_butcher] run superpower remove final_lanterns:host_butcher @s
execute if score #state_butcher gl_ent matches 1 at @e[tag=gl_ent_butcher] as @a[tag=gl_red,distance=..24] at @s run function final_lanterns:entity/butcher/near_ring
execute if score #state_butcher gl_ent matches 3 run scoreboard players remove #life_butcher gl_ent 1
execute if score #state_butcher gl_ent matches 3 if score #life_butcher gl_ent matches ..0 run function final_lanterns:entity/butcher/break_free
