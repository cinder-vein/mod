execute as @e[tag=gl_ent_ion] unless score @s gl_eser = #ser_ion gl_ent run function greenlantern:entity/remove_body
execute unless score #state_ion gl_ent matches 1 as @e[tag=gl_ent_ion] at @s run function greenlantern:entity/remove_body
execute if score #state_ion gl_ent matches 1 run scoreboard players remove #life_ion gl_ent 1
execute if score #state_ion gl_ent matches 1 if score #life_ion gl_ent matches ..0 run function greenlantern:entity/ion/depart
execute if score #state_ion gl_ent matches 1 unless entity @e[tag=gl_ent_ion] run scoreboard players add #miss_ion gl_ent 1
execute if score #state_ion gl_ent matches 1 if entity @e[tag=gl_ent_ion] run scoreboard players set #miss_ion gl_ent 0
execute if score #state_ion gl_ent matches 1 if score #miss_ion gl_ent matches 20.. run scoreboard players set #state_ion gl_ent 0
execute as @a[tag=gl_host_ion] unless score #state_ion gl_ent matches 2 run function greenlantern:entity/ion/strip
execute as @a[tag=gl_host_ion] unless score @s gl_id = #host_ion gl_ent run function greenlantern:entity/ion/strip
execute as @a[tag=gl_host_ion] run superpower add greenlantern:host_ion @s
execute as @a[tag=!gl_host_ion] run superpower remove greenlantern:host_ion @s
execute if score #state_ion gl_ent matches 3 run scoreboard players remove #life_ion gl_ent 1
execute if score #state_ion gl_ent matches 3 if score #life_ion gl_ent matches ..0 run function greenlantern:entity/ion/break_free
