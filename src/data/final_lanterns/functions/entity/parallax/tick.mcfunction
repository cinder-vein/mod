execute on passengers run data modify entity @s Rotation set from entity @e[tag=gl_ent_parallax,limit=1] Rotation
execute if entity @a[tag=gl_hunted_parallax,limit=1] facing entity @a[tag=gl_hunted_parallax,limit=1] eyes run tp @s ^ ^ ^0.3 ~ ~
execute as @a[tag=gl_hunted_parallax,tag=!gl_host,scores={gl_ehcd=..0},distance=..2] at @s run function final_lanterns:entity/parallax/host
execute as @a[tag=gl_hunted_parallax,distance=2..10] run title @s actionbar [{"text":"Parallax is right behind you...","color":"#F5CD1E"}]
