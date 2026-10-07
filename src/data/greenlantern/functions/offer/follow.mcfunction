scoreboard players operation #cur gl_id = @s gl_id
execute anchored eyes positioned ^ ^ ^1.6 as @e[type=minecraft:item_display,tag=gl_offer_disp] if score @s gl_id = #cur gl_id run tp @s ~ ~ ~
