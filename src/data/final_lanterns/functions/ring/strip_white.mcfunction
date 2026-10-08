execute store result score #stripped gl_tmp run clear @s final_lanterns:whitelanternring
scoreboard players set #strip gl_tmp 8
function final_lanterns:ring/curios_strip
tag @s remove gl_member_white
tag @s remove gl_leader_white
scoreboard players set @s gl_ser_white -1
tag @s remove gl_legacy_white
function final_lanterns:ring/save_serials
