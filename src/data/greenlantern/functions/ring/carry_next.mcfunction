data modify storage greenlantern:binding cur set from storage greenlantern:binding carry[0]
data remove storage greenlantern:binding carry[0]
scoreboard players set #corps gl_tmp 0
execute if data storage greenlantern:binding cur{id:"greenlantern:green_lantern_ring"} run scoreboard players set #corps gl_tmp 1
execute if data storage greenlantern:binding cur{id:"greenlantern:yellow_lantern_ring"} run scoreboard players set #corps gl_tmp 2
execute if data storage greenlantern:binding cur{id:"greenlantern:red_lantern_ring"} run scoreboard players set #corps gl_tmp 3
execute if data storage greenlantern:binding cur{id:"greenlantern:orange_lantern_ring"} run scoreboard players set #corps gl_tmp 4
execute if data storage greenlantern:binding cur{id:"greenlantern:blue_lantern_ring"} run scoreboard players set #corps gl_tmp 5
execute if data storage greenlantern:binding cur{id:"greenlantern:violet_lantern_ring"} run scoreboard players set #corps gl_tmp 6
execute if data storage greenlantern:binding cur{id:"greenlantern:indigo_lantern_ring"} run scoreboard players set #corps gl_tmp 7
execute if data storage greenlantern:binding cur{id:"greenlantern:white_lantern_ring"} run scoreboard players set #corps gl_tmp 8
execute if data storage greenlantern:binding cur{id:"greenlantern:black_lantern_ring"} run scoreboard players set #corps gl_tmp 9
execute if score #corps gl_tmp matches 1.. unless data storage greenlantern:binding cur.tag{gl_bound:1b} run function greenlantern:ring/carry_item
execute if data storage greenlantern:binding carry[0] run function greenlantern:ring/carry_next
