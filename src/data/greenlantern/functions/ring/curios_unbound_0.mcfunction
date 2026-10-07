summon minecraft:item ~ ~1.4 ~ {Tags:["gl_eject"],PickupDelay:40s,Item:{id:"minecraft:stone",Count:1b}}
data modify entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Item set from entity @s ForgeCaps."curios:inventory".Curios[{Identifier:"ring"}].StacksHandler.Stacks.Items[{Slot:0}]
data remove entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Item.Slot
curios replace ring 0 @s with minecraft:air
data merge entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] {Motion:[0.0d,0.45d,0.0d]}
tag @e[type=minecraft:item,tag=gl_eject] remove gl_eject
tellraw @s [{"text":"Hold a new ring in your hand once to bind it to you, then wear it.","color":"gray","italic":true}]
