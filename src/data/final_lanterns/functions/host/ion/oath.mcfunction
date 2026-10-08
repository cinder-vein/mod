tellraw @a[distance=..16] [{"selector":"@s","color":"#2EC846"},{"text":": ","color":"gray"},{"text":"In brightest day, in blackest night,","color":"#2EC846","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"No evil shall escape my sight.","color":"#2EC846","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Let those who worship evil's might,","color":"#2EC846","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Beware my power... Green Lantern's light!","color":"#2EC846","italic":true}]
energybar value add @s final_lanterns:greenlantern will_power 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_ion entity_power 800
particle minecraft:dust 0.18 0.78 0.27 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
