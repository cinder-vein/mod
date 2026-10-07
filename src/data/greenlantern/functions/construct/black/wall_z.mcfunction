fill ~ ~ ~-2 ~ ~3 ~2 greenlantern:black_hardlight replace #greenlantern:empty
summon minecraft:marker ~ ~ ~ {Tags:["gl_hl","gl_hl_new","gl_hl_wz"]}
scoreboard players set @e[type=minecraft:marker,tag=gl_hl_new] gl_life 300
tag @e[type=minecraft:marker,tag=gl_hl_new] remove gl_hl_new
scoreboard players set @e[type=minecraft:marker,tag=gl_hl,distance=..34,scores={gl_life=..300}] gl_life 300
