scoreboard players set #r gl_tmp 0
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 1
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 2
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 4
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 8
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 16
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 32
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 64
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 128
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 256
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 512
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 1024
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 2048
execute if predicate final_lanterns:random/half run scoreboard players add #r gl_tmp 4096
scoreboard players operation #r gl_tmp *= #span gl_cfg
scoreboard players operation #r gl_tmp /= #bits gl_cfg
scoreboard players add #r gl_tmp 10000
