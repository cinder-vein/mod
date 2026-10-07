execute store result score #stripped gl_tmp run clear @s greenlantern:blue_lantern_ring
scoreboard players set #strip gl_tmp 5
function greenlantern:ring/curios_strip
tag @s remove gl_member_blue
tag @s remove gl_leader_blue
