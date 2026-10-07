summon minecraft:wither_skeleton ~ ~ ~ {Tags:["gl_ent","gl_ent_nekron","gl_ent_new"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",Silent:1b,HandItems:[{},{}],HandDropChances:[0f,0f],CustomName:'{"text": "Nekron", "color": "#969BAA"}',Passengers:[{id:"minecraft:item_display",Tags:["gl_entm","gl_entm_nekron"],item_display:"none",view_range:6f,brightness:{sky:15,block:15},item:{id:"greenlantern:entity_body",Count:1b,tag:{CustomModelData:9}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.1f,0.1f,0.1f]}}]}
effect give @e[tag=gl_ent_new] minecraft:invisibility infinite 0 true
execute as @e[tag=gl_ent_new] at @s run particle minecraft:dust 0.59 0.61 0.67 3.0 ~ ~1 ~ 2 2 2 0 200 force
scoreboard players set #placed gl_tmp 1
attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.max_health base set 320
data merge entity @e[tag=gl_ent_new,limit=1] {Health:320f}
attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.knockback_resistance base set 1
attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.follow_range base set 48
effect give @e[tag=gl_ent_new] minecraft:fire_resistance infinite 0 true
effect give @e[tag=gl_ent_new] minecraft:resistance infinite 0 true
attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.attack_damage base set 14
attribute @e[tag=gl_ent_new,limit=1] minecraft:generic.movement_speed base set 0.32
