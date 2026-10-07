scoreboard players operation #v gl_tmp = @s gl_id
tag @s remove gl_b0
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b0
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b1
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b1
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b2
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b2
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b3
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b3
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b4
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b4
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b5
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b5
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b6
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b6
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b7
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b7
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b8
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b8
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b9
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b9
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b10
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b10
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b11
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b11
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b12
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b12
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b13
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b13
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b14
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b14
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s remove gl_b15
scoreboard players operation #bit gl_tmp = #v gl_tmp
scoreboard players operation #bit gl_tmp %= #2 gl_cfg
execute if score #bit gl_tmp matches 1 run tag @s add gl_b15
scoreboard players operation #v gl_tmp /= #2 gl_cfg
tag @s add gl_hasid
