execute store result score #eid gl_tmp run data get storage greenlantern:binding look[0].id
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_green run data get storage greenlantern:binding look[0].green
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_yellow run data get storage greenlantern:binding look[0].yellow
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_red run data get storage greenlantern:binding look[0].red
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_orange run data get storage greenlantern:binding look[0].orange
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_blue run data get storage greenlantern:binding look[0].blue
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_violet run data get storage greenlantern:binding look[0].violet
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_indigo run data get storage greenlantern:binding look[0].indigo
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_white run data get storage greenlantern:binding look[0].white
execute if score #eid gl_tmp = @s gl_id store result score @s gl_ser_black run data get storage greenlantern:binding look[0].black
data remove storage greenlantern:binding look[0]
execute if data storage greenlantern:binding look[0] run function greenlantern:ring/load_next
