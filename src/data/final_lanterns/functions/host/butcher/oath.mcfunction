tellraw @a[distance=..16] [{"selector":"@s","color":"#DC1E23"},{"text":": ","color":"gray"},{"text":"With blood and rage of crimson red,","color":"#DC1E23","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Ripped from a corpse so freshly dead,","color":"#DC1E23","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"Together with our hellish hate,","color":"#DC1E23","italic":true}]
tellraw @a[distance=..16] [{"text":"   "},{"text":"We'll burn you all... that is your fate!","color":"#DC1E23","italic":true}]
energybar value add @s final_lanterns:redlantern rage 4000
scoreboard players set @s gl_lcd 30
energybar value subtract @a[tag=gl_lantern_host,limit=1] final_lanterns:host_butcher entity_power 800
particle minecraft:dust 0.86 0.12 0.14 2.0 ~ ~1 ~ 0.6 1 0.6 0 120 force
playsound minecraft:block.beacon.activate player @a[distance=..24] ~ ~ ~ 1 1.4
