function final_lanterns:ring/store_owner
function final_lanterns:ring/new_serial
item modify entity @s weapon.offhand final_lanterns:bind
execute if predicate final_lanterns:held/green_offhand run scoreboard players operation @s gl_ser_green = #serial gl_cfg
execute if predicate final_lanterns:held/yellow_offhand run scoreboard players operation @s gl_ser_yellow = #serial gl_cfg
execute if predicate final_lanterns:held/red_offhand run scoreboard players operation @s gl_ser_red = #serial gl_cfg
execute if predicate final_lanterns:held/orange_offhand run scoreboard players operation @s gl_ser_orange = #serial gl_cfg
execute if predicate final_lanterns:held/blue_offhand run scoreboard players operation @s gl_ser_blue = #serial gl_cfg
execute if predicate final_lanterns:held/violet_offhand run scoreboard players operation @s gl_ser_violet = #serial gl_cfg
execute if predicate final_lanterns:held/indigo_offhand run scoreboard players operation @s gl_ser_indigo = #serial gl_cfg
execute if predicate final_lanterns:held/white_offhand run scoreboard players operation @s gl_ser_white = #serial gl_cfg
execute if predicate final_lanterns:held/black_offhand run scoreboard players operation @s gl_ser_black = #serial gl_cfg
execute if predicate final_lanterns:held/green_offhand run tag @s remove gl_legacy_green
execute if predicate final_lanterns:held/yellow_offhand run tag @s remove gl_legacy_yellow
execute if predicate final_lanterns:held/red_offhand run tag @s remove gl_legacy_red
execute if predicate final_lanterns:held/orange_offhand run tag @s remove gl_legacy_orange
execute if predicate final_lanterns:held/blue_offhand run tag @s remove gl_legacy_blue
execute if predicate final_lanterns:held/violet_offhand run tag @s remove gl_legacy_violet
execute if predicate final_lanterns:held/indigo_offhand run tag @s remove gl_legacy_indigo
execute if predicate final_lanterns:held/white_offhand run tag @s remove gl_legacy_white
execute if predicate final_lanterns:held/black_offhand run tag @s remove gl_legacy_black
function final_lanterns:ring/save_serials
