execute as @e[tag=gl_ent_nekron] unless score @s gl_eser = #ser_nekron gl_ent run function greenlantern:entity/remove_body
execute unless score #state_nekron gl_ent matches 1 as @e[tag=gl_ent_nekron] at @s run function greenlantern:entity/remove_body
execute if score #state_nekron gl_ent matches 1 run scoreboard players remove #life_nekron gl_ent 1
execute if score #state_nekron gl_ent matches 1 if score #life_nekron gl_ent matches ..0 run function greenlantern:entity/nekron/depart
execute if score #state_nekron gl_ent matches 1 unless entity @e[tag=gl_ent_nekron] run scoreboard players add #miss_nekron gl_ent 1
execute if score #state_nekron gl_ent matches 1 if entity @e[tag=gl_ent_nekron] run scoreboard players set #miss_nekron gl_ent 0
execute if score #state_nekron gl_ent matches 1 if score #miss_nekron gl_ent matches 20.. run scoreboard players set #state_nekron gl_ent 0
execute unless score #state_nekron gl_ent matches 1 run bossbar set greenlantern:nekron players
execute as @a[tag=gl_host_nekron] unless score #state_nekron gl_ent matches 2 run function greenlantern:entity/nekron/strip
execute as @a[tag=gl_host_nekron] unless score @s gl_id = #host_nekron gl_ent run function greenlantern:entity/nekron/strip
execute as @a[tag=gl_host_nekron] run superpower add greenlantern:host_nekron @s
execute as @a[tag=!gl_host_nekron] run superpower remove greenlantern:host_nekron @s
execute if score #state_nekron gl_ent matches 3 run scoreboard players remove #life_nekron gl_ent 1
execute if score #state_nekron gl_ent matches 3 if score #life_nekron gl_ent matches ..0 run function greenlantern:entity/nekron/break_free
