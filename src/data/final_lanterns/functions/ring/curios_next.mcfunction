data modify storage final_lanterns:binding cur set from storage final_lanterns:binding rings[0]
data remove storage final_lanterns:binding rings[0]
scoreboard players set #lantern gl_tmp 0
execute if data storage final_lanterns:binding cur{id:"final_lanterns:greenlanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:yellowlanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:redlanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:orangelanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:bluelanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:pinklanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:indigolanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:whitelanternring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage final_lanterns:binding cur{id:"final_lanterns:blacklanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #lantern gl_tmp matches 1 run function final_lanterns:ring/curios_item
execute if data storage final_lanterns:binding rings[0] run function final_lanterns:ring/curios_next
