execute as @a[tag=gl_exo_target] run function final_lanterns:entity/butcher/strip
scoreboard players set #state_butcher gl_ent 3
scoreboard players set #host_butcher gl_ent 0
scoreboard players add #seal_butcher gl_ent 1
scoreboard players set #life_butcher gl_ent 7200
item replace entity @s weapon.mainhand with final_lanterns:entity_lantern{CustomModelData:3,gl_entity:3,gl_seal:0,Enchantments:[{}],display:{Name:'{"text": "Lantern of The Butcher", "color": "#DC1E23", "italic": false}',Lore:['{"text": "Right-click to release it, or to host it.", "color": "gray"}']}}
execute store result storage final_lanterns:entity seal int 1 run scoreboard players get #seal_butcher gl_ent
item modify entity @s weapon.mainhand final_lanterns:entity/seal
particle minecraft:dust 0.86 0.12 0.14 3.0 ~ ~1 ~ 0.6 1 0.6 0 200 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force
playsound minecraft:block.end_portal_frame.fill player @a[distance=..24] ~ ~ ~ 1 0.6
playsound minecraft:entity.evoker.prepare_summon player @a[distance=..24] ~ ~ ~ 1 0.8
tellraw @a [{"selector": "@s", "color": "#DC1E23"}, {"text": " has drawn The Butcher out of ", "color": "gray"}, {"selector": "@a[tag=gl_exo_target]", "color": "#DC1E23"}, {"text": " and sealed it in a lantern.", "color": "gray"}]
