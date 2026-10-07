scoreboard players set #done gl_tmp 1
scoreboard players set #ok gl_tmp 0
function greenlantern:construct/green/scuba_try
execute if score #ok gl_tmp matches 1 if entity @s[tag=gl_du_twin_constructs] run energybar value add @s greenlantern:green_lantern ring_charge 5
