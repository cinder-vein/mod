particle minecraft:smoke ~ ~1.2 ~ 0.2 0.3 0.2 0.02 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 0.6
tellraw @s [{"text":"This ring has gone dark: its power answers another ring now. It crumbles to dust.","color":"gray","italic":true}]
