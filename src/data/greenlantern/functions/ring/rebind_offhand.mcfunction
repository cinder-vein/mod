function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
item modify entity @s weapon.offhand greenlantern:bind
execute if predicate greenlantern:held/green_offhand run scoreboard players operation @s gl_ser_green = #serial gl_cfg
execute if predicate greenlantern:held/yellow_offhand run scoreboard players operation @s gl_ser_yellow = #serial gl_cfg
execute if predicate greenlantern:held/red_offhand run scoreboard players operation @s gl_ser_red = #serial gl_cfg
execute if predicate greenlantern:held/orange_offhand run scoreboard players operation @s gl_ser_orange = #serial gl_cfg
execute if predicate greenlantern:held/blue_offhand run scoreboard players operation @s gl_ser_blue = #serial gl_cfg
execute if predicate greenlantern:held/violet_offhand run scoreboard players operation @s gl_ser_violet = #serial gl_cfg
execute if predicate greenlantern:held/indigo_offhand run scoreboard players operation @s gl_ser_indigo = #serial gl_cfg
execute if predicate greenlantern:held/white_offhand run scoreboard players operation @s gl_ser_white = #serial gl_cfg
execute if predicate greenlantern:held/black_offhand run scoreboard players operation @s gl_ser_black = #serial gl_cfg
execute if predicate greenlantern:held/green_offhand run tag @s remove gl_legacy_green
execute if predicate greenlantern:held/yellow_offhand run tag @s remove gl_legacy_yellow
execute if predicate greenlantern:held/red_offhand run tag @s remove gl_legacy_red
execute if predicate greenlantern:held/orange_offhand run tag @s remove gl_legacy_orange
execute if predicate greenlantern:held/blue_offhand run tag @s remove gl_legacy_blue
execute if predicate greenlantern:held/violet_offhand run tag @s remove gl_legacy_violet
execute if predicate greenlantern:held/indigo_offhand run tag @s remove gl_legacy_indigo
execute if predicate greenlantern:held/white_offhand run tag @s remove gl_legacy_white
execute if predicate greenlantern:held/black_offhand run tag @s remove gl_legacy_black
function greenlantern:ring/save_serials
