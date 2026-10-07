execute store result score #owner gl_tmp run data get entity @s SelectedItem.tag.gl_owner
execute if score #owner gl_tmp = @s gl_id run function greenlantern:ring/rebind_mainhand
execute unless score #owner gl_tmp = @s gl_id run function greenlantern:ring/eject_mainhand
