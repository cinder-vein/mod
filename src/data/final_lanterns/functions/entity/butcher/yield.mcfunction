tag @a remove gl_ent_victor
tag @p[distance=..24,tag=!gl_host,scores={gl_ehcd=..0}] add gl_ent_victor
execute as @a[tag=gl_ent_victor] if score @s gl_e_rage >= #req95 gl_ent run tag @s add gl_ent_worthy
execute as @a[tag=gl_ent_worthy,limit=1] at @s run function final_lanterns:entity/butcher/host
execute unless entity @a[tag=gl_ent_worthy] run function final_lanterns:entity/butcher/scorn
tag @a remove gl_ent_worthy
tag @a remove gl_ent_victor
