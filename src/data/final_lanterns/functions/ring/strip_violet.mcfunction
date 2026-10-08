execute store result score #stripped gl_tmp run clear @s final_lanterns:pinklanternring
scoreboard players set #strip gl_tmp 6
function final_lanterns:ring/curios_strip
tag @s remove gl_member_violet
tag @s remove gl_leader_violet
scoreboard players set @s gl_ser_violet -1
tag @s remove gl_legacy_violet
function final_lanterns:ring/save_serials
