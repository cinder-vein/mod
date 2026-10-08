scoreboard players add #called gl_tmp 1
scoreboard players set @s gl_rcd 10
scoreboard players set #found gl_tmp 0
tag @a remove gl_caller
tag @s add gl_caller
function final_lanterns:recall/self_orange
execute if score #found gl_tmp matches 0 as @e[type=minecraft:item,nbt={Item:{id:"final_lanterns:orangelanternring",tag:{gl_bound:1b}}}] run function final_lanterns:recall/item_orange
execute if score #found gl_tmp matches 0 run function final_lanterns:recall/reforge_orange
execute if score #found gl_tmp matches 1 run tellraw @s [{"text":"Your Orange Lantern ring is already with you.","color":"#FA8214"}]
execute if score #found gl_tmp matches 2 run tellraw @s [{"text":"Your Orange Lantern ring flies back to you.","color":"#FA8214"}]
execute if score #found gl_tmp matches 2 run playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
tag @s remove gl_caller
