execute store result score #charge gl_tmp run energybar value get @s greenlantern:black_lantern ring_charge
execute if score #charge gl_tmp matches ..2 run function greenlantern:construct/low_charge
execute if score #charge gl_tmp matches 3.. run function greenlantern:construct/black/gatling_fire
