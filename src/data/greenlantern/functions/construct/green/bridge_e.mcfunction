fill ~1 ~-1 ~-1 ~16 ~-1 ~1 greenlantern:green_hardlight replace #greenlantern:empty
summon minecraft:marker ~ ~ ~ {Tags:["gl_hl","gl_hl_new","gl_hl_be"]}
scoreboard players set @e[type=minecraft:marker,tag=gl_hl_new] gl_life 600
tag @e[type=minecraft:marker,tag=gl_hl_new] remove gl_hl_new
