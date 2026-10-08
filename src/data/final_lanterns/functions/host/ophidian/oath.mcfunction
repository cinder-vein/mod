tellraw @a[distance=..16] [{"selector":"@s","color":"#FA8214"},{"text":": ","color":"gray"},{"text":"What's mine is mine,","color":"#FA8214","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"and mine,","color":"#FA8214","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"and mine...","color":"#FA8214","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"and mine! And not yours!","color":"#FA8214","italic":true}]
energybar value add @s final_lanterns:orangelantern greed 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_ophidian entity_power 800
particle minecraft:dust 0.98 0.51 0.08 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
