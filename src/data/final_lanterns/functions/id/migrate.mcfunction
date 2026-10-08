scoreboard players set #old gl_tmp 0
execute if entity @s[tag=gl_member_green] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_yellow] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_red] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_orange] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_blue] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_violet] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_indigo] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_white] run scoreboard players set #old gl_tmp 1
execute if entity @s[tag=gl_member_black] run scoreboard players set #old gl_tmp 1
execute if score #old gl_tmp matches 1 run function final_lanterns:id/to_tags
execute if score #old gl_tmp matches 0 run function final_lanterns:id/fresh
