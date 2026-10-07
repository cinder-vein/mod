scoreboard players operation #owner gl_tmp = @s gl_tmp
summon minecraft:item ~ ~1.4 ~ {Tags:["gl_eject"],PickupDelay:40s,Item:{id:"minecraft:stone",Count:1b}}
data modify entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Item set from entity @s Inventory[{Slot:-106b}]
item replace entity @s weapon.offhand with minecraft:air
data merge entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] {Motion:[0.0d,0.45d,0.0d]}
execute as @a if score @s gl_id = #owner gl_tmp at @s run tp @e[type=minecraft:item,tag=gl_eject] ~ ~1 ~
particle minecraft:end_rod ~ ~1.4 ~ 0.2 0.2 0.2 0.05 20 force
tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject
tellraw @s [{"text":"This ring has already chosen its bearer. It returns to them.","color":"gray","italic":true}]
playsound minecraft:entity.enderman.teleport player @s ~ ~ ~ 1 1.4
