function final_lanterns:ring/store_owner
function final_lanterns:ring/new_serial
scoreboard players operation @s gl_ser_orange = #serial gl_cfg
tag @s remove gl_legacy_orange
function final_lanterns:ring/save_serials
execute store result score #given gl_tmp run loot give @s loot final_lanterns:rings/orange
execute if score #given gl_tmp matches 0 at @s run loot spawn ~ ~ ~ loot final_lanterns:rings/orange
execute if score #given gl_tmp matches 0 at @s run function final_lanterns:ring/secure_drop
tag @s add gl_member_orange
particle minecraft:dust 0.98 0.51 0.08 1.5 ~ ~1.2 ~ 0.4 0.6 0.4 0 60 force
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.6
tellraw @s [{"text":"Your Orange Lantern ring answers your call and forms on you. ","color":"#FA8214"},{"text":"The ring you left behind has gone dark.","color":"gray","italic":true}]
