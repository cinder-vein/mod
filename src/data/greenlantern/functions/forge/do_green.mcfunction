energybar value subtract @s greenlantern:green_lantern ring_charge 500
scoreboard players operation @s gl_fcd = #forge_cd gl_cfg
function greenlantern:ring/store_giver
execute store result score #given gl_tmp run loot give @s loot greenlantern:rings/giver_green
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot greenlantern:rings/giver_green
execute if score #given gl_tmp matches 0 at @s run data merge entity @e[type=minecraft:item,distance=..1.5,nbt={Item:{tag:{gl_gv:1b}}},limit=1,sort=nearest] {Age:-32768s}
particle minecraft:dust 0.18 0.78 0.27 2 ~ ~1.2 ~ 0.5 0.8 0.5 0 150 force
particle minecraft:flash ~ ~1.2 ~ 0 0 0 0 1 force
playsound minecraft:block.anvil.use player @a[distance=..24] ~ ~ ~ 0.6 1.6
playsound minecraft:block.beacon.power_select player @a[distance=..24] ~ ~ ~ 1 1.2
title @s times 10 50 15
title @s subtitle {"text": "Give it to someone worthy: it binds to the next one who holds it.", "color": "gray"}
title @s title {"text": "A new Green Lantern ring is forged", "color": "#2EC846"}
tellraw @a[distance=0.1..24] [{"selector":"@s","color":"#2EC846"},{"text":" forged a new Green Lantern ring!","color":"white"}]
