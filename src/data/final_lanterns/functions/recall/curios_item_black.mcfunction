execute store result score #owner gl_tmp run data get storage final_lanterns:binding rc.tag.gl_owner
execute store result score #s gl_tmp run data get storage final_lanterns:binding rc.tag.gl_serial
execute if score #owner gl_tmp = @s gl_id if score #s gl_tmp = @s gl_ser_black run scoreboard players set #found gl_tmp 1
execute if score #owner gl_tmp = @s gl_id unless score #s gl_tmp = @s gl_ser_black run function final_lanterns:recall/dark_curios
