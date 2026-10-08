execute unless predicate final_lanterns:entity/lantern_parallax run tellraw @s ["",{"text":"Hold the Lantern of Parallax in your main hand.","color":"gray"}]
execute unless predicate final_lanterns:entity/lantern_parallax run scoreboard players set #fresh gl_tmp -1
execute if predicate final_lanterns:entity/lantern_parallax run execute store result score #s gl_tmp run data get entity @s SelectedItem.tag.gl_seal
execute if predicate final_lanterns:entity/lantern_parallax run scoreboard players set #fresh gl_tmp 0
execute if predicate final_lanterns:entity/lantern_parallax run execute if score #state_parallax gl_ent matches 3 if score #s gl_tmp = #seal_parallax gl_ent run scoreboard players set #fresh gl_tmp 1
execute if predicate final_lanterns:entity/lantern_parallax run execute if score #fresh gl_tmp matches 0 run item replace entity @s weapon.mainhand with kubejs:yellowlanternbattery
execute if predicate final_lanterns:entity/lantern_parallax run execute if score #fresh gl_tmp matches 0 run tellraw @s ["",{"text":"The lantern is empty: the entity broke free long ago.","color":"gray"}]
execute if score #fresh gl_tmp matches 1 run item replace entity @s weapon.mainhand with kubejs:yellowlanternbattery
execute if score #fresh gl_tmp matches 1 run scoreboard players set #state_parallax gl_ent 0
execute if score #fresh gl_tmp matches 1 run particle minecraft:dust 0.96 0.80 0.12 3.0 ~ ~1 ~ 1 2 1 0 200 force
execute if score #fresh gl_tmp matches 1 run tellraw @a ["",{"text":"Parallax bursts free of its lantern and vanishes into the world.","color":"#F5CD1E"}]
