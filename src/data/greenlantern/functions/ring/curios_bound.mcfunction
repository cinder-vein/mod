execute store result score #owner gl_tmp run data get storage greenlantern:binding cur.tag.gl_owner
execute unless score #owner gl_tmp = @s gl_id run function greenlantern:ring/curios_eject
execute if score #owner gl_tmp = @s gl_id run function greenlantern:ring/curios_serial
