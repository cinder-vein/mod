execute store result entity @s Motion[0] double 0.002500 run scoreboard players get #x1 gl_tmp
execute store result entity @s Motion[1] double 0.002500 run scoreboard players get #y1 gl_tmp
execute store result entity @s Motion[2] double 0.002500 run scoreboard players get #z1 gl_tmp
data modify entity @s Owner set from entity @a[tag=gl_shooter,limit=1] UUID
tag @s remove gl_proj_new
