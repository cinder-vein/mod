execute store result score #eid gl_tmp run data get storage final_lanterns:binding sers[0].id
execute unless score #eid gl_tmp = @s gl_id run data modify storage final_lanterns:binding rest append from storage final_lanterns:binding sers[0]
data remove storage final_lanterns:binding sers[0]
execute if data storage final_lanterns:binding sers[0] run function final_lanterns:ring/save_next
