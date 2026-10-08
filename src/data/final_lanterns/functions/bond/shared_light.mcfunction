function final_lanterns:bond/read
scoreboard players operation #d gl_tmp = #c1 gl_tmp
scoreboard players operation #d gl_tmp -= #c2 gl_tmp
execute if score #d gl_tmp matches 40.. run function final_lanterns:bond/flow_12
execute if score #d gl_tmp matches 10..39 run function final_lanterns:bond/flow_12_small
execute if score #d gl_tmp matches ..-40 run function final_lanterns:bond/flow_21
execute if score #d gl_tmp matches -39..-10 run function final_lanterns:bond/flow_21_small
