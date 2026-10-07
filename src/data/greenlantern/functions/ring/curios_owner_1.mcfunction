execute store result score @s gl_tmp run data get entity @s ForgeCaps."curios:inventory".Curios[{Identifier:"ring"}].StacksHandler.Stacks.Items[{Slot:1}].tag.gl_owner
execute unless score @s gl_tmp = @s gl_id run function greenlantern:ring/curios_eject_1
