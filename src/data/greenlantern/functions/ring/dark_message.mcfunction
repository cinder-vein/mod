particle minecraft:smoke ~ ~1.2 ~ 0.2 0.3 0.2 0.02 30 force
playsound minecraft:block.beacon.deactivate player @a[distance=..16] ~ ~ ~ 1 0.6
tellraw @s [{"text":"This ring has gone dark: you called a new one to you. It crumbles to dust.","color":"gray","italic":true}]
