tellraw @a[distance=..16] [{"selector":"@s","color":"#2882FF"},{"text":": ","color":"gray"},{"text":"In fearful day, in raging night,","color":"#2882FF","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"With strong hearts full, our souls ignite,","color":"#2882FF","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"When all seems lost in the War of Light,","color":"#2882FF","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Look to the stars... for hope burns bright!","color":"#2882FF","italic":true}]
energybar value add @s final_lanterns:bluelantern hope 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_adara entity_power 800
particle minecraft:dust 0.16 0.51 1.00 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
