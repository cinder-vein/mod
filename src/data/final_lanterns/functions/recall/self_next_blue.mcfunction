data modify storage final_lanterns:binding rc set from storage final_lanterns:binding scan[0]
data remove storage final_lanterns:binding scan[0]
execute if data storage final_lanterns:binding rc{id:"final_lanterns:bluelanternring",tag:{gl_bound:1b}} run function final_lanterns:recall/self_item_blue
execute if data storage final_lanterns:binding scan[0] run function final_lanterns:recall/self_next_blue
