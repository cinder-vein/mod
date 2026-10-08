execute store result score #stripped gl_tmp run clear @s final_lanterns:orangelanternring
scoreboard players set #strip gl_tmp 4
function final_lanterns:ring/curios_strip
tag @s remove gl_member_orange
tag @s remove gl_leader_orange
scoreboard players set @s gl_ser_orange -1
tag @s remove gl_legacy_orange
function final_lanterns:ring/save_serials
