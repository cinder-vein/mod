execute store result score #stripped gl_tmp run clear @s greenlantern:red_lantern_ring
scoreboard players set #strip gl_tmp 3
function greenlantern:ring/curios_strip
tag @s remove gl_member_red
tag @s remove gl_leader_red
scoreboard players set @s gl_ser_red -1
