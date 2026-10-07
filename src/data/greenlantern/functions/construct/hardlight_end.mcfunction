execute if entity @s[tag=gl_hl_wx] run fill ~-2 ~ ~ ~2 ~3 ~ minecraft:air replace #greenlantern:hardlight
execute if entity @s[tag=gl_hl_wz] run fill ~ ~ ~-2 ~ ~3 ~2 minecraft:air replace #greenlantern:hardlight
execute if entity @s[tag=gl_hl_dome] run fill ~-5 ~-1 ~-5 ~5 ~5 ~5 minecraft:air replace #greenlantern:hardlight
execute if entity @s[tag=gl_hl_bs] run fill ~-1 ~-1 ~1 ~1 ~-1 ~16 minecraft:air replace #greenlantern:hardlight
execute if entity @s[tag=gl_hl_bn] run fill ~-1 ~-1 ~-16 ~1 ~-1 ~-1 minecraft:air replace #greenlantern:hardlight
execute if entity @s[tag=gl_hl_bw] run fill ~-16 ~-1 ~-1 ~-1 ~-1 ~1 minecraft:air replace #greenlantern:hardlight
execute if entity @s[tag=gl_hl_be] run fill ~1 ~-1 ~-1 ~16 ~-1 ~1 minecraft:air replace #greenlantern:hardlight
particle minecraft:end_rod ~ ~1 ~ 1.5 1.5 1.5 0.02 30 force
playsound minecraft:block.amethyst_block.break block @a[distance=..24] ~ ~ ~ 1 1.2
kill @s
