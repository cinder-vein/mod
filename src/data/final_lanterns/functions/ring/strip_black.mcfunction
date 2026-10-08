execute store result score #stripped gl_tmp run clear @s final_lanterns:blacklanternring
scoreboard players set #strip gl_tmp 9
function final_lanterns:ring/curios_strip
tag @s remove gl_member_black
tag @s remove gl_leader_black
scoreboard players set @s gl_ser_black -1
tag @s remove gl_legacy_black
function final_lanterns:ring/save_serials
