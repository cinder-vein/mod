summon minecraft:bat ~ ~ ~ {Tags:["gl_ent","gl_ent_life","gl_ent_new"],PersistenceRequired:1b,NoAI:1b,NoGravity:1b,Invulnerable:1b,Silent:1b,DeathLootTable:"minecraft:empty",Passengers:[{id:"minecraft:item_display",Tags:["gl_entm","gl_entm_life"],item_display:"none",view_range:6f,brightness:{sky:15,block:15},item:{id:"greenlantern:entity_body",Count:1b,tag:{CustomModelData:8}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.1f,0.1f,0.1f]}}]}
effect give @e[tag=gl_ent_new] minecraft:invisibility infinite 0 true
execute as @e[tag=gl_ent_new] at @s run particle minecraft:dust 0.92 0.95 0.98 3.0 ~ ~1 ~ 2 2 2 0 200 force
scoreboard players set #placed gl_tmp 1
