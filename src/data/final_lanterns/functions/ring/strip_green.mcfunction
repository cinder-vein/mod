execute store result score #stripped gl_tmp run clear @s final_lanterns:greenlanternring
scoreboard players set #strip gl_tmp 1
function final_lanterns:ring/curios_strip
tag @s remove gl_member_green
tag @s remove gl_leader_green
scoreboard players set @s gl_ser_green -1
tag @s remove gl_legacy_green
function final_lanterns:ring/save_serials
