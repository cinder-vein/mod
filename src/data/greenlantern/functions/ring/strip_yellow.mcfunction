execute store result score #stripped gl_tmp run clear @s greenlantern:yellow_lantern_ring
scoreboard players set #strip gl_tmp 2
function greenlantern:ring/curios_strip
tag @s remove gl_member_yellow
tag @s remove gl_leader_yellow
scoreboard players set @s gl_ser_yellow -1
tag @s remove gl_legacy_yellow
function greenlantern:ring/save_serials
