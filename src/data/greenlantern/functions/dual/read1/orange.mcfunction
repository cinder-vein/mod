execute store result score #c1 gl_tmp run energybar value get @s greenlantern:orange_lantern ring_charge
execute if score @s glmax_orange matches 1.. run scoreboard players operation #m1 gl_tmp = @s glmax_orange
execute if entity @s[tag=gl_cr_orange] run scoreboard players add #ready gl_tmp 1
