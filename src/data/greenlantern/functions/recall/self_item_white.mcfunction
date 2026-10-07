execute store result score #owner gl_tmp run data get storage greenlantern:binding rc.tag.gl_owner
execute store result score #s gl_tmp run data get storage greenlantern:binding rc.tag.gl_serial
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp = @s gl_ser_white run scoreboard players set #found gl_tmp 1
execute if score #owner gl_tmp = @s gl_id unless score #s gl_tmp = @s gl_ser_white run function greenlantern:recall/dark_inv
