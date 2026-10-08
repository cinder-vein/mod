scoreboard players operation #v gl_tmp = @s gl_entity
scoreboard players set @s gl_entity 0
scoreboard players enable @s gl_entity
execute if score #v gl_tmp matches 1 at @s run function final_lanterns:entity/ion/accept
execute if score #v gl_tmp matches 11 run function final_lanterns:entity/ion/decline
execute if score #v gl_tmp matches 21 at @s run function final_lanterns:entity/ion/lantern_host
execute if score #v gl_tmp matches 31 at @s run function final_lanterns:entity/ion/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_ion] at @s run function final_lanterns:entity/ion/release
execute if score #v gl_tmp matches 2 at @s run function final_lanterns:entity/parallax/accept
execute if score #v gl_tmp matches 12 run function final_lanterns:entity/parallax/decline
execute if score #v gl_tmp matches 22 at @s run function final_lanterns:entity/parallax/lantern_host
execute if score #v gl_tmp matches 32 at @s run function final_lanterns:entity/parallax/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_parallax] at @s run function final_lanterns:entity/parallax/release
execute if score #v gl_tmp matches 3 at @s run function final_lanterns:entity/butcher/accept
execute if score #v gl_tmp matches 13 run function final_lanterns:entity/butcher/decline
execute if score #v gl_tmp matches 23 at @s run function final_lanterns:entity/butcher/lantern_host
execute if score #v gl_tmp matches 33 at @s run function final_lanterns:entity/butcher/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_butcher] at @s run function final_lanterns:entity/butcher/release
execute if score #v gl_tmp matches 4 at @s run function final_lanterns:entity/ophidian/accept
execute if score #v gl_tmp matches 14 run function final_lanterns:entity/ophidian/decline
execute if score #v gl_tmp matches 24 at @s run function final_lanterns:entity/ophidian/lantern_host
execute if score #v gl_tmp matches 34 at @s run function final_lanterns:entity/ophidian/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_ophidian] at @s run function final_lanterns:entity/ophidian/release
execute if score #v gl_tmp matches 5 at @s run function final_lanterns:entity/adara/accept
execute if score #v gl_tmp matches 15 run function final_lanterns:entity/adara/decline
execute if score #v gl_tmp matches 25 at @s run function final_lanterns:entity/adara/lantern_host
execute if score #v gl_tmp matches 35 at @s run function final_lanterns:entity/adara/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_adara] at @s run function final_lanterns:entity/adara/release
execute if score #v gl_tmp matches 6 at @s run function final_lanterns:entity/predator/accept
execute if score #v gl_tmp matches 16 run function final_lanterns:entity/predator/decline
execute if score #v gl_tmp matches 26 at @s run function final_lanterns:entity/predator/lantern_host
execute if score #v gl_tmp matches 36 at @s run function final_lanterns:entity/predator/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_predator] at @s run function final_lanterns:entity/predator/release
execute if score #v gl_tmp matches 7 at @s run function final_lanterns:entity/proselyte/accept
execute if score #v gl_tmp matches 17 run function final_lanterns:entity/proselyte/decline
execute if score #v gl_tmp matches 27 at @s run function final_lanterns:entity/proselyte/lantern_host
execute if score #v gl_tmp matches 37 at @s run function final_lanterns:entity/proselyte/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_proselyte] at @s run function final_lanterns:entity/proselyte/release
execute if score #v gl_tmp matches 8 at @s run function final_lanterns:entity/life/accept
execute if score #v gl_tmp matches 18 run function final_lanterns:entity/life/decline
execute if score #v gl_tmp matches 28 at @s run function final_lanterns:entity/life/lantern_host
execute if score #v gl_tmp matches 38 at @s run function final_lanterns:entity/life/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_life] at @s run function final_lanterns:entity/life/release
execute if score #v gl_tmp matches 9 at @s run function final_lanterns:entity/nekron/accept
execute if score #v gl_tmp matches 19 run function final_lanterns:entity/nekron/decline
execute if score #v gl_tmp matches 29 at @s run function final_lanterns:entity/nekron/lantern_host
execute if score #v gl_tmp matches 39 at @s run function final_lanterns:entity/nekron/lantern_release
execute if score #v gl_tmp matches 40 if entity @s[tag=gl_host_nekron] at @s run function final_lanterns:entity/nekron/release
