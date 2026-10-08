tellraw @a[distance=..16] [{"selector":"@s","color":"#AAAFBE"},{"text":": ","color":"gray"},{"text":"The Blackest Night falls from the skies,","color":"#AAAFBE","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"The darkness grows as all light dies,","color":"#AAAFBE","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"We crave your hearts and your demise,","color":"#AAAFBE","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"By my black hand, the dead shall rise!","color":"#AAAFBE","italic":true}]
energybar value add @s final_lanterns:blacklantern death 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_nekron entity_power 800
particle minecraft:dust 0.59 0.61 0.67 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
