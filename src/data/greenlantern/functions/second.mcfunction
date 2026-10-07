scoreboard players set #second gl_cfg 0
execute if score #enabled gl_cfg matches 1 as @a run function greenlantern:emotion/feed
execute if score #enabled gl_cfg matches 1 run function greenlantern:offer/scan
scoreboard players remove @a[scores={gl_cd_green=1..}] gl_cd_green 1
scoreboard players remove @a[scores={gl_cd_yellow=1..}] gl_cd_yellow 1
scoreboard players remove @a[scores={gl_cd_red=1..}] gl_cd_red 1
scoreboard players remove @a[scores={gl_cd_orange=1..}] gl_cd_orange 1
scoreboard players remove @a[scores={gl_cd_blue=1..}] gl_cd_blue 1
scoreboard players remove @a[scores={gl_cd_violet=1..}] gl_cd_violet 1
scoreboard players remove @a[scores={gl_cd_indigo=1..}] gl_cd_indigo 1
scoreboard players remove @a[scores={gl_cd_white=1..}] gl_cd_white 1
scoreboard players remove @a[scores={gl_cd_black=1..}] gl_cd_black 1
scoreboard players remove @a[tag=gl_offer_any] gl_offer 1
execute as @a[tag=gl_offer_any,scores={gl_offer=..0}] at @s run function greenlantern:offer/timeout
scoreboard players enable @a[tag=gl_offer_any] gl_accept
scoreboard players enable @a[tag=gl_offer_any] gl_decline
scoreboard players enable @a[tag=gl_leader_any] gl_revoke
scoreboard players enable @a[tag=gl_leader_any] gl_roster
scoreboard players enable @a gl_emotions
scoreboard players enable @a gl_recall
scoreboard players remove @a[scores={gl_rcd=1..}] gl_rcd 1
function greenlantern:charge/save
execute at @a[tag=gl_yellow] run effect give @e[type=#greenlantern:greed_prey,distance=..8] minecraft:weakness 2 0 true
clear @a[tag=!gl_ring] #greenlantern:constructs
kill @e[type=minecraft:item,nbt={Item:{tag:{gl_construct:1b}}}]
tag @a[tag=gl_scuba_green,tag=!gl_green] remove gl_scuba_green
tag @a[tag=gl_scuba_yellow,tag=!gl_yellow] remove gl_scuba_yellow
tag @a[tag=gl_scuba_red,tag=!gl_red] remove gl_scuba_red
tag @a[tag=gl_scuba_orange,tag=!gl_orange] remove gl_scuba_orange
tag @a[tag=gl_scuba_blue,tag=!gl_blue] remove gl_scuba_blue
tag @a[tag=gl_scuba_violet,tag=!gl_violet] remove gl_scuba_violet
tag @a[tag=gl_scuba_indigo,tag=!gl_indigo] remove gl_scuba_indigo
tag @a[tag=gl_scuba_white,tag=!gl_white] remove gl_scuba_white
tag @a[tag=gl_scuba_black,tag=!gl_black] remove gl_scuba_black
scoreboard players enable @a gl_construct
