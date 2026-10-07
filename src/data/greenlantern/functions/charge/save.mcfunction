execute as @a[tag=gl_cr_green] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:green_lantern ring_charge
execute as @a[tag=gl_cr_green,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_green = @s gl_tmp
execute as @a[tag=gl_cr_yellow] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:yellow_lantern ring_charge
execute as @a[tag=gl_cr_yellow,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_yellow = @s gl_tmp
execute as @a[tag=gl_cr_red] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:red_lantern ring_charge
execute as @a[tag=gl_cr_red,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_red = @s gl_tmp
execute as @a[tag=gl_cr_orange] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:orange_lantern ring_charge
execute as @a[tag=gl_cr_orange,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_orange = @s gl_tmp
execute as @a[tag=gl_cr_blue] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:blue_lantern ring_charge
execute as @a[tag=gl_cr_blue,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_blue = @s gl_tmp
execute as @a[tag=gl_cr_violet] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:violet_lantern ring_charge
execute as @a[tag=gl_cr_violet,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_violet = @s gl_tmp
execute as @a[tag=gl_cr_indigo] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:indigo_lantern ring_charge
execute as @a[tag=gl_cr_indigo,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_indigo = @s gl_tmp
execute as @a[tag=gl_cr_white] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:white_lantern ring_charge
execute as @a[tag=gl_cr_white,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_white = @s gl_tmp
execute as @a[tag=gl_cr_black] store success score @s gl_ok store result score @s gl_tmp run energybar value get @s greenlantern:black_lantern ring_charge
execute as @a[tag=gl_cr_black,scores={gl_ok=1}] run scoreboard players operation @s gl_ch_black = @s gl_tmp
