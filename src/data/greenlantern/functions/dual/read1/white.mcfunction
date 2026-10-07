execute store result score #c1 gl_tmp run energybar value get @s greenlantern:white_lantern ring_charge
execute if score @s glmax_white matches 1.. run scoreboard players operation #m1 gl_tmp = @s glmax_white
execute if entity @s[tag=gl_cr_white] run scoreboard players add #ready gl_tmp 1
