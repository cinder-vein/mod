execute if score @s gl_decline matches 1 if entity @s[tag=gl_offer_green] run function greenlantern:offer/decline_green
execute if score @s gl_decline matches 2 if entity @s[tag=gl_offer_yellow] run function greenlantern:offer/decline_yellow
execute if score @s gl_decline matches 3 if entity @s[tag=gl_offer_red] run function greenlantern:offer/decline_red
execute if score @s gl_decline matches 4 if entity @s[tag=gl_offer_orange] run function greenlantern:offer/decline_orange
execute if score @s gl_decline matches 5 if entity @s[tag=gl_offer_blue] run function greenlantern:offer/decline_blue
execute if score @s gl_decline matches 6 if entity @s[tag=gl_offer_violet] run function greenlantern:offer/decline_violet
execute if score @s gl_decline matches 7 if entity @s[tag=gl_offer_indigo] run function greenlantern:offer/decline_indigo
execute if score @s gl_decline matches 8 if entity @s[tag=gl_offer_white] run function greenlantern:offer/decline_white
execute if score @s gl_decline matches 9 if entity @s[tag=gl_offer_black] run function greenlantern:offer/decline_black
scoreboard players set @s gl_decline 0
