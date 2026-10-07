scoreboard players set #free gl_tmp 1
execute if data entity @s SelectedItem run scoreboard players set #free gl_tmp 0
execute if score #free gl_tmp matches 0 run function greenlantern:construct/stash_main
