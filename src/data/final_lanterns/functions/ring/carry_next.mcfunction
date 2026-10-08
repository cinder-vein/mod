data modify storage final_lanterns:binding cur set from storage final_lanterns:binding carry[0]
data remove storage final_lanterns:binding carry[0]
scoreboard players set #corps gl_tmp 0
execute if data storage final_lanterns:binding cur{id:"final_lanterns:greenlanternring"} run scoreboard players set #corps gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:yellowlanternring"} run scoreboard players set #corps gl_tmp 2
execute if data storage final_lanterns:binding cur{id:"final_lanterns:redlanternring"} run scoreboard players set #corps gl_tmp 3
execute if data storage final_lanterns:binding cur{id:"final_lanterns:orangelanternring"} run scoreboard players set #corps gl_tmp 4
execute if data storage final_lanterns:binding cur{id:"final_lanterns:bluelanternring"} run scoreboard players set #corps gl_tmp 5
execute if data storage final_lanterns:binding cur{id:"final_lanterns:pinklanternring"} run scoreboard players set #corps gl_tmp 6
execute if data storage final_lanterns:binding cur{id:"final_lanterns:indigolanternring"} run scoreboard players set #corps gl_tmp 7
execute if data storage final_lanterns:binding cur{id:"final_lanterns:whitelanternring"} run scoreboard players set #corps gl_tmp 8
execute if data storage final_lanterns:binding cur{id:"final_lanterns:blacklanternring"} run scoreboard players set #corps gl_tmp 9
execute if score #corps gl_tmp matches 1.. unless data storage final_lanterns:binding cur.tag{gl_bound:1b} run function final_lanterns:ring/carry_item
execute if data storage final_lanterns:binding carry[0] run function final_lanterns:ring/carry_next
