summon minecraft:item ~ ~0.5 ~ {Tags:["gl_drop"],PickupDelay:40s,Age:-32768s,Item:{id:"minecraft:stone",Count:1b}}
data modify entity @e[type=minecraft:item,tag=gl_drop,limit=1,sort=nearest] Item set from entity @s SelectedItem
item replace entity @s weapon.mainhand with minecraft:air
tag @e[type=minecraft:item,tag=gl_drop] remove gl_drop
title @s actionbar {"text": "This ring won't serve you: drop it for the one it should choose. It binds to the next player who holds it.", "color": "gray"}
