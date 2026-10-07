execute store result score #stripped gl_tmp run clear @s greenlantern:orange_lantern_ring
scoreboard players set #strip gl_tmp 4
function greenlantern:ring/curios_strip
tag @s remove gl_member_orange
tag @s remove gl_leader_orange
scoreboard players set @s gl_ser_orange -1
tag @s remove gl_legacy_orange
function greenlantern:ring/save_serials
