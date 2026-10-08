execute store result score #owner gl_tmp run data get entity @s Inventory[{Slot:-106b}].tag.gl_owner
summon minecraft:item ~ ~1 ~ {Tags:["gl_eject"],PickupDelay:20s,Age:-32768s,Motion:[0.0d,0.3d,0.0d],Item:{id:"minecraft:stone",Count:1b}}
data modify entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Item set from entity @s Inventory[{Slot:-106b}]
data modify entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Owner set from entity @s Inventory[{Slot:-106b}].tag.gl_owner_uuid
item replace entity @s weapon.offhand with minecraft:air
particle minecraft:end_rod ~ ~1 ~ 0.2 0.2 0.2 0.05 20 force
tellraw @s [{"text":"This ring has already chosen its bearer. It returns to them.","color":"gray","italic":true}]
playsound minecraft:entity.enderman.teleport player @a[distance=..16] ~ ~ ~ 1 1.4
execute as @a if score @s gl_id = #owner gl_tmp at @s run function final_lanterns:ring/return_to_owner
tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject
