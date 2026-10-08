execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_proselyte,limit=1] Rotation
execute as @a[tag=!gl_host,scores={gl_edc_proselyte=..0,gl_ehcd=..0},distance=..40] at @s if score @s gl_e_compassion >= #req100 gl_ent run tag @s add gl_ent_worthy
execute if entity @a[tag=gl_ent_worthy,distance=6..40] facing entity @p[tag=gl_ent_worthy] eyes run tp @s ^ ^ ^0.2 ~ ~
execute unless entity @a[tag=gl_ent_worthy,distance=..40] run tp @s ~ ~ ~ ~1 ~
execute if entity @a[tag=gl_ent_worthy,distance=..6] facing entity @p[tag=gl_ent_worthy] eyes run tp @s ~ ~ ~ ~ ~
execute as @a[tag=gl_ent_worthy,distance=..8,tag=!gl_eoffer_proselyte] run function final_lanterns:entity/proselyte/offer
tag @a[tag=gl_ent_worthy] remove gl_ent_worthy
