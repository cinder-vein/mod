data remove storage final_lanterns:binding carry
data modify storage final_lanterns:binding carry set from entity @s Inventory
execute if data storage final_lanterns:binding carry[0] run function final_lanterns:ring/carry_next
