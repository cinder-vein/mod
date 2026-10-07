execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_predator,limit=1] Rotation
execute if entity @a[tag=gl_hunted_predator,limit=1] facing entity @a[tag=gl_hunted_predator,limit=1] eyes run tp @s ^ ^ ^0.3 ~ ~
execute as @a[tag=gl_hunted_predator,distance=..2] at @s run function greenlantern:entity/predator/host
execute as @a[tag=gl_hunted_predator,distance=2..10] run title @s actionbar [{"text":"The Predator is right behind you...","color":"#D737DC"}]
