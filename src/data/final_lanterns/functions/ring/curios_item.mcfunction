execute store result score #slot gl_tmp run data get storage final_lanterns:binding cur.Slot
execute if data storage final_lanterns:binding cur.tag{gl_bound:1b} run function final_lanterns:ring/curios_bound
execute unless data storage final_lanterns:binding cur.tag{gl_bound:1b} run function final_lanterns:ring/curios_unbound
