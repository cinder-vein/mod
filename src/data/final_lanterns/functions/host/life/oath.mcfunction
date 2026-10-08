tellraw @a[distance=..16] [{"selector":"@s","color":"#EBF2FA"},{"text":": ","color":"gray"},{"text":"From the light of creation,","color":"#EBF2FA","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"every color of the spectrum,","color":"#EBF2FA","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"all life, as one,","color":"#EBF2FA","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"...shines White!","color":"#EBF2FA","italic":true}]
energybar value add @s final_lanterns:whitelantern life 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_life life 800
particle minecraft:dust 0.92 0.95 0.98 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
