execute store result score #stripped gl_tmp run clear @s final_lanterns:bluelanternring
scoreboard players set #strip gl_tmp 5
function final_lanterns:ring/curios_strip
tag @s remove gl_member_blue
tag @s remove gl_leader_blue
scoreboard players set @s gl_ser_blue -1
tag @s remove gl_legacy_blue
function final_lanterns:ring/save_serials
