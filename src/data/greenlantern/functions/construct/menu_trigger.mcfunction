execute unless score @s gl_slotinit matches 1 run function greenlantern:construct/default_slots
scoreboard players operation #v gl_tmp = @s gl_construct
scoreboard players set @s gl_construct 0
scoreboard players enable @s gl_construct
execute if score #v gl_tmp matches 1..5 run scoreboard players operation @s gl_cfgslot = #v gl_tmp
execute if score #v gl_tmp matches 11..14 run scoreboard players operation @s gl_cfgcat = #v gl_tmp
execute if score #v gl_tmp matches 11..14 run scoreboard players remove @s gl_cfgcat 10
execute if score #v gl_tmp matches 99 run function greenlantern:construct/assign_0
execute if score #v gl_tmp matches 101 run function greenlantern:construct/assign_1
execute if score #v gl_tmp matches 102 run function greenlantern:construct/assign_2
execute if score #v gl_tmp matches 103 run function greenlantern:construct/assign_3
execute if score #v gl_tmp matches 104 run function greenlantern:construct/assign_4
execute if score #v gl_tmp matches 105 run function greenlantern:construct/assign_5
execute if score #v gl_tmp matches 106 run function greenlantern:construct/assign_6
execute if score #v gl_tmp matches 107 run function greenlantern:construct/assign_7
execute if score #v gl_tmp matches 108 run function greenlantern:construct/assign_8
execute if score #v gl_tmp matches 109 run function greenlantern:construct/assign_9
execute if score #v gl_tmp matches 110 run function greenlantern:construct/assign_10
execute if score #v gl_tmp matches 111 run function greenlantern:construct/assign_11
execute if score #v gl_tmp matches 112 run function greenlantern:construct/assign_12
execute if score #v gl_tmp matches 113 run function greenlantern:construct/assign_13
execute if score #v gl_tmp matches 114 run function greenlantern:construct/assign_14
execute if score #v gl_tmp matches 115 run function greenlantern:construct/assign_15
execute if score #v gl_tmp matches 116 run function greenlantern:construct/assign_16
execute if score #v gl_tmp matches 117 run function greenlantern:construct/assign_17
execute if score #v gl_tmp matches 118 run function greenlantern:construct/assign_18
execute if score #v gl_tmp matches 119 run function greenlantern:construct/assign_19
execute if score #v gl_tmp matches 120 run function greenlantern:construct/assign_20
function greenlantern:construct/menu
