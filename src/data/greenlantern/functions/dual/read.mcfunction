scoreboard players set #c1 gl_tmp 0
scoreboard players set #c2 gl_tmp 0
scoreboard players set #m1 gl_tmp 1000
scoreboard players set #m2 gl_tmp 1000
scoreboard players set #ready gl_tmp 0
execute if entity @s[tag=gl_p1_green] run function greenlantern:dual/read1/green
execute if entity @s[tag=gl_p2_green] run function greenlantern:dual/read2/green
execute if entity @s[tag=gl_p1_yellow] run function greenlantern:dual/read1/yellow
execute if entity @s[tag=gl_p2_yellow] run function greenlantern:dual/read2/yellow
execute if entity @s[tag=gl_p1_red] run function greenlantern:dual/read1/red
execute if entity @s[tag=gl_p2_red] run function greenlantern:dual/read2/red
execute if entity @s[tag=gl_p1_orange] run function greenlantern:dual/read1/orange
execute if entity @s[tag=gl_p2_orange] run function greenlantern:dual/read2/orange
execute if entity @s[tag=gl_p1_blue] run function greenlantern:dual/read1/blue
execute if entity @s[tag=gl_p2_blue] run function greenlantern:dual/read2/blue
execute if entity @s[tag=gl_p1_violet] run function greenlantern:dual/read1/violet
execute if entity @s[tag=gl_p2_violet] run function greenlantern:dual/read2/violet
execute if entity @s[tag=gl_p1_indigo] run function greenlantern:dual/read1/indigo
execute if entity @s[tag=gl_p2_indigo] run function greenlantern:dual/read2/indigo
execute if entity @s[tag=gl_p1_white] run function greenlantern:dual/read1/white
execute if entity @s[tag=gl_p2_white] run function greenlantern:dual/read2/white
execute if entity @s[tag=gl_p1_black] run function greenlantern:dual/read1/black
execute if entity @s[tag=gl_p2_black] run function greenlantern:dual/read2/black
