data modify storage greenlantern:binding cur set from storage greenlantern:binding rings[0]
data remove storage greenlantern:binding rings[0]
scoreboard players set #lantern gl_tmp 0
execute if data storage greenlantern:binding cur{id:"greenlantern:green_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:yellow_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:red_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:orange_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:blue_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:violet_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:indigo_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:white_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:black_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #lantern gl_tmp matches 1 run function greenlantern:ring/curios_item
execute if data storage greenlantern:binding rings[0] run function greenlantern:ring/curios_next
