execute store result score #stripped gl_tmp run clear @s greenlantern:green_lantern_ring
scoreboard players set #strip gl_tmp 1
function greenlantern:ring/curios_strip
tag @s remove gl_member_green
tag @s remove gl_leader_green
scoreboard players set @s gl_ser_green -1
tag @s remove gl_legacy_green
function greenlantern:ring/save_serials
