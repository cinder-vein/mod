execute as @a unless entity @s[palladium.power=final_lanterns:base] run superpower add final_lanterns:base @a

superpower add final_lanterns:base @a

# Create objective (will show error on subsequent reloads, harmless)
scoreboard objectives add hostileKills dummy {"text":"Hostile Kills"},