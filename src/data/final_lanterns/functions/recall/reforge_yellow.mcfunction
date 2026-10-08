function final_lanterns:ring/store_owner
function final_lanterns:ring/new_serial
scoreboard players operation @s gl_ser_yellow = #serial gl_cfg
tag @s remove gl_legacy_yellow
function final_lanterns:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot final_lanterns:rings/yellow
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot final_lanterns:rings/yellow
execute if score #given gl_tmp matches 0 at @s run function final_lanterns:ring/secure_drop
tag @s add gl_member_yellow
particle minecraft:dust 0.96 0.80 0.12 1.5 ~ ~1.2 ~ 0.4 0.6 0.4 0 60 force
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.6
tellraw @s [{"text":"Your Sinestro Corps ring answers your call and forms on you. ","color":"#F5CD1E"},{"text":"The ring you left behind has gone dark.","color":"gray","italic":true}]
