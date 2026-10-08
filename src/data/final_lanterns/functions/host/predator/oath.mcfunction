tellraw @a[distance=..16] [{"selector":"@s","color":"#D737DC"},{"text":": ","color":"gray"},{"text":"For hearts long lost and full of fright,","color":"#D737DC","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"For those alone in blackest night,","color":"#D737DC","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Accept our ring and join our fight,","color":"#D737DC","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Love conquers all... with violet light!","color":"#D737DC","italic":true}]
energybar value add @s final_lanterns:pinklantern love 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_predator entity_power 800
particle minecraft:dust 0.84 0.22 0.86 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
