execute store result score #eid gl_tmp run data get storage greenlantern:binding sers[0].id
execute unless score #eid gl_tmp = @s gl_id run data modify storage greenlantern:binding rest append from storage greenlantern:binding sers[0]
data remove storage greenlantern:binding sers[0]
execute if data storage greenlantern:binding sers[0] run function greenlantern:ring/save_next
