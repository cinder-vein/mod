execute as @a[scores={rings_sacrificed=10..}] at @s run function final_lanterns:entity/parallax/sacrifice
scoreboard players reset @a[scores={rings_sacrificed=10..}] rings_sacrificed
