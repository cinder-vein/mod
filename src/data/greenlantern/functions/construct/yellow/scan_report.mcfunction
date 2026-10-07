tellraw @s [{"text":"Scan: ","color":"#F5CD1E","bold":true},{"selector":"@e[tag=gl_scanned]"},{"text":"  Health ","color":"gray"},{"score":{"name":"#hp","objective":"gl_tmp"}},{"text":"/","color":"gray"},{"score":{"name":"#maxhp","objective":"gl_tmp"}},{"text":"  Armor ","color":"gray"},{"score":{"name":"#armor","objective":"gl_tmp"}}]
execute as @e[tag=gl_scanned] at @s run particle minecraft:dust 0.96 0.80 0.12 1.0 ~ ~1 ~ 0.3 0.6 0.3 0 30 force
tag @e[tag=gl_scanned] remove gl_scanned
