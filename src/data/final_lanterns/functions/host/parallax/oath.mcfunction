tellraw @a[distance=..16] [{"selector":"@s","color":"#F5CD1E"},{"text":": ","color":"gray"},{"text":"In blackest day, in brightest night,","color":"#F5CD1E","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Beware your fears made into light.","color":"#F5CD1E","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Let those who try to stop what's right,","color":"#F5CD1E","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Burn like my power... Sinestro's might!","color":"#F5CD1E","italic":true}]
energybar value add @s final_lanterns:yellowlantern fear 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_parallax fear 800
particle minecraft:dust 0.96 0.80 0.12 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
