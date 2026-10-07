execute store result score #stripped gl_tmp run clear @s greenlantern:violet_lantern_ring
scoreboard players set #strip gl_tmp 6
function greenlantern:ring/curios_strip
tag @s remove gl_member_violet
tag @s remove gl_leader_violet
scoreboard players set @s gl_ser_violet -1
tag @s remove gl_legacy_violet
function greenlantern:ring/save_serials
