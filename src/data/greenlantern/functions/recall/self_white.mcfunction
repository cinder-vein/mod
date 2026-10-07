data remove storage greenlantern:binding scan
data modify storage greenlantern:binding scan set from entity @s Inventory
execute if data storage greenlantern:binding scan[0] run function greenlantern:recall/self_next_white
data remove storage greenlantern:binding scan
data modify storage greenlantern:binding scan set from entity @s ForgeCaps."curios:inventory".Curios[{Identifier:"ring"}].StacksHandler.Stacks.Items
execute if data storage greenlantern:binding scan[0] run function greenlantern:recall/curios_next_white
data remove storage greenlantern:binding scan
execute if score #found gl_tmp matches 0 run data modify storage greenlantern:binding scan set from entity @s EnderItems
execute if data storage greenlantern:binding scan[0] run function greenlantern:recall/ender_next_white
