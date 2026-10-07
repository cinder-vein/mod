scoreboard players set #ok gl_tmp 1
scoreboard players add @s gl_ser_red 0
execute unless entity @s[tag=gl_red] run scoreboard players set #ok gl_tmp 0
execute if score @s gl_ser_red matches -1 run scoreboard players set #ok gl_tmp 0
execute if score @s gl_ser_red matches 0 unless entity @s[tag=gl_legacy_red] run scoreboard players set #ok gl_tmp 0
execute if score #ok gl_tmp matches 0 run tellraw @s [{"text":"Your words echo, but no ring answers. Wear your own Red Lantern ring to forge another.","color":"gray","italic":true}]
execute if score #ok gl_tmp matches 1 if score @s gl_fcd matches 1.. run function greenlantern:forge/resting
execute if score #ok gl_tmp matches 1 store result score #charge gl_tmp run energybar value get @s greenlantern:red_lantern ring_charge
execute if score #ok gl_tmp matches 1 if score #charge gl_tmp matches ..499 run function greenlantern:forge/low_charge
execute if score #ok gl_tmp matches 1 run function greenlantern:forge/do_red
