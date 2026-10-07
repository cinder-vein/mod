scoreboard players add #called gl_tmp 1
scoreboard players set @s gl_rcd 10
scoreboard players set #found gl_tmp 0
tag @a remove gl_caller
tag @s add gl_caller
function greenlantern:recall/self_green
execute if score #found gl_tmp matches 0 as @e[type=minecraft:item,nbt={Item:{id:"greenlantern:green_lantern_ring",tag:{gl_bound:1b}}}] run function greenlantern:recall/item_green
execute if score #found gl_tmp matches 0 run function greenlantern:recall/reforge_green
execute if score #found gl_tmp matches 1 run tellraw @s [{"text":"Your Green Lantern ring is already with you.","color":"#2EC846"}]
execute if score #found gl_tmp matches 2 run tellraw @s [{"text":"Your Green Lantern ring flies back to you.","color":"#2EC846"}]
execute if score #found gl_tmp matches 2 run playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
tag @s remove gl_caller
