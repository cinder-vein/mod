execute store result score #owner gl_tmp run data get entity @s Item.tag.gl_owner
execute store result score #s gl_tmp run data get entity @s Item.tag.gl_serial
execute if score #owner gl_tmp = @a[tag=gl_caller,limit=1] gl_id unless score #s gl_tmp = @a[tag=gl_caller,limit=1] gl_ser_red run execute at @s run particle minecraft:smoke ~ ~0.3 ~ 0.1 0.1 0.1 0.02 15 force
execute if score #owner gl_tmp = @a[tag=gl_caller,limit=1] gl_id unless score #s gl_tmp = @a[tag=gl_caller,limit=1] gl_ser_red run kill @s
execute if score #owner gl_tmp = @a[tag=gl_caller,limit=1] gl_id if score #s gl_tmp = @a[tag=gl_caller,limit=1] gl_ser_red run function greenlantern:recall/fly
