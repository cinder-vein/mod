function greenlantern:ring/store_owner
function greenlantern:ring/new_serial
item modify entity @s weapon.mainhand greenlantern:bind
execute if predicate greenlantern:held/green_mainhand run scoreboard players operation @s gl_ser_green = #serial gl_cfg
execute if predicate greenlantern:held/yellow_mainhand run scoreboard players operation @s gl_ser_yellow = #serial gl_cfg
execute if predicate greenlantern:held/red_mainhand run scoreboard players operation @s gl_ser_red = #serial gl_cfg
execute if predicate greenlantern:held/orange_mainhand run scoreboard players operation @s gl_ser_orange = #serial gl_cfg
execute if predicate greenlantern:held/blue_mainhand run scoreboard players operation @s gl_ser_blue = #serial gl_cfg
execute if predicate greenlantern:held/violet_mainhand run scoreboard players operation @s gl_ser_violet = #serial gl_cfg
execute if predicate greenlantern:held/indigo_mainhand run scoreboard players operation @s gl_ser_indigo = #serial gl_cfg
execute if predicate greenlantern:held/white_mainhand run scoreboard players operation @s gl_ser_white = #serial gl_cfg
execute if predicate greenlantern:held/black_mainhand run scoreboard players operation @s gl_ser_black = #serial gl_cfg
