data remove storage final_lanterns:binding scan
data modify storage final_lanterns:binding scan set from entity @s Inventory
execute if data storage final_lanterns:binding scan[0] run function final_lanterns:recall/self_next_red
data remove storage final_lanterns:binding scan
data modify storage final_lanterns:binding scan set from entity @s ForgeCaps."curios:inventory".Curios[{Identifier:"lantern_rings"}].StacksHandler.Stacks.Items
execute if data storage final_lanterns:binding scan[0] run function final_lanterns:recall/curios_next_red
data remove storage final_lanterns:binding scan
execute if score #found gl_tmp matches 0 run data modify storage final_lanterns:binding scan set from entity @s EnderItems
execute if data storage final_lanterns:binding scan[0] run function final_lanterns:recall/ender_next_red
