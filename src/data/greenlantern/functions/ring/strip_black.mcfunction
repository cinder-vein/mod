execute store result score #stripped gl_tmp run clear @s greenlantern:black_lantern_ring
scoreboard players set #strip gl_tmp 9
function greenlantern:ring/curios_strip
tag @s remove gl_member_black
tag @s remove gl_leader_black
scoreboard players set @s gl_ser_black -1
