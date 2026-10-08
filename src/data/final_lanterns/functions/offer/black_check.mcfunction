scoreboard players set #low gl_tmp 0
execute if score @s gl_e_will < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_fear < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_rage < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_greed < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_hope < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_love < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_compassion < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score #low gl_tmp matches 4.. run function final_lanterns:offer/start_black
