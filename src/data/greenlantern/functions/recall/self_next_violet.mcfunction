data modify storage greenlantern:binding rc set from storage greenlantern:binding scan[0]
data remove storage greenlantern:binding scan[0]
execute if data storage greenlantern:binding rc{id:"greenlantern:violet_lantern_ring",tag:{gl_bound:1b}} run function greenlantern:recall/self_item_violet
execute if data storage greenlantern:binding scan[0] run function greenlantern:recall/self_next_violet
