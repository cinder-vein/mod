summon minecraft:item ~ ~1 ~ {Tags:["gl_eject"],PickupDelay:20s,Age:-32768s,Motion:[0.0d,0.3d,0.0d],Item:{id:"minecraft:stone",Count:1b}}
data modify entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Item set from storage greenlantern:binding cur
data remove entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Item.Slot
execute if data storage greenlantern:binding cur.tag{gl_bound:1b} run data modify entity @e[type=minecraft:item,tag=gl_eject,limit=1,sort=nearest] Owner set from storage greenlantern:binding cur.tag.gl_owner_uuid
function #greenlantern:curios_clear_slot
