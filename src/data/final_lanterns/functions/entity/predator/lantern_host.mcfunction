execute unless predicate final_lanterns:entity/lantern_predator run tellraw @s ["",{"text":"Hold the Lantern of The Predator in your main hand.","color":"gray"}]
execute unless predicate final_lanterns:entity/lantern_predator run scoreboard players set #fresh gl_tmp -1
execute if predicate final_lanterns:entity/lantern_predator run execute store result score #s gl_tmp run data get entity @s SelectedItem.tag.gl_seal
execute if predicate final_lanterns:entity/lantern_predator run scoreboard players set #fresh gl_tmp 0
execute if predicate final_lanterns:entity/lantern_predator run execute if score #state_predator gl_ent matches 3 if score #s gl_tmp = #seal_predator gl_ent run scoreboard players set #fresh gl_tmp 1
execute if predicate final_lanterns:entity/lantern_predator run execute if score #fresh gl_tmp matches 0 run item replace entity @s weapon.mainhand with kubejs:pinklanternbattery
execute if predicate final_lanterns:entity/lantern_predator run execute if score #fresh gl_tmp matches 0 run tellraw @s ["",{"text":"The lantern is empty: the entity broke free long ago.","color":"gray"}]
scoreboard players set #worthy gl_tmp 0
execute if score @s gl_e_love >= #req60 gl_ent run scoreboard players set #worthy gl_tmp 1
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 0 run tellraw @s ["",{"text":"The Predator doesn't answer you: you need ","color":"gray"},{"text":"60% love","color":"#D737DC"},{"text":" (see your Emotional Spectrum menu).","color":"gray"}]
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity @s[tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity @s[tag=!gl_host,scores={gl_ehcd=1..}] run tellraw @s ["",{"text":"No entity will join you yet: you lost one too recently. ","color":"gray"},{"text":"(see your Emotional Spectrum menu)","color":"dark_gray"}]
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity @s[tag=!gl_host,scores={gl_ehcd=..0}] run item replace entity @s weapon.mainhand with kubejs:pinklanternbattery
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity @s[tag=!gl_host,scores={gl_ehcd=..0}] at @s run function final_lanterns:entity/predator/host
