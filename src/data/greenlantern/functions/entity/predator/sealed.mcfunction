execute as @a[tag=gl_exo_target] run function greenlantern:entity/predator/strip
scoreboard players set #state_predator gl_ent 3
scoreboard players set #host_predator gl_ent 0
scoreboard players add #seal_predator gl_ent 1
scoreboard players set #life_predator gl_ent 7200
item replace entity @s weapon.mainhand with greenlantern:entity_lantern{CustomModelData:6,gl_entity:6,gl_seal:0,Enchantments:[{}],display:{Name:'{"text": "Lantern of The Predator", "color": "#D737DC", "italic": false}',Lore:['{"text": "Right-click to release it, or to host it.", "color": "gray"}']}}
execute store result storage greenlantern:entity seal int 1 run scoreboard players get #seal_predator gl_ent
item modify entity @s weapon.mainhand greenlantern:entity/seal
particle minecraft:dust 0.84 0.22 0.86 3.0 ~ ~1 ~ 0.6 1 0.6 0 200 force
particle minecraft:flash ~ ~1 ~ 0 0 0 0 1 force
playsound minecraft:block.end_portal_frame.fill player @a[distance=..24] ~ ~ ~ 1 0.6
playsound minecraft:entity.evoker.prepare_summon player @a[distance=..24] ~ ~ ~ 1 0.8
tellraw @a [{"selector": "@s", "color": "#D737DC"}, {"text": " has drawn The Predator out of ", "color": "gray"}, {"selector": "@a[tag=gl_exo_target]", "color": "#D737DC"}, {"text": " and sealed it in a lantern.", "color": "gray"}]
