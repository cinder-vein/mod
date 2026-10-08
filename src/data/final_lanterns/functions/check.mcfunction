tellraw @s ["",{"text":"\n\u2b22 Final Lanterns check","color":"white","bold":true}]
execute if score #ticks gl_cfg matches 1.. run tellraw @s ["",{"text":"\u2714 ","color":"green"},{"text":"The datapack is running.","color":"gray"}]
execute unless score #ticks gl_cfg matches 1.. run tellraw @s ["",{"text":"\u2718 ","color":"red"},{"text":"The datapack's tick isn't running: nothing happens on its own. Check logs/latest.log for \"final_lanterns\" errors, and remove the old Lantern Corps jar.","color":"gray"}]
execute if score #kubejs gl_cfg matches 1.. run tellraw @s ["",{"text":"\u2714 ","color":"green"},{"text":"KubeJS commands loaded: /lantern, /ring, /emotions.","color":"gray"}]
execute unless score #kubejs gl_cfg matches 1.. run tellraw @s ["",{"text":"\u2718 ","color":"red"},{"text":"The Final Lanterns KubeJS script isn't loaded, so /lantern and /ring don't work (an old copy in your kubejs folder can make them do nothing). Delete lantern_commands.js and lantern_keys.js from kubejs/server_scripts and kubejs/client_scripts, then copy in the new lantern_commands.js. Without KubeJS everything still works through chat, /trigger and ","color":"gray"},{"text":"/function final_lanterns:admin/help","color":"aqua","clickEvent":{"action":"run_command","value":"/function final_lanterns:admin/help"}},{"text":".","color":"gray"}]
execute unless score #enabled gl_cfg matches 1 run tellraw @s ["",{"text":"\u2718 ","color":"red"},{"text":"Ring offers and emotions are turned off (/lantern enable).","color":"gray"}]
execute unless entity @s[gamemode=survival] run tellraw @s ["",{"text":"\u2718 ","color":"red"},{"text":"You're not in survival mode: rings only come to players in survival.","color":"gray"}]
execute if entity @s[tag=gl_offer_any] run tellraw @s ["",{"text":"\u2022 ","color":"gold"},{"text":"A ring is waiting for your answer right now.","color":"gray"}]
tellraw @s ["",{"text":" Rings (they come at ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"},{"text":"):","color":"gray"}]
scoreboard players add @s gl_cd_green 0
scoreboard players add @s gl_ser_green 0
execute if entity @s[tag=gl_member_green] run tellraw @s ["",{"text":"  Green Lantern: ","color":"#2EC846"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_green] if score @s gl_ser_green matches ..-1 run tellraw @s ["",{"text":"  Green Lantern: ","color":"#2EC846"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_green] if score @s gl_cd_green matches 1.. run tellraw @s ["",{"text":"  Green Lantern: ","color":"#2EC846"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_green"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_green] if score @s gl_cd_green matches ..0 if score @s gl_ser_green matches 0.. run tellraw @s ["",{"text":"  Green Lantern: ","color":"#2EC846"},{"text":"willpower ","color":"gray"},{"score":{"name":"@s","objective":"gl_e_will"},"color":"white"},{"text":" / ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"}]
scoreboard players add @s gl_cd_yellow 0
scoreboard players add @s gl_ser_yellow 0
execute if entity @s[tag=gl_member_yellow] run tellraw @s ["",{"text":"  Sinestro Corps: ","color":"#F5CD1E"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_yellow] if score @s gl_ser_yellow matches ..-1 run tellraw @s ["",{"text":"  Sinestro Corps: ","color":"#F5CD1E"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_yellow] if score @s gl_cd_yellow matches 1.. run tellraw @s ["",{"text":"  Sinestro Corps: ","color":"#F5CD1E"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_yellow"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_yellow] if score @s gl_cd_yellow matches ..0 if score @s gl_ser_yellow matches 0.. run tellraw @s ["",{"text":"  Sinestro Corps: ","color":"#F5CD1E"},{"text":"fear ","color":"gray"},{"score":{"name":"@s","objective":"gl_e_fear"},"color":"white"},{"text":" / ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"}]
scoreboard players add @s gl_cd_red 0
scoreboard players add @s gl_ser_red 0
execute if entity @s[tag=gl_member_red] run tellraw @s ["",{"text":"  Red Lantern: ","color":"#DC1E23"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_red] if score @s gl_ser_red matches ..-1 run tellraw @s ["",{"text":"  Red Lantern: ","color":"#DC1E23"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_red] if score @s gl_cd_red matches 1.. run tellraw @s ["",{"text":"  Red Lantern: ","color":"#DC1E23"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_red"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_red] if score @s gl_cd_red matches ..0 if score @s gl_ser_red matches 0.. run tellraw @s ["",{"text":"  Red Lantern: ","color":"#DC1E23"},{"text":"rage ","color":"gray"},{"score":{"name":"@s","objective":"gl_e_rage"},"color":"white"},{"text":" / ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"}]
scoreboard players add @s gl_cd_orange 0
scoreboard players add @s gl_ser_orange 0
execute if entity @s[tag=gl_member_orange] run tellraw @s ["",{"text":"  Orange Lantern: ","color":"#FA8214"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_orange] if score @s gl_ser_orange matches ..-1 run tellraw @s ["",{"text":"  Orange Lantern: ","color":"#FA8214"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_orange] if score @s gl_cd_orange matches 1.. run tellraw @s ["",{"text":"  Orange Lantern: ","color":"#FA8214"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_orange"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_orange] if score @s gl_cd_orange matches ..0 if score @s gl_ser_orange matches 0.. run tellraw @s ["",{"text":"  Orange Lantern: ","color":"#FA8214"},{"text":"avarice ","color":"gray"},{"score":{"name":"@s","objective":"gl_e_greed"},"color":"white"},{"text":" / ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"}]
scoreboard players add @s gl_cd_blue 0
scoreboard players add @s gl_ser_blue 0
execute if entity @s[tag=gl_member_blue] run tellraw @s ["",{"text":"  Blue Lantern: ","color":"#2882FF"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_blue] if score @s gl_ser_blue matches ..-1 run tellraw @s ["",{"text":"  Blue Lantern: ","color":"#2882FF"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_blue] if score @s gl_cd_blue matches 1.. run tellraw @s ["",{"text":"  Blue Lantern: ","color":"#2882FF"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_blue"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_blue] if score @s gl_cd_blue matches ..0 if score @s gl_ser_blue matches 0.. run tellraw @s ["",{"text":"  Blue Lantern: ","color":"#2882FF"},{"text":"hope ","color":"gray"},{"score":{"name":"@s","objective":"gl_e_hope"},"color":"white"},{"text":" / ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"}]
scoreboard players add @s gl_cd_violet 0
scoreboard players add @s gl_ser_violet 0
execute if entity @s[tag=gl_member_violet] run tellraw @s ["",{"text":"  Star Sapphire: ","color":"#D737DC"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_violet] if score @s gl_ser_violet matches ..-1 run tellraw @s ["",{"text":"  Star Sapphire: ","color":"#D737DC"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_violet] if score @s gl_cd_violet matches 1.. run tellraw @s ["",{"text":"  Star Sapphire: ","color":"#D737DC"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_violet"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_violet] if score @s gl_cd_violet matches ..0 if score @s gl_ser_violet matches 0.. run tellraw @s ["",{"text":"  Star Sapphire: ","color":"#D737DC"},{"text":"love ","color":"gray"},{"score":{"name":"@s","objective":"gl_e_love"},"color":"white"},{"text":" / ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"}]
scoreboard players add @s gl_cd_indigo 0
scoreboard players add @s gl_ser_indigo 0
execute if entity @s[tag=gl_member_indigo] run tellraw @s ["",{"text":"  Indigo Tribe: ","color":"#693CE6"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_indigo] if score @s gl_ser_indigo matches ..-1 run tellraw @s ["",{"text":"  Indigo Tribe: ","color":"#693CE6"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_indigo] if score @s gl_cd_indigo matches 1.. run tellraw @s ["",{"text":"  Indigo Tribe: ","color":"#693CE6"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_indigo"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_indigo] if score @s gl_cd_indigo matches ..0 if score @s gl_ser_indigo matches 0.. run tellraw @s ["",{"text":"  Indigo Tribe: ","color":"#693CE6"},{"text":"compassion ","color":"gray"},{"score":{"name":"@s","objective":"gl_e_compassion"},"color":"white"},{"text":" / ","color":"gray"},{"score":{"name":"#threshold","objective":"gl_cfg"},"color":"white"}]
scoreboard players add @s gl_cd_white 0
scoreboard players add @s gl_ser_white 0
execute if entity @s[tag=gl_member_white] run tellraw @s ["",{"text":"  White Lantern: ","color":"#EBF2FA"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_white] if score @s gl_ser_white matches ..-1 run tellraw @s ["",{"text":"  White Lantern: ","color":"#EBF2FA"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_white] if score @s gl_cd_white matches 1.. run tellraw @s ["",{"text":"  White Lantern: ","color":"#EBF2FA"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_white"},"color":"white"},{"text":" s.","color":"gray"}]
execute unless entity @s[tag=gl_member_white] if score @s gl_cd_white matches ..0 if score @s gl_ser_white matches 0.. run tellraw @s ["",{"text":"  White Lantern: ","color":"#EBF2FA"},{"text":"comes when all seven spectrum emotions reach the threshold.","color":"gray"}]
scoreboard players add @s gl_cd_black 0
scoreboard players add @s gl_ser_black 0
execute if entity @s[tag=gl_member_black] run tellraw @s ["",{"text":"  Black Lantern: ","color":"#AAAFBE"},{"text":"you bear its ring.","color":"gray"}]
execute unless entity @s[tag=gl_member_black] if score @s gl_ser_black matches ..-1 run tellraw @s ["",{"text":"  Black Lantern: ","color":"#AAAFBE"},{"text":"your ring was taken away: only an admin can offer it again.","color":"gray"}]
execute unless entity @s[tag=gl_member_black] if score @s gl_cd_black matches 1.. run tellraw @s ["",{"text":"  Black Lantern: ","color":"#AAAFBE"},{"text":"you turned it away; it may come again in ","color":"gray"},{"score":{"name":"@s","objective":"gl_cd_black"},"color":"white"},{"text":" s.","color":"gray"}]
scoreboard players set #low gl_tmp 0
execute if score @s gl_e_will < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_fear < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_rage < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_greed < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_hope < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_love < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute if score @s gl_e_compassion < #black_floor gl_cfg run scoreboard players add #low gl_tmp 1
execute unless entity @s[tag=gl_member_black] if score @s gl_cd_black matches ..0 if score @s gl_ser_black matches 0.. run tellraw @s ["",{"text":"  Black Lantern: ","color":"#AAAFBE"},{"text":"comes when ","color":"gray"},{"text":"4+","color":"white"},{"text":" spectrum emotions are below ","color":"gray"},{"score":{"name":"#black_floor","objective":"gl_cfg"},"color":"white"},{"text":"; you have ","color":"gray"},{"score":{"name":"#low","objective":"gl_tmp"},"color":"white"},{"text":".","color":"gray"}]
execute unless score #entities gl_cfg matches 1 run tellraw @s ["",{"text":"\u2022 ","color":"gold"},{"text":"Entities don't appear on their own (/lantern entity on).","color":"gray"}]
scoreboard players add @s gl_ehcd 0
execute if score @s gl_ehcd matches 1.. run tellraw @s ["",{"text":"\u2022 ","color":"gold"},{"text":"No entity will choose you for another ","color":"gray"},{"score":{"name":"@s","objective":"gl_ehcd"},"color":"white"},{"text":" s (you lost one lately).","color":"gray"}]
function final_lanterns:entity/admin/status
