function final_lanterns:deathonremoval
function final_lanterns:ring_sacrifice


execute as @e[tag=Foi1y-Portal_A] at @e[tag=Foi1y-Opened_Portal] run tp @e[distance=..1,type=minecraft:player] @s
execute as @e[tag=Foi1y-Portal_B] at @e[tag=Foi1y-Opened_Portal] run tp @e[distance=..1,type=minecraft:player] @s
execute as @e[type=minecraft:player] if entity @s[advancements={lanterncorps:root=false}] run advancement grant @s only lanterncorps:root