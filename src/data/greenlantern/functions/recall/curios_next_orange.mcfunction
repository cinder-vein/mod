data modify storage greenlantern:binding rc set from storage greenlantern:binding scan[0]
data remove storage greenlantern:binding scan[0]
execute if data storage greenlantern:binding rc{id:"greenlantern:orange_lantern_ring",tag:{gl_bound:1b}} run function greenlantern:recall/curios_item_orange
execute if data storage greenlantern:binding scan[0] run function greenlantern:recall/curios_next_orange
