data modify storage final_lanterns:binding cur set from storage final_lanterns:binding rings[0]
data remove storage final_lanterns:binding rings[0]
scoreboard players set #lantern gl_tmp 0
execute if score #strip gl_tmp matches 1 if data storage final_lanterns:binding cur{id:"final_lanterns:greenlanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 2 if data storage final_lanterns:binding cur{id:"final_lanterns:yellowlanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 3 if data storage final_lanterns:binding cur{id:"final_lanterns:redlanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 4 if data storage final_lanterns:binding cur{id:"final_lanterns:orangelanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 5 if data storage final_lanterns:binding cur{id:"final_lanterns:bluelanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 6 if data storage final_lanterns:binding cur{id:"final_lanterns:pinklanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 7 if data storage final_lanterns:binding cur{id:"final_lanterns:indigolanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 8 if data storage final_lanterns:binding cur{id:"final_lanterns:whitelanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 9 if data storage final_lanterns:binding cur{id:"final_lanterns:blacklanternring"} run scoreboard players set #lantern gl_tmp 1
execute if score #lantern gl_tmp matches 1 store result score #slot gl_tmp run data get storage final_lanterns:binding cur.Slot
execute if score #lantern gl_tmp matches 1 unless score #slot gl_tmp matches 0..31 run scoreboard players set #lantern gl_tmp 0
execute if score #lantern gl_tmp matches 1 run function #final_lanterns:curios_clear_slot
execute if score #lantern gl_tmp matches 1 run scoreboard players add #stripped gl_tmp 1
execute if data storage final_lanterns:binding rings[0] run function final_lanterns:ring/curios_strip_next
