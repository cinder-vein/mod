execute store result score #charge gl_tmp run energybar value get @s greenlantern:indigo_lantern ring_charge
execute if score #charge gl_tmp matches ..39 run function greenlantern:construct/low_charge
execute if score #charge gl_tmp matches 40.. run function greenlantern:ring/indigo/blast_go
