execute as @a[tag=kill] unless entity @a[tag=battery] run damage @s 99999 final_lanterns:red_lantern_death
execute at @a[tag=kill] unless entity @a[tag=battery] run particle minecraft:dust 1 0 0 2 ~ ~0.5 ~ 1 1 1 0.5 200
execute at @a[tag=kill] unless entity @a[tag=battery] run playsound minecraft:block.respawn_anchor.deplete player @a ~ ~ ~ 1 1.5
execute at @a[tag=kill] unless entity @a[tag=battery] run playsound minecraft:entity.generic.explode player @a ~ ~ ~ 1 1.5

execute as @a[tag=kill,tag=!battery] run tag @a remove kill