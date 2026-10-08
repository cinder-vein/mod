data modify storage final_lanterns:binding rc set from storage final_lanterns:binding scan[0]
data remove storage final_lanterns:binding scan[0]
execute if data storage final_lanterns:binding rc{id:"final_lanterns:pinklanternring",tag:{gl_bound:1b}} run function final_lanterns:recall/curios_item_violet
execute if data storage final_lanterns:binding scan[0] run function final_lanterns:recall/curios_next_violet
