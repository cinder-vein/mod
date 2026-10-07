function greenlantern:dual/read
scoreboard players operation #sum gl_tmp = #c1 gl_tmp
scoreboard players operation #sum gl_tmp += #c2 gl_tmp
scoreboard players operation @s gl_dmax = #m1 gl_tmp
scoreboard players operation @s gl_dmax += #m2 gl_tmp
execute unless score @s gl_dlast = #sum gl_tmp run function greenlantern:dual/mirror_set
