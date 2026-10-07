scoreboard players set #giver gl_tmp 0
execute if predicate greenlantern:giver_ring_mainhand store result score #giver gl_tmp run data get entity @s SelectedItem.tag.gl_giver
execute unless score #giver gl_tmp = @s gl_id run function greenlantern:ring/bind_mainhand
