tag @s add gl_lantern_host
execute as @a[tag=gl_black,distance=..8] run energybar value add @s final_lanterns:blacklantern death 100
execute as @a[tag=gl_black,distance=..8] at @s run particle minecraft:dust 0.59 0.61 0.67 1.0 ~ ~1 ~ 0.3 0.6 0.3 0 6 force
execute as @a[tag=gl_black,distance=..3,predicate=final_lanterns:entity/sneaking,scores={gl_lcd=..0}] at @s run function final_lanterns:host/nekron/oath
particle minecraft:dust 0.59 0.61 0.67 1.0 ~ ~1 ~ 1.5 1 1.5 0 12 force
tag @s remove gl_lantern_host
