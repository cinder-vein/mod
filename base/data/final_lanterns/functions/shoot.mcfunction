# Remove 1 red_trident from hand
clear @s final_lanterns:red_trident 1

# Summon a trident projectile but tagged as your custom item
summon trident ~ ~1.5 ~ {pickup:0b,damage:12,Trident:{id:"final_lanterns:red_trident",Count:1b}}

# Propel it forward
execute as @s at @s run tp @e[type=trident,limit=1,sort=nearest] ^ ^ ^0.6

# Play throw sound
playsound minecraft:item.trident.throw master @s ~ ~ ~ 1 1
