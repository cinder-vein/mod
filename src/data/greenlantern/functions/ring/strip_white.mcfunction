execute store result score #stripped gl_tmp run clear @s greenlantern:white_lantern_ring
scoreboard players set #strip gl_tmp 8
function greenlantern:ring/curios_strip
tag @s remove gl_member_white
tag @s remove gl_leader_white
