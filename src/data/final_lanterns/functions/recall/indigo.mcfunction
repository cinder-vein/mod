scoreboard players add #called gl_tmp 1
scoreboard players set @s gl_rcd 10
scoreboard players set #found gl_tmp 0
tag @a remove gl_caller
tag @s add gl_caller
function final_lanterns:recall/self_indigo
execute if score #found gl_tmp matches 0 as @e[type=minecraft:item,nbt={Item:{id:"final_lanterns:indigolanternring",tag:{gl_bound:1b}}}] run function final_lanterns:recall/item_indigo
execute if score #found gl_tmp matches 0 run function final_lanterns:recall/reforge_indigo
execute if score #found gl_tmp matches 1 run tellraw @s [{"text":"Your Indigo Tribe ring is already with you.","color":"#693CE6"}]
execute if score #found gl_tmp matches 2 run tellraw @s [{"text":"Your Indigo Tribe ring flies back to you.","color":"#693CE6"}]
execute if score #found gl_tmp matches 2 run playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 1 1.6
tag @s remove gl_caller
