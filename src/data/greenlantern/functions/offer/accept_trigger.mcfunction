execute if score @s gl_accept matches 1 if entity @s[tag=gl_offer_green] run function greenlantern:offer/accept_green
execute if score @s gl_accept matches 2 if entity @s[tag=gl_offer_yellow] run function greenlantern:offer/accept_yellow
execute if score @s gl_accept matches 3 if entity @s[tag=gl_offer_red] run function greenlantern:offer/accept_red
execute if score @s gl_accept matches 4 if entity @s[tag=gl_offer_orange] run function greenlantern:offer/accept_orange
execute if score @s gl_accept matches 5 if entity @s[tag=gl_offer_blue] run function greenlantern:offer/accept_blue
execute if score @s gl_accept matches 6 if entity @s[tag=gl_offer_violet] run function greenlantern:offer/accept_violet
execute if score @s gl_accept matches 7 if entity @s[tag=gl_offer_indigo] run function greenlantern:offer/accept_indigo
execute if score @s gl_accept matches 8 if entity @s[tag=gl_offer_white] run function greenlantern:offer/accept_white
execute if score @s gl_accept matches 9 if entity @s[tag=gl_offer_black] run function greenlantern:offer/accept_black
scoreboard players set @s gl_accept 0
