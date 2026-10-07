execute store result score #c2 gl_tmp run energybar value get @s greenlantern:indigo_lantern ring_charge
execute if score @s glmax_indigo matches 1.. run scoreboard players operation #m2 gl_tmp = @s glmax_indigo
execute if entity @s[tag=gl_cr_indigo] run scoreboard players add #ready gl_tmp 1
