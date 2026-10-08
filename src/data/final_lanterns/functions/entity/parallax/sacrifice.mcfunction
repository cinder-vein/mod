scoreboard players set #ok gl_tmp 0
execute if score #state_parallax gl_ent matches 0..1 if entity @s[tag=!gl_host,scores={gl_ehcd=..0}] run scoreboard players set #ok gl_tmp 1
execute if score #ok gl_tmp matches 1 run function final_lanterns:entity/parallax/host
execute if score #ok gl_tmp matches 1 run advancement grant @s only lanterncorps:parallax
execute if score #ok gl_tmp matches 0 run tellraw @s ["",{"text":"Parallax does not answer your sacrifice: ","color":"yellow"},{"text":"it is bound elsewhere, or you can't take an entity right now.","color":"gray"}]
