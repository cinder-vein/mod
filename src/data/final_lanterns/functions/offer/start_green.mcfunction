tag @s add gl_offer_green
tag @s add gl_offer_any
scoreboard players set @s gl_offer 60
scoreboard players enable @s gl_accept
scoreboard players enable @s gl_decline
scoreboard players operation #cur gl_id = @s gl_id
execute anchored eyes positioned ^ ^ ^1.6 run summon minecraft:item_display ~ ~6 ~ {Tags:["gl_offer_disp","gl_offer_new"],item:{id:"final_lanterns:greenlanternring",Count:1b},billboard:"center",brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
scoreboard players operation @e[type=minecraft:item_display,tag=gl_offer_new] gl_id = #cur gl_id
tag @e[type=minecraft:item_display,tag=gl_offer_new] remove gl_offer_new
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 1.5
tellraw @s [{"text":"\u2726 ","color":"#2EC846"},{"text":"A Green Lantern ring streaks down from the sky.","color":"#2EC846"}]
tellraw @s [{"selector":"@s","color":"#2EC846"},{"text":", you have great willpower. Welcome to the Green Lantern Corps. Do you accept?","color":"white"}]
tellraw @s [{"text":"  [ACCEPT]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_accept set 1"},"hoverEvent":{"action":"show_text","contents":"Join the Green Lantern Corps"}},{"text":"   "},{"text":"[DECLINE]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/trigger gl_decline set 1"},"hoverEvent":{"action":"show_text","contents":"Send the ring away"}},{"text":"   (or type yes / no in chat)","color":"dark_gray","italic":true}]
