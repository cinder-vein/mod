execute unless predicate greenlantern:entity/lantern_butcher run tellraw @s ["",{"text":"Hold the Lantern of The Butcher in your main hand.","color":"gray"}]
execute unless predicate greenlantern:entity/lantern_butcher run scoreboard players set #fresh gl_tmp -1
execute if predicate greenlantern:entity/lantern_butcher run execute store result score #s gl_tmp run data get entity @s SelectedItem.tag.gl_seal
execute if predicate greenlantern:entity/lantern_butcher run scoreboard players set #fresh gl_tmp 0
execute if predicate greenlantern:entity/lantern_butcher run execute if score #state_butcher gl_ent matches 3 if score #s gl_tmp = #seal_butcher gl_ent run scoreboard players set #fresh gl_tmp 1
execute if predicate greenlantern:entity/lantern_butcher run execute if score #fresh gl_tmp matches 0 run item replace entity @s weapon.mainhand with greenlantern:red_power_battery
execute if predicate greenlantern:entity/lantern_butcher run execute if score #fresh gl_tmp matches 0 run tellraw @s ["",{"text":"The lantern is empty: the entity broke free long ago.","color":"gray"}]
execute if score #fresh gl_tmp matches 1 run item replace entity @s weapon.mainhand with greenlantern:red_power_battery
execute if score #fresh gl_tmp matches 1 run scoreboard players set #state_butcher gl_ent 0
execute if score #fresh gl_tmp matches 1 run particle minecraft:dust 0.86 0.12 0.14 3.0 ~ ~1 ~ 1 2 1 0 200 force
execute if score #fresh gl_tmp matches 1 run tellraw @a ["",{"text":"The Butcher bursts free of its lantern and vanishes into the world.","color":"#DC1E23"}]
