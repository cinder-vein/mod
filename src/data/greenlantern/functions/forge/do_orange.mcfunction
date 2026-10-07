energybar value subtract @s greenlantern:orange_lantern ring_charge 500
scoreboard players operation @s gl_fcd = #forge_cd gl_cfg
function greenlantern:ring/store_giver
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/giver_orange
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/giver_orange
particle minecraft:dust 0.98 0.51 0.08 2 ~ ~1.2 ~ 0.5 0.8 0.5 0 150 force
particle minecraft:flash ~ ~1.2 ~ 0 0 0 0 1 force
playsound minecraft:block.anvil.use player @a[distance=..24] ~ ~ ~ 0.6 1.6
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.2
title @s times 10 50 15
title @s subtitle {"text": "Give it to someone worthy: it binds to the next one who holds it.", "color": "gray"}
title @s title {"text": "A new Orange Lantern ring is forged", "color": "#FA8214"}
tellraw @a[distance=0.1..24] [{"selector":"@s","color":"#FA8214"},{"text":" forged a new Orange Lantern ring!","color":"white"}]
