execute as @e[scores={rings_sacrificed=10..}] run superpower add final_lanterns:parallax @s
execute as @e[scores={rings_sacrificed=10..}] run advancement grant @s only lanterncorps:parallax
execute as @e[type=minecraft:player] as @e[scores={rings_sacrificed=10..}] run title @s actionbar [{"text":"Now hosting: Parallax","color":"green","bold":true}]
execute as @e[scores={rings_sacrificed=10..}] run scoreboard players reset @s rings_sacrificed