scoreboard players set #found gl_tmp 1
tag @s add gl_scanned
effect give @s minecraft:glowing 10 0 true
execute store result score #hp gl_tmp run data get entity @s Health
execute store result score #maxhp gl_tmp run attribute @s minecraft:generic.max_health get
execute store result score #armor gl_tmp run attribute @s minecraft:generic.armor get
