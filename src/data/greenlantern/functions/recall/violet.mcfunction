scoreboard players add #called gl_tmp 1
scoreboard players set @s gl_rcd 10
scoreboard players set #found gl_tmp 0
tag @s add gl_caller
function greenlantern:recall/self_violet
execute if score #found gl_tmp matches 0 as @e[type=minecraft:item,nbt={Item:{id:"greenlantern:violet_lantern_ring",tag:{gl_bound:1b}}}] run function greenlantern:recall/item_violet
execute if score #found gl_tmp matches 0 run function greenlantern:recall/reforge_violet
execute if score #found gl_tmp matches 1 run tellraw @s [{"text":"Your Star Sapphire ring is already with you.","color":"#D737DC"}]
execute if score #found gl_tmp matches 2 run tellraw @s [{"text":"Your Star Sapphire ring flies back to you.","color":"#D737DC"}]
execute if score #found gl_tmp matches 2 run playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
tag @s remove gl_caller
