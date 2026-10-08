scoreboard players set #giver gl_tmp 0
execute if predicate final_lanterns:giver_ring_mainhand store result score #giver gl_tmp run data get entity @s SelectedItem.tag.gl_giver
execute if score #giver gl_tmp = @s gl_id run function final_lanterns:ring/giver_held_mainhand
execute unless score #giver gl_tmp = @s gl_id run function final_lanterns:ring/claim_new_mainhand
