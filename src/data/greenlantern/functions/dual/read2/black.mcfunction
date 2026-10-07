execute store result score #c2 gl_tmp run energybar value get @s greenlantern:black_lantern ring_charge
execute if score @s glmax_black matches 1.. run scoreboard players operation #m2 gl_tmp = @s glmax_black
execute if entity @s[tag=gl_cr_black] run scoreboard players add #ready gl_tmp 1
