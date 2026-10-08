execute store result score #stripped gl_tmp run clear @s final_lanterns:yellowlanternring
scoreboard players set #strip gl_tmp 2
function final_lanterns:ring/curios_strip
tag @s remove gl_member_yellow
tag @s remove gl_leader_yellow
scoreboard players set @s gl_ser_yellow -1
tag @s remove gl_legacy_yellow
function final_lanterns:ring/save_serials
