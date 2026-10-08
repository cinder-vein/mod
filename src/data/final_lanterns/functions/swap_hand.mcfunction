tag @e[distance=..3,sort=nearest,tag=!swap_hand,type=!item] add swap_hand_ability
summon minecraft:armor_stand ~ ~20 ~ {Invisible:1b,Tags:["swap_hand_as"]}
execute as @e[tag=swap_hand_ability,limit=1] run item replace entity @e[tag=swap_hand_as] weapon.mainhand from entity @s weapon.mainhand
execute as @e[tag=swap_hand_ability,limit=1] run item replace entity @s weapon.mainhand from entity @p[tag=swap_hand] weapon.mainhand
execute as @e[tag=swap_hand_as,limit=1] run item replace entity @e[tag=swap_hand] weapon.mainhand from entity @s weapon.mainhand
kill @e[tag=swap_hand_as]