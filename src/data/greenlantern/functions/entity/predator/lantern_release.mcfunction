execute unless predicate greenlantern:entity/lantern_predator run tellraw @s ["",{"text":"Hold the Lantern of The Predator in your main hand.","color":"gray"}]
execute unless predicate greenlantern:entity/lantern_predator run scoreboard players set #fresh gl_tmp -1
execute if predicate greenlantern:entity/lantern_predator run execute store result score #s gl_tmp run data get entity @s SelectedItem.tag.gl_seal
execute if predicate greenlantern:entity/lantern_predator run scoreboard players set #fresh gl_tmp 0
execute if predicate greenlantern:entity/lantern_predator run execute if score #state_predator gl_ent matches 3 if score #s gl_tmp = #seal_predator gl_ent run scoreboard players set #fresh gl_tmp 1
execute if predicate greenlantern:entity/lantern_predator run execute if score #fresh gl_tmp matches 0 run item replace entity @s weapon.mainhand with greenlantern:violet_power_battery
execute if predicate greenlantern:entity/lantern_predator run execute if score #fresh gl_tmp matches 0 run tellraw @s ["",{"text":"The lantern is empty: the entity broke free long ago.","color":"gray"}]
execute if score #fresh gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:violet_power_battery
execute if score #fresh gl_tmp matches 1 run scoreboard players set #state_predator gl_ent 0
execute if score #fresh gl_tmp matches 1 run particle minecraft:dust 0.84 0.22 0.86 3.0 ~ ~1 ~ 1 2 1 0 200 force
execute if score #fresh gl_tmp matches 1 run tellraw @a ["",{"text":"The Predator bursts free of its lantern and vanishes into the world.","color":"#D737DC"}]
