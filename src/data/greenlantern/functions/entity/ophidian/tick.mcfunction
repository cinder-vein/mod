execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_ophidian,limit=1] Rotation
execute as @a[tag=!gl_host,distance=..40,scores={gl_edc_ophidian=..0}] at @s if score @s gl_e_greed >= #req100 gl_ent run tag @s add gl_ent_worthy
execute if entity @a[tag=gl_ent_worthy,distance=6..40] facing entity @p[tag=gl_ent_worthy] eyes run tp @s ^ ^ ^0.2 ~ ~
execute unless entity @a[tag=gl_ent_worthy,distance=..40] run tp @s ~ ~ ~ ~1 ~
execute if entity @a[tag=gl_ent_worthy,distance=..6] facing entity @p[tag=gl_ent_worthy] eyes run tp @s ~ ~ ~ ~ ~
execute unless entity @s[tag=gl_ent_fed] as @e[type=minecraft:item,distance=..4,limit=1,nbt={Item:{id:"minecraft:gold_block"}}] run function greenlantern:entity/ophidian/fed
execute unless entity @s[tag=gl_ent_fed] as @a[tag=gl_ent_worthy,distance=..8] run title @s actionbar [{"text":"Ophidian eyes your hoard. Throw it a block of gold.","color":"#FA8214"}]
execute if entity @s[tag=gl_ent_fed] as @a[tag=gl_ent_worthy,distance=..8,tag=!gl_eoffer_ophidian] run function greenlantern:entity/ophidian/offer
tag @a[tag=gl_ent_worthy] remove gl_ent_worthy
