tellraw @a[distance=..16] [{"selector":"@s","color":"#693CE6"},{"text":": ","color":"gray"},{"text":"Tor lowar lan, Abin Sur,","color":"#693CE6","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Ak wo tauva, Ihla wo nauva,","color":"#693CE6","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Natromo faan, Dur ak naja,","color":"#693CE6","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Ono ot vauva, Abin Sur.","color":"#693CE6","italic":true}]
energybar value add @s final_lanterns:indigolantern compassion 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_proselyte entity_power 800
particle minecraft:dust 0.41 0.24 0.90 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
