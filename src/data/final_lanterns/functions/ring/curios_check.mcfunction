data remove storage final_lanterns:binding rings
data modify storage final_lanterns:binding rings set from entity @s ForgeCaps."curios:inventory".Curios[{Identifier:"lantern_rings"}].StacksHandler.Stacks.Items
execute if data storage final_lanterns:binding rings[0] run function final_lanterns:ring/curios_next
