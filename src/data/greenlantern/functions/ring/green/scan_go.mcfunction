energybar value subtract @s greenlantern:green_lantern ring_charge 10
tag @s add gl_user
scoreboard players set #found gl_tmp 0
tag @e[tag=gl_scanned] remove gl_scanned
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^0.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^0.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^1.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^1.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^1.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^1.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^2.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^2.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^2.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^2.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^3.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^3.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^3.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^3.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^4.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^4.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^4.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^4.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^5.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^5.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^5.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^5.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^6.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^6.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^6.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^6.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^7.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^7.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^7.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^7.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^8.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^8.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^8.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^8.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^9.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^9.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^9.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^9.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^10.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^10.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^10.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^10.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^11.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^11.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^11.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^11.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^12.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^12.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^12.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^12.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^13.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^13.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^13.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^13.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^14.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^14.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^14.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^14.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^15.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^15.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^15.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^15.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^16.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^16.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^16.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^16.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^17.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^17.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^17.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^17.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^18.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^18.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^18.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^18.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^19.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^19.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^19.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^19.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^20.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^20.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^20.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^20.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^21.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^21.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^21.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^21.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^22.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^22.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^22.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^22.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^23.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^23.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^23.5 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^23.5 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^24.0 positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=!#greenlantern:not_creatures,tag=!gl_user,dx=0,dy=0,dz=0,limit=1,sort=nearest] run function greenlantern:construct/scan_hit
execute if score #found gl_tmp matches 0 anchored eyes positioned ^ ^ ^24.0 unless block ~ ~ ~ #minecraft:replaceable run scoreboard players set #found gl_tmp 2
execute unless score #found gl_tmp matches 1 run title @s actionbar [{"text":"Scan found nothing in your line of sight.","color":"gray"}]
execute if score #found gl_tmp matches 1 run function greenlantern:construct/green/scan_report
playsound minecraft:block.beacon.ambient player @a[distance=..24] ~ ~ ~ 1 2.0
tag @s remove gl_user
