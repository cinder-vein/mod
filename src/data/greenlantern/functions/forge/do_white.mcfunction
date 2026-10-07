energybar value subtract @s greenlantern:white_lantern ring_charge 500
scoreboard players operation @s gl_fcd = #forge_cd gl_cfg
function greenlantern:ring/store_giver
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/giver_white
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/giver_white
particle minecraft:dust 0.92 0.95 0.98 2 ~ ~1.2 ~ 0.5 0.8 0.5 0 150 force
particle minecraft:flash ~ ~1.2 ~ 0 0 0 0 1 force
playsound minecraft:block.anvil.use player @a[distance=..24] ~ ~ ~ 0.6 1.6
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.2
title @s times 10 50 15
title @s subtitle {"text": "Give it to someone worthy: it binds to the next one who holds it.", "color": "gray"}
title @s title {"text": "A new White Lantern ring is forged", "color": "#EBF2FA"}
tellraw @a[distance=0.1..24] [{"selector":"@s","color":"#EBF2FA"},{"text":" forged a new White Lantern ring!","color":"white"}]
