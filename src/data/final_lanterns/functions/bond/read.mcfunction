scoreboard players set #c1 gl_tmp 0
scoreboard players set #c2 gl_tmp 0
execute if entity @s[tag=gl_p1_green] store result score #c1 gl_tmp run energybar value get @s final_lanterns:greenlantern will_power
execute if entity @s[tag=gl_p2_green] store result score #c2 gl_tmp run energybar value get @s final_lanterns:greenlantern will_power
execute if entity @s[tag=gl_p1_yellow] store result score #c1 gl_tmp run energybar value get @s final_lanterns:yellowlantern fear
execute if entity @s[tag=gl_p2_yellow] store result score #c2 gl_tmp run energybar value get @s final_lanterns:yellowlantern fear
execute if entity @s[tag=gl_p1_red] store result score #c1 gl_tmp run energybar value get @s final_lanterns:redlantern rage
execute if entity @s[tag=gl_p2_red] store result score #c2 gl_tmp run energybar value get @s final_lanterns:redlantern rage
execute if entity @s[tag=gl_p1_orange] store result score #c1 gl_tmp run energybar value get @s final_lanterns:orangelantern greed
execute if entity @s[tag=gl_p2_orange] store result score #c2 gl_tmp run energybar value get @s final_lanterns:orangelantern greed
execute if entity @s[tag=gl_p1_blue] store result score #c1 gl_tmp run energybar value get @s final_lanterns:bluelantern hope
execute if entity @s[tag=gl_p2_blue] store result score #c2 gl_tmp run energybar value get @s final_lanterns:bluelantern hope
execute if entity @s[tag=gl_p1_violet] store result score #c1 gl_tmp run energybar value get @s final_lanterns:pinklantern love
execute if entity @s[tag=gl_p2_violet] store result score #c2 gl_tmp run energybar value get @s final_lanterns:pinklantern love
execute if entity @s[tag=gl_p1_indigo] store result score #c1 gl_tmp run energybar value get @s final_lanterns:indigolantern compassion
execute if entity @s[tag=gl_p2_indigo] store result score #c2 gl_tmp run energybar value get @s final_lanterns:indigolantern compassion
execute if entity @s[tag=gl_p1_white] store result score #c1 gl_tmp run energybar value get @s final_lanterns:whitelantern life
execute if entity @s[tag=gl_p2_white] store result score #c2 gl_tmp run energybar value get @s final_lanterns:whitelantern life
execute if entity @s[tag=gl_p1_black] store result score #c1 gl_tmp run energybar value get @s final_lanterns:blacklantern death
execute if entity @s[tag=gl_p2_black] store result score #c2 gl_tmp run energybar value get @s final_lanterns:blacklantern death
