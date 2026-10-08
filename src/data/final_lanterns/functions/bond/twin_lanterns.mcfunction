function final_lanterns:bond/read
execute unless score @s gl_dc1 matches 0.. run scoreboard players operation @s gl_dc1 = #c1 gl_tmp
execute unless score @s gl_dc2 matches 0.. run scoreboard players operation @s gl_dc2 = #c2 gl_tmp
scoreboard players operation #j1 gl_tmp = #c1 gl_tmp
scoreboard players operation #j1 gl_tmp -= @s gl_dc1
scoreboard players operation #j2 gl_tmp = #c2 gl_tmp
scoreboard players operation #j2 gl_tmp -= @s gl_dc2
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_green] run energybar value add @s final_lanterns:greenlantern will_power 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_yellow] run energybar value add @s final_lanterns:yellowlantern fear 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_red] run energybar value add @s final_lanterns:redlantern rage 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_orange] run energybar value add @s final_lanterns:orangelantern greed 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_blue] run energybar value add @s final_lanterns:bluelantern hope 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_violet] run energybar value add @s final_lanterns:pinklantern love 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_indigo] run energybar value add @s final_lanterns:indigolantern compassion 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_white] run energybar value add @s final_lanterns:whitelantern life 100000
execute if score #j1 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p2_black] run energybar value add @s final_lanterns:blacklantern death 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_green] run energybar value add @s final_lanterns:greenlantern will_power 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_yellow] run energybar value add @s final_lanterns:yellowlantern fear 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_red] run energybar value add @s final_lanterns:redlantern rage 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_orange] run energybar value add @s final_lanterns:orangelantern greed 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_blue] run energybar value add @s final_lanterns:bluelantern hope 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_violet] run energybar value add @s final_lanterns:pinklantern love 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_indigo] run energybar value add @s final_lanterns:indigolantern compassion 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_white] run energybar value add @s final_lanterns:whitelantern life 100000
execute if score #j2 gl_tmp matches 1000.. run execute if entity @s[tag=gl_p1_black] run energybar value add @s final_lanterns:blacklantern death 100000
function final_lanterns:bond/read
scoreboard players operation @s gl_dc1 = #c1 gl_tmp
scoreboard players operation @s gl_dc2 = #c2 gl_tmp
