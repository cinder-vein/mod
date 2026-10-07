execute store result score #charge gl_tmp run energybar value get @s greenlantern:blue_lantern ring_charge
execute if score #charge gl_tmp matches ..9 run function greenlantern:construct/low_charge
execute if score #charge gl_tmp matches 10.. run function greenlantern:ring/blue/scan_go
