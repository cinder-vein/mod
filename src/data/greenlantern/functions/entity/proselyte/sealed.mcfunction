execute as @a[tag=gl_exo_target] run function greenlantern:entity/proselyte/strip
scoreboard players set #state_proselyte gl_ent 3
scoreboard players set #host_proselyte gl_ent 0
scoreboard players add #seal_proselyte gl_ent 1
scoreboard players set #life_proselyte gl_ent 7200
item replace entity @s weapon.mainhand with greenlantern:entity_lantern{CustomModelData:7,gl_entity:7,gl_seal:0,Enchantments:[{}],display:{Name:'{"text": "Lantern of The Proselyte", "color": "#693CE6", "italic": false}',Lore:['{"text": "Right-click to release it, or to host it.", "color": "gray"}']}}
execute store result storage greenlantern:entity seal int 1 run scoreboard players get #seal_proselyte gl_ent
item modify entity @s weapon.mainhand greenlantern:entity/seal
particle minecraft:dust 0.41 0.24 0.90 3.0 ~ ~1 ~ 0.6 1 0.6 0 200 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force
playsound minecraft:block.end_portal_frame.fill player @a[distance=..24] ~ ~ ~ 1 0.6
playsound minecraft:entity.evoker.prepare_summon player @a[distance=..24] ~ ~ ~ 1 0.8
tellraw @a [{"selector": "@s", "color": "#693CE6"}, {"text": " has drawn The Proselyte out of ", "color": "gray"}, {"selector": "@a[tag=gl_exo_target]", "color": "#693CE6"}, {"text": " and sealed it in a lantern.", "color": "gray"}]
