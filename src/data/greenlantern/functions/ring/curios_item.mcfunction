execute store result score #slot gl_tmp run data get storage greenlantern:binding cur.Slot
execute if data storage greenlantern:binding cur.tag{gl_bound:1b} run function greenlantern:ring/curios_bound
execute unless data storage greenlantern:binding cur.tag{gl_bound:1b} run function greenlantern:ring/curios_unbound
