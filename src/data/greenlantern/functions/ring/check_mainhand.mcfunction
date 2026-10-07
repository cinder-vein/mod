execute store result score @s gl_tmp run data get entity @s SelectedItem.tag.gl_owner
execute unless score @s gl_tmp = @s gl_id run function greenlantern:ring/eject_mainhand
