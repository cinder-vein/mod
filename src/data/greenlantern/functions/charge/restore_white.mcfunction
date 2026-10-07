scoreboard players add @s gl_ch_white 0
scoreboard players operation @s gl_tmp = @s gl_ch_white
energybar value set @s greenlantern:white_lantern ring_charge 0
execute if score @s gl_tmp matches 2048.. run energybar value add @s greenlantern:white_lantern ring_charge 2048
execute if score @s gl_tmp matches 2048.. run scoreboard players remove @s gl_tmp 2048
execute if score @s gl_tmp matches 1024.. run energybar value add @s greenlantern:white_lantern ring_charge 1024
execute if score @s gl_tmp matches 1024.. run scoreboard players remove @s gl_tmp 1024
execute if score @s gl_tmp matches 512.. run energybar value add @s greenlantern:white_lantern ring_charge 512
execute if score @s gl_tmp matches 512.. run scoreboard players remove @s gl_tmp 512
execute if score @s gl_tmp matches 256.. run energybar value add @s greenlantern:white_lantern ring_charge 256
execute if score @s gl_tmp matches 256.. run scoreboard players remove @s gl_tmp 256
execute if score @s gl_tmp matches 128.. run energybar value add @s greenlantern:white_lantern ring_charge 128
execute if score @s gl_tmp matches 128.. run scoreboard players remove @s gl_tmp 128
execute if score @s gl_tmp matches 64.. run energybar value add @s greenlantern:white_lantern ring_charge 64
execute if score @s gl_tmp matches 64.. run scoreboard players remove @s gl_tmp 64
execute if score @s gl_tmp matches 32.. run energybar value add @s greenlantern:white_lantern ring_charge 32
execute if score @s gl_tmp matches 32.. run scoreboard players remove @s gl_tmp 32
execute if score @s gl_tmp matches 16.. run energybar value add @s greenlantern:white_lantern ring_charge 16
execute if score @s gl_tmp matches 16.. run scoreboard players remove @s gl_tmp 16
execute if score @s gl_tmp matches 8.. run energybar value add @s greenlantern:white_lantern ring_charge 8
execute if score @s gl_tmp matches 8.. run scoreboard players remove @s gl_tmp 8
execute if score @s gl_tmp matches 4.. run energybar value add @s greenlantern:white_lantern ring_charge 4
execute if score @s gl_tmp matches 4.. run scoreboard players remove @s gl_tmp 4
execute if score @s gl_tmp matches 2.. run energybar value add @s greenlantern:white_lantern ring_charge 2
execute if score @s gl_tmp matches 2.. run scoreboard players remove @s gl_tmp 2
execute if score @s gl_tmp matches 1.. run energybar value add @s greenlantern:white_lantern ring_charge 1
execute if score @s gl_tmp matches 1.. run scoreboard players remove @s gl_tmp 1
tag @s add gl_cr_white
