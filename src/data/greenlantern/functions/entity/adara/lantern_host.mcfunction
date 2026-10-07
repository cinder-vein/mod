execute unless predicate greenlantern:entity/lantern_adara run tellraw @s ["",{"text":"Hold the Lantern of Adara in your main hand.","color":"gray"}]
execute unless predicate greenlantern:entity/lantern_adara run scoreboard players set #fresh gl_tmp -1
execute if predicate greenlantern:entity/lantern_adara run execute store result score #s gl_tmp run data get entity @s SelectedItem.tag.gl_seal
execute if predicate greenlantern:entity/lantern_adara run scoreboard players set #fresh gl_tmp 0
execute if predicate greenlantern:entity/lantern_adara run execute if score #state_adara gl_ent matches 3 if score #s gl_tmp = #seal_adara gl_ent run scoreboard players set #fresh gl_tmp 1
execute if predicate greenlantern:entity/lantern_adara run execute if score #fresh gl_tmp matches 0 run item replace entity @s weapon.mainhand with greenlantern:blue_power_battery
execute if predicate greenlantern:entity/lantern_adara run execute if score #fresh gl_tmp matches 0 run tellraw @s ["",{"text":"The lantern is empty: the entity broke free long ago.","color":"gray"}]
scoreboard players set #worthy gl_tmp 0
execute if score @s gl_e_hope >= #req100 gl_ent run scoreboard players set #worthy gl_tmp 1
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 0 run tellraw @s ["",{"text":"Adara doesn't answer you: you need ","color":"gray"},{"text":"100% hope","color":"#2882FF"},{"text":" (see your Emotional Spectrum menu).","color":"gray"}]
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 if entity @s[tag=gl_host] run tellraw @s ["",{"text":"You already host an entity.","color":"gray"}]
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 unless entity @s[tag=gl_host] run item replace entity @s weapon.mainhand with greenlantern:blue_power_battery
execute if score #fresh gl_tmp matches 1 if score #worthy gl_tmp matches 1 unless entity @s[tag=gl_host] at @s run function greenlantern:entity/adara/host
