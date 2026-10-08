execute if score @s gl_accept matches 1 if entity @s[tag=gl_offer_green] run function final_lanterns:offer/accept_green
execute if score @s gl_accept matches 2 if entity @s[tag=gl_offer_yellow] run function final_lanterns:offer/accept_yellow
execute if score @s gl_accept matches 3 if entity @s[tag=gl_offer_red] run function final_lanterns:offer/accept_red
execute if score @s gl_accept matches 4 if entity @s[tag=gl_offer_orange] run function final_lanterns:offer/accept_orange
execute if score @s gl_accept matches 5 if entity @s[tag=gl_offer_blue] run function final_lanterns:offer/accept_blue
execute if score @s gl_accept matches 6 if entity @s[tag=gl_offer_violet] run function final_lanterns:offer/accept_violet
execute if score @s gl_accept matches 7 if entity @s[tag=gl_offer_indigo] run function final_lanterns:offer/accept_indigo
execute if score @s gl_accept matches 8 if entity @s[tag=gl_offer_white] run function final_lanterns:offer/accept_white
execute if score @s gl_accept matches 9 if entity @s[tag=gl_offer_black] run function final_lanterns:offer/accept_black
scoreboard players set @s gl_accept 0
