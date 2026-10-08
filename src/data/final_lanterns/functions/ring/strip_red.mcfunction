execute store result score #stripped gl_tmp run clear @s final_lanterns:redlanternring
scoreboard players set #strip gl_tmp 3
function final_lanterns:ring/curios_strip
tag @s remove gl_member_red
tag @s remove gl_leader_red
scoreboard players set @s gl_ser_red -1
tag @s remove gl_legacy_red
function final_lanterns:ring/save_serials
