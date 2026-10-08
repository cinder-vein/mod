tag @s add gl_offer_yellow
tag @s add gl_offer_any
scoreboard players set @s gl_offer 60
scoreboard players enable @s gl_accept
scoreboard players enable @s gl_decline
scoreboard players operation #cur gl_id = @s gl_id
execute anchored eyes positioned ^ ^ ^1.6 run summon minecraft:item_display ~ ~6 ~ {Tags:["gl_offer_disp","gl_offer_new"],item:{id:"final_lanterns:yellowlanternring",Count:1b},billboard:"center",brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
scoreboard players operation @e[type=minecraft:item_display,tag=gl_offer_new] gl_id = #cur gl_id
tag @e[type=minecraft:item_display,tag=gl_offer_new] remove gl_offer_new
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.5
tellraw @s [{"text":"\u2726 ","color":"#F5CD1E"},{"text":"A Sinestro ring streaks down from the sky.","color":"#F5CD1E"}]
tellraw @s [{"selector":"@s","color":"#F5CD1E"},{"text":", you have great fear. Welcome to the Sinestro Corps. Do you accept?","color":"white"}]
tellraw @s [{"text":"  [ACCEPT]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_accept set 2"},"hoverEvent":{"action":"show_text","contents":"Join the Sinestro Corps"}},{"text":"   "},{"text":"[DECLINE]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_decline set 2"},"hoverEvent":{"action":"show_text","contents":"Send the ring away"}},{"text":"   (or type yes / no in chat)","color":"dark_gray","italic":true}]
