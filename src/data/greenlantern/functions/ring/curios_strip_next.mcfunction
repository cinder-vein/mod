data modify storage greenlantern:binding cur set from storage greenlantern:binding rings[0]
data remove storage greenlantern:binding rings[0]
scoreboard players set #lantern gl_tmp 0
execute if score #strip gl_tmp matches 1 if data storage greenlantern:binding cur{id:"greenlantern:green_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 2 if data storage greenlantern:binding cur{id:"greenlantern:yellow_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 3 if data storage greenlantern:binding cur{id:"greenlantern:red_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 4 if data storage greenlantern:binding cur{id:"greenlantern:orange_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 5 if data storage greenlantern:binding cur{id:"greenlantern:blue_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 6 if data storage greenlantern:binding cur{id:"greenlantern:violet_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 7 if data storage greenlantern:binding cur{id:"greenlantern:indigo_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 8 if data storage greenlantern:binding cur{id:"greenlantern:white_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #strip gl_tmp matches 9 if data storage greenlantern:binding cur{id:"greenlantern:black_lantern_ring"} run scoreboard players set #lantern gl_tmp 1
execute if score #lantern gl_tmp matches 1 store result score #slot gl_tmp run data get storage greenlantern:binding cur.Slot
execute if score #lantern gl_tmp matches 1 unless score #slot gl_tmp matches 0..31 run scoreboard players set #lantern gl_tmp 0
execute if score #lantern gl_tmp matches 1 run function #greenlantern:curios_clear_slot
execute if score #lantern gl_tmp matches 1 run scoreboard players add #stripped gl_tmp 1
execute if data storage greenlantern:binding rings[0] run function greenlantern:ring/curios_strip_next
