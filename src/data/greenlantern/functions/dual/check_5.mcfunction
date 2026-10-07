scoreboard players set #ok gl_tmp 1
execute if score #c1 gl_tmp matches ..4 run function greenlantern:construct/low_charge
execute if score #ok gl_tmp matches 1 if score #c2 gl_tmp matches ..4 run function greenlantern:construct/low_charge
