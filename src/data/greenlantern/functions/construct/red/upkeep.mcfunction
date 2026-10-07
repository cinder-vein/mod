execute store result score #charge gl_tmp run energybar value get @s greenlantern:red_lantern ring_charge
execute if score #charge gl_tmp matches ..2 run function greenlantern:construct/red/dissolve
execute if score #charge gl_tmp matches 3.. run energybar value subtract @s greenlantern:red_lantern ring_charge 3
