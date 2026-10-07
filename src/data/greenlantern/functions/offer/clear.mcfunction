tag @s remove gl_offer_green
tag @s remove gl_offer_yellow
tag @s remove gl_offer_red
tag @s remove gl_offer_orange
tag @s remove gl_offer_blue
tag @s remove gl_offer_violet
tag @s remove gl_offer_indigo
tag @s remove gl_offer_white
tag @s remove gl_offer_black
tag @s remove gl_offer_any
scoreboard players set @s gl_offer 0
scoreboard players set @s gl_accept 0
scoreboard players set @s gl_decline 0
scoreboard players operation #cur gl_id = @s gl_id
execute as @e[type=minecraft:item_display,tag=gl_offer_disp] if score @s gl_id = #cur gl_id run kill @s
