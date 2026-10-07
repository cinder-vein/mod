execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_life,limit=1] Rotation
execute as @a[tag=!gl_host,distance=..40,scores={gl_edc_life=..0}] at @s if score @s gl_e_will >= #req100 gl_ent if score @s gl_e_fear >= #req100 gl_ent if score @s gl_e_rage >= #req100 gl_ent if score @s gl_e_greed >= #req100 gl_ent if score @s gl_e_hope >= #req100 gl_ent if score @s gl_e_love >= #req100 gl_ent if score @s gl_e_compassion >= #req100 gl_ent run tag @s add gl_ent_worthy
execute if entity @a[tag=gl_ent_worthy,distance=6..40] facing entity @p[tag=gl_ent_worthy] eyes run tp @s ^ ^ ^0.2 ~ ~
execute unless entity @a[tag=gl_ent_worthy,distance=..40] run tp @s ~ ~ ~ ~1 ~
execute if entity @a[tag=gl_ent_worthy,distance=..6] facing entity @p[tag=gl_ent_worthy] eyes run tp @s ~ ~ ~ ~ ~
execute as @a[tag=gl_ent_worthy,distance=..8,tag=!gl_eoffer_life] run function greenlantern:entity/life/offer
tag @a[tag=gl_ent_worthy] remove gl_ent_worthy
