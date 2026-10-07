scoreboard players set #found gl_tmp 2
execute store result score #slot gl_tmp run data get storage greenlantern:binding rc.Slot
summon minecraft:item ~ ~0.5 ~ {Tags:["gl_drop"],PickupDelay:0s,Age:-32768s,Item:{id:"minecraft:stone",Count:1b}}
data modify entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Item set from storage greenlantern:binding rc
data remove entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Item.Slot
data modify entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Owner set from entity @s UUID
tag @e[type=minecraft:item,tag=gl_drop] remove gl_drop
function greenlantern:recall/clear_ender_slot
