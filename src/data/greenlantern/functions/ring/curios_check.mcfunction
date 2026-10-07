data remove storage greenlantern:binding rings
data modify storage greenlantern:binding rings set from entity @s ForgeCaps."curios:inventory".Curios[{Identifier:"ring"}].StacksHandler.Stacks.Items
execute if data storage greenlantern:binding rings[0] run function greenlantern:ring/curios_next
