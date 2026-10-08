execute store result score #stripped gl_tmp run clear @s final_lanterns:indigolanternring
scoreboard players set #strip gl_tmp 7
function final_lanterns:ring/curios_strip
tag @s remove gl_member_indigo
tag @s remove gl_leader_indigo
scoreboard players set @s gl_ser_indigo -1
tag @s remove gl_legacy_indigo
function final_lanterns:ring/save_serials
