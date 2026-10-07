scoreboard players operation #diff gl_tmp = #c1 gl_tmp
scoreboard players operation #diff gl_tmp -= #c2 gl_tmp
execute if score #diff gl_tmp matches 20.. if score #c2 gl_tmp < #m2 gl_tmp run function greenlantern:dual/move/1to2_10
execute if score #diff gl_tmp matches 2..19 if score #c2 gl_tmp < #m2 gl_tmp run function greenlantern:dual/move/1to2_1
execute if score #diff gl_tmp matches ..-20 if score #c1 gl_tmp < #m1 gl_tmp run function greenlantern:dual/move/2to1_10
execute if score #diff gl_tmp matches -19..-2 if score #c1 gl_tmp < #m1 gl_tmp run function greenlantern:dual/move/2to1_1
